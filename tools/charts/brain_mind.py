#!/usr/bin/env python3
"""Charts for folders 02 (brain) and 03 (thinking and feeling).

Stdlib only. This script is the source of truth: it writes every chart in
assets/charts/02/ and assets/charts/03/ as a light SVG and a dark SVG.

    python3 tools/charts/brain_mind.py

Every number plotted here is copied from the page the chart sits on (same
source, same rounding). Overlap percentages are those pages' own calculation,
OVL = 2 * Phi(-|d| / 2), and are labelled as such.
"""

import math
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = {
    "02": os.path.join(ROOT, "assets", "charts", "02"),
    "03": os.path.join(ROOT, "assets", "charts", "03"),
}

W = 720
FONT = 'system-ui, -apple-system, &quot;Segoe UI&quot;, Roboto, sans-serif'

# Validated reference palette (dataviz skill, references/palette.md).
THEMES = {
    "light": {
        "surface": "#ffffff",
        "ink": "#191919",
        "ink2": "#666666",
        "grid": "#e7e7e7",
        "axis": "#c2c2c2",
        "s1": "#257de0",
        "s2": "#f47230",
        "overlap": "#9c9c9c",
        "border": "rgba(11,11,11,0.10)",
    },
    "dark": {
        "surface": "#191919",
        "ink": "#efefef",
        "ink2": "#9c9c9c",
        "grid": "#303030",
        "axis": "#474747",
        "s1": "#338ced",
        "s2": "#e76624",
        "overlap": "#8a8a8a",
        "border": "rgba(255,255,255,0.10)",
    },
}

MINUS = "−"


def num(x, dp=2):
    """Format a number with a true minus sign."""
    s = f"{abs(x):.{dp}f}"
    return (MINUS + s) if x < 0 else s


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def ovl(d):
    return 2 * phi(-abs(d) / 2)


class Svg:
    def __init__(self, theme, height, title, desc):
        self.t = THEMES[theme]
        self.h = height
        self.parts = []
        self.title = title
        self.desc = desc

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=14, color="ink", anchor="start", weight=400, italic=False):
        style = ' font-style="italic"' if italic else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{self.t[color]}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{style}>{escape(s)}</text>'
        )

    def line(self, x1, y1, x2, y2, color="grid", width=1, cap="butt"):
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{self.t[color]}" stroke-width="{width}" stroke-linecap="{cap}"/>'
        )

    def dot(self, x, y, r=5, color="s1"):
        # 2px surface ring keeps dots legible over lines and each other.
        self.add(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{self.t[color]}" '
            f'stroke="{self.t["surface"]}" stroke-width="2"/>'
        )

    def capsule(self, x1, x2, y, h=8, color="s1", opacity=1.0):
        self.add(
            f'<rect x="{x1:.1f}" y="{y - h / 2:.1f}" width="{max(x2 - x1, h):.1f}" height="{h}" '
            f'rx="{h / 2}" fill="{self.t[color]}" fill-opacity="{opacity}"/>'
        )

    def hbar(self, x0, x1, y, h=24, color="s1", r=4):
        """Horizontal bar from baseline x0 to data end x1: square at baseline, 4px round at data end."""
        top, bot = y - h / 2, y + h / 2
        if x1 >= x0:
            d = (f"M{x0:.1f},{top:.1f} H{x1 - r:.1f} Q{x1:.1f},{top:.1f} {x1:.1f},{top + r:.1f} "
                 f"V{bot - r:.1f} Q{x1:.1f},{bot:.1f} {x1 - r:.1f},{bot:.1f} H{x0:.1f} Z")
        else:
            d = (f"M{x0:.1f},{top:.1f} H{x1 + r:.1f} Q{x1:.1f},{top:.1f} {x1:.1f},{top + r:.1f} "
                 f"V{bot - r:.1f} Q{x1:.1f},{bot:.1f} {x1 + r:.1f},{bot:.1f} H{x0:.1f} Z")
        self.add(f'<path d="{d}" fill="{self.t[color]}"/>')

    def header(self, title_lines, subtitle_lines):
        y = 34
        for ln in title_lines:
            self.text(24, y, ln, size=18, weight=600)
            y += 24
        y += 2
        for ln in subtitle_lines:
            self.text(24, y, ln, size=14, color="ink2")
            y += 20
        return y

    def footer(self, source_lines):
        y = self.h - 18 - 18 * (len(source_lines) - 1)
        for ln in source_lines:
            self.text(24, y, ln, size=13, color="ink2")
            y += 18

    def render(self):
        t = self.t
        head = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {self.h}" width="{W}" '
            f'height="{self.h}" role="img" aria-labelledby="t d" font-family="{FONT}">\n'
            f'<title id="t">{escape(self.title)}</title>\n<desc id="d">{escape(self.desc)}</desc>\n'
            f'<rect x="0.5" y="0.5" width="{W - 1}" height="{self.h - 1}" rx="8" '
            f'fill="{t["surface"]}" stroke="{t["border"]}"/>\n'
        )
        return head + "\n".join(self.parts) + "\n</svg>\n"


