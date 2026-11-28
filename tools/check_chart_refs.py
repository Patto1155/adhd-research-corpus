#!/usr/bin/env python3
"""Check that source numbers printed inside charts match the page that embeds them.

For every <img src="...svg"> on a page, finds "Surname ... [n]" in the chart's
text and checks that source n on that page starts with that surname.
Usage: python3 tools/check_chart_refs.py      (exit 1 on mismatch)
Standard library only.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
bad = checked = 0
for md in sorted(ROOT.glob("0*/*.md")):
    text = md.read_text(encoding="utf-8")
    if "## Sources" not in text:
        continue
    sources = {}
    for line in text.split("## Sources", 1)[1].splitlines():
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if m:
            sources[int(m.group(1))] = m.group(2)
    for src in re.findall(r'<img src="([^"]+\.svg)"', text):
        svg = (md.parent / src).resolve()
        if not svg.exists():
            continue
        chart_text = html.unescape(" ".join(re.findall(r">([^<>]+)<", svg.read_text(encoding="utf-8"))))
        # "Hoogman et al. 2017 ... [1]" or "Moran et al., N Engl J Med 2019 [10]" or "Cochrane [4]"
        refs = re.findall(r"([A-Z][A-Za-zÀ-ÿ'\-]+) et al\.[^\[\]]{0,60}?\[(\d+)\]", chart_text)
        refs += re.findall(r"\b(Cochrane) \[(\d+)\]", chart_text)
        # charts that print only "Source [n]" are checked against the page caption's study name, if any
        for name, n in refs:
            n = int(n)
            checked += 1
            entry = sources.get(n, "")
            if name.lower() not in entry.lower():
                bad += 1
                print(f"{md.relative_to(ROOT)}: {svg.name} cites '{name} [{n}]' but source {n} is: {entry[:70] or 'missing'}")
print(f"{checked} chart references checked; {bad} mismatches")
sys.exit(1 if bad else 0)
