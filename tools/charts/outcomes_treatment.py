#!/usr/bin/env python3
"""Charts for folders 04-07 (outcomes, co-occurring conditions, treatment, family).

Standard library only. This script is the source of truth: run

    python3 tools/charts/outcomes_treatment.py

to regenerate every chart in assets/charts/04 ... assets/charts/07, each as a
light (`name.svg`) and a dark (`name-dark.svg`) file.

Every number drawn here is copied from the page the chart sits on, with the
same rounding and the same source number. Change the page first, then the
number here.

Colour follows the dataviz reference palette (light surface #ffffff, dark
surface #191919). Two-group comparisons use the emphasis pattern: the group
the sentence is about takes series blue, the comparison group a neutral
reference grey, and every bar carries a direct text label, so identity never
rests on colour alone. Deaths and other serious harms use the same calm blue,
never red.
"""

import math
import os
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "assets", "charts")

W = 720
PAD = 24
FONT = 'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif'

THEMES = {
    "light": dict(
        surface="#ffffff", ink="#191919", ink2="#666666", grid="#e7e7e7",
        axis="#c2c2c2", accent="#257de0", strong="#1757ac", ref="#8a8a8a",
        dot="#dedede", band1="#f3f7fd", band2="#e5effc", band3="#d5e6fb",
        border="#e7e7e7",
    ),
    "dark": dict(
        surface="#191919", ink="#efefef", ink2="#9c9c9c", grid="#303030",
        axis="#474747", accent="#338ced", strong="#84b9f3", ref="#6e6e6e",
        dot="#333333", band1="#1c2129", band2="#1e2836", band3="#213047",
        border="#303030",
    ),
}


def text_width(s, size, bold=False):
    """Rough rendered width of system-ui text, erring wide."""
    w = 0.0
    for ch in s:
        if ch in "il.,:;'|!()[] ":
            w += 0.30
        elif ch in "mwMW%":
            w += 0.85
        elif ch.isupper() or ch.isdigit():
            w += 0.62
        else:
            w += 0.53
    return w * size * (1.06 if bold else 1.0)


def wrap(s, size, maxw, bold=False):
    words, lines, cur = s.split(), [], ""
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


class Svg:
    def __init__(self, theme, title, desc):
        self.t = THEMES[theme]
        self.title = title
        self.desc = desc
        self.body = []
        self.defs = []
        self.y = PAD

    def add(self, s):
        self.body.append(s)

    def text(self, x, y, s, size=14, fill=None, weight=400, anchor="start", italic=False):
        fill = fill or self.t["ink"]
        st = ' font-style="italic"' if italic else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{st}>{escape(s)}</text>'
        )

    def para(self, x, s, size=14, fill=None, weight=400, maxw=W - 2 * PAD, lh=1.35, gap_after=0):
        """Wrapped paragraph at the running y cursor (top of the first line)."""
        lines = wrap(s, size, maxw, weight >= 600)
        for ln in lines:
            self.y += size
            self.text(x, self.y, ln, size, fill, weight)
            self.y += size * (lh - 1)
        self.y += gap_after
        return len(lines)

    def header(self, title, subtitle=None):
        self.para(PAD, title, 18, self.t["ink"], 650, lh=1.3)
        if subtitle:
            self.y += 4
            self.para(PAD, subtitle, 14, self.t["ink2"], lh=1.4)
        self.y += 18

    def footer(self, source):
        self.y += 14
        self.add(f'<line x1="{PAD}" x2="{W - PAD}" y1="{self.y:.1f}" y2="{self.y:.1f}" '
                 f'stroke="{self.t["grid"]}" stroke-width="1"/>')
        self.y += 8
        self.para(PAD, source, 13, self.t["ink2"], lh=1.4)
        self.y += PAD - 6

    def hbar(self, x0, y, length, h, fill, extra=""):
        """Horizontal bar: square at the baseline, 4px rounded data end."""
        if length <= 0:
            return
        r = min(4.0, length / 2, h / 2)
        x1 = x0 + length
        d = (f"M{x0:.2f},{y:.2f} H{x1 - r:.2f} Q{x1:.2f},{y:.2f} {x1:.2f},{y + r:.2f} "
             f"V{y + h - r:.2f} Q{x1:.2f},{y + h:.2f} {x1 - r:.2f},{y + h:.2f} H{x0:.2f} Z")
        self.add(f'<path d="{d}" fill="{fill}"{extra}/>')

    def render(self):
        h = math.ceil(self.y)
        t = self.t
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" '
            f'role="img" aria-labelledby="title desc" font-family=\'{FONT}\'>',
            f'<title id="title">{escape(self.title)}</title>',
            f'<desc id="desc">{escape(self.desc)}</desc>',
        ]
        if self.defs:
            out.append("<defs>" + "".join(self.defs) + "</defs>")
        out.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="8" '
                   f'fill="{t["surface"]}" stroke="{t["border"]}" stroke-width="1"/>')
        out.extend(self.body)
        out.append("</svg>")
        return "\n".join(out) + "\n"


