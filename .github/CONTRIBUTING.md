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
- Each research source carries an evidence grade (**Strong**, **Moderate**, **Limited** or **Contested**) and a few words on why. Guidelines, consensus statements and expert commentary are labelled by what they are.
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
