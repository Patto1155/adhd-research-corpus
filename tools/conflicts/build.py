#!/usr/bin/env python3
"""Merge research/conflicts/g*.json into research/conflicts/conflicts.json and
research/conflicting-claims.md (a readable register for later analysis).

Usage: python3 tools/conflicts/build.py
Standard library only. Safe to re-run whenever a group file changes.
"""
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "research" / "conflicts"
SEV_ORDER = {"major": 0, "moderate": 1, "minor": 2}
HANDLING_PLAIN = {
    "reports both": "Page reports both sides",
    "reports one side": "Page reports one side only",
    "not mentioned": "Page does not mention it",
}


def load():
    recs = []
    for f in sorted(SRC.glob("g*.json")):
        recs.extend(json.loads(f.read_text(encoding="utf-8")))
    ids = [r["id"] for r in recs]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"duplicate ids: {sorted(dup)}")
    return recs


def page_title(path):
    p = ROOT / path
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return path


def src_line(s):
    bits = [s.get("citation", "").strip()]
    ids = []
    if s.get("doi"):
        ids.append(f"[DOI {s['doi']}](https://doi.org/{s['doi']})")
    if s.get("pmid"):
        ids.append(f"[PMID {s['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{s['pmid']}/)")
    meta = [x for x in (s.get("design"), f"n = {s['n']}" if s.get("n") else None) if x]
    tail = []
    if ids:
        tail.append(" · ".join(ids))
    if meta:
        tail.append(", ".join(str(m) for m in meta))
    tail.append("cited on page" if s.get("cited_on_page") else "**not yet cited on page**")
    if s.get("verified"):
        tail.append(f"checked: {s['verified']}")
    return f"  - {' '.join(bits)} — {'; '.join(tail)}"


def main():
    recs = load()
    recs.sort(key=lambda r: (SEV_ORDER.get(r.get("severity"), 9), r["page"], r["id"]))
    (SRC / "conflicts.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    sev = Counter(r.get("severity") for r in recs)
    hand = Counter(r.get("page_handling") for r in recs)
    new = sum(bool(r.get("new_research")) for r in recs)
    by_page = defaultdict(list)
    for r in recs:
        by_page[r["page"]].append(r)

    out = []
    out.append("# Where the research disagrees: a register for analysis\n")
    out.append(
        "This is a working register for editors, not a reader page. It lists places where good sources disagree "
        "about a claim on this site, including evidence the pages do not yet cite. Each entry gives both sides, "
        "why they may differ, how the page currently handles it, and a next step. It was compiled in November 2026 "
        "by AI agents searching PubMed and Crossref; every PubMed ID was resolved against PubMed, but sources were "
        "read at abstract level and no clinician has reviewed the entries.\n"
    )
    out.append(f"Generated {date.today().isoformat()} by `python3 tools/conflicts/build.py` from `research/conflicts/g*.json` "
               "(schema in [SCHEMA.md](conflicts/SCHEMA.md); merged data in [conflicts.json](conflicts/conflicts.json)).\n")
    out.append("## At a glance\n")
    out.append("| | Count |\n|---|---|")
    out.append(f"| Conflicts recorded | {len(recs)} |")
    for k in ("major", "moderate", "minor"):
        out.append(f"| Severity: {k} | {sev.get(k, 0)} |")
    for k in ("reports both", "reports one side", "not mentioned"):
        out.append(f"| {HANDLING_PLAIN[k]} | {hand.get(k, 0)} |")
    out.append(f"| Include research the page does not yet cite | {new} |\n")

    out.append("## Action list: major conflicts, or pages that show only one side\n")
    out.append("| ID | Page | Topic | Severity | Page handling |\n|---|---|---|---|---|")
    for r in recs:
        if r.get("severity") == "major" or r.get("page_handling") != "reports both":
            out.append(f"| [{r['id']}](#{r['id'].lower()}) | [{page_title(r['page'])}](../{r['page']}) | {r['topic']} | "
                       f"{r.get('severity')} | {HANDLING_PLAIN.get(r.get('page_handling'), r.get('page_handling'))} |")
    out.append("")

    out.append("## All conflicts, by page\n")
    for page in sorted(by_page):
        out.append(f"### [{page_title(page)}](../{page})\n")
        for r in sorted(by_page[page], key=lambda r: (SEV_ORDER.get(r.get("severity"), 9), r["id"])):
            out.append(f"#### {r['id']}\n")
            out.append(f"**{r['topic']}** · {r.get('severity')} · {r.get('conflict_type')} · "
                       f"{HANDLING_PLAIN.get(r.get('page_handling'), r.get('page_handling'))}\n")
            out.append(f"**In dispute:** {r['claim']}\n")
            for p in r["positions"]:
                out.append(f"- **Position {p['label']}:** {p['summary']}")
                for s in p.get("sources", []):
                    out.append(src_line(s))
            out.append("")
            out.append(f"**Why they may differ:** {r.get('why_they_may_differ', '')}\n")
            out.append(f"**Next step:** {r.get('next_step', '')}\n")
    (ROOT / "research" / "conflicting-claims.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(recs)} conflicts -> research/conflicting-claims.md and research/conflicts/conflicts.json")


if __name__ == "__main__":
    main()
