# Conflicting-claims register: record schema

Each group file (`research/conflicts/<group>.json`) is a JSON array of records:

```json
{
  "id": "C02-001",
  "topic": "short topic name",
  "page": "02-whats-happening-in-my-brain/brain-structure-and-development.md",
  "claim": "the claim as it stands on the page, or the question in dispute",
  "positions": [
    {
      "label": "A",
      "summary": "what this side finds, in one or two plain sentences",
      "sources": [
        {"citation": "First-author surname and initials, et al. Title. Journal. Year.",
         "doi": "10.xxxx/...", "pmid": "12345678", "year": 2020,
         "design": "meta-analysis | registry | RCT | cohort | guideline | ...",
         "n": "sample size as reported, or null",
         "cited_on_page": true,
         "verified": "PubMed record + abstract | Crossref record | search result only"}
      ]
    },
    {"label": "B", "summary": "...", "sources": []}
  ],
  "conflict_type": "direct contradiction | size of effect | population/age | method/measurement | causal interpretation | guideline disagreement",
  "why_they_may_differ": "plain explanation of likely reasons (design, confounding, sample, era, definitions)",
  "page_handling": "reports both | reports one side | not mentioned",
  "severity": "major | moderate | minor",
  "next_step": "what a later analysis should do to resolve or weigh it",
  "new_research": true
}
```

Rules: never construct a DOI or PMID (take them from PubMed/Crossref records); `new_research` is true when at least one side's sources are not yet cited on the page.
