#!/usr/bin/env python3
"""Build a picture of the whole corpus from the pages' own source lists.

Run from anywhere:  python3 tools/charts/corpus.py
  --charts-only  redraw SVGs and JSON but leave the .md pages untouched
  --from-json    redraw from the saved corpus.json instead of re-reading the pages (style-only changes)

What it does (Python standard library only, safe to re-run as pages change):

1. Reads every content page (each ``NN-folder/*.md`` except README.md) and parses
   the numbered list under its ``## Sources`` heading.
2. Extracts, per source: page, folder, first author, year, journal, title, DOI,
   PMID, PMC ID, the evidence label written on the page ("**Evidence: ...**"),
   a coarse evidence bucket, and a coarse study type inferred from the text.
3. Writes ``assets/charts/corpus/corpus.json`` and prints summary counts.
4. Draws the corpus charts as light and dark SVG pairs in ``assets/charts/corpus/``.
5. Refreshes the generated blocks in ``08-reading-this-well/the-evidence-at-a-glance.md``
   (between ``<!-- corpus:NAME -->`` and ``<!-- /corpus:NAME -->`` markers), so the
   numbers, alt text and captions on that page always match the charts.

The study type is a keyword guess from each citation's title, journal and note.
It is meant for an overview, not as a formal classification of each paper.
"""

from __future__ import annotations

import datetime as _dt
import json
import re
import statistics
from collections import Counter, defaultdict
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "assets" / "charts" / "corpus"
PAGE = ROOT / "08-reading-this-well" / "the-evidence-at-a-glance.md"
GITHUB_BLOB = "https://github.com/Patto1155/adhd-research-corpus/blob/draft/round-1/"

FOLDER_SHORT = {
    "01": "Is ADHD real?",
    "02": "My brain",
    "03": "How I think and feel",
    "04": "Causes and outlook",
    "05": "What comes with it",
    "06": "Treatment",
    "07": "Family, work, others",
    "08": "Reading this well",
}

EVIDENCE_ORDER = [
    "Strong",
    "Moderate",
    "Limited",
    "Contested",
    "Guideline or consensus",
    "Commentary or not graded",
]

TYPE_ORDER = [
    "Meta-analysis",
    "Systematic or umbrella review",
    "Guideline or consensus",
    "Registry, cohort or large dataset",
    "Trial",
    "Other",
]

# --------------------------------------------------------------------------- parsing

ITEM_RE = re.compile(r"^(\d+)\.\s+(.*)$")
EVID_RE = re.compile(r"\*\*Evidence:\s*([^*]+?)\.?\s*\*\*")
BOLD_RE = re.compile(r"\*\*([^*]+?)\.?\*\*")
JOURNAL_RE = re.compile(r"\*([^*]+)\*")
YEAR_RE = re.compile(r"\b(19[5-9]\d|20[0-4]\d)\b")
DOI_RE = re.compile(r"(?:\bDOI:?\s*|doi\.org/)(10\.\d{4,9}/\S+)", re.I)
PMID_RE = re.compile(r"\bPMID:?\s*(\d{5,9})")
PMC_RE = re.compile(r"\b(PMC\d{5,9})\b")
PERSON_AUTHORS_RE = re.compile(r"^((?:[^.]*?\bet al)|(?:[^.]*?\b[A-Z][A-Z\-]{0,3}))\.\s+(.*)$")


def clean_doi(doi: str) -> str:
    doi = doi.rstrip(".,;:")
    while doi.endswith(")") and doi.count("(") < doi.count(")"):
        doi = doi[:-1].rstrip(".,;:")
    return doi


def evidence_bucket(raw: str | None) -> str:
    """Map the label written on the page to one of six buckets.

    In-between grades ("Limited to moderate", "Moderate to strong") count toward
    the lower grade, so the charts never overstate the evidence.
    """
    if not raw:
        return "Commentary or not graded"
    r = raw.lower().strip()
    if r.startswith("limited"):
        return "Limited"
    if r.startswith("moderate"):
        return "Moderate"
    if r.startswith("strong"):
        return "Strong"
    if r.startswith("contested"):
        return "Contested"
    if any(k in r for k in ("guideline", "consensus", "regulatory")):
        return "Guideline or consensus"
    return "Commentary or not graded"


TYPE_RULES = [
    ("Guideline or consensus", r"guideline|consensus|regulatory|food and drug administration|"
                               r"national institute for health|medicines and healthcare|de novo classification|"
                               r"diagnostic and statistical manual|icd-11 |practice parameter"),
    ("Systematic or umbrella review", r"umbrella"),
    ("Registry, cohort or large dataset", r"genome-wide|gwas|enigma|mega-analys|consortium|polygenic|"
                                          r"target[- ]trial|emulation"),
    ("Meta-analysis", r"meta-?analy|meta-regression"),
    ("Systematic or umbrella review", r"systematic review|cochrane|scoping review|systematic literature|"
                                      r"rapid review|meta-synthesis"),
    ("Trial", r"multimodal treatment study|\bmta\b|\bpats\b|randomi[sz]ed|\btrial\b|placebo|crossover|cross-over|double-blind|withdrawal design"),
    ("Registry, cohort or large dataset", r"regist|cohort|nationwide|population|longitudinal|follow-up|"
                                          r"prospective|swedish|danish|norwegian|finnish|sibling|twin|"
                                          r"incidence|prevalence|claims data|national|insurance|database|"
                                          r"natural[- ]experiment|pooled|\d+ cohorts|datasets"),
]


