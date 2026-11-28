# Contributing

Corrections matter more here than almost anywhere else. Readers take these pages to doctors and to sceptical relatives, so a wrong number or citation does real harm. Thank you for checking.

## Report an error

Open an issue and include:

1. **The page** (its path, for example `06-treatment-what-works/medication-safety.md`) and the sentence or source entry concerned.
2. **What is wrong**: a number that does not match the source, a citation that does not exist or points to the wrong paper, a claim stronger than the evidence, a broken link, or language that reads as advice.
3. **Your evidence**: the source and, where you can, the exact figure or passage, with a DOI, PubMed ID or link.

Errors in crisis contacts on [not medical advice](../08-reading-this-well/not-medical-advice.md) are treated as the most urgent. Please say in the issue title that it concerns a crisis number.

## Suggest a source

Open an issue with the full citation (authors, title, journal, year, DOI or PubMed ID), the page it belongs on, and the finding it supports or challenges. Sources that disagree with the current text are especially welcome.

The corpus prefers, in order: consensus statements and national guidelines; systematic reviews and meta-analyses; large registry, genetic or imaging studies; then individual trials and cohorts. Single small studies are used only where nothing better exists, and are labelled **Limited**.

## Standards a change has to meet

### Sourcing

- Every factual claim with a number has a numbered source on the same page.
- A source is cited only if its record has been confirmed (first author, title, journal, year, and a DOI or PubMed ID). Never construct or guess a DOI: give one only if you have seen it in the source's index record or publisher page; if you only have a PubMed ID, give that.
- Use this format: `First-author surname and initials, et al. Title. *Journal*. Year. DOI or PMID. — **Evidence: label**, short reason.`
- Each research source carries an evidence grade (**Strong**, **Moderate**, **Limited** or **Contested**) and a few words on why. Guidelines, consensus statements and expert commentary are labelled by what they are. Use only the labels defined in [the evidence labels used on every page](../08-reading-this-well/how-to-read-the-evidence.md#the-evidence-labels-used-on-every-page); if you need a new one, define it there first. If a source already appears on another page, check its grade there and either match it or say in the note why it differs.
- A technical term is defined where it first appears on a page, in words that match the [glossary](../08-reading-this-well/glossary.md). Add new terms to the glossary in alphabetical order, with a link to the page where the term matters most.
- If a number comes from memory, a secondary source, or an identifier you could not confirm, add `<!-- CHECK: what needs confirming -->` after it so reviewers can find it.
- Where good sources disagree, report the disagreement rather than choosing one.
- Each key fact has one home page: for example, heritability on `02-whats-happening-in-my-brain/genes-and-inheritance.md`, mortality on `04-did-i-cause-this-and-where-is-it-going/the-hard-statistics-in-context.md`, and medication effect sizes on `06-treatment-what-works/how-well-medication-works.md`. The full numbers and caveats live on the home page, and a change to a number is made there first. Other pages may state the headline figure, provided it matches the home page, and should link to the home page for the detail.

### Numbers

- Say what each number is a number of and what it means in practice.
- Give the absolute risk alongside every relative risk. If it cannot be found, say so.
- State group findings as group findings ("on average, across thousands of people"), never as facts about the reader.
- Say when a finding comes from children and is being applied to adults.

### Tone and language

- Plain language, roughly year-9 reading level, with each technical term defined where it first appears on a page.
- Australian/British spelling.
- Lead with the point; paragraphs of three sentences or fewer.
- Write to an intelligent adult. No cheerleading or "superpower" framing, no pathologising, and no telling readers how to feel.
- Keep every content page in the standard shape: short answer, evidence, what is uncertain, what it means for you, related pages, sources. The "uncertain" section is never removed. Reference pages (the glossary, myths, sources, not-medical-advice and the folder READMEs) have their own shapes.

### Information, not advice

- No doses to take. A dose threshold found in a study may be reported as that study's finding.
- Never advise starting, stopping or changing medication; say once per relevant page that these are decisions to make with a prescriber.
- No self-tests. Screening questionnaires may be described, not reproduced as a diagnostic quiz.
- Report evidence on supplements, diets, apps and devices without telling readers what to buy.
- Content on suicide, self-harm or mortality follows safe-messaging practice (no method detail) and links to [not medical advice](../08-reading-this-well/not-medical-advice.md) for crisis contacts.

## For editors and researchers

These tools and files support the pages. None of them is written for readers, and none needs anything beyond Python's standard library.

- **Check before you submit.** Run `python3 tools/check_format.py` (or give it one or more page paths). It checks each page's standard shape, that every `[n]` has a matching source and vice versa, the source-line format, tables, chart markup, and that relative links and `#anchors` resolve. Lines marked `(warn)` are heuristics for a person to judge; anything else must be fixed.
- **The register of disagreements.** [research/conflicting-claims.md](../research/conflicting-claims.md) is a working register of places where good sources disagree, including research the pages do not yet cite. Each entry gives both sides, why they may differ, how the page handles it now, and a next step. It is a to-do list for editors, not reader advice and not a source to cite. Edit the group files in `research/conflicts/` (schema in `research/conflicts/SCHEMA.md`), then run `python3 tools/conflicts/build.py` to rebuild the register.
- **The source data.** `python3 tools/charts/corpus.py` reads every page's source list, writes `assets/charts/corpus/corpus.json`, and refreshes the corpus charts and the marked sections of the folder READMEs and [the evidence at a glance](../08-reading-this-well/the-evidence-at-a-glance.md). Edit around the `<!-- corpus:... -->` markers, never inside them.
- **Interactive explorer.** `python3 tools/explorer/build.py` inlines `corpus.json` into a single HTML file (default `tools/explorer/index.html`, not committed) for searching and filtering every source by folder, evidence label and study type. Re-run it after `corpus.py`. It is a quick way to spot the same source graded differently on two pages.
- **Interactive reader.** `python3 tools/reader/build.py` builds a low-attention reading version of the whole site as one HTML file (default `tools/reader/index.html`, not committed). It reads the pages, the "Find your worry" list in the root README, the folder READMEs, the charts, the evidence-label definitions and the conflicts register, and never rewrites page text. Because it parses these files, keep the root README's folder table and `### [Folder](…)` worry headings, the folder READMEs' `- [Title](page.md): blurb` lists, and the evidence-label list on [Reading ADHD research](../08-reading-this-well/how-to-read-the-evidence.md) in their current shape.

## Charts

Some pages carry charts. They follow one shared style so the site reads as one piece.

- **Scripts are the source of truth.** Every chart is drawn by a Python script in `tools/charts/` that uses only the standard library. Edit the script and re-run it; never hand-edit an SVG. `python3 tools/charts/corpus.py` also refreshes the corpus charts and the generated numbers on [the evidence at a glance](../08-reading-this-well/the-evidence-at-a-glance.md) and the folder READMEs.
- **Light and dark pair.** Each chart is saved as `name.svg` and `name-dark.svg`, with viewBox width 720, the font stack `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`, and no text smaller than 13px.
- **Embed both**, with alt text and a caption:

  ```html
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../assets/charts/folder/name-dark.svg">
    <img src="../assets/charts/folder/name.svg" alt="What the chart shows, with every number in it" width="720">
  </picture>

  *One-line italic caption saying what to take from it.*
  ```

- **Numbers must match the page.** A chart shows only figures that the page text states and cites. If a number changes, change the page and the script together.
- **Absolute risk first.** Where a chart shows risk, show the absolute figures (for example, per 1,000 people) before or instead of a relative risk.
- **Say what it shows.** The title states the takeaway in plain words; bars and lines are labelled directly; a small source line names where the numbers came from.
- **Alt text and caption are required.** Alt text gives the full numbers, so a screen-reader user loses nothing.
- **Calm colours for hard topics.** Charts about mortality, suicide or other serious harms use calm blues and greys, never alarm reds, and follow the safe-messaging rules above.
- **Colour is never the only cue.** Reuse the palette already in the `tools/charts/` scripts: blue (`#257de0` light, `#338ced` dark) for a single series, a light-to-dark blue ramp for evidence strength, neutral greys for text and gridlines. Pair colour with labels or a legend.
