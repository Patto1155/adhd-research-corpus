#!/usr/bin/env python3
"""Check the Markdown pages for formatting problems that GitHub rendering or the
house style (.github/CONTRIBUTING.md) would catch.

Run from anywhere:  python3 tools/check_format.py [--quiet] [path ...]

Standard library only. It reads every .md page (except research/ and tools/),
prints one line per problem as ``path:line: [category] message`` and a count per
category, and exits 1 if any error-level problem was found. Lines tagged
``(warn)`` are heuristics (sentence counts, spelling) for a human to judge.

Checks:
  shape      content-page shape: H1 question, short-answer blockquote <= 60 words,
             required H2 sections in order, footer line after a ``---`` rule
  heading    one H1, no skipped heading levels
  cite       every [n] has a source n and vice versa, first use in numerical order,
             source line format, duplicate sources
  table      header separator, equal column counts, blank lines around tables
  block      blank lines around lists, <details>, <picture>; blank line after </summary>
  html       unexpected HTML tags, unbalanced ** or *
  chart      <picture> markup, both SVGs exist, img width + alt, italic caption
  link       relative links and #anchors resolve; raw URLs in prose
  style      (warn) paragraphs over 3 sentences, US spellings, number formatting
"""
from __future__ import annotations

import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "research", "tools", "node_modules"}
REFERENCE_PAGES = {"glossary.md", "not-medical-advice.md", "sources-and-guidelines.md",
                   "myths-and-corrections.md", "the-evidence-at-a-glance.md"}
# Explainer whose evidence section is "The ideas, with worked examples".
ALT_H2 = {"how-to-read-the-evidence.md": {"What the evidence shows": "The ideas, with worked examples"}}
# Pages whose Sources list is a plain reference list (crisis contacts), not numbered citations.
PLAIN_SOURCES = {"not-medical-advice.md"}
REQUIRED_H2 = ["What the evidence shows", "What is uncertain or debated",
               "What this means for you", "Related pages", "Sources"]
FOOTER_RE = re.compile(
    r"^Last reviewed: [A-Z][a-z]+ \d{4} · \[How these pages are made\]\((?:\.\./08-reading-this-well/)?"
    r"sources-and-guidelines\.md\) · \[Not medical advice\]\((?:\.\./08-reading-this-well/)?not-medical-advice\.md\)$")
ALLOWED_TAGS = {"details", "summary", "picture", "source", "img", "br", "sup", "sub", "a", "kbd"}

US_WORDS = {
    "behavior", "behaviors", "behavioral", "behaviorally", "color", "colors", "colored", "center", "centers",
    "centered", "pediatric", "pediatrician", "pediatrics", "favor", "favors", "favored", "favorable",
    "labor", "estrogen", "hemoglobin", "anemia", "gray", "modeling", "modeled", "defense", "fiber",
    "tumor", "humor", "neighbor", "honor", "rumor", "favorite", "analyze", "analyzed", "analyzing",
    "paralyze", "catalog", "counseling", "counselor", "traveling", "labeled", "labeling", "canceled",
    "signaling", "enrollment", "fulfill", "skeptical", "skeptic", "skeptics", "orthopedic", "anesthesia",
    "diarrhea", "edema", "esophagus", "leukemia", "maneuver", "aging", "judgment",
}
IZE_RE = re.compile(r"\b([A-Za-z]+?)(iz)(e|es|ed|ing|ation|ations|er|ers)\b")
IZE_OK = {"siz", "priz", "seiz", "capsiz", "baiz", "maiz", "giz", "fiz", "ritz", "assiz", "bronz", "z", "dz",
          "fizz", "citiz", "deniz"}