def study_type(primary: str, note: str) -> str:
    for is_note, text in ((False, primary.lower()), (True, note.lower())):
        for label, pattern in TYPE_RULES:
            if is_note and label == "Guideline or consensus":
                # notes often say "not a consensus"; only trust the citation itself here
                continue
            if re.search(pattern, text):
                return label
    return "Other"


def split_authors(citation: str) -> tuple[str, str]:
    m = PERSON_AUTHORS_RE.match(citation)
    if m and len(m.group(1)) < 200:
        return m.group(1).strip(), m.group(2)
    head, _, rest = citation.partition(". ")
    return head.strip(), rest


def parse_source(text: str) -> dict:
    # The note follows " — "; titles can contain a dash too, so split after the journal.
    jm0 = JOURNAL_RE.search(text)
    cut = text.find(" — ", jm0.end() if jm0 else 0)
    if cut < 0:
        cut = text.find(" — ")
    citation, note = (text[:cut], text[cut + 3:]) if cut >= 0 else (text, "")
    authors, rest = split_authors(citation)
    first_author = re.sub(r"\s*,?\s*et al$", "", authors.split(",")[0]).strip()
    jm = JOURNAL_RE.search(rest)
    journal = jm.group(1).strip().rstrip(".") if jm else None
    title = (rest[: jm.start()] if jm else rest.split(". ")[0]).strip().rstrip(".").strip()
    if not title and journal:  # a book cited by its italic title alone (e.g. DSM-5-TR)
        title, journal = journal, None
    year = None
    if jm:
        ym = YEAR_RE.search(rest[jm.end():])
        year = int(ym.group(1)) if ym else None
    if year is None:
        ym = YEAR_RE.search(citation)
        year = int(ym.group(1)) if ym else None
    dm = DOI_RE.search(text)
    pm = PMID_RE.search(text)
    pcm = PMC_RE.search(text)
    em = EVID_RE.search(text)
    raw_label = em.group(1).strip() if em else None
    if raw_label is None:
        bm = BOLD_RE.search(note)
        raw_label = bm.group(1).strip() if bm else None
    return {
        "first_author": first_author,
        "title": title,
        "journal": journal,
        "year": year,
        "doi": clean_doi(dm.group(1)) if dm else None,
        "pmid": pm.group(1) if pm else None,
        "pmc": pcm.group(1) if pcm else None,
        "evidence_label": raw_label,
        "evidence": evidence_bucket(raw_label),
        "study_type": study_type(f"{authors} {title} {journal or ''}", note),
        "note": note.strip(),
        "citation": text.strip(),
    }


