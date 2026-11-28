#!/usr/bin/env python3
"""Inline corpus.json into the explorer template.

Usage: python3 tools/explorer/build.py [out.html]   (default: tools/explorer/index.html, git-ignored)
Re-run after tools/charts/corpus.py.
"""
import sys
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent.parent / "assets" / "charts" / "corpus" / "corpus.json"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "index.html"

d = json.loads(CORPUS.read_text(encoding="utf-8"))
keep = ["page", "folder", "n", "first_author", "year", "journal", "title", "doi", "pmid", "pmc",
        "evidence_label", "evidence", "study_type", "note", "key", "cited_on_pages"]
slim = {
    "generated": d["generated"],
    "folders": d["folders"],
    "pages": [{k: p[k] for k in ("path", "folder", "title", "short", "n_sources")} for p in d["pages"]],
    "evidence_order": d["evidence_order"],
    "type_order": d["type_order"],
    "fields": keep,
    "sources": [[s[k] for k in keep] for s in d["sources"]],
}
blob = json.dumps(slim, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
tpl = (HERE / "template.html").read_text(encoding="utf-8")
OUT.write_text(tpl.replace("__CORPUS_DATA__", blob), encoding="utf-8")
print(f"{OUT} written, {len(slim['sources'])} sources, {len(blob) // 1024} KB data")