def save(folder, name, build):
    d = os.path.join(OUT, folder)
    os.makedirs(d, exist_ok=True)
    for theme, suffix in (("light", ""), ("dark", "-dark")):
        svg = build(theme)
        with open(os.path.join(d, f"{name}{suffix}.svg"), "w", encoding="utf-8") as f:
            f.write(svg.render())


# ---------------------------------------------------------------- shared forms

def legend(svg, items, x=PAD):
    """items: list of (label, fill, hatched)."""
    t = svg.t
    y = svg.y
    for label, fill, hatch in items:
        if hatch:
            svg.add(f'<rect x="{x}" y="{y + 2}" width="14" height="14" rx="3" fill="url(#{hatch})" '
                    f'stroke="{fill}" stroke-width="1.5"/>')
        else:
            svg.add(f'<rect x="{x}" y="{y + 2}" width="14" height="14" rx="3" fill="{fill}"/>')
        svg.text(x + 20, y + 14, label, 14, t["ink2"])
        x += 20 + text_width(label, 14) + 24
    svg.y += 30


def x_axis(svg, x0, x1, vmax, ticks, fmt, y_top, y_bot, label=None):
    t = svg.t
    for v in ticks:
        x = x0 + (x1 - x0) * v / vmax
        svg.add(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{y_top:.1f}" y2="{y_bot:.1f}" '
                f'stroke="{t["axis"] if v == 0 else t["grid"]}" stroke-width="1"/>')
        svg.text(x, y_bot + 18, fmt(v), 13, t["ink2"], anchor="middle")
    if label:
        svg.text(x1, y_bot + 38, label, 13, t["ink2"], anchor="end")
        return y_bot + 44
    return y_bot + 24


def paired_bars(svg, groups, vmax, ticks, fmt, names, label_w=200, unit_label=None,
                value_fmt=None):
    """groups: list of (group label, [value_a, value_b]); names: (name_a, name_b).

    Bar a is the group the page is about (accent), bar b the comparison (reference grey).
    Each bar carries its own name and value, so nothing depends on colour.
    """
    t = svg.t
    value_fmt = value_fmt or (lambda v: f"{v}%")
    x0 = PAD + label_w
    x1 = W - PAD - 120
    bh, gap, ggap = 18, 6, 26
    y_top = svg.y
    rows = []
    y = y_top + 4
    for g, vals in groups:
        rows.append((g, vals, y))
        y += 2 * bh + gap + ggap
    y_bot = y - ggap + 4
    x_axis_end = x_axis(svg, x0, x1, vmax, ticks, fmt, y_top, y_bot, unit_label)
    for g, vals, y in rows:
        glines = wrap(g, 14, label_w - 14, True)
        gy = y + bh + gap / 2 - (len(glines) - 1) * 9 + 5
        for i, ln in enumerate(glines):
            svg.text(PAD, gy + i * 18, ln, 14, t["ink"], 600)
        for i, v in enumerate(vals):
            by = y + i * (bh + gap)
            ln = (x1 - x0) * v / vmax
            svg.hbar(x0, by, ln, bh, t["accent"] if i == 0 else t["ref"])
            svg.text(x0 + ln + 8, by + 14, f"{value_fmt(v)} {names[i]}", 14, t["ink"],
                     600 if i == 0 else 400)
    svg.y = x_axis_end + 10