def page_title(md: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


PAGE_SHORT = {
    "brain-structure-and-development": "Brain structure",
    "dopamine-noradrenaline-and-myths": "Dopamine and myths",
    "why-no-two-adhd-brains-are-alike": "No two brains alike",
    "attention-regulation-and-hyperfocus": "Attention and hyperfocus",
    "executive-function-and-working-memory": "Executive function",
    "time-waiting-and-rewards": "Time and waiting",
    "sleep-and-the-body-clock": "Sleep and body clock",
    "hormones-cycles-and-menopause": "Hormones and menopause",
    "what-does-and-doesnt-cause-adhd": "What causes ADHD",
    "the-hard-statistics-in-context": "The hard statistics",
    "alcohol-drugs-and-addiction": "Alcohol, drugs, addiction",
    "is-it-adhd-or-something-else": "ADHD or something else?",
    "lifestyle-and-other-approaches": "Lifestyle approaches",
    "staying-on-or-stopping-medication": "Staying on or stopping",
    "pregnancy-and-breastfeeding": "Pregnancy, breastfeeding",
    "adhd-in-children-and-teenagers": "Children and teenagers",
    "when-your-partner-has-adhd": "Partners with ADHD",
    "the-evidence-at-a-glance": "Evidence at a glance",
    "how-adhd-changes-over-life": "Changes over a lifetime",
    "how-well-medication-works": "How well medication works",
}


def short_page_name(stem: str) -> str:
    if stem in PAGE_SHORT:
        return PAGE_SHORT[stem]
    words = stem.replace("-", " ")
    words = re.sub(r"\badhd\b", "ADHD", words)
    words = words.replace("doesnt", "doesn't").replace("isnt", "isn't")
    return words[0].upper() + words[1:]


def source_lines(md: str) -> list[tuple[int, str]]:
    out, inside = [], False
    for line in md.splitlines():
        if line.startswith("## "):
            inside = line.strip().lower() == "## sources"
            continue
        if inside and line.startswith("---"):
            break
        if inside:
            m = ITEM_RE.match(line.strip())
            if m:
                out.append((int(m.group(1)), m.group(2)))
            elif out and line.startswith("   ") and line.strip():
                n, prev = out[-1]
                out[-1] = (n, prev + " " + line.strip())
    return out


def dedupe_key(s: dict) -> str:
    if re.search(r"\bNG87\b", s["citation"]) and "surveillance" not in s["citation"].lower():
        return "nice:ng87"
    if s["doi"]:
        return "doi:" + s["doi"].lower()
    if s["pmid"]:
        return "pmid:" + s["pmid"]
    return "title:" + re.sub(r"[^a-z0-9]", "", (s["title"] or s["citation"]).lower())[:60]


def build_corpus() -> dict:
    folders, pages, sources = [], [], []
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
        fid = folder.name[:2]
        readme = folder / "README.md"
        folders.append({
            "id": fid,
            "path": folder.name,
            "title": page_title(readme.read_text(encoding="utf-8")) if readme.exists() else folder.name,
            "short": FOLDER_SHORT.get(fid, folder.name[3:].replace("-", " ").capitalize()),
        })
        for md_path in sorted(folder.glob("*.md")):
            if md_path.name == "README.md":
                continue
            md = md_path.read_text(encoding="utf-8")
            rel = md_path.relative_to(ROOT).as_posix()
            items = source_lines(md)
            pages.append({
                "path": rel,
                "folder": fid,
                "title": page_title(md),
                "short": short_page_name(md_path.stem),
                "n_sources": len(items),
                "url": GITHUB_BLOB + rel,
            })
            for n, text in items:
                s = parse_source(text)
                s.update({"id": f"{rel}#{n}", "page": rel, "folder": fid, "n": n})
                s["key"] = dedupe_key(s)
                sources.append(s)
    cited_on = defaultdict(set)
    for s in sources:
        cited_on[s["key"]].add(s["page"])
    for s in sources:
        s["cited_on_pages"] = len(cited_on[s["key"]])
    return {"folders": folders, "pages": pages, "sources": sources}


def unique_sources(sources: list[dict]) -> list[dict]:
    seen, out = set(), []
    for s in sources:
        if s["key"] not in seen:
            seen.add(s["key"])
            out.append(s)
    return out


def summarise(corpus: dict) -> dict:
    src = corpus["sources"]
    uniq = unique_sources(src)
    years = [s["year"] for s in uniq if s["year"]]
    ev = Counter(s["evidence"] for s in src)
    types = Counter(s["study_type"] for s in uniq)
    return {
        "folders": len(corpus["folders"]),
        "pages": len(corpus["pages"]),
        "pages_with_sources": sum(1 for p in corpus["pages"] if p["n_sources"]),
        "citations": len(src),
        "unique_sources": len(uniq),
        "with_doi": sum(1 for s in uniq if s["doi"]),
        "with_pmid": sum(1 for s in uniq if s["pmid"]),
        "with_doi_or_pmid": sum(1 for s in uniq if s["doi"] or s["pmid"]),
        "evidence_citations": {k: ev.get(k, 0) for k in EVIDENCE_ORDER},
        "study_types_unique": {k: types.get(k, 0) for k in TYPE_ORDER},
        "year_min": min(years) if years else None,
        "year_max": max(years) if years else None,
        "year_median": int(statistics.median(years)) if years else None,
        "years_known": len(years),
        "since_2020": sum(1 for y in years if y >= 2020),
        "before_2010": sum(1 for y in years if y < 2010),
    }


# --------------------------------------------------------------------------- SVG drawing

import sys as _sys

_sys.path.insert(0, str(Path(__file__).resolve().parent))
import chartkit as ck  # noqa: E402

W = ck.W
PAD = ck.PAD
# Colours from tools/design/tokens.json; "evidence" is the six-step evidence palette
# shared with the reader and explorer (ordinal blues, then contested, guideline, other).
THEMES = {m: dict(ck.theme(m), bar=ck.theme(m)["series"], bar_soft=ck.theme(m)["series_soft"])
          for m in ("light", "dark")}


text_width = ck.text_width


def ink_on(fill: str) -> str:
    h = fill.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    lum = 0.2126 * r ** 2.2 + 0.7152 * g ** 2.2 + 0.0722 * b ** 2.2
    return "#0b0b0b" if lum > 0.36 else "#ffffff"


def t(x, y, s, size=13, fill="#000", weight=400, anchor="start", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{extra}>{escape(str(s))}</text>')


def bar_path(x, y, w, h, r=4, round_right=True):
    """Horizontal bar, square at the baseline, rounded data end."""
    if w <= 0:
        return ""
    r = min(r, w / 2, h / 2) if round_right else 0
    return (f'<path d="M{x:.1f},{y:.1f} h{w - r:.1f} a{r},{r} 0 0 1 {r},{r} v{h - 2 * r:.1f} '
            f'a{r},{r} 0 0 1 {-r},{r} h{-(w - r):.1f} z"')


def col_path(x, y_base, w, h, r=3):
    """Vertical column grown from the baseline, rounded top."""
    if h <= 0:
        return ""
    r = min(r, w / 2, h)
    return (f'<path d="M{x:.1f},{y_base:.1f} v{-(h - r):.1f} a{r},{r} 0 0 1 {r},{-r} h{w - 2 * r:.1f} '
            f'a{r},{r} 0 0 1 {r},{r} v{h - r:.1f} z"')


def svg_doc(height, theme, body, title, desc):
    return ck.document(THEMES[theme], height, title, desc, body)


def header(th, title, subtitle):
    """Shared header block. Returns (parts, top) where top is where content starts."""
    return ck.header(th, title, subtitle)


def footer(th, y, today, extra=""):
    """Source footer below content ending at y. Returns (parts, height)."""
    line = f"Source: this site's own source lists, generated {today}.{(' ' + extra) if extra else ''}"
    return ck.footer(th, y, line)


def chart_evidence_by_folder(corpus, theme, today, meta):
    th = THEMES[theme]
    cols = th["evidence"]
    rows = []
    for f in corpus["folders"]:
        c = Counter(s["evidence"] for s in corpus["sources"] if s["folder"] == f["id"])
        rows.append((f, [c.get(k, 0) for k in EVIDENCE_ORDER]))
    label_w = 190
    x0 = PAD + label_w
    max_total = max(sum(v) for _, v in rows) or 1
    plot_w = W - x0 - PAD - 40
    scale = plot_w / max_total
    body, top0 = header(th, meta["title"], meta["subtitle"])
    # legend, two rows
    lx, ly = PAD, top0
    for i, k in enumerate(EVIDENCE_ORDER):
        if i == 3:
            lx, ly = PAD, ly + 22
        body.append(f'<rect x="{lx}" y="{ly - 10}" width="12" height="12" rx="3" fill="{cols[i]}"/>')
        body.append(t(lx + 18, ly, k, 13, th["ink2"]))
        lx += 18 + text_width(k) + 26
    top = ly + 26
    bar_h, gap = 22, 14
    for r, (f, vals) in enumerate(rows):
        y = top + r * (bar_h + gap)
        body.append(t(x0 - 12, y + bar_h / 2 + 5, f"{f['id']}  {f['short']}", 14, th["ink"], anchor="end"))
        x = x0
        nonzero = [i for i, v in enumerate(vals) if v]
        last = nonzero[-1] if nonzero else -1
        for i, v in enumerate(vals):
            if not v:
                continue
            w = v * scale
            seg_w = w - (2 if i != last else 0)
            p = bar_path(x, y, max(seg_w, 1), bar_h, round_right=(i == last))
            body.append(p + f' fill="{cols[i]}"><title>{escape(f["short"])}: {v} {escape(EVIDENCE_ORDER[i])}</title></path>')
            lbl = str(v)
            if text_width(lbl) + 10 <= seg_w:
                body.append(t(x + seg_w / 2, y + bar_h / 2 + 4.5, lbl, 13, ink_on(cols[i]), 600, "middle"))
            x += w
        body.append(t(x + 8, y + bar_h / 2 + 5, str(sum(vals)), 14, th["ink"], 600))
    f_parts, height = footer(th, top + len(rows) * (bar_h + gap) - gap, today,
                             "Counts are citations on each folder's pages.")
    body += f_parts
    return svg_doc(height, theme, body, meta["title"], meta["alt"])


def chart_study_types(corpus, theme, today, meta):
    th = THEMES[theme]
    uniq = unique_sources(corpus["sources"])
    c = Counter(s["study_type"] for s in uniq)
    total = len(uniq) or 1
    items = sorted(((k, c.get(k, 0)) for k in TYPE_ORDER), key=lambda kv: (kv[0] == "Other", -kv[1]))
    label_w = 230
    x0 = PAD + label_w
    plot_w = W - x0 - PAD - 90
    mx = max(v for _, v in items) or 1
    body, top = header(th, meta["title"], meta["subtitle"])
    top += 4
    bar_h, gap = 22, 16
    for i, (k, v) in enumerate(items):
        y = top + i * (bar_h + gap)
        fill = th["bar_soft"] if k == "Other" else th["bar"]
        body.append(t(x0 - 12, y + bar_h / 2 + 5, k, 14, th["ink"], anchor="end"))
        w = v / mx * plot_w
        body.append(bar_path(x0, y, max(w, 1), bar_h) + f' fill="{fill}"><title>{escape(k)}: {v}</title></path>')
        body.append(t(x0 + w + 8, y + bar_h / 2 + 5, f"{v}  ({round(100 * v / total)}%)", 14, th["ink"], 600))
    body.append(f'<line x1="{x0}" x2="{x0}" y1="{top - 6}" y2="{top + len(items) * (bar_h + gap) - gap + 6}" stroke="{th["axis"]}"/>')
    f_parts, height = footer(th, top + len(items) * (bar_h + gap) - gap + 6, today, "Types are a keyword guess.")
    body += f_parts
    return svg_doc(height, theme, body, meta["title"], meta["alt"])


def chart_years(corpus, theme, today, meta):
    th = THEMES[theme]
    uniq = unique_sources(corpus["sources"])
    years = [s["year"] for s in uniq if s["year"]]
    c = Counter(years)
    y_min = (min(years) // 5) * 5
    y_max = max(years)
    span = list(range(y_min, y_max + 1))
    med = int(statistics.median(years))
    mx = max(c.values())
    tick_step = 5 if mx > 20 else 2 if mx > 8 else 1
    y_top_val = ((mx + tick_step - 1) // tick_step) * tick_step
    left, right = PAD + 34, W - PAD
    body, top0 = header(th, meta["title"], meta["subtitle"])
    plot_top = top0 + 40
    plot_bot = plot_top + 202
    slot = (right - left) / len(span)
    cw = max(min(slot - 2, 24), 2)
    sy = (plot_bot - plot_top) / y_top_val
    for v in range(0, y_top_val + 1, tick_step):
        yy = plot_bot - v * sy
        if v:
            body.append(f'<line x1="{left}" x2="{right}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="{th["grid"]}"/>')
        body.append(t(left - 8, yy + 4.5, v, 13, th["ink2"], anchor="end", extra=' style="font-variant-numeric:tabular-nums"'))
    for i, yr in enumerate(span):
        v = c.get(yr, 0)
        x = left + i * slot + (slot - cw) / 2
        fill = th["bar"] if yr >= med else th["bar_soft"]
        if v:
            body.append(col_path(x, plot_bot, cw, v * sy) + f' fill="{fill}"><title>{yr}: {v} sources</title></path>')
        if yr % 5 == 0:
            body.append(t(x + cw / 2, plot_bot + 20, yr, 13, th["ink2"], anchor="middle"))
    body.append(f'<line x1="{left}" x2="{right}" y1="{plot_bot}" y2="{plot_bot}" stroke="{th["axis"]}"/>')
    # median marker
    mi = span.index(med)
    mxp = left + mi * slot
    body.append(f'<line x1="{mxp:.1f}" x2="{mxp:.1f}" y1="{plot_top - 40}" y2="{plot_bot}" stroke="{th["ink2"]}" stroke-width="1"/>')
    body.append(t(mxp - 6, plot_top - 28, f"Older half, before {med}", 13, th["ink2"], anchor="end"))
    body.append(t(mxp + 6, plot_top - 28, "Newer half", 13, th["ink"], 600))
    # peak label
    peak = max(span, key=lambda yr: (c.get(yr, 0), yr))
    pi = span.index(peak)
    px = left + pi * slot + slot / 2
    body.append(t(px, plot_bot - c[peak] * sy - 7, c[peak], 14, th["ink"], 600, "middle"))
    f_parts, height = footer(th, plot_bot + 26, today, f"Each source counted once. {y_max} is a part year.")
    body += f_parts
    return svg_doc(height, theme, body, meta["title"], meta["alt"])


def chart_site_map(corpus, theme, today, meta):
    th = THEMES[theme]
    folders = corpus["folders"]
    by_folder = defaultdict(list)
    for p in corpus["pages"]:
        by_folder[p["folder"]].append(p)
    mx = max(p["n_sources"] for p in corpus["pages"]) or 1
    col_w = (W - 2 * PAD - 24) / 2
    cols = [folders[:4], folders[4:]]
    row_h, head_h, block_gap = 21, 40, 16
    body, top = header(th, meta["title"], meta["subtitle"])
    max_y = top
    for ci, fl in enumerate(cols):
        x = PAD + ci * (col_w + 24)
        y = top
        for f in fl:
            pages = by_folder[f["id"]]
            n_src = sum(p["n_sources"] for p in pages)
            block_h = head_h + len(pages) * row_h + 8
            body.append(f'<rect x="{x:.1f}" y="{y}" width="{col_w:.1f}" height="{block_h}" rx="{ck.RADIUS["inner"]}" fill="none" stroke="{th["border"]}"/>')
            body.append(t(x + 12, y + 22, f"{f['id']}  {f['short']}", 14, th["ink"], 600))
            body.append(t(x + col_w - 12, y + 22, f"{len(pages)} pages · {n_src} sources", 13, th["ink2"], anchor="end"))
            label_w = 176
            bx = x + 12 + label_w
            bw_max = col_w - 24 - label_w - 28
            for j, p in enumerate(pages):
                ry = y + head_h + j * row_h
                name = p["short"]
                while text_width(name) > label_w - 6 and len(name) > 4:
                    name = name[:-2].rstrip() + "…" if not name.endswith("…") else name[:-2].rstrip() + "…"
                body.append(t(x + 12, ry + 9, name, 13, th["ink"]))
                w = p["n_sources"] / mx * bw_max
                if w:
                    body.append(bar_path(bx, ry - 1, w, 12) + f' fill="{th["bar"]}"><title>{escape(p["title"])}: {p["n_sources"]} sources</title></path>')
                body.append(t(bx + w + 6, ry + 9, p["n_sources"], 13, th["ink2"]))
            y += block_h + block_gap
        max_y = max(max_y, y)
    f_parts, height = footer(th, max_y - block_gap, today, "Bar length = sources listed on the page.")
    body += f_parts
    return svg_doc(height, theme, body, meta["title"], meta["alt"])


ORG_ABBR = {
    "American Psychiatric Association": "APA",
    "National Institute for Health and Care Excellence": "NICE",
    "US Food and Drug Administration": "FDA",
    "National Institute of Mental Health": "NIMH",
}


def reuse_label(s):
    org = ORG_ABBR.get(s["first_author"], s["first_author"])
    if len(org) > 26:
        org = re.sub(r"\(.*?\)", "", org).strip()
        if len(org) > 26:
            org = org[:24].rstrip() + "…"
    return f"{org} {s['year'] or ''}".strip()


def chart_reused(corpus, theme, today, meta, top_n=10):
    th = THEMES[theme]
    items = reused_sources(corpus)[:top_n]
    label_w = 330
    x0 = PAD + label_w
    plot_w = W - x0 - PAD - 70
    mx = max(n for _, n in items) or 1
    body, top = header(th, meta["title"], meta["subtitle"])
    top += 4
    bar_h, gap = 20, 14
    for i, (s, n) in enumerate(items):
        y = top + i * (bar_h + gap)
        what = s["journal"] or ("NG87" if s["key"] == "nice:ng87" else s["title"])
        lbl = reuse_label(s) + (f", {what}" if what else "")
        while text_width(lbl, 14) > label_w - 14:
            lbl = lbl[:-2].rstrip() + "…"
        body.append(t(x0 - 12, y + bar_h / 2 + 5, lbl, 14, th["ink"], anchor="end"))
        w = n / mx * plot_w
        body.append(bar_path(x0, y, w, bar_h) + f' fill="{th["bar"]}"><title>{escape(s["title"])}: {n} pages</title></path>')
        body.append(t(x0 + w + 8, y + bar_h / 2 + 5, f"{n} pages", 14, th["ink"], 600))
    f_parts, height = footer(th, top + len(items) * (bar_h + gap) - gap, today)
    body += f_parts
    return svg_doc(height, theme, body, meta["title"], meta["alt"])


def reused_sources(corpus):
    pages_by_key = defaultdict(set)
    first = {}
    for s in corpus["sources"]:
        pages_by_key[s["key"]].add(s["page"])
        first.setdefault(s["key"], s)
    items = [(first[k], len(v)) for k, v in pages_by_key.items() if len(v) >= 2]
    items.sort(key=lambda kv: (-kv[1], -(kv[0]["year"] or 0)))
    return items


# --------------------------------------------------------------------------- chart text

TYPE_PLURAL = {
    "Meta-analysis": "meta-analyses",
    "Systematic or umbrella review": "systematic reviews",
    "Guideline or consensus": "guidelines",
    "Registry, cohort or large dataset": "registry and cohort studies",
    "Trial": "trials",
}


def pct(a, b):
    return round(100 * a / b) if b else 0


def chart_meta(corpus, summ):
    ev = summ["evidence_citations"]
    cit = summ["citations"]
    sm = ev["Strong"] + ev["Moderate"]
    folder_rows = []
    for f in corpus["folders"]:
        c = Counter(s["evidence"] for s in corpus["sources"] if s["folder"] == f["id"])
        tot = sum(c.values())
        folder_rows.append((f, c, tot))
    thin = max((r for r in folder_rows if r[2] >= 10), key=lambda r: r[1]["Limited"] / r[2])
    strongest = max((r for r in folder_rows if r[2] >= 10), key=lambda r: (r[1]["Strong"] + r[1]["Moderate"]) / r[2])
    per_folder = "; ".join(
        f"{f['id']} {f['short']}: {tot} sources ("
        + ", ".join(f"{c[k]} {k.lower()}" for k in EVIDENCE_ORDER if c[k]) + ")"
        for f, c, tot in folder_rows)

    types = summ["study_types_unique"]
    uniq = summ["unique_sources"]
    ranked = sorted(((k, v) for k, v in types.items() if k != "Other"), key=lambda kv: -kv[1])
    type_list = ", ".join(f"{k.lower()} {v} ({pct(v, uniq)}%)" for k, v in sorted(types.items(), key=lambda kv: -kv[1]))

    reused = reused_sources(corpus)
    top_r = reused[0] if reused else None
    reused_list = "; ".join(f"{reuse_label(s)} ({s['journal'] or 'no journal'}), {n} pages" for s, n in reused[:10])

    pages = corpus["pages"]
    biggest = max(pages, key=lambda p: p["n_sources"])
    folder_pages = Counter(p["folder"] for p in pages)
    site_list = "; ".join(
        f"{f['id']} {f['short']}: {folder_pages[f['id']]} pages, "
        f"{sum(p['n_sources'] for p in pages if p['folder'] == f['id'])} sources" for f in corpus["folders"])

    med = summ["year_median"]
    return {
        "site-map": {
            "title": f"{summ['folders']} folders, {summ['pages']} pages, {summ['citations']} cited sources",
            "subtitle": "Each bar shows how many sources a page lists",
            "alt": (f"Map of the site. {summ['folders']} folders hold {summ['pages']} pages with "
                    f"{summ['citations']} source entries in total. {site_list}. The page with the most "
                    f"sources is {biggest['short']} with {biggest['n_sources']}."),
            "caption": (f"*The {summ['folders']} folders and their pages. Longer bars mean more sources listed, "
                        f"not more reliable answers.*"),
        },
        "evidence-by-folder": {
            "title": f"{pct(sm, cit)}% of cited sources are labelled Strong or Moderate",
            "subtitle": "Sources cited in each folder, by the evidence label given on the page",
            "alt": (f"Stacked bar chart of {cit} source entries by folder and evidence label. Overall: "
                    + ", ".join(f"{ev[k]} {k.lower()}" for k in EVIDENCE_ORDER)
                    + f". By folder: {per_folder}. "
                    f"{thin[0]['short']} has the largest share labelled Limited "
                    f"({pct(thin[1]['Limited'], thin[2])}%)."),
            "caption": (f"*Evidence labels as written on each page. In-between grades such as "
                        f"\"Limited to moderate\" count toward the lower grade. {thin[0]['short']} leans most on "
                        f"Limited evidence; {strongest[0]['short']} has the highest share of Strong or Moderate.*"),
        },
        "study-types": {
            "title": (("Over half" if ranked[0][1] + ranked[1][1] > uniq / 2 else "Most common")
                      + f" are {TYPE_PLURAL[ranked[0][0]]} or {TYPE_PLURAL[ranked[1][0]]}"),
            "subtitle": f"The {uniq} different sources, each counted once, by kind of study",
            "alt": (f"Bar chart of {uniq} unique sources by study type: {type_list}. "
                    f"Study types were guessed from words in each citation."),
            "caption": ("*Kinds of study, guessed from each citation's title and notes, so some will be "
                        "misfiled. \"Other\" includes narrative reviews, commentaries, single surveys and "
                        "service pages.*"),
        },
        "publication-years": {
            "title": f"Half the sources were published in {med} or later",
            "subtitle": f"Publication year of the {summ['years_known']} sources with a year, each counted once",
            "alt": (f"Column chart of publication years from {summ['year_min']} to {summ['year_max']}. "
                    f"The median year is {med}. {summ['since_2020']} of {summ['years_known']} sources "
                    f"({pct(summ['since_2020'], summ['years_known'])}%) are from 2020 or later, and "
                    f"{summ['before_2010']} ({pct(summ['before_2010'], summ['years_known'])}%) are from before 2010."),
            "caption": (f"*{pct(summ['since_2020'], summ['years_known'])}% of sources are from 2020 or later. "
                        f"Older papers mostly appear where they are the original study behind an idea.*"),
        },
        "most-reused": {
            "title": (f"{reuse_label(reused[0][0])} ({reused[0][0]['journal'] or reused[0][0]['title']}) "
                      f"is cited on the most pages: {reused[0][1]}" if reused else "Reused sources"),
            "subtitle": "Sources cited on more than one page (top 10)",
            "alt": (f"Bar chart of the ten sources cited on the most pages: {reused_list}. "
                    f"{len(reused)} sources in all appear on two or more pages."),
            "caption": (f"*{len(reused)} sources appear on two or more pages. Being cited often makes a "
                        f"source central to these pages, not more likely to be right.*"),
        },
    }


CHARTS = [
    ("site-map", chart_site_map),
    ("evidence-by-folder", chart_evidence_by_folder),
    ("study-types", chart_study_types),
    ("publication-years", chart_years),
    ("most-reused", chart_reused),
]


def picture_md(name, meta, rel_prefix="../assets/charts/corpus/"):
    alt = meta["alt"].replace('"', "&quot;")
    return (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{rel_prefix}{name}-dark.svg">\n'
            f'  <img src="{rel_prefix}{name}.svg" alt="{alt}" width="720">\n</picture>\n\n{meta["caption"]}')


def summary_md(summ):
    ev = summ["evidence_citations"]
    cit = summ["citations"]
    return "\n".join([
        "| What was counted | Number |",
        "| --- | ---: |",
        f"| Content pages | {summ['pages']} ({summ['pages_with_sources']} with a source list) |",
        f"| Source entries across all pages | {cit} |",
        f"| Different sources (each counted once) | {summ['unique_sources']} |",
        f"| Different sources with a DOI or PubMed ID | {summ['with_doi_or_pmid']} ({pct(summ['with_doi_or_pmid'], summ['unique_sources'])}%) |",
        f"| Entries labelled Strong | {ev['Strong']} ({pct(ev['Strong'], cit)}%) |",
        f"| Entries labelled Moderate | {ev['Moderate']} ({pct(ev['Moderate'], cit)}%) |",
        f"| Entries labelled Limited | {ev['Limited']} ({pct(ev['Limited'], cit)}%) |",
        f"| Entries labelled Contested | {ev['Contested']} ({pct(ev['Contested'], cit)}%) |",
        f"| Guidelines and consensus statements | {ev['Guideline or consensus']} ({pct(ev['Guideline or consensus'], cit)}%) |",
        f"| Commentary, reviews or entries with no grade | {ev['Commentary or not graded']} ({pct(ev['Commentary or not graded'], cit)}%) |",
        f"| Median publication year | {summ['year_median']} |",
    ])


def thin_pages_md(corpus, threshold=0.5):
    rows = []
    for p in corpus["pages"]:
        src = [s for s in corpus["sources"] if s["page"] == p["path"]]
        if len(src) < 4:
            continue
        lim = sum(1 for s in src if s["evidence"] == "Limited")
        if lim / len(src) >= threshold:
            rows.append((lim / len(src), lim, len(src), p))
    rows.sort(key=lambda r: (-r[0], r[3]["path"]))
    out = []
    for share, lim, n, p in rows:
        link = "../" + p["path"] if not p["path"].startswith("08-") else p["path"].split("/", 1)[1]
        out.append(f"- [{p['title']}]({link}): {lim} of {n} sources labelled Limited")
    return "\n".join(out) if out else "- No page has half or more of its sources labelled Limited."


def refresh_page(blocks: dict[str, str], page: Path = PAGE):
    if not page.exists():
        return False
    text = page.read_text(encoding="utf-8")
    for name, content in blocks.items():
        pat = re.compile(rf"(<!-- corpus:{re.escape(name)} -->).*?(<!-- /corpus:{re.escape(name)} -->)", re.S)
        text, n = pat.subn(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), text)
        if not n:
            print(f"  note: no marker for '{name}' on {page.relative_to(ROOT)}")
    page.write_text(text, encoding="utf-8")
    return True


def folder_stats_md(corpus, fid):
    pages = [p for p in corpus["pages"] if p["folder"] == fid]
    src = [s for s in corpus["sources"] if s["folder"] == fid]
    c = Counter(s["evidence"] for s in src)
    n = len(src)
    parts = [f"{len(pages)} pages", f"{n} sources"]
    if n:
        parts.append(f"{pct(c['Strong'] + c['Moderate'], n)}% labelled Strong or Moderate")
        parts.append(f"{pct(c['Limited'], n)}% Limited")
    return ("**In this folder:** " + " · ".join(parts) + ". "
            "[Compare the folders](../08-reading-this-well/the-evidence-at-a-glance.md"
            "#how-strong-is-the-evidence-folder-by-folder)")


def main():
    if "--from-json" in _sys.argv:
        # Redraw from the saved corpus.json (same numbers, same date) without re-reading the pages.
        # Useful for style-only changes while pages are being edited.
        saved = json.loads((OUT / "corpus.json").read_text(encoding="utf-8"))
        today = saved["generated"]
        corpus = {k: saved[k] for k in ("folders", "pages", "sources")}
        summ = summarise(corpus)
    else:
        today = _dt.date.today().isoformat()
        corpus = build_corpus()
        summ = summarise(corpus)
        OUT.mkdir(parents=True, exist_ok=True)
        data = {"generated": today, "summary": summ, "evidence_order": EVIDENCE_ORDER,
                "type_order": TYPE_ORDER, **corpus}
        (OUT / "corpus.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    metas = chart_meta(corpus, summ)
    for name, fn in CHARTS:
        for theme in ("light", "dark"):
            suffix = "" if theme == "light" else "-dark"
            (OUT / f"{name}{suffix}.svg").write_text(fn(corpus, theme, today, metas[name]), encoding="utf-8")
    (OUT / "charts.json").write_text(json.dumps(metas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    refreshed = False
    if "--charts-only" not in _sys.argv:  # --charts-only: redraw SVGs and JSON, leave the .md pages alone
        blocks = {name: picture_md(name, m) for name, m in metas.items()}
        blocks["summary"] = summary_md(summ)
        blocks["thin-pages"] = thin_pages_md(corpus)
        refreshed = refresh_page(blocks)
        for f in corpus["folders"]:
            refresh_page({"folder-stats": folder_stats_md(corpus, f["id"])}, ROOT / f["path"] / "README.md")

    print(f"Corpus generated {today}")
    print(f"  folders {summ['folders']}, pages {summ['pages']} ({summ['pages_with_sources']} with sources)")
    print(f"  source entries {summ['citations']}, unique sources {summ['unique_sources']}")
    print(f"  unique with DOI {summ['with_doi']}, with PMID {summ['with_pmid']}, either {summ['with_doi_or_pmid']}")
    print("  evidence (entries): " + ", ".join(f"{k} {v}" for k, v in summ["evidence_citations"].items()))
    print("  study type (unique): " + ", ".join(f"{k} {v}" for k, v in summ["study_types_unique"].items()))
    print(f"  years {summ['year_min']}-{summ['year_max']}, median {summ['year_median']}, "
          f"since 2020 {summ['since_2020']}/{summ['years_known']}")
    print(f"  wrote {len(CHARTS) * 2} SVGs" + ("" if "--from-json" in _sys.argv else f" and {OUT.relative_to(ROOT)}/corpus.json")
          + ("; refreshed " + str(PAGE.relative_to(ROOT)) if refreshed else ""))


if __name__ == "__main__":
    main()