def write(folder, name, build):
    os.makedirs(OUT[folder], exist_ok=True)
    for theme in ("light", "dark"):
        svg = build(theme)
        suffix = "" if theme == "light" else "-dark"
        path = os.path.join(OUT[folder], f"{name}{suffix}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg.render())
        print("wrote", os.path.relpath(path, ROOT))


# ---------------------------------------------------------------- helpers


def x_axis(s, x0, x1, y_top, y_bot, lo, hi, ticks, fmt, small=None, zero_line=True,
           left_note=None, right_note=None):
    """Gridlines, tick labels below y_bot, optional 'small' markers and direction notes."""
    sx = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    for v in ticks:
        if zero_line and abs(v) < 1e-9:
            continue
        s.line(sx(v), y_top, sx(v), y_bot, "grid")
    if small is not None:
        for v in small:
            s.line(sx(v), y_top, sx(v), y_bot, "axis", 1.5)
    if zero_line and lo <= 0 <= hi:
        s.line(sx(0), y_top, sx(0), y_bot, "axis", 1.5)
    for v in ticks:
        s.text(sx(v), y_bot + 20, fmt(v), size=13, color="ink2", anchor="middle")
    if left_note:
        s.text(x0, y_bot + 42, left_note, size=13, color="ink2", anchor="start")
    if right_note:
        s.text(x1, y_bot + 42, right_note, size=13, color="ink2", anchor="end")
    return sx


# ---------------------------------------------------------------- 02 charts


def enigma_subcortical(theme):
    rows = [
        ("Amygdala", "emotion", -0.19, "about 92%"),
        ("Nucleus accumbens", "reward", -0.15, "about 94%"),
        ("Putamen", "movement, habits", -0.14, "about 94%"),
        ("Caudate", "goal-directed action", -0.11, "about 96%"),
        ("Hippocampus", "memory", -0.11, "about 96%"),
        ("Whole-skull volume", "intracranial", -0.10, "about 96%"),
    ]
    row_h = 44
    s = Svg(theme, 0, "Deep brain structures differ only slightly in ADHD, on average",
            "Dot plot of ENIGMA-ADHD effect sizes (Cohen's d), all between -0.10 and -0.19, "
            "inside the conventional 'small' threshold of 0.2.")
    top = 34 + 24 * 2 + 2 + 20 * 2 + 28
    plot_bot = top + row_h * len(rows)
    s.h = plot_bot + 60 + 50
    y = s.header(["Deep brain structures were only very slightly smaller,",
                  "on average, in the ADHD group"],
                 ["Effect size (Cohen’s d) for 1,713 people with ADHD vs 1,529 without.",
                  "Every value is smaller than 0.2, the conventional “small” effect."])
    x0, x1 = 250, 560
    lo, hi = -0.3, 0.3
    s.text(580, top - 10, "Groups overlap", size=13, color="ink2")
    sx = x_axis(s, x0, x1, top - 4, plot_bot, lo, hi, [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3],
                lambda v: num(v, 1) if v else "0", small=[-0.2, 0.2],
                left_note="← smaller in ADHD", right_note="larger in ADHD →")
    s.text(sx(-0.2), top - 10, "small", size=13, color="ink2", anchor="middle")
    s.text(sx(0.2), top - 10, "small", size=13, color="ink2", anchor="middle")
    for i, (name, role, d, ov) in enumerate(rows):
        cy = top + row_h * i + row_h / 2
        s.text(24, cy - 2, name, size=14)
        s.text(24, cy + 15, role, size=13, color="ink2")
        s.line(sx(d), cy, sx(0), cy, "s1", 2, "round")
        s.dot(sx(d), cy, 6)
        s.text(sx(d) - 12, cy + 5, num(d), size=13, color="ink", anchor="end")
        s.text(580, cy + 5, ov, size=14)
    s.footer(["Source: Hoogman et al. 2017, Lancet Psychiatry — see source 1 on this page.",
              "Overlap is this page’s calculation from each effect size, not a figure from the paper."])
    return s


def bell_pair(theme, d, ov_label, title_lines, sub_lines, group_a, group_b, axis_label,
              source_lines, desc, a_left=True, a_color="s1", b_color="s2"):
    """Two equal-spread normal curves whose means differ by |d| SDs; overlap shaded."""
    s = Svg(theme, 0, " ".join(title_lines), desc)
    top = 34 + 24 * len(title_lines) + 2 + 20 * len(sub_lines) + 30
    plot_h = 190
    base = top + plot_h
    s.h = base + 40 + 18 * len(source_lines) + 26
    s.header(title_lines, sub_lines)
    x0, x1 = 60, 660
    lo, hi = -3.6, 3.6
    sx = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    pdf = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    peak = pdf(0)
    sy = lambda p: base - p / peak * (plot_h - 20)
    ma, mb = (-abs(d) / 2, abs(d) / 2) if a_left else (abs(d) / 2, -abs(d) / 2)
    xs = [lo + (hi - lo) * i / 360 for i in range(361)]

    def path(fn):
        pts = " ".join(f"L{sx(x):.1f},{sy(fn(x)):.1f}" for x in xs)
        return f"M{sx(lo):.1f},{base:.1f} {pts} L{sx(hi):.1f},{base:.1f} Z"

    def curve(fn):
        return "M" + " L".join(f"{sx(x):.1f},{sy(fn(x)):.1f}" for x in xs)

    fa = lambda x: pdf(x - ma)
    fb = lambda x: pdf(x - mb)
    t = s.t
    s.add(f'<path d="{path(fa)}" fill="{t[a_color]}" fill-opacity="0.14"/>')
    s.add(f'<path d="{path(fb)}" fill="{t[b_color]}" fill-opacity="0.14"/>')
    s.add(f'<path d="{path(lambda x: min(fa(x), fb(x)))}" fill="{t["overlap"]}" fill-opacity="0.38"/>')
    s.add(f'<path d="{curve(fb)}" fill="none" stroke="{t[b_color]}" stroke-width="2" stroke-linejoin="round"/>')
    s.add(f'<path d="{curve(fa)}" fill="none" stroke="{t[a_color]}" stroke-width="2" stroke-linejoin="round"/>')
    s.line(x0, base, x1, base, "axis", 1)
    # Average markers
    for m, col in ((ma, a_color), (mb, b_color)):
        s.line(sx(m), sy(peak), sx(m), base, col, 1.5)
    # Overlap label in the middle of the shared area
    s.text(sx(0), base - 62, ov_label, size=16, weight=600, anchor="middle")
    s.text(sx(0), base - 42, "overlap", size=14, anchor="middle")
    # Legend-style direct labels with swatches, placed at the outer shoulders
    la_x, lb_x = (sx(-2.15), sx(2.15))
    if not a_left:
        la_x, lb_x = lb_x, la_x
    for (lx, label, col, anchor) in ((la_x, group_a, a_color, "end" if a_left else "start"),
                                     (lb_x, group_b, b_color, "start" if a_left else "end")):
        ly = sy(pdf(2.15)) - 30
        sw = lx - 14 if anchor == "end" else lx
        tx = lx - 20 if anchor == "end" else lx + 18
        s.add(f'<rect x="{sw - (0 if anchor == "start" else 0):.1f}" y="{ly - 6:.1f}" width="12" height="4" rx="2" fill="{t[col]}"/>')
        s.text(tx, ly, label, size=14, anchor=anchor)
    s.text(sx(0), base + 22, axis_label, size=13, color="ink2", anchor="middle")
    s.footer(source_lines)
    return s


def amygdala_overlap(theme):
    return bell_pair(
        theme, 0.19, "about 92%",
        ["With an effect size of −0.19, the two groups’",
         "amygdala sizes are almost completely mixed"],
        ["Illustration: two bell curves 0.19 standard deviations apart, the amygdala",
         "difference in the largest study. The grey area is shared by both groups."],
        "People with ADHD", "People without ADHD",
        "Amygdala volume → (larger to the right)",
        ["Source: Hoogman et al. 2017, Lancet Psychiatry — see source 1 on this page.",
         "Overlap is this page’s calculation, OVL = 2Φ(−|d|/2); real volumes only roughly follow bell curves."],
        "Two overlapping bell curves, means 0.19 standard deviations apart, the ADHD curve slightly "
        "to the left; about 92% of the area is shared.",
        a_left=True)


def classifier_vs_chance(theme):
    s = Svg(theme, 0, "Brain-scan classifiers are only a little better than chance",
            "Two scales. Accuracy: careful studies 60-80% vs 50% coin toss and an 80% proposed bar. "
            "AUROC: best ABCD structural model 0.567 vs 0.5 chance and 1.0 perfect.")
    title = ["Scan-based classifiers sit closer to a coin toss",
             "than to a usable diagnostic test"]
    sub = ["Two measures, each on its own scale."]
    y = s.header(title, sub)
    x0, x1 = 40, 600
    # Panel A
    pa = y + 18
    s.text(24, pa, "Accuracy in studies that tested on separate data (review of 69 studies)", size=14, weight=600)
    ty = pa + 64
    sx = lambda v: x0 + v / 100 * (x1 - x0)
    for v in (0, 25, 50, 75, 100):
        s.line(sx(v), ty - 26, sx(v), ty + 12, "grid")
        s.text(sx(v), ty + 32, f"{v}%", size=13, color="ink2", anchor="middle")
    s.line(x0, ty + 12, x1, ty + 12, "axis")
    s.capsule(sx(60), sx(80), ty, h=12)
    s.text((sx(60) + sx(80)) / 2, ty - 16, "mostly 60–80%", size=14, anchor="middle")
    s.line(sx(50), ty - 30, sx(50), ty + 12, "ink2", 1.5)
    s.text(sx(50) - 8, ty - 34, "coin toss, 50%", size=13, color="ink2", anchor="end")
    s.line(sx(80), ty - 30, sx(80), ty + 12, "ink", 1.5)
    s.text(sx(80) + 8, ty - 34, "proposed bar for a test: 80%", size=13, color="ink", anchor="start")
    s.text(sx(80) + 8, ty - 18, "sensitivity and specificity", size=13, color="ink2", anchor="start")
    # Panel B
    pb = ty + 74
    s.text(24, pb, "AUROC of the best structural-scan model, 6,916 children (ABCD Study)", size=14, weight=600)
    ty2 = pb + 64
    sb = lambda v: x0 + (v - 0.5) / 0.5 * (x1 - x0)
    for v in (0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
        s.line(sb(v), ty2 - 26, sb(v), ty2 + 12, "grid")
        s.text(sb(v), ty2 + 32, f"{v:.1f}", size=13, color="ink2", anchor="middle")
    s.line(x0, ty2 + 12, x1, ty2 + 12, "axis")
    s.line(sb(0.5), ty2, sb(0.567), ty2, "s1", 2, "round")
    s.dot(sb(0.567), ty2, 6)
    s.text(sb(0.567) + 12, ty2 + 5, "0.567", size=14, weight=600)
    s.text(sb(0.5) + 4, ty2 - 16, "0.5 = coin toss", size=13, color="ink2")
    s.text(sb(1.0), ty2 - 16, "1.0 = perfect", size=13, color="ink2", anchor="end")
    s.h = ty2 + 32 + 26 + 18 * 2 + 10
    s.footer(["Sources: Pulini et al. 2019 (source 19), APA work group 2012 (24) and Gaus et al. 2023 (21),",
              "see this page. The proposed bar is 80% sensitivity and 80% specificity, not accuracy itself."])
    return s


def dat_direction(theme):
    rows = [
        ("One PET study, never-medicated adults", "53 with ADHD vs 44 without; nucleus accumbens",
         -11, "about 11% lower"),
        ("Pooled 9 PET and SPECT studies", "169 with ADHD vs 173 without; striatum",
         14, "14% higher"),
    ]
    s = Svg(theme, 0, "Dopamine transporter studies disagree on direction",
            "Diverging bars: one PET study about 11% lower in ADHD; a meta-analysis of 9 studies 14% higher.")
    y = s.header(["Dopamine transporter scans point in opposite",
                  "directions, so they cannot show a “deficiency”"],
                 ["Average dopamine transporter level in ADHD compared with people without ADHD."])
    top = y + 24
    row_h = 64
    plot_bot = top + row_h * len(rows)
    x0, x1 = 360, 680
    sx = x_axis(s, x0, x1, top - 6, plot_bot, -30, 30, [-30, -20, -10, 0, 10, 20, 30],
                lambda v: (f"+{v}%" if v > 0 else (f"{MINUS}{abs(v)}%" if v < 0 else "0")),
                left_note="← lower in ADHD", right_note="higher in ADHD →")
    for i, (name, sub, v, lab) in enumerate(rows):
        cy = top + row_h * i + row_h / 2
        s.text(24, cy - 2, name, size=14)
        s.text(24, cy + 16, sub, size=13, color="ink2")
        s.hbar(sx(0), sx(v), cy, 24)
        if v < 0:
            s.text(sx(v) - 8, cy + 5, lab, size=13, anchor="end")
        else:
            s.text(sx(v) + 8, cy + 5, lab, size=13, anchor="start")
    s.h = plot_bot + 42 + 30 + 18 * 2
    s.footer(["Sources: Volkow et al. 2009, JAMA (source 1) and Fusar-Poli et al. 2012 (source 3), see this page.",
              "The 11% is this page’s calculation from the paper’s figures (0.63 vs 0.71)."])
    return s


# ---------------------------------------------------------------- 03 charts


def dot_rows(s, rows, top, row_h, x0, x1, lo, hi, ticks, small=0.2, value_dx=12, axis_note=None):
    """Rows of ('label', 'sub', kind, values, value_label) on a zero-anchored magnitude axis.

    kind: 'dot' (values = [v,...]), 'range' (values = [lo, hi]), 'open' (values = [lo], arrow right),
    'head' (group heading; values ignored), 'text' (no mark, value_label only).
    """
    plot_bot = top + sum(row_h if r[2] != "head" else 30 for r in rows)
    sx = x_axis(s, x0, x1, top - 6, plot_bot, lo, hi, ticks,
                lambda v: "0" if v == 0 else f"{v:.1f}", small=[small])
    s.text(sx(small), top - 12, "small", size=13, color="ink2", anchor="middle")
    if axis_note:
        s.text(x1, plot_bot + 42, axis_note, size=13, color="ink2", anchor="end")
    y = top
    for label, sub, kind, vals, vlab in rows:
        if kind == "head":
            s.text(24, y + 21, label, size=14, weight=600)
            y += 30
            continue
        cy = y + row_h / 2
        if sub:
            s.text(24, cy - 2, label, size=14)
            s.text(24, cy + 15, sub, size=13, color="ink2")
        else:
            s.text(24, cy + 5, label, size=14)
        if kind == "dot":
            s.line(sx(0), cy, sx(max(vals)), cy, "s1", 2, "round")
            for v in vals:
                s.dot(sx(v), cy, 6)
            s.text(sx(max(vals)) + value_dx, cy + 5, vlab, size=13)
        elif kind == "range":
            s.line(sx(0), cy, sx(vals[0]), cy, "s1", 2, "round")
            s.capsule(sx(vals[0]), sx(vals[1]), cy, h=12)
            s.text(sx(vals[1]) + value_dx, cy + 5, vlab, size=13)
        elif kind == "open":
            s.line(sx(0), cy, sx(vals[0]), cy, "s1", 2, "round")
            s.dot(sx(vals[0]), cy, 6)
            ax = sx(vals[0]) + 40
            s.line(sx(vals[0]) + 8, cy, ax, cy, "s1", 2, "round")
            t = s.t
            s.add(f'<path d="M{ax - 6:.1f},{cy - 5:.1f} L{ax + 2:.1f},{cy:.1f} L{ax - 6:.1f},{cy + 5:.1f}" '
                  f'fill="none" stroke="{t["s1"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
            s.text(ax + 10, cy + 5, vlab, size=13)
        elif kind == "text":
            s.text(sx(0) + 10, cy + 5, vlab, size=13, color="ink2", italic=True)
        y += row_h
    return plot_bot


def exec_function(theme):
    rows = [
        ("Mostly children and teenagers", "", "head", None, None),
        ("Executive tasks, 83 studies", "3,734 with ADHD vs 2,969 without", "range", [0.46, 0.69], "0.46–0.69"),
        ("Visual–spatial working memory", "26 studies, two measures", "dot", [0.85, 1.06], "0.85 and 1.06"),
        ("Verbal working memory", "words and numbers, two measures", "dot", [0.43, 0.47], "0.43 and 0.47"),
        ("Adults (13 studies)", "", "head", None, None),
        ("Verbal fluency", "", "dot", [0.62], "0.62"),
        ("Inhibition", "two measures", "dot", [0.64, 0.89], "0.64 and 0.89"),
        ("Set shifting", "switching tasks or rules", "dot", [0.65], "0.65"),
        ("Consistency of responding", "not an executive measure", "dot", [0.57], "0.57"),
        ("Speed of naming colours", "not an executive measure", "dot", [0.62], "0.62"),
    ]
    s = Svg(theme, 0, "Executive-function gaps are medium-sized in children and adults",
            "Dot plot of effect sizes (d) for ADHD vs comparison groups: children 0.43 to 1.06, adults 0.57 to 0.89.")
    y = s.header(["On average, executive gaps are medium-sized,",
                  "in children and in adults"],
                 ["Effect size (d): how far apart the group averages are, in standard deviations.",
                  "Further right = weaker average performance in the ADHD group."])
    top = y + 22
    bot = dot_rows(s, rows, top, 42, 330, 600, 0, 1.2, [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
    s.h = bot + 30 + 26 + 18 * 2 + 6
    s.footer(["Sources: Willcutt et al. 2005 (source 1), Martinussen et al. 2005 (3), Boonstra et al. 2005 (4),",
              "see this page. Even at 0.69 the groups’ scores overlap by about 73% (this page’s calculation)."])
    return s


def rt_variability(theme):
    rows = [
        ("ADHD vs typically developing peers", "", "head", None, None),
        ("Children and teenagers", "", "dot", [0.76], "g = 0.76"),
        ("Adults", "", "dot", [0.46], "g = 0.46"),
        ("ADHD vs other clinical conditions", "", "head", None, None),
        ("Children", "", "dot", [0.25], "g = 0.25"),
        ("Teenagers and adults", "", "text", None, "could not be told apart"),
    ]
    s = Svg(theme, 0, "Reaction times vary more in ADHD, but not much more than in other conditions",
            "Dot plot of Hedges' g for reaction-time variability: 0.76 children vs peers, 0.46 adults vs peers, "
            "0.25 children vs other clinical groups; teenagers and adults not distinguishable from other clinical groups.")
    y = s.header(["Reaction times are more variable in ADHD, but only",
                  "slightly more than in other conditions"],
                 ["Trial-to-trial reaction-time variability, effect size (g), from 319 studies.",
                  "Further right = more variable on average in the ADHD group."])
    top = y + 22
    bot = dot_rows(s, rows, top, 40, 330, 640, 0, 1.0, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
    s.h = bot + 30 + 26 + 18 + 6
    s.footer(["Source: Kofler et al. 2013, Clinical Psychology Review — see source 1 on this page."])
    return s


def time_and_rewards(theme):
    rows = [
        ("Time perception, young people (27 studies)", "", "head", None, None),
        ("Less precise", "", "dot", [0.66], "g = 0.66"),
        ("Less accurate", "", "open", [0.40], "g above 0.40"),
        ("Preferring “now” over “later”", "", "head", None, None),
        ("Delay discounting, all ages", "21 studies, 3,913 participants", "dot", [0.43], "d = 0.43"),
        ("\u201cNow\u201d choices, children and teens", "26 studies, 4,320 young people", "dot", [0.47], "g = 0.47"),
    ]
    s = Svg(theme, 0, "Time perception and preference for sooner rewards differ by a medium amount",
            "Dot plot: time-perception precision g = 0.66, accuracy g above 0.40, delay discounting d = 0.43, "
            "children's choice-impulsivity g = 0.47.")
    y = s.header(["Time perception and the pull of “now” differ",
                  "by a medium amount, on average"],
                 ["Effect size (d or g) for ADHD vs comparison groups, in standard deviations.",
                  "Further right = larger average difference."])
    top = y + 22
    bot = dot_rows(s, rows, top, 42, 330, 640, 0, 1.0, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
    s.h = bot + 30 + 26 + 18 * 2 + 6
    s.footer(["Sources: Zheng et al. 2022 (source 2), Jackson & MacKillop 2016 (3), Patros et al. 2016 (4),",
              "see this page. Even at g = 0.66 the groups overlap by about 74% (this page’s calculation)."])
    return s


def emotion_overlap(theme):
    return bell_pair(
        theme, 1.17, "about 56%",
        ["A large average difference in emotion dysregulation",
         "still leaves the groups overlapping by more than half"],
        ["Illustration: two bell curves 1.17 standard deviations apart, the adult",
         "meta-analysis result. The grey area is shared by both groups."],
        "Adults without ADHD", "Adults with ADHD",
        "Emotion dysregulation score → (more to the right)",
        ["Source: Beheshti et al. 2020, BMC Psychiatry — see source 2 on this page.",
         "Overlap is this page’s calculation, OVL = 2Φ(−|g|/2); mostly self-report, 13 studies."],
        "Two bell curves 1.17 standard deviations apart, ADHD to the right; about 56% of the area is shared.",
        a_left=True, a_color="s2", b_color="s1")


CHARTS = [
    ("02", "enigma-subcortical-effect-sizes", enigma_subcortical),
    ("02", "amygdala-overlap", amygdala_overlap),
    ("02", "scan-classifiers-vs-chance", classifier_vs_chance),
    ("02", "dopamine-transporter-direction", dat_direction),
    ("03", "executive-function-effect-sizes", exec_function),
    ("03", "reaction-time-variability", rt_variability),
    ("03", "time-and-reward-effect-sizes", time_and_rewards),
    ("03", "emotion-dysregulation-overlap", emotion_overlap),
]


def self_check():
    # The overlap labels must match the pages' own rounding.
    assert round(ovl(0.19) * 100) == 92
    assert round(ovl(1.17) * 100) == 56
    assert round(ovl(0.69) * 100) == 73
    assert round(ovl(0.66) * 100) == 74
    for d, pct in ((0.15, 94), (0.14, 94), (0.11, 96), (0.10, 96)):
        assert round(ovl(d) * 100) == pct, d


if __name__ == "__main__":
    self_check()
    for folder, name, fn in CHARTS:
        write(folder, name, fn)
