"""Shared chart style for every script in tools/charts/ (standard library only).

Colours, type sizes and radii come from tools/design/tokens.json, the same file
the reader and the explorer use, so static charts and both HTML tools match.
This module only draws the common frame: the card, the header block (takeaway
title + subtitle), the source footer, and text measuring. Each chart script
draws its own marks.
"""

import sys
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "design"))
import tokens as _tokens  # noqa: E402

TOK = _tokens.load()
TYPE = TOK["chart_type"]
RADIUS = TOK["radius"]
W = TYPE["width"]
PAD = TYPE["pad"]
FONT = TOK["font"]["chart"]            # GitHub shows SVGs through <img>, so no web fonts
FONT_ATTR = escape(FONT, {'"': "&quot;"})


def theme(mode):
    """Chart colours for 'light' or 'dark'. 'border' is the card outline."""
    c = _tokens.colors(mode)
    c["border"] = c["line"]
    c["evidence"] = [c["ev_strong"], c["ev_moderate"], c["ev_limited"],
                     c["ev_contested"], c["ev_guideline"], c["ev_other"]]
    return c


def text_width(s, size=13, bold=False):
    """Rough rendered width of a system sans, erring wide, to keep labels clear of marks."""
    w = 0.0
    for ch in str(s):
        if ch in "iljtf.,:;'!|()[] ":
            w += 0.30
        elif ch in "mwMW%":
            w += 0.85
        elif ch.isupper() or ch.isdigit():
            w += 0.63
        else:
            w += 0.54
    return w * size * (1.06 if bold else 1.0)


def wrap(s, size, maxw, bold=False):
    words, lines, cur = str(s).split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if text_width(trial, size, bold) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def wrap_balanced(s, size, maxw, bold=False):
    """Like CSS text-wrap: balance - same line count as greedy, lines of even length."""
    lines = wrap(s, size, maxw, bold)
    if len(lines) < 2:
        return lines
    lo, hi = maxw * 0.4, maxw
    for _ in range(18):
        mid = (lo + hi) / 2
        if len(wrap(s, size, mid, bold)) <= len(lines):
            hi = mid
        else:
            lo = mid
    return wrap(s, size, hi, bold)


def text(th, x, y, s, size=None, fill="ink", weight=None, anchor="start", italic=False, extra=""):
    """One <text>. size/weight default to the label style; fill is a token name or a colour."""
    size = size or TYPE["label"]["size"]
    weight = weight or TYPE["label"]["weight"]
    colour = th.get(fill, fill)
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{colour}" text-anchor="{anchor}"{st}{extra}>{escape(str(s))}</text>')


def header(th, title, subtitle=None):
    """Takeaway title (balanced wrap) and a one-line subtitle. Returns (svg parts, content top y)."""
    tt, st = TYPE["title"], TYPE["subtitle"]
    maxw = W - 2 * PAD
    parts = []
    y = TYPE["first_baseline"]
    for i, ln in enumerate(wrap_balanced(title, tt["size"], maxw, True)):
        if i:
            y += tt["line"]
        parts.append(text(th, PAD, y, ln, tt["size"], "ink", tt["weight"]))
    if subtitle:
        sub = wrap(subtitle, st["size"], maxw)
        if len(sub) > 1:
            print(f"  note: subtitle wraps to {len(sub)} lines: {subtitle[:60]}...", file=sys.stderr)
        y += 6
        for ln in sub:
            y += st["line"]
            parts.append(text(th, PAD, y, ln, st["size"], "ink2", st["weight"]))
    return parts, y + 26


def footer(th, y, source):
    """Hairline rule, then the source line(s). `source` is a string (wrapped) or a list of lines.
    Returns (svg parts, total chart height)."""
    sz, lh = TYPE["source"]["size"], TYPE["source"]["line"]
    y += 16
    parts = [f'<line x1="{PAD}" x2="{W - PAD}" y1="{y:.1f}" y2="{y:.1f}" stroke="{th["grid"]}" stroke-width="1"/>']
    lines = source if isinstance(source, (list, tuple)) else wrap(source, sz, W - 2 * PAD)
    y += 6
    for ln in lines:
        y += lh
        parts.append(text(th, PAD, y, ln, sz, "ink2"))
    return parts, int(round(y + 18))


def document(th, height, title, desc, body, defs=None):
    """The SVG card: surface, 1px border, card radius, title/desc for assistive tech."""
    height = int(round(height))
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" width="{W}" height="{height}" '
        f'role="img" aria-labelledby="t d" font-family="{FONT_ATTR}">',
        f'<title id="t">{escape(title)}</title>',
        f'<desc id="d">{escape(desc)}</desc>',
    ]
    if defs:
        out.append("<defs>" + "".join(defs) + "</defs>")
    out.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{height - 1}" rx="{RADIUS["card"]}" '
               f'fill="{th["surface"]}" stroke="{th["border"]}" stroke-width="1"/>')
    out.extend(b for b in body if b)
    out.append("</svg>")
    return "\n".join(out) + "\n"


def hbar_d(x0, y, length, h, r=None):
    """Path data for a horizontal bar: square at the baseline, rounded data end."""
    r = RADIUS["mark"] if r is None else r
    if length <= 0:
        return ""
    r = min(r, length / 2, h / 2)
    x1 = x0 + length
    return (f"M{x0:.2f},{y:.2f} H{x1 - r:.2f} Q{x1:.2f},{y:.2f} {x1:.2f},{y + r:.2f} "
            f"V{y + h - r:.2f} Q{x1:.2f},{y + h:.2f} {x1 - r:.2f},{y + h:.2f} H{x0:.2f} Z")
