#!/usr/bin/env python3
"""Build the low-attention reader (V2) from the content pages.

Usage: python3 tools/reader/build.py [out.html] [--conflicts DIR]
  out.html      default tools/reader/index.html (git-ignored)
  --conflicts   folder of conflict-register JSON files (default research/conflicts)

Standard library only. Reads every content page, the root README ("Find your worry"),
the folder READMEs, the chart SVGs and any research/conflicts/*.json, and inlines
them into tools/reader/template.html. Page text is never rewritten: markdown is
converted to HTML as written. Safe to re-run at any time.
"""
import html
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
GH = "https://github.com/Patto1155/adhd-research-corpus/blob/draft/round-1/"
CRISIS = GH + "08-reading-this-well/not-medical-advice.md#if-you-need-help-now"

# ---------------------------------------------------------------- arguments
args = sys.argv[1:]
conflicts_dir = ROOT / "research" / "conflicts"
out_path = HERE / "index.html"
i = 0
positional = []
while i < len(args):
    if args[i] == "--conflicts" and i + 1 < len(args):
        conflicts_dir = Path(args[i + 1]).resolve()
        i += 2
        continue
    positional.append(args[i])
    i += 1
if positional:
    out_path = Path(positional[0]).resolve()

FOLDERS = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name))
PAGE_PATHS = sorted(
    str(p.relative_to(ROOT)) for f in FOLDERS for p in (ROOT / f).glob("*.md") if p.name != "README.md"
)


def slug_for(path):
    folder, name = path.split("/", 1)
    return folder[:2] + "-" + name[:-3]


PAGE_SLUGS = {p: slug_for(p) for p in PAGE_PATHS}


def gh_anchor(text):
    """GitHub-style heading anchor."""
    t = re.sub(r"<[^>]+>", "", text).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def word_count(s):
    return len(re.findall(r"\w+", strip_tags(s)))


def minutes(words):
    return max(1, round(words / 200))


# ---------------------------------------------------------------- inline markdown
class Ctx:
    def __init__(self, path):
        self.path = path  # repo-relative path of the md file
        self.dir = os.path.dirname(path)
        self.charts = []


def resolve_link(href, ctx):
    """Return (href, attrs) for a markdown link target."""
    if re.match(r"^(https?:|mailto:)", href):
        return href, ' target="_blank" rel="noopener"'
    path, _, anchor = href.partition("#")
    if not path:
        target = ctx.path
    else:
        target = os.path.normpath(os.path.join(ctx.dir, path)).replace(os.sep, "/")
    if target in PAGE_SLUGS:
        attrs = ' data-page="%s"' % PAGE_SLUGS[target]
        if anchor:
            attrs += ' data-anchor="%s"' % html.escape(anchor)
        return "#" + PAGE_SLUGS[target], attrs
    if target == "README.md":
        return "#start", ""
    m = re.match(r"^(\d\d)-[^/]+/README\.md$", target)
    if m:
        return "#start", ' data-folder="%s"' % m.group(1)
    url = GH + target + ("#" + anchor if anchor else "")
    return url, ' target="_blank" rel="noopener"'


def inline(text, ctx):
    holds = []

    def hold(s):
        holds.append(s)
        return "\x00%d\x00" % (len(holds) - 1)

    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", lambda m: hold("<code>%s</code>" % m.group(1)), text)

    def link(m):
        label, href = m.group(1), html.unescape(m.group(2))
        url, attrs = resolve_link(href, ctx)
        ext = ' <span class="ext" aria-hidden="true">↗</span>' if "_blank" in attrs else ""
        return hold('<a href="%s"%s>%s%s</a>' % (html.escape(url), attrs, emph(label), ext))

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(
        r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]",
        lambda m: hold('<a class="cite" href="#" data-cite="%s">[%s]</a>'
                       % (re.match(r"\d+", m.group(1)).group(0), m.group(1))),
        text,
    )
    text = emph(text)
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: holds[int(m.group(1))], text)
    return text


def emph(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", t)
    return t


# ---------------------------------------------------------------- charts
CHARTS = {}


def load_svg(rel, key):
    p = ROOT / rel
    if not p.exists():
        return None
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"<\?xml[^>]*\?>\s*", "", s)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    pre = re.sub(r"[^a-z0-9]", "", key.lower())[-24:] + "-"
    s = re.sub(r'\bid="([^"]+)"', lambda m: 'id="%s%s"' % (pre, m.group(1)), s)
    s = re.sub(r'aria-labelledby="([^"]+)"',
               lambda m: 'aria-labelledby="%s"' % " ".join(pre + x for x in m.group(1).split()), s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: "url(#%s%s)" % (pre, m.group(1)), s)
    s = re.sub(r'href="#([^"]+)"', lambda m: 'href="#%s%s"' % (pre, m.group(1)), s)
    return s.strip()