def dot_grid(svg, x, y, cols, rows, pitch, r, n_full, frac, fill_on, fill_off, block=None,
             block_gap=0, clip_id=None):
    """Icon array drawn row by row from the top-left. n_full dots filled, then one dot
    filled by `frac` (0-1) from the left. Returns (width, height)."""
    def pos(i):
        c, rr = i % cols, i // cols
        ox = x + c * pitch + (c // block) * block_gap if block else x + c * pitch
        oy = y + rr * pitch + (rr // block) * block_gap if block else y + rr * pitch
        return ox + pitch / 2, oy + pitch / 2

    # Base dots as a tiled pattern (one tile per block) to keep the file small.
    pid = f"grid{len(svg.defs)}"
    tile = block * pitch + block_gap if block else pitch
    k = block if block else 1
    circles = "".join(
        f'<circle cx="{c * pitch + pitch / 2:.2f}" cy="{rr * pitch + pitch / 2:.2f}" r="{r}"/>'
        for rr in range(k) for c in range(k))
    svg.defs.append(f'<pattern id="{pid}" x="{x}" y="{y}" width="{tile}" height="{tile}" '
                    f'patternUnits="userSpaceOnUse"><g fill="{fill_off}">{circles}</g></pattern>')
    gw_ = cols * pitch + ((cols - 1) // block) * block_gap if block else cols * pitch
    gh_ = rows * pitch + ((rows - 1) // block) * block_gap if block else rows * pitch
    svg.add(f'<rect x="{x}" y="{y}" width="{gw_}" height="{gh_}" fill="url(#{pid})"/>')
    on = []
    for i in range(n_full):
        cx, cy = pos(i)
        on.append(f"M{cx - r:.2f},{cy:.2f}a{r},{r} 0 1,0 {2 * r},0a{r},{r} 0 1,0 {-2 * r},0")
    if on:
        svg.add(f'<path d="{"".join(on)}" fill="{fill_on}"/>')
    if frac > 0:
        cx, cy = pos(n_full)
        svg.defs.append(f'<clipPath id="{clip_id}"><rect x="{cx - r:.2f}" y="{cy - r:.2f}" '
                        f'width="{2 * r * frac:.2f}" height="{2 * r:.2f}"/></clipPath>')
        svg.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{fill_on}" clip-path="url(#{clip_id})"/>')
    wdt = cols * pitch + ((cols - 1) // block) * block_gap if block else cols * pitch
    hgt = rows * pitch + ((rows - 1) // block) * block_gap if block else rows * pitch
    return wdt, hgt


def hatch_def(svg, pid, color):
    svg.defs.append(
        f'<pattern id="{pid}" width="6" height="6" patternUnits="userSpaceOnUse" '
        f'patternTransform="rotate(45)"><rect width="6" height="6" fill="{svg.t["surface"]}"/>'
        f'<line x1="0" y1="0" x2="0" y2="6" stroke="{color}" stroke-width="2.2"/></pattern>'
    )


# ---------------------------------------------------------------- 04 charts

def deaths_grid(theme):
    title = "In young Danes, about 6 in 10,000 people with ADHD died each year, against about 2 without"
    desc = ("Two grids of 10,000 dots, each standing for 10,000 people followed for one year. "
            "In the grid for people with ADHD, 6 dots are filled (5.85 deaths per 10,000 person-years); "
            "in the grid for people without ADHD, 2 dots are filled (2.21 per 10,000 person-years). "
            "Rate ratio 2.07 after adjustment, falling to 1.50 when people who also had oppositional "
            "defiant disorder, conduct disorder or a substance use disorder were removed. Danish registry "
            "study of about 1.92 million people; the cohort was aged 32 or under.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Each grid is 10,000 people followed for one year. A filled dot is one death. "
                    "Nearly every dot in both grids is someone who did not die that year.")
    pitch, r, gapb = 3.0, 1.1, 2
    gw = 100 * pitch + 9 * gapb
    gx = [PAD, W - PAD - gw]
    heads = [("With ADHD", "5.85 per 10,000 person-years", 6),
             ("Without ADHD", "2.21 per 10,000 person-years", 2)]
    y0 = s.y
    for (h1, h2, n), x in zip(heads, gx):
        s.text(x, y0 + 15, h1, 15, t["ink"], 650)
        s.text(x, y0 + 35, h2, 14, t["ink2"])
    gy = y0 + 70
    for (h1, h2, n), x in zip(heads, gx):
        dot_grid(s, x, gy, 100, 100, pitch, r, n, 0, t["strong"], t["dot"], block=10, block_gap=gapb)
        # leader from the filled dots (top-left of the grid) to their label
        lx = x + pitch * n / 2
        s.add(f'<path d="M{lx:.1f},{gy:.1f} V{gy - 9:.1f} H{x + 70:.1f}" '
              f'stroke="{t["ink2"]}" stroke-width="1" fill="none"/>')
        s.text(x + 74, gy - 5, f"about {n} deaths", 13, t["ink"], 600)
    s.y = gy + gw + 18
    s.para(PAD, "In relative terms: a rate ratio of 2.07 after adjustment, and 1.50 after "
                "removing people who also had oppositional defiant, conduct or substance use disorders.",
           14, t["ink"], lh=1.4)
    s.footer("Source: Dalsgaard et al., Lancet 2015 [1]. Danish national registry, about 1.92 million "
             "people, 32,061 with ADHD; oldest aged 32. Group averages, not a prediction for any person.")
    return s


def life_years(theme):
    title = ("Counted deaths put the gap at about 7 to 9 years in diagnosed UK adults; "
             "the “13 years” figure is a calculator estimate")
    desc = ("Horizontal bars of years of life lost. Counted, from UK GP records of 30,039 diagnosed adults: "
            "men 6.8 years (73.3 against 80.0), women 8.6 years (75.2 against 83.8). Modelled with an online "
            "life-expectancy calculator in one Milwaukee clinical cohort, with no deaths counted: 8.4 fewer "
            "years of total life for the childhood hyperactivity group, and a 12.7-year reduction for those "
            "whose ADHD persisted into adulthood.")
    s = Svg(theme, title, desc)
    t = s.t
    hatch_def(s, "est", t["ref"])
    s.header(title, "Years of life expectancy lost, compared with people without ADHD. "
                    "Solid bars come from deaths that happened; striped bars are predictions.")
    legend(s, [("Counted from deaths", t["accent"], None),
               ("Modelled, no deaths counted", t["ref"], "est")])
    s.y += 6
    label_w = 270
    x0, x1, vmax = PAD + label_w, W - PAD - 150, 14
    bh = 20
    sections = [
        ("UK adults with diagnosed ADHD [4]", [
            ("Men", 6.8, "6.8 years (73.3 v 80.0)", False),
            ("Women", 8.6, "8.6 years (75.2 v 83.8)", False)]),
        ("Milwaukee childhood cohort, calculator [5]", [
            ("Whole group, total life", 8.4, "8.4 years", True),
            ("ADHD persisted into adulthood", 12.7, "12.7 years", True)]),
    ]
    y_top = s.y
    y = y_top + 4
    rows = []
    for sec, items in sections:
        rows.append(("sec", sec, y))
        y += 26
        for it in items:
            rows.append(("row", it, y))
            y += bh + 12
        y += 10
    y_bot = y - 14
    for v in range(0, 15, 2):
        x = x0 + (x1 - x0) * v / vmax
        s.add(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{y_top + 26:.1f}" y2="{y_bot:.1f}" '
              f'stroke="{t["axis"] if v == 0 else t["grid"]}" stroke-width="1"/>')
        s.text(x, y_bot + 18, str(v), 13, t["ink2"], anchor="middle")
    s.text(x1, y_bot + 38, "years of life lost", 13, t["ink2"], anchor="end")
    for kind, item, y in rows:
        if kind == "sec":
            s.text(PAD, y + 15, item, 14, t["ink"], 650)
            continue
        name, v, lab, est = item
        s.text(PAD + 12, y + 15, name, 14, t["ink"])
        ln = (x1 - x0) * v / vmax
        if est:
            r = 4
            xe = x0 + ln
            d = (f"M{x0:.2f},{y + 0.75:.2f} H{xe - r:.2f} Q{xe - 0.75:.2f},{y + 0.75:.2f} {xe - 0.75:.2f},{y + r:.2f} "
                 f"V{y + bh - r:.2f} Q{xe - 0.75:.2f},{y + bh - 0.75:.2f} {xe - r:.2f},{y + bh - 0.75:.2f} H{x0:.2f} Z")
            s.add(f'<path d="{d}" fill="url(#est)" stroke="{t["ref"]}" stroke-width="1.5"/>')
        else:
            s.hbar(x0, y, ln, bh, t["accent"])
        s.text(x0 + ln + 8, y + 15, lab, 14, t["ink"], 600)
    s.y = y_bot + 54
    s.para(PAD, "The calculator turned 14 health and lifestyle answers into a prediction for 131 young "
                "adults (mostly boys, more severe than ADHD in the community). The UK authors say their own "
                "gap probably overstates it for everyone with ADHD.", 14, t["ink"], lh=1.4)
    s.footer("Sources: O’Nions et al., Br J Psychiatry 2025 [4]; Barkley et al., J Atten Disord 2019 [5]. "
             "Group averages, not a prediction for any person.")
    return s


def paracetamol(theme):
    title = "Paracetamol in pregnancy: a small raw gap that disappeared when siblings were compared"
    desc = ("Two bars. Among 2.48 million Swedish children, 2.87% of those exposed to paracetamol before "
            "birth had an ADHD diagnosis by age 10, against 2.46% of those not exposed. Comparing siblings, "
            "the hazard ratio was 0.98, meaning no difference.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Share of 2.48 million Swedish children with an ADHD diagnosis by age 10.")
    paired_bars(s, [("By age 10", [2.87, 2.46])], 4, [0, 1, 2, 3, 4], lambda v: f"{v}%",
                ("exposed before birth", "not exposed"), label_w=130)
    s.y += 10
    bx, bw = PAD, W - 2 * PAD
    by = s.y
    s.add(f'<rect x="{bx}" y="{by}" width="{bw}" height="58" rx="6" fill="{t["band1"]}"/>')
    s.text(bx + 16, by + 24, "Comparing brothers and sisters, one exposed and one not:", 14, t["ink"])
    s.text(bx + 16, by + 45, "hazard ratio 0.98, no difference.", 14, t["ink"], 650)
    s.y = by + 58
    s.footer("Source: Ahlqvist et al. [3]. Swedish national registry. Sibling comparisons account for "
             "family factors that siblings share.")
    return s


# ---------------------------------------------------------------- 05 charts

def physical_health(theme):
    title = "Where absolute figures exist, the gaps are real but modest"
    desc = ("Paired bars, people with ADHD against people without. Obesity in adults 28.2% against 16.4%, "
            "and in children 10.3% against 7.4% (meta-analysis of 42 studies). In Swedish adults aged 18 to 64: "
            "high blood pressure 8.5% against 4.5%, type 2 diabetes 3.9% against 1.6%.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Share of people with each condition, with and without ADHD.")
    legend(s, [("With ADHD", t["accent"], None), ("Without ADHD", t["ref"], None)])
    s.y += 4
    paired_bars(s, [
        ("Obesity, adults [3]", [28.2, 16.4]),
        ("Obesity, children [3]", [10.3, 7.4]),
        ("High blood pressure [2]", [8.5, 4.5]),
        ("Type 2 diabetes [2]", [3.9, 1.6]),
    ], 30, [0, 10, 20, 30], lambda v: f"{v}%", ("", ""), label_w=190,
        value_fmt=lambda v: f"{v}%")
    s.footer("Sources: Cortese et al., Am J Psychiatry 2016 [3] (pooled from 42 studies); Chen et al., "
             "PLoS One 2018 [2] (Swedish adults aged 18 to 64, one point in time). Diagnosed cases only.")
    return s


def depression_anxiety(theme):
    title = ("About 4 in 10 adults with diagnosed ADHD also had a recorded depression diagnosis, "
             "against about 1 in 20 without")
    desc = ("Paired bars from Swedish registers of 5.55 million adults aged 18 to 64. Depression diagnosis "
            "recorded in 42% of adults with ADHD against 4.7% without; anxiety 45% against 4.9%. "
            "Adjusted for age and sex.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Share of Swedish adults aged 18 to 64 with a diagnosis recorded at some point "
                    "in adulthood, adjusted for age and sex.")
    legend(s, [("With ADHD", t["accent"], None), ("Without ADHD", t["ref"], None)])
    s.y += 4
    paired_bars(s, [("Depression", [42, 4.7]), ("Anxiety", [45, 4.9])], 50,
                [0, 10, 20, 30, 40, 50], lambda v: f"{v}%", ("", ""), label_w=120)
    s.footer("Source: Chen et al., PLoS One 2018 [2]. 5.55 million adults, 61,129 with diagnosed ADHD. "
             "Health-record diagnoses only, so milder or untreated conditions are missed.")
    return s


def autism_overlap(theme):
    title = "How often autism and ADHD overlap depends on who is counted and how"
    desc = ("Dot plot of pooled estimates. Children and adolescents with ADHD who meet the threshold for "
            "autism: 21% overall, 19% in community samples, 24% in clinic samples (22 studies). Autistic "
            "people who have ADHD: 28% counting only confirmed clinical diagnoses (2019 meta-analysis), "
            "38.5% currently and 40.2% at some point (2021 meta-analysis of 63 articles). The two main "
            "estimates differ by about ten percentage points.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Pooled estimates from meta-analyses. Each dot is one estimate; each pooled figure "
                    "hides a wide range between studies.")
    label_w = 300
    x0, x1, vmax = PAD + label_w, W - PAD - 30, 50
    sections = [
        ("Children with ADHD who meet the autism threshold", [
            ("All samples [3]", 21, "21%"),
            ("Community samples [3]", 19, "19%"),
            ("Clinic samples [3]", 24, "24%")]),
        ("Autistic people who have ADHD", [
            ("Confirmed clinical diagnoses only [5]", 28, "28%"),
            ("Currently have ADHD [4]", 38.5, "38.5%"),
            ("Have had ADHD at some point [4]", 40.2, "40.2%")]),
    ]
    rh = 30
    y_top = s.y
    y = y_top
    rows = []
    for sec, items in sections:
        rows.append(("sec", sec, y))
        y += 28
        for it in items:
            rows.append(("row", it, y))
            y += rh
        y += 12
    y_bot = y - 8
    for v in range(0, 51, 10):
        x = x0 + (x1 - x0) * v / vmax
        s.add(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{y_top + 22:.1f}" y2="{y_bot:.1f}" '
              f'stroke="{t["axis"] if v == 0 else t["grid"]}" stroke-width="1"/>')
        s.text(x, y_bot + 18, f"{v}%", 13, t["ink2"], anchor="middle")
    pos = {}
    for kind, item, y in rows:
        if kind == "sec":
            s.text(PAD, y + 16, item, 14, t["ink"], 650)
            continue
        name, v, lab = item
        cy = y + rh / 2
        s.text(PAD + 12, cy + 5, name, 14, t["ink"])
        s.add(f'<line x1="{x0:.1f}" x2="{W - PAD - 30:.1f}" y1="{cy:.1f}" y2="{cy:.1f}" '
              f'stroke="{t["grid"]}" stroke-width="1"/>')
        cx = x0 + (x1 - x0) * v / vmax
        s.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{t["accent"]}" '
              f'stroke="{t["surface"]}" stroke-width="2"/>')
        s.text(cx - 12, cy + 5, lab, 14, t["ink"], 600, anchor="end")
        pos[v] = (cx, cy)
    # bracket between the two main ADHD-in-autism estimates
    (ax, ay), (bx, by) = pos[28], pos[38.5]
    bxr = W - PAD - 6
    s.add(f'<path d="M{ax + 10:.1f},{ay:.1f} H{bxr:.1f} V{by:.1f} H{bx + 10:.1f}" '
          f'stroke="{t["ink2"]}" stroke-width="1" fill="none"/>')
    s.y = y_bot + 40
    s.para(PAD, "The two main estimates of ADHD in autistic people (28% and 38.5%) differ by about ten "
                "percentage points, probably because of method (what counts as having ADHD, and who was "
                "sampled) rather than one being wrong.", 14, t["ink"], lh=1.4)
    s.footer("Sources: Hollingdale et al., Psychol Med 2020 [3]; Lai et al., Lancet Psychiatry 2019 [5]; "
             "Rong et al., Res Autism Spectr Disord 2021 [4]. Child figures are from children only.")
    return s


# ---------------------------------------------------------------- 06 charts

def effect_sizes(theme):
    title = "In short trials, medicines beat placebo on core symptoms, with bigger effects in children than adults"
    desc = ("Dot plot of standardised mean differences (SMD) against placebo at around 12 weeks. Children and "
            "teenagers: amphetamines about 1.02 and methylphenidate about 0.78 (network meta-analysis, "
            "clinician-rated); methylphenidate 0.74 teacher-rated (Cochrane). Adults: stimulants roughly 0.6 "
            "and atomoxetine roughly 0.5 clinician-rated; both about 0.4 self-rated; emotional lability about "
            "0.41. Reference lines mark the conventions 0.2 small, 0.5 medium and 0.8 large.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Standardised mean difference (SMD) against placebo, mostly at around 12 weeks. "
                    "Further right means a bigger average effect. Values marked “about” are "
                    "rounded on the page.")
    label_w = 330
    x0, x1, vmax = PAD + label_w, W - PAD - 10, 1.2
    sx = lambda v: x0 + (x1 - x0) * v / vmax
    sections = [
        ("Children and teenagers", [
            ("Amphetamines, clinician-rated [1]", 1.02, "1.02"),
            ("Methylphenidate, clinician-rated [1]", 0.78, "0.78"),
            ("Methylphenidate, teacher-rated, Cochrane [3]", 0.74, "0.74")]),
        ("Adults", [
            ("Stimulants, clinician-rated [2]", 0.6, "about 0.6"),
            ("Atomoxetine, clinician-rated [2]", 0.5, "about 0.5"),
            ("Stimulants, self-rated [2]", 0.4, "about 0.4"),
            ("Atomoxetine, self-rated [2]", 0.4, "about 0.4"),
            ("Emotional lability, both [6]", 0.41, "0.41")]),
    ]
    rh = 28
    y_top = s.y + 24
    y = y_top
    rows = []
    for sec, items in sections:
        rows.append(("sec", sec, y))
        y += 28
        for it in items:
            rows.append(("row", it, y))
            y += rh
        y += 10
    y_bot = y - 6
    # convention bands
    bands = [(0.2, 0.5, t["band1"]), (0.5, 0.8, t["band2"]), (0.8, vmax, t["band3"])]
    for a, b, c in bands:
        s.add(f'<rect x="{sx(a):.1f}" y="{y_top - 6:.1f}" width="{sx(b) - sx(a):.1f}" '
              f'height="{y_bot - y_top + 6:.1f}" fill="{c}"/>')
    for a, b, lab in ((0.2, 0.5, "small"), (0.5, 0.8, "medium"), (0.8, vmax, "large")):
        s.text((sx(a) + sx(b)) / 2, y_top - 12, lab, 13, t["ink2"], anchor="middle")
    for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2):
        s.add(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="{y_top - 6:.1f}" y2="{y_bot:.1f}" '
              f'stroke="{t["axis"] if v == 0 else t["grid"]}" stroke-width="1"/>')
        s.text(sx(v), y_bot + 18, f"{v:g}", 13, t["ink2"], anchor="middle")
    s.text(x1, y_bot + 38, "SMD", 13, t["ink2"], anchor="end")
    for kind, item, y in rows:
        if kind == "sec":
            s.text(PAD, y + 16, item, 14, t["ink"], 650)
            continue
        name, v, lab = item
        cy = y + rh / 2
        s.text(PAD + 12, cy + 5, name, 14, t["ink"])
        cx = sx(v)
        s.add(f'<line x1="{sx(0):.1f}" x2="{cx:.1f}" y1="{cy:.1f}" y2="{cy:.1f}" '
              f'stroke="{t["accent"]}" stroke-width="2" stroke-linecap="round"/>')
        s.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="{t["accent"]}" '
              f'stroke="{t["surface"]}" stroke-width="2"/>')
        s.text(cx + 12, cy + 5, lab, 14, t["ink"], 600)
    s.y = y_bot + 46
    s.footer("Sources: Cortese et al., Lancet Psychiatry 2018 [1]; Ostinelli et al., Lancet Psychiatry 2025 [2]; "
             "Storebø et al., Cochrane 2023/2025 [3]; Moukhtarian et al., Eur Psychiatry 2017 [6]. "
             "Short-term symptom ratings only, not quality of life or long-term outcomes.")
    return s


def heart_defects(theme):
    title = "Heart defects per 1,000 births: raw rates differ, the adjusted signal is small and uncertain"
    desc = ("Three grids of 1,000 dots, one per group of births in US Medicaid data, with filled dots for heart "
            "defects. Unadjusted rates: 12.7 per 1,000 with no stimulant exposure, 18.8 per 1,000 with "
            "methylphenidate, 15.4 per 1,000 with amphetamines. These raw rates do not account for differences "
            "between the women. After adjustment, the pooled US and Nordic relative risk for methylphenidate "
            "was 1.28 (range 1.00 to 1.64), a possible small increase; for amphetamines in the US data it was "
            "0.96, not linked to more heart defects.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Unadjusted (raw) rates in US Medicaid data, early-pregnancy exposure. Each grid is "
                    "1,000 births; a filled dot is a baby with a heart defect.")
    cols, rows, pitch, r = 40, 25, 5.0, 1.75
    gw = cols * pitch
    gap = (W - 2 * PAD - 3 * gw) / 2
    groups = [("No stimulant", "12.7 per 1,000", 12.7),
              ("Methylphenidate", "18.8 per 1,000", 18.8),
              ("Amphetamines", "15.4 per 1,000", 15.4)]
    y0 = s.y
    for i, (h1, h2, v) in enumerate(groups):
        x = PAD + i * (gw + gap)
        s.text(x, y0 + 15, h1, 15, t["ink"], 650)
        s.text(x, y0 + 35, h2 + " (unadjusted)", 14, t["ink2"])
        n = int(v)
        dot_grid(s, x, y0 + 46, cols, rows, pitch, r, n, round(v - n, 2), t["strong"], t["dot"],
                 clip_id=f"frac{i}")
    s.y = y0 + 46 + rows * pitch + 20
    bx, bw = PAD, W - 2 * PAD
    by = s.y
    lines = [
        ("After adjusting for differences between the women:", 400),
        ("Methylphenidate: relative risk 1.28 (range 1.00 to 1.64), a possible small increase.", 650),
        ("Amphetamines: relative risk 0.96 in the US data, not linked to more heart defects.", 650),
    ]
    s.add(f'<rect x="{bx}" y="{by}" width="{bw}" height="{20 + 22 * len(lines)}" rx="6" fill="{t["band1"]}"/>')
    for i, (ln, wgt) in enumerate(lines):
        s.text(bx + 16, by + 26 + 22 * i, ln, 14, t["ink"], wgt)
    s.y = by + 20 + 22 * len(lines)
    s.footer("Source: Huybrechts et al., JAMA Psychiatry 2018 [1]. US Medicaid with Nordic replication. "
             "The raw gap is larger than the adjusted one because the groups of women differed.")
    return s


def psychosis(theme):
    title = "New psychosis after starting a stimulant was rare: about 2 in 1,000 with amphetamine"
    desc = ("Two grids of 1,000 dots for 13- to 25-year-olds starting a stimulant in US insurance data. "
            "New psychosis treated with an antipsychotic occurred in 0.10% of those starting methylphenidate "
            "(1 dot in 1,000) and 0.21% of those starting amphetamine (just over 2 dots in 1,000); hazard ratio "
            "1.65 for amphetamine; about 1 in 660 overall.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "13- to 25-year-olds in US insurance data. Each grid is 1,000 people starting a "
                    "medicine; a filled dot is someone who developed new psychosis treated with an antipsychotic.")
    cols, rows, pitch, r = 40, 25, 7.6, 2.6
    gw = cols * pitch
    gap = W - 2 * PAD - 2 * gw
    groups = [("Starting methylphenidate", "0.10%", 1.0), ("Starting amphetamine", "0.21%", 2.1)]
    y0 = s.y
    for i, (h1, h2, v) in enumerate(groups):
        x = PAD + i * (gw + gap)
        s.text(x, y0 + 15, h1, 15, t["ink"], 650)
        s.text(x, y0 + 35, h2, 14, t["ink2"])
        n = int(v)
        dot_grid(s, x, y0 + 46, cols, rows, pitch, r, n, round(v - n, 2), t["strong"], t["dot"],
                 clip_id=f"pfrac{i}")
    s.y = y0 + 46 + rows * pitch + 16
    s.para(PAD, "In relative terms: hazard ratio 1.65 for amphetamine compared with methylphenidate. "
                "About 1 in 660 people overall.", 14, t["ink"], lh=1.4)
    s.footer("Source: Moran et al., N Engl J Med 2019 [8]. Two US insurance cohorts, 221,846 people aged "
             "13 to 25. Young people only; may not apply to older adults.")
    return s


def withdrawal(theme):
    title = "In two withdrawal trials, more people worsened after switching to placebo"
    desc = ("Paired bars. Children and adolescents who had taken methylphenidate for more than two years: "
            "40.4% switched to placebo were rated worse, against 15.9% who continued. Adults stable on "
            "lisdexamfetamine: 75.0% on placebo relapsed, against 8.9% who continued. Different trials with "
            "different definitions of worsening.")
    s = Svg(theme, title, desc)
    t = s.t
    s.header(title, "Share who worsened (children) or relapsed (adults) in randomised trials of people "
                    "already doing well on a medicine. The two trials define worsening differently.")
    legend(s, [("Switched to placebo", t["accent"], None), ("Continued the medicine", t["ref"], None)])
    s.y += 4
    paired_bars(s, [("Children, methylphenidate [1]", [40.4, 15.9]),
                    ("Adults, lisdexamfetamine [2]", [75.0, 8.9])],
                100, [0, 25, 50, 75, 100], lambda v: f"{v}%", ("", ""), label_w=230,
                value_fmt=lambda v: f"{v:.1f}%")
    s.y += 2
    s.para(PAD, "Most children who stopped did not clearly worsen. Both trials enrolled people who had "
                "already responded to and tolerated the medicine.", 14, t["ink"], lh=1.4)
    s.footer("Sources: Matthijssen et al. [1] (94 children and adolescents aged 8 to 18); Brams et al. [2]. "
             "Decisions about stopping are made with a prescriber.")
    return s


CHARTS = [
    ("04", "deaths-per-10000", deaths_grid),
    ("04", "life-expectancy-counted-vs-modelled", life_years),
    ("04", "paracetamol-siblings", paracetamol),
    ("05", "physical-health-absolute", physical_health),
    ("05", "depression-anxiety-absolute", depression_anxiety),
    ("05", "autism-adhd-overlap", autism_overlap),
    ("06", "medication-effect-sizes", effect_sizes),
    ("06", "heart-defects-per-1000", heart_defects),
    ("06", "psychosis-per-1000", psychosis),
    ("06", "withdrawal-trials", withdrawal),
]


if __name__ == "__main__":
    for folder, name, fn in CHARTS:
        save(folder, name, fn)
        print(f"assets/charts/{folder}/{name}.svg (+ -dark)")