def slugify(text: str) -> str:
    """GitHub heading anchor slug."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "")
    text = re.sub(r"(\*\*|__|\*|_)", "", text) if False else text.replace("*", "")
    text = text.strip().lower()
    out = []
    for ch in text:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in "LN" or cat == "Mn":
            out.append(ch)
    return "".join(out).replace(" ", "-")


def anchors_for(text: str) -> set[str]:
    seen: Counter = Counter()
    result = set()
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m and not in_code:
            s = slugify(m.group(2))
            n = seen[s]
            result.add(s if n == 0 else f"{s}-{n}")
            seen[s] += 1
    for m in re.finditer(r'<a\s+(?:name|id)="([^"]+)"', text):
        result.add(m.group(1))
    return result


class Page:
    def __init__(self, path: Path):
        self.path = path
        try:
            self.rel = path.relative_to(ROOT).as_posix()
        except ValueError:
            self.rel = str(path)
        self.text = path.read_text(encoding="utf-8")
        self.lines = self.text.split("\n")
        # mask fenced code and HTML comments (keep line structure)
        masked, in_code = [], False
        for line in self.lines:
            if line.lstrip().startswith("```"):
                in_code = not in_code
                masked.append("")
                continue
            masked.append("" if in_code else line)
        joined = "\n".join(masked)
        joined = re.sub(r"<!--.*?-->", lambda m: re.sub(r"[^\n]", "", m.group(0)), joined, flags=re.S)
        self.m = joined.split("\n")


problems: list[tuple[str, int, str, str, bool]] = []


def report(page: Page, line: int, cat: str, msg: str, warn: bool = False) -> None:
    problems.append((page.rel, line, cat, msg, warn))


def strip_code(s: str) -> str:
    return re.sub(r"`[^`]*`", "", s)


def is_content(page: Page) -> bool:
    return page.path.name != "README.md" and page.path.name not in REFERENCE_PAGES \
        and re.match(r"^\d\d-", page.path.parent.name) is not None


def sources_start(page: Page) -> int | None:
    for i, l in enumerate(page.m):
        if l.strip() == "## Sources":
            return i
    return None


def check_headings(page: Page) -> None:
    prev = 0
    h1 = 0
    for i, l in enumerate(page.m):
        m = re.match(r"^(#{1,6})\s", l)
        if not m:
            # setext heading created by --- straight after text
            if re.match(r"^-{3,}\s*$", l) and i > 0 and page.m[i - 1].strip() and not page.m[i - 1].startswith("|"):
                report(page, i + 1, "heading", "'---' directly under text makes it a setext H2; add a blank line")
            continue
        lvl = len(m.group(1))
        if lvl == 1:
            h1 += 1
        if prev and lvl > prev + 1:
            report(page, i + 1, "heading", f"skips from H{prev} to H{lvl}")
        prev = lvl
        if i > 0 and page.m[i - 1].strip():
            report(page, i + 1, "block", "heading needs a blank line before it")
    if h1 != 1:
        report(page, 1, "heading", f"{h1} H1 headings (expected 1)")
    if not page.lines[0].startswith("# "):
        report(page, 1, "heading", "first line is not the H1")


def check_shape(page: Page) -> None:
    lines = page.m
    if is_content(page) or page.path.name in {"myths-and-corrections.md", "sources-and-guidelines.md"}:
        pass
    if is_content(page):
        if "?" not in lines[0]:
            report(page, 1, "shape", "H1 is not a question")
        # short answer
        j = 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if not lines[j].startswith("> **Short answer:**"):
            report(page, j + 1, "shape", "no '> **Short answer:**' blockquote after the H1")
        else:
            quote = []
            while j < len(lines) and lines[j].startswith(">"):
                quote.append(lines[j].lstrip("> "))
                j += 1
            words = re.sub(r"\*\*Short answer:\*\*", "", " ".join(quote)).split()
            if len(words) > 60:
                report(page, 2, "shape", f"short answer is {len(words)} words (max 60)")
        h2 = [(i, l[3:].strip()) for i, l in enumerate(lines) if l.startswith("## ")]
        names = [n for _, n in h2]
        pos = []
        for req in REQUIRED_H2:
            req = ALT_H2.get(page.path.name, {}).get(req, req)
            if req not in names:
                report(page, 1, "shape", f"missing section '## {req}'")
            else:
                pos.append(names.index(req))
        if pos != sorted(pos):
            report(page, 1, "shape", "required sections out of order")
        if names and names[-1] != "Sources":
            report(page, h2[-1][0] + 1, "shape", f"last H2 is '{names[-1]}', expected 'Sources'")
    # footer (all pages but the root README and CONTRIBUTING)
    if page.rel in ("README.md", ".github/CONTRIBUTING.md"):
        return
    body = [l for l in page.lines]
    while body and not body[-1].strip():
        body.pop()
    last = body[-1] if body else ""
    if not FOOTER_RE.match(last):
        report(page, len(body), "shape", "last line is not the standard 'Last reviewed' footer")
    else:
        if len(body) < 3 or body[-2].strip() != "---" or body[-3].strip():
            report(page, len(body), "shape", "footer should follow a blank line and a '---' rule")
        if "../08-reading-this-well/" not in last:
            report(page, len(body), "shape", "footer links differ from the standard ../08-reading-this-well/ form", True)
    if not page.text.endswith("\n") or page.text.endswith("\n\n"):
        report(page, len(body), "shape", "file should end with exactly one newline")


CITE_RE = re.compile(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\](?!\()")


def expand(spec: str) -> list[int]:
    out = []
    for part in re.split(r"\s*,\s*", spec):
        if re.search(r"[–-]", part):
            a, b = [int(x) for x in re.split(r"\s*[–-]\s*", part)]
            out.extend(range(a, b + 1))
        else:
            out.append(int(part))
    return out


SRC_FORMAT = re.compile(
    r"^(?P<n>\d+)\. (?P<auth>[^.]+?(?:, et al)?)\. (?P<rest>.+) — \*\*(?P<label>[^*]+)\*\*(?P<tail>.*)$")


def check_citations(page: Page) -> None:
    s = sources_start(page)
    if page.path.name in PLAIN_SOURCES:
        return
    body_cites: list[tuple[int, int]] = []
    end = s if s is not None else len(page.m)
    for i in range(end):
        l = strip_code(page.m[i])
        l = re.sub(r"\]\([^)]*\)", "]", l)  # link targets
        for m in CITE_RE.finditer(l):
            # skip link texts like [1](...) handled by lookahead; skip footnote-like [^1]
            for n in expand(m.group(1)):
                body_cites.append((n, i + 1))
    if s is None:
        if body_cites:
            report(page, body_cites[0][1], "cite", "citations but no '## Sources' section")
        return
    srcs: dict[int, int] = {}
    keys: dict[str, int] = {}
    expected = 1
    for i in range(s + 1, len(page.m)):
        l = page.m[i]
        if l.startswith("## ") or l.strip() == "---":
            break
        m = re.match(r"^(\d+)\. ", l)
        if not m:
            if l.strip() and not l.startswith("   ") and not l.startswith("<!--"):
                report(page, i + 1, "cite", "non-list text inside Sources", True)
            continue
        n = int(m.group(1))
        if n != expected:
            report(page, i + 1, "cite", f"source numbered {n}, expected {expected}")
        expected = n + 1
        if n in srcs:
            report(page, i + 1, "cite", f"source {n} listed twice")
        srcs[n] = i + 1
        line = page.lines[i]
        fm = SRC_FORMAT.match(re.sub(r"\s*<!--.*?-->", "", line))
        if not fm:
            report(page, i + 1, "cite", f"source {n} does not match 'Author. Title. *Journal*. Year. ID. — **Label**, reason.'")
        else:
            if "*" not in fm.group("rest").replace("**", ""):
                report(page, i + 1, "cite", f"source {n} has no italic *Journal*", True)
            if not re.search(r"\bDOI 10\.|\bPMID \d|\bPMC\d|https?://|ISBN|<!-- CHECK", line):
                report(page, i + 1, "cite", f"source {n} has no DOI, PMID or link", True)
        if re.search(r"\bdoi:|DOI: |PMID: |doi\.org/10|PMID\d", line):
            report(page, i + 1, "cite", f"source {n} identifier not in 'DOI 10.x' / 'PMID n' form")
        for k in re.findall(r"DOI (10\.\S+?)\.?(?=\s|$)|PMID (\d+)", line):
            key = k[0].lower().rstrip(".") or k[1]
            if key in keys and keys[key] != n:
                report(page, i + 1, "cite", f"source {n} duplicates source {keys[key]} ({key})")
            keys.setdefault(key, n)
    used = {n for n, _ in body_cites}
    for n, ln in body_cites:
        if n not in srcs:
            report(page, ln, "cite", f"[{n}] has no matching source")
    for n, ln in srcs.items():
        if n not in used:
            report(page, ln, "cite", f"source {n} is never cited in the body")
    order = []
    for n, ln in body_cites:
        if n not in order:
            order.append(n)
    want = 1
    for n in order:
        if n != want:
            ln = next(l for x, l in body_cites if x == n)
            report(page, ln, "cite", f"first citation here is [{n}], expected [{want}] (number in order of first appearance)")
            break
        want += 1


def cells(row: str) -> int:
    r = strip_code(row).strip()
    r = r.replace("\\|", "")
    if r.startswith("|"):
        r = r[1:]
    if r.endswith("|"):
        r = r[:-1]
    return r.count("|") + 1


def check_blocks(page: Page) -> None:
    m = page.m
    n = len(m)
    i = 0
    in_details = 0
    while i < n:
        l = m[i]
        st = l.strip()
        # tables
        if st.startswith("|") and (i == 0 or not m[i - 1].strip().startswith("|")):
            start = i
            while i < n and m[i].strip().startswith("|"):
                i += 1
            rows = m[start:i]
            if start > 0 and m[start - 1].strip():
                report(page, start + 1, "table", "table needs a blank line before it")
            if i < n and m[i].strip():
                report(page, i + 1, "table", "table needs a blank line after it")
            if len(rows) < 2 or not re.match(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$", rows[1].strip()):
                report(page, start + 1, "table", "table has no header separator row")
            want = cells(rows[0])
            for k, r in enumerate(rows):
                if cells(r) != want:
                    report(page, start + k + 1, "table", f"row has {cells(r)} columns, header has {want}")
            continue
        # lists
        if re.match(r"^(\s*)([-*+]|\d+\.)\s", l) and i > 0:
            prev = m[i - 1]
            if prev.strip() and not re.match(r"^\s*([-*+]|\d+\.)\s", prev) and not prev.startswith("  ") \
                    and not prev.startswith(">") and not prev.startswith("#"):
                report(page, i + 1, "block", "list needs a blank line before it")
        if re.match(r"^\s*(?:[-*+]|\d+\.)\s", l) and i + 1 < n:
            nxt = m[i + 1]
            if nxt.strip() and not nxt.startswith((" ", "\t")) and not re.match(r"^\s*([-*+]|\d+\.)\s", nxt):
                report(page, i + 2, "block", "text directly after a list item joins the item; add a blank line")
        # details/summary
        if st.startswith("<details"):
            in_details += 1
            if i > 0 and m[i - 1].strip():
                report(page, i + 1, "block", "<details> needs a blank line before it")
        if "</summary>" in st:
            if i + 1 < n and m[i + 1].strip():
                report(page, i + 2, "block", "GitHub needs a blank line after </summary> before Markdown")
        if st.startswith("</details>"):
            in_details -= 1
            if m[i - 1].strip():
                report(page, i + 1, "block", "</details> needs a blank line before it (else last Markdown block breaks)")
            if i + 1 < n and m[i + 1].strip():
                report(page, i + 2, "block", "</details> needs a blank line after it")
        if st.startswith("<picture"):
            check_picture(page, i)
        i += 1
    if in_details:
        report(page, 1, "html", "unbalanced <details>")


def check_picture(page: Page, i: int) -> None:
    m = page.m
    if i > 0 and m[i - 1].strip():
        report(page, i + 1, "block", "<picture> needs a blank line before it")
    j = i
    while j < len(m) and "</picture>" not in m[j]:
        j += 1
    block = "\n".join(m[i:j + 1])
    if j >= len(m):
        report(page, i + 1, "chart", "<picture> is never closed")
        return
    src = re.search(r'<source media="\(prefers-color-scheme: dark\)" srcset="([^"]+)">', block)
    img = re.search(r'<img src="([^"]+)" alt="([^"]*)" width="720">', block)
    if not src:
        report(page, i + 1, "chart", "<source> missing or not in the standard dark-mode form")
    if not img:
        report(page, i + 1, "chart", "<img> not in the form <img src=... alt=... width=\"720\">")
    if src and img:
        a, b = src.group(1), img.group(1)
        if a != b[:-4] + "-dark.svg":
            report(page, i + 1, "chart", f"dark srcset {a} does not pair with {b}")
        for p in (a, b):
            if not (page.path.parent / p).resolve().is_file():
                report(page, i + 1, "chart", f"chart file not found: {p}")
        alt = img.group(2)
        if len(alt.split()) < 12 or not re.search(r"\d", alt):
            report(page, i + 1, "chart", "alt text looks too short to carry the chart's numbers", True)
    if j + 1 < len(m) and m[j + 1].strip():
        report(page, j + 2, "block", "</picture> needs a blank line after it")
    k = j + 1
    while k < len(m) and not m[k].strip():
        k += 1
    cap = m[k] if k < len(m) else ""
    if not (re.match(r"^\*[^*].*[^*]\*$", cap.strip()) or re.match(r"^_[^_].*_$", cap.strip())):
        report(page, k + 1, "chart", "<picture> is not followed by a one-line *italic caption*")


def check_inline(page: Page) -> None:
    s = sources_start(page)
    in_html_block = False
    para: list[tuple[int, str]] = []

    def flush():
        if not para:
            return
        txt = " ".join(t for _, t in para)
        check_paragraph(page, para[0][0], txt)
        para.clear()

    for i, raw in enumerate(page.m):
        l = strip_code(raw)
        # HTML tags
        for t in re.finditer(r"</?([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>", l):
            if t.group(1).lower() not in ALLOWED_TAGS:
                report(page, i + 1, "html", f"unexpected HTML tag <{t.group(1)}>")
        if re.search(r"<(picture|details)", l):
            in_html_block = True
        noimg = re.sub(r"<[^>]+>", "", l)
        # emphasis balance per line (paragraph lines are single lines in this corpus)
        bare = re.sub(r"\]\([^)]*\)", "]", noimg)
        bare = re.sub(r"<[^>]*>", "", bare)
        bold = bare.count("**")
        rest = bare.replace("**", "")
        rest = re.sub(r"^\s*[*-]\s", "", rest)
        rest = re.sub(r"(?<=\s)\*(?=\s)", "", rest)  # lone multiplication-like stars
        rest = re.sub(r"\d\*", "", rest)
        if bold % 2:
            report(page, i + 1, "html", "unbalanced ** on this line")
        elif rest.count("*") % 2:
            report(page, i + 1, "html", "unbalanced * (italic) on this line")
        if re.search(r"__\w|\w__", bare):
            report(page, i + 1, "html", "underscore emphasis; use * for consistency", True)
        # raw URLs
        noln = re.sub(r"\]\([^)]*\)", "]", l)
        noln = re.sub(r'(src|srcset|href)="[^"]*"', "", noln)
        noln = re.sub(r"<https?://[^>]+>", "", noln)
        if re.search(r"https?://", noln):
            report(page, i + 1, "link", "raw URL; make it a [text](url) link" + (" (in Sources)" if s is not None and i > s else ""),
                   s is not None and i > s)
        if "</picture>" in l or "</details>" in l:
            in_html_block = False
        # paragraphs
        st = raw.strip()
        prev = page.m[i - 1] if i else ""
        if st and prev.strip() and not prev.endswith(("  ", "\\")) and not in_html_block \
                and not re.match(r"^(#|>|\||<|[-*+]\s|\d+\.\s|-{3,}|\s)", raw) \
                and not re.match(r"^(#|>|\||<|[-*+]\s|\d+\.\s|-{3,}|\s)", prev):
            report(page, i + 1, "block", "line continues the paragraph above (GitHub joins them); add a blank line")
        if s is not None and i >= s:
            flush()
            continue
        if not st or st.startswith(("#", ">", "|", "<", "-", "*", "+")) or re.match(r"^\d+\.\s", st) or in_html_block:
            flush()
            if st.startswith(("- ", "* ", "+ ")) or re.match(r"^\d+\.\s", st):
                check_paragraph(page, i, re.sub(r"^([-*+]|\d+\.)\s", "", st), item=True)
            elif st.startswith("**") or (st.startswith("*") and not st.endswith("*")):
                para.append((i, st))
            continue
        para.append((i, st))
    flush()


ABBREV = re.compile(r"\b(et al|e\.g|i\.e|vs|Dr|Prof|approx|No|St|Vol|cf|Fig|Mr|Mrs|Ms|Jr|Inc|Ltd)\.$")


def sentences(txt: str) -> int:
    t = re.sub(r"\[[^\]]*\]\([^)]*\)", "LINK", txt)
    t = re.sub(r"<!--.*?-->", "", t)
    t = re.sub(r"\*\*[^*]+\*\*", lambda m: "HEAD." if m.group(0).rstrip("*").rstrip().endswith((".", "?", "!")) else "X", t, count=1) \
        if t.startswith("**") else t
    count = 0
    parts = re.split(r"(?<=[.!?])[\"”’)\]*]*\s+(?=[\"“‘(*]*[A-Z0-9])", t)
    buf = ""
    for p in parts:
        buf = (buf + " " + p).strip()
        if ABBREV.search(buf) or re.search(r"\b[A-Z]\.$", buf):
            continue
        count += 1
        buf = ""
    if buf:
        count += 1
    return count


def check_paragraph(page: Page, i: int, txt: str, item: bool = False) -> None:
    lead = re.match(r"^\*\*([^*]+)\*\*\s*", txt)
    body = txt[lead.end():] if lead and lead.group(1).rstrip().endswith((".", "?", "!", ":")) else txt
    n = sentences(body)
    if n > 3 and not item:
        report(page, i + 1, "style", f"paragraph has about {n} sentences (max 3)", True)
    # spelling outside quotes, italics (titles) and links
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", "", txt)
    t = re.sub(r"\"[^\"]*\"|“[^”]*”|\*[^*\s][^*]*\*", "", t)
    for w in re.findall(r"[A-Za-z]+", t):
        lw = w.lower()
        if lw in US_WORDS and w[0].islower():
            report(page, i + 1, "style", f"US spelling '{w}'", True)
    for mm in IZE_RE.finditer(t):
        stem = mm.group(1).lower()
        word = mm.group(0)
        if stem in IZE_OK or stem.endswith(("s", "z")) and len(stem) < 3 or word[0].isupper():
            continue
        if stem + "iz" in IZE_OK or lw_ok(word):
            continue
        report(page, i + 1, "style", f"-ize spelling '{word}'", True)
    # numbers (phone numbers on the crisis-contacts page are left as written)
    if page.path.name in PLAIN_SOURCES:
        return
    if re.search(r"(?<![\w.])-\d+\.\d", t) and "−" in page.text:
        report(page, i + 1, "style", "hyphen used as minus sign; this page uses U+2212 −", True)
    for mm in re.finditer(r"(?<![\w./–-])(\d{5,}|[1-9]\d{3})(?![\w.,/–-]|\d)", t):
        v = mm.group(1)
        if len(v) == 4 and 1800 <= int(v) <= 2100:
            continue
        ctx = t[max(0, mm.start() - 12):mm.start()]
        if re.search(r"(PMID|ISBN|DOI|CD|NG|code|No\.|number)\s*$", ctx):
            continue
        report(page, i + 1, "style", f"number '{v}' without thousands separator", True)
    for mm in re.finditer(r"(?<![\w.:/])(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)(?![\w-])", t):
        report(page, i + 1, "style", f"range '{mm.group(0)}' uses a hyphen; use an en dash", True)


def lw_ok(word: str) -> bool:
    return word.lower() in {"size", "sizes", "sized", "prize", "prizes", "seize", "seized", "citizen", "citizens",
                            "oversized", "undersized", "downsize", "bizarre", "wizard", "blizzard", "pizza"}


def check_links(page: Page, anchors_cache: dict) -> None:
    for i, l in enumerate(page.m):
        l = strip_code(l)
        for mm in re.finditer(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|(?:src|srcset|href)=\"([^\"]+)\"", l):
            target = mm.group(1) or mm.group(2)
            if re.match(r"^(https?:|mailto:|tel:)", target):
                continue
            path, _, frag = target.partition("#")
            dest = (page.path.parent / path).resolve() if path else page.path
            if path and not dest.exists():
                report(page, i + 1, "link", f"broken link: {target}")
                continue
            if frag:
                if dest.is_dir():
                    dest = dest / "README.md"
                if dest.suffix != ".md":
                    continue
                if dest not in anchors_cache:
                    anchors_cache[dest] = anchors_for(dest.read_text(encoding="utf-8"))
                if frag not in anchors_cache[dest]:
                    report(page, i + 1, "link", f"anchor #{frag} not found in {dest.relative_to(ROOT)}")


def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv
    args = [a for a in argv if not a.startswith("--")]
    if args:
        files = [Path(a).resolve() for a in args]
    else:
        files = sorted(p for p in ROOT.rglob("*.md")
                       if not (set(p.relative_to(ROOT).parts[:-1]) & SKIP_DIRS))
    cache: dict = {}
    for f in files:
        page = Page(f)
        check_headings(page)
        check_shape(page)
        check_citations(page)
        check_blocks(page)
        check_inline(page)
        check_links(page, cache)
    problems.sort()
    for rel, ln, cat, msg, warn in problems:
        if quiet and warn:
            continue
        print(f"{rel}:{ln}: [{cat}]{' (warn)' if warn else ''} {msg}")
    errs = Counter(c for _, _, c, _, w in problems if not w)
    warns = Counter(c for _, _, c, _, w in problems if w)
    print(f"\n{len(files)} files; errors: {dict(errs) or 0}; warnings: {dict(warns) or 0}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