def chart_figure(block, caption_md, ctx):
    dark = re.search(r'srcset="([^"]+)"', block)
    img = re.search(r'<img[^>]*src="([^"]+)"', block)
    alt = re.search(r'alt="([^"]*)"', block)
    if not img:
        return None
    light_rel = os.path.normpath(os.path.join(ctx.dir, img.group(1))).replace(os.sep, "/")
    dark_rel = os.path.normpath(os.path.join(ctx.dir, dark.group(1))).replace(os.sep, "/") if dark else light_rel
    key = light_rel.replace("assets/charts/", "")[:-4]
    if key not in CHARTS:
        light = load_svg(light_rel, key)
        if light is None:
            return None
        CHARTS[key] = {"l": light, "d": load_svg(dark_rel, key + "d") or light}
    alt_text = html.unescape(alt.group(1)) if alt else ""
    cap = ""
    if caption_md:
        inner = caption_md.strip()
        if inner.startswith("*") and inner.endswith("*"):
            inner = inner[1:-1]
        cap = inline(inner, ctx)
    ctx.charts.append(key)
    h = ['<figure class="chart" data-chart="%s">' % key,
         '<div class="chart-box" role="img" aria-label="%s"></div>' % html.escape(alt_text)]
    if cap:
        h.append("<figcaption>%s</figcaption>" % cap)
    h.append('<div class="chart-tools"><button type="button" class="link-btn" data-enlarge="%s">Enlarge chart</button>'
             '<details class="alt"><summary>Describe this chart in words</summary><p>%s</p></details></div>'
             % (key, html.escape(alt_text)))
    h.append("</figure>")
    return {"t": "figure", "key": key, "html": "".join(h), "alt": alt_text, "cap": cap}


# ---------------------------------------------------------------- block markdown
ITEM = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def parse_blocks(lines, ctx):
    """Return a list of nodes {t, html, ...}."""
    nodes = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("<details"):
            depth, j = 0, i
            body = []
            while j < n:
                ls = lines[j].strip()
                if ls.startswith("<details"):
                    depth += 1
                if ls.startswith("</details>"):
                    depth -= 1
                    if depth == 0:
                        break
                body.append(lines[j])
                j += 1
            body = body[1:]  # drop <details>
            summary = ""
            if body and "<summary>" in body[0]:
                summary = re.sub(r"</?summary>", "", body[0]).strip()
                body = body[1:]
            inner = parse_blocks(body, ctx)
            nodes.append({"t": "details", "summary": inline(summary, ctx),
                          "html": '<details class="inner"><summary>%s</summary><div class="inner-body">%s</div></details>'
                          % (inline(summary, ctx), "".join(x["html"] for x in inner))})
            i = j + 1
            continue
        if s.startswith("<picture"):
            j = i
            buf = []
            while j < n:
                buf.append(lines[j])
                if "</picture>" in lines[j]:
                    break
                j += 1
            j += 1
            k = j
            while k < n and not lines[k].strip():
                k += 1
            caption = None
            if k < n and re.match(r"^\*[^*].*\*$", lines[k].strip()):
                caption = lines[k].strip()
                j = k + 1
            fig = chart_figure("\n".join(buf), caption, ctx)
            if fig:
                nodes.append(fig)
            i = j
            continue
        m = re.match(r"^(#{3,6})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            title = m.group(2)
            nodes.append({"t": "h", "level": level, "title": title,
                          "html": '<h%d id="s-%s" class="sub">%s</h%d>'
                          % (level + 1, gh_anchor(title), inline(title, ctx), level + 1)})
            i += 1
            continue
        if s.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            nodes.append({"t": "table", "html": table_html(rows, ctx)})
            continue
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            kind = "note"
            if buf and re.match(r"^\[!(\w+)\]", buf[0].strip()):
                kind = re.match(r"^\[!(\w+)\]", buf[0].strip()).group(1).lower()
                buf = buf[1:]
            inner = parse_blocks(buf, ctx)
            nodes.append({"t": "quote", "kind": kind, "md": "\n".join(buf),
                          "html": '<div class="callout callout-%s">%s</div>' % (kind, "".join(x["html"] for x in inner))})
            continue
        if re.match(r"^-{3,}$", s):
            i += 1
            continue
        if ITEM.match(line):
            j = i
            buf = []
            while j < n:
                l = lines[j]
                if not l.strip():
                    # a blank line ends the list unless the next line continues it
                    if j + 1 < n and ITEM.match(lines[j + 1]):
                        j += 1
                        continue
                    break
                if not ITEM.match(l) and not l.startswith((" ", "\t")) and buf and l.strip().startswith(("#", "|", "<")):
                    break
                buf.append(l)
                j += 1
            nodes.append(list_node(buf, ctx))
            i = j
            continue
        # paragraph
        buf = []
        while i < n and lines[i].strip() and not lines[i].strip().startswith(("<details", "<picture", "|", ">", "#")) \
                and not ITEM.match(lines[i]) and not re.match(r"^-{3,}$", lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        if not buf:
            # unknown construct, emit verbatim as text to avoid an infinite loop
            buf = [lines[i].strip()]
            i += 1
        md = "\n".join(buf)
        nodes.append({"t": "p", "md": md, "html": "<p>%s</p>" % "<br>".join(inline(x, ctx) for x in buf)})
    return nodes


def list_node(buf, ctx):
    items = []  # (indent, marker, text)
    for l in buf:
        m = ITEM.match(l)
        if m:
            items.append([len(m.group(1).expandtabs(4)), m.group(2), m.group(3)])
        elif items:
            items[-1][2] += "\n" + l.strip()

    def render(start, indent):
        out = []
        k = start
        ordered = items[start][1][0].isdigit()
        first_num = int(items[start][1][:-1]) if ordered else 1
        while k < len(items) and items[k][0] >= indent:
            if items[k][0] > indent:
                sub, k2 = render(k, items[k][0])
                out[-1] = out[-1][:-5] + sub + "</li>"
                k = k2
                continue
            text = items[k][2]
            out.append("<li>%s</li>" % "<br>".join(inline(x, ctx) for x in text.split("\n")))
            k += 1
        tag = "ol" if ordered else "ul"
        attr = ' start="%d"' % first_num if ordered and first_num != 1 else ""
        return "<%s%s>%s</%s>" % (tag, attr, "".join(out), tag), k

    h, _ = render(0, items[0][0]) if items else ("", 0)
    return {"t": "list", "items": items, "html": h}


def table_html(rows, ctx):
    def cells(r):
        r = r.strip().strip("|")
        return [c.strip() for c in re.split(r"(?<!\\)\|", r)]

    head = cells(rows[0])
    aligns = []
    body = rows[1:]
    if body and re.match(r"^\|?\s*:?-{2,}", body[0]):
        for c in cells(body[0]):
            aligns.append("right" if c.endswith(":") and not c.startswith(":") else "left")
        body = body[1:]
    def al(k):
        return ' class="num"' if k < len(aligns) and aligns[k] == "right" else ""
    h = ['<div class="table-wrap" tabindex="0" role="region" aria-label="Table, scrolls sideways if needed"><table><thead><tr>']
    h += ["<th%s>%s</th>" % (al(k), inline(c, ctx)) for k, c in enumerate(head)]
    h.append("</tr></thead><tbody>")
    for r in body:
        h.append("<tr>" + "".join("<td%s>%s</td>" % (al(k), inline(c, ctx)) for k, c in enumerate(cells(r))) + "</tr>")
    h.append("</tbody></table></div>")
    return "".join(h)


# ---------------------------------------------------------------- sources
def grade_of(label):
    l = label.lower()
    if "contested" in l:
        return "Contested"
    if " to " in l and any(g in l for g in ("strong", "moderate", "limited")):
        return "Range"
    for g in ("Strong", "Moderate", "Limited"):
        if l.startswith(g.lower()):
            return g
    if "guideline" in l or "consensus" in l:
        return "Guideline"
    return "Other"


def parse_sources(node, ctx):
    out = []
    if not node or node["t"] != "list":
        return out
    for k, (_, marker, text) in enumerate(node["items"]):
        num = int(marker[:-1]) if marker[0].isdigit() else k + 1
        m = re.search(r"— \*\*(?:Evidence:\s*)?([^*]+?)\.?\*\*", text)
        label = m.group(1).strip() if m else ""
        doi = re.search(r"\bDOI:?\s*(10\.\d{4,9}/[^\s]+?)(?=[.,;]?(?:\s|$))", text)
        pmid = re.search(r"\bPMID:?\s*(\d+)", text)
        pmids = re.findall(r"\bPMID:?\s*(\d+)", text)
        out.append({
            "n": num,
            "html": "<br>".join(inline(x, ctx) for x in text.split("\n")),
            "label": label,
            "grade": grade_of(label) if label else "Other",
            "doi": doi.group(1) if doi else None,
            "pmid": pmid.group(1) if pmid else None,
            "pmids": pmids,
        })
    return out


# ---------------------------------------------------------------- pages
SECTION_KINDS = [
    ("what the evidence shows", "evidence"),
    ("what is uncertain", "uncertain"),
    ("what this means for you", "meaning"),
    ("related pages", "related"),
    ("sources", "sources"),
]


def section_kind(title):
    t = title.lower()
    for prefix, kind in SECTION_KINDS:
        if t.startswith(prefix):
            return kind
    return "other"


def key_points(nodes, limit=4):
    """Bold lead sentences, spread across H3 sub-sections when there are any."""
    groups = [[]]
    for idx, nd in enumerate(nodes):
        if nd["t"] == "h":
            groups.append([])
        elif nd["t"] == "p" and nd["md"].startswith("**"):
            m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", nd["md"], flags=re.S)
            if m:
                groups[-1].append((idx, m.group(1), m.group(2)))
    groups = [g for g in groups if g]
    picked = []
    rnd = 0
    while len(picked) < limit and any(len(g) > rnd for g in groups):
        for g in groups:
            if len(g) > rnd and len(picked) < limit:
                picked.append(g[rnd])
        rnd += 1
    picked.sort()
    return picked


def parse_page(path):
    raw = (ROOT / path).read_text(encoding="utf-8")
    raw = re.sub(r"[ \t]*<!--.*?-->", "", raw, flags=re.S)
    lines = raw.split("\n")
    ctx = Ctx(path)
    reviewed = ""
    # footer after the last '---'
    for k in range(len(lines) - 1, -1, -1):
        if re.match(r"^-{3,}\s*$", lines[k]):
            foot = " ".join(lines[k + 1:])
            m = re.search(r"Last reviewed:\s*([^·\n]+)", foot)
            if m:
                reviewed = m.group(1).strip()
                lines = lines[:k]
            break
    title = ""
    for k, l in enumerate(lines):
        if l.startswith("# "):
            title = l[2:].strip()
            lines = lines[k + 1:]
            break
    # split on H2
    pre, sections, cur = [], [], None
    for l in lines:
        m = re.match(r"^##\s+(.*)$", l)
        if m:
            cur = {"title": m.group(1).strip(), "lines": []}
            sections.append(cur)
        elif cur is None:
            pre.append(l)
        else:
            cur["lines"].append(l)
    pre_nodes = parse_blocks(pre, ctx)
    short = ""
    preface = []
    for nd in pre_nodes:
        if not short and nd["t"] == "quote" and "Short answer" in nd["md"]:
            md = re.sub(r"^\*\*Short answer:\*\*\s*", "", nd["md"].strip())
            short = "<br>".join(inline(x, ctx) for x in md.split("\n"))
        else:
            preface.append(nd["html"])
    out_sections, kp, related, sources = [], [], [], []
    first_chart = None
    for sec in sections:
        kind = section_kind(sec["title"])
        nodes = parse_blocks(sec["lines"], ctx)
        for nd in nodes:
            if nd["t"] == "figure" and first_chart is None:
                first_chart = nd
        if kind == "evidence" and not kp:
            kp = key_points(nodes)
        if kind == "related":
            for nd in nodes:
                if nd["t"] == "list":
                    for _, _, text in nd["items"]:
                        m = re.match(r"^\[([^\]]+)\]\(([^)\s]+)\)", text.strip())
                        if m:
                            target = os.path.normpath(os.path.join(ctx.dir, m.group(2).split("#")[0])).replace(os.sep, "/")
                            if target in PAGE_SLUGS:
                                related.append({"slug": PAGE_SLUGS[target], "text": m.group(1)})
        if kind == "sources":
            lst = next((nd for nd in nodes if nd["t"] == "list"), None)
            sources = parse_sources(lst, ctx)
            rest = [nd["html"] for nd in nodes if nd is not lst]
            body = "".join(rest)
        else:
            body = "".join(nd["html"] for nd in nodes)
        out_sections.append({
            "id": "s-" + gh_anchor(sec["title"]),
            "title": inline(sec["title"], ctx),
            "kind": kind,
            "html": body,
            "words": word_count(body) + (sum(word_count(s["html"]) for s in sources) if kind == "sources" else 0),
        })
    words = word_count(short) + sum(s["words"] for s in out_sections) + sum(word_count(p) for p in preface)
    return {
        "path": path,
        "slug": PAGE_SLUGS[path],
        "folder": path[:2],
        "q": inline(title, ctx),
        "qtext": title,
        "short": short,
        "shortWords": word_count(short),
        "preface": "".join(preface),
        "keys": [{"lead": inline(lead, ctx), "rest": "<br>".join(inline(x, ctx) for x in rest.split("\n")) if rest.strip() else ""}
                 for _, lead, rest in kp],
        "chart": first_chart["key"] if first_chart else None,
        "chartCap": first_chart["cap"] if first_chart else "",
        "chartAlt": first_chart["alt"] if first_chart else "",
        "sections": out_sections,
        "related": related,
        "sources": sources,
        "words": words,
        "reviewed": reviewed,
        "url": GH + path,
        "text": strip_tags(" ".join([title, short] + [s["html"] for s in out_sections]))[:20000],
    }


# ---------------------------------------------------------------- README + folders
def parse_readme():
    raw = (ROOT / "README.md").read_text(encoding="utf-8")
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    ctx = Ctx("README.md")
    folders = {}
    for m in re.finditer(r"^\|\s*(\d\d)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*$", raw, flags=re.M):
        folders[m.group(1)] = {"id": m.group(1), "title": m.group(2), "covers": m.group(4)}
    worries = []
    part = raw.split("## Find your worry", 1)[1] if "## Find your worry" in raw else ""
    part = re.split(r"^## ", part, maxsplit=1, flags=re.M)[0]
    folder = None
    for l in part.split("\n"):
        m = re.match(r"^###\s+\[([^\]]+)\]\(([^)]+)\)", l)
        if m:
            folder = m.group(2)[:2]
            if folder in folders:
                folders[folder]["heading"] = m.group(1)
            continue
        m = re.match(r"^-\s+(.*)$", l)
        if m and folder:
            text = m.group(1)
            links = re.findall(r"\[([^\]]+)\]\(([^)\s]+)\)", text)
            if not links:
                continue
            href = links[0][1]
            target = os.path.normpath(href.split("#")[0])
            anchor = href.split("#")[1] if "#" in href else ""
            full = re.match(r"^\[([^\]]+)\]\(([^)\s]+)\)$", text.strip())
            if full:
                q, note = full.group(1), ""
            else:
                plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
                q, _, note = plain.partition("? ")
                q = q + "?" if note else plain
            if target in PAGE_SLUGS:
                worries.append({"folder": folder, "q": html.escape(q), "note": html.escape(note),
                                "slug": PAGE_SLUGS[target], "anchor": anchor})
    lead = re.search(r"^# .*?\n\n(.*?)\n", raw, flags=re.S)
    return folders, worries, inline(lead.group(1), ctx) if lead else ""


def folder_order(fid):
    """Page order and one-line blurbs from the folder README."""
    fdir = next(f for f in FOLDERS if f.startswith(fid))
    p = ROOT / fdir / "README.md"
    order = []
    if p.exists():
        ctx = Ctx(fdir + "/README.md")
        for m in re.finditer(r"^-\s+\[([^\]]+)\]\(([^)\s]+)\)(?::\s*(.*))?$", p.read_text(encoding="utf-8"), flags=re.M):
            target = os.path.normpath(os.path.join(fdir, m.group(2))).replace(os.sep, "/")
            if target in PAGE_SLUGS:
                order.append({"slug": PAGE_SLUGS[target], "blurb": inline(m.group(3) or "", ctx)})
    seen = {o["slug"] for o in order}
    for path in PAGE_PATHS:
        if path.startswith(fdir + "/") and PAGE_SLUGS[path] not in seen:
            order.append({"slug": PAGE_SLUGS[path], "blurb": ""})
    return order


def evidence_explainers():
    """Plain-word meanings of the evidence labels, verbatim from how-to-read-the-evidence."""
    path = "08-reading-this-well/how-to-read-the-evidence.md"
    p = ROOT / path
    out = {"grades": {}, "other": "", "source": PAGE_SLUGS.get(path)}
    if not p.exists():
        return out
    raw = p.read_text(encoding="utf-8")
    m = re.search(r"### The evidence labels used on every page\n(.*?)(?=\n##)", raw, flags=re.S)
    if not m:
        return out
    ctx = Ctx(path)
    for g, text in re.findall(r"^- \*\*(\w+):\*\*\s*(.*)$", m.group(1), flags=re.M):
        out["grades"][g] = inline(text, ctx)
    paras = [x.strip() for x in m.group(1).split("\n\n") if x.strip() and not x.strip().startswith(("-", "Each"))]
    out["other"] = "".join("<p>%s</p>" % inline(x, ctx) for x in paras)
    return out


# ---------------------------------------------------------------- conflicts
def load_conflicts():
    recs = []
    files = 0
    if conflicts_dir.is_dir():
        for f in sorted(conflicts_dir.glob("*.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except Exception as e:  # half-written file: skip it, keep building
                print("  skipped %s (%s)" % (f.name, e), file=sys.stderr)
                continue
            if isinstance(data, dict):
                data = data.get("records") or data.get("conflicts") or [data]
            if not isinstance(data, list):
                continue
            files += 1
            for r in data:
                if not isinstance(r, dict) or not r.get("claim") and not r.get("topic"):
                    continue
                page = str(r.get("page") or "").split("#")[0].lstrip("./")
                positions = []
                for pos in r.get("positions") or []:
                    if not isinstance(pos, dict):
                        continue
                    srcs = []
                    for s in pos.get("sources") or []:
                        if isinstance(s, dict):
                            srcs.append({k: s.get(k) for k in ("citation", "doi", "pmid", "year", "design", "n", "cited_on_page", "verified")})
                        elif isinstance(s, str):
                            srcs.append({"citation": s})
                    positions.append({"label": pos.get("label") or "", "summary": pos.get("summary") or "", "sources": srcs})
                recs.append({
                    "id": r.get("id") or "",
                    "topic": r.get("topic") or "",
                    "page": PAGE_SLUGS.get(page),
                    "pagePath": page,
                    "claim": r.get("claim") or "",
                    "positions": positions,
                    "type": r.get("conflict_type") or "",
                    "why": r.get("why_they_may_differ") or "",
                    "handling": r.get("page_handling") or "",
                    "severity": r.get("severity") or "",
                    "next": r.get("next_step") or "",
                    "newResearch": bool(r.get("new_research")),
                })
    order = {"major": 0, "moderate": 1, "minor": 2}
    recs.sort(key=lambda r: (r["pagePath"], order.get(str(r["severity"]).lower(), 3), r["id"]))
    return recs, files


# ---------------------------------------------------------------- main
def main():
    folders, worries, lead = parse_readme()
    corpus = ROOT / "assets" / "charts" / "corpus" / "corpus.json"
    if corpus.exists():
        try:
            for f in json.loads(corpus.read_text(encoding="utf-8")).get("folders", []):
                if f["id"] in folders:
                    folders[f["id"]]["short"] = f.get("short") or folders[f["id"]]["title"]
        except Exception:
            pass
    pages = [parse_page(p) for p in PAGE_PATHS]
    for fid in folders:
        folders[fid]["pages"] = folder_order(fid)
        folders[fid].setdefault("short", folders[fid]["title"])
        folders[fid]["title"] = html.escape(folders[fid]["title"])
        folders[fid]["covers"] = html.escape(folders[fid]["covers"])
    conflicts, conflict_files = load_conflicts()
    data = {
        "gh": GH,
        "crisis": CRISIS,
        "lead": lead,
        "folders": [folders[k] for k in sorted(folders)],
        "worries": worries,
        "pages": pages,
        "evidence": evidence_explainers(),
        "conflicts": conflicts,
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    charts = json.dumps(CHARTS, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (HERE / "template.html").read_text(encoding="utf-8")
    out = tpl.replace("__READER_DATA__", blob).replace("__CHART_DATA__", charts)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(".tmp")
    tmp.write_text(out, encoding="utf-8")
    tmp.replace(out_path)
    n_src = sum(len(p["sources"]) for p in pages)
    print("%s written: %d pages, %d worries, %d charts, %d sources, %d conflicts (%d files), %d KB"
          % (out_path, len(pages), len(worries), len(CHARTS), n_src, len(conflicts), conflict_files, len(out) // 1024))


if __name__ == "__main__":
    main()
