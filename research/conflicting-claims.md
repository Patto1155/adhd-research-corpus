# Where the research disagrees: a register for analysis

This is a working register for editors, not a reader page. It lists places where good sources disagree about a claim on this site, including evidence the pages do not yet cite. Each entry gives both sides, why they may differ, how the page currently handles it, and a next step. It was compiled in November 2026 by AI agents searching PubMed and Crossref; every PubMed ID was resolved against PubMed, but sources were read at abstract level and no clinician has reviewed the entries.

Generated 2026-11-28 by `python3 tools/conflicts/build.py` from `research/conflicts/g*.json` (schema in [SCHEMA.md](conflicts/SCHEMA.md); merged data in [conflicts.json](conflicts/conflicts.json)).

## At a glance

| | Count |
|---|---|
| Conflicts recorded | 78 |
| Severity: major | 11 |
| Severity: moderate | 44 |
| Severity: minor | 23 |
| Page reports both sides | 42 |
| Page reports one side only | 19 |
| Page does not mention it | 17 |
| Include research the page does not yet cite | 61 |

## Action list: major conflicts, or pages that show only one side

| ID | Page | Topic | Severity | Page handling |
|---|---|---|---|---|
| [C01-003](#c01-003) | [Diagnosed as an adult: how was my ADHD missed, and is it the same?](../01-is-this-real/diagnosed-as-an-adult.md) | Late-onset (adult-onset) ADHD | major | Page reports both sides |
| [C01-002](#c01-002) | [Why are ADHD diagnoses rising, and is it a fad?](../01-is-this-real/more-diagnoses-than-ever.md) | Is the rise filling a gap or overdiagnosis? | major | Page reports both sides |
| [C02-001](#c02-001) | [Is ADHD genetic, and will my children have it?](../02-whats-happening-in-my-brain/genes-and-inheritance.md) | Twin heritability versus measured DNA and indirect genetic effects | major | Page reports one side only |
| [C04-013](#c04-013) | [Do periods, pregnancy and menopause make ADHD worse?](../04-did-i-cause-this-and-where-is-it-going/hormones-cycles-and-menopause.md) | After giving birth: is the evidence only two uncontrolled surveys? | major | Page does not mention it |
| [C04-019](#c04-019) | [Will ADHD shorten my life? The hard statistics in context](../04-did-i-cause-this-and-where-is-it-going/the-hard-statistics-in-context.md) | Dementia risk | major | Page reports both sides |
| [C04-001](#c04-001) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Paracetamol (acetaminophen) in pregnancy | major | Page reports both sides |
| [C06-001](#c06-001) | [How well does ADHD medication work?](../06-treatment-what-works/how-well-medication-works.md) | Certainty of methylphenidate evidence in children (Cochrane vs umbrella/network reviews) | major | Page reports both sides |
| [C06-011](#c06-011) | [How well does ADHD medication work?](../06-treatment-what-works/how-well-medication-works.md) | Does medication improve quality of life in adults? | major | Page reports one side only |
| [C06-002](#c06-002) | [Is ADHD medication safe? Heart, growth, psychosis and misuse](../06-treatment-what-works/medication-safety.md) | How often psychosis or mania follows stimulant treatment | major | Page reports one side only |
| [C06-012](#c06-012) | [Stopping ADHD medication: do benefits fade, and is it for life?](../06-treatment-what-works/staying-on-or-stopping-medication.md) | Long-term benefit: withdrawal trials vs naturalistic MTA follow-up | major | Page reports both sides |
| [C06-004](#c06-004) | [Real-life outcomes on ADHD medication: what do registries show?](../06-treatment-what-works/what-registries-show.md) | Size of registry benefits: within-person designs vs target-trial emulation | major | Page does not mention it |
| [C01-009](#c01-009) | [What is ADHD, actually?](../01-is-this-real/what-adhd-is.md) | How common is ADHD in children: 5-8% or about 2.7%? | moderate | Page does not mention it |
| [C01-006](#c01-006) | [Why are girls and women with ADHD so often missed?](../01-is-this-real/women-and-girls.md) | Sex differences in symptom presentation | moderate | Page reports one side only |
| [C02-006](#c02-006) | [Does ADHD mean my brain is damaged or "three years behind"?](../02-whats-happening-in-my-brain/brain-structure-and-development.md) | White-matter (DTI) differences: robust or fragile? | moderate | Page reports one side only |
| [C03-004](#c03-004) | [ADHD and hyperfocus: why can I focus for hours on some things?](../03-why-i-think-and-feel-this-way/attention-regulation-and-hyperfocus.md) | Is hyperfocus more common in diagnosed ADHD? | moderate | Page reports one side only |
| [C03-005](#c03-005) | [Sleep and ADHD: why can't I fall asleep, and is sleep the cause?](../03-why-i-think-and-feel-this-way/sleep-and-the-body-clock.md) | Does poor sleep cause ADHD, or the reverse? | moderate | Page does not mention it |
| [C04-014](#c04-014) | [Do periods, pregnancy and menopause make ADHD worse?](../04-did-i-cause-this-and-where-is-it-going/hormones-cycles-and-menopause.md) | Hormonal contraception and mood in ADHD | moderate | Page does not mention it |
| [C04-002](#c04-002) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Smoking in pregnancy | moderate | Page reports one side only |
| [C04-003](#c04-003) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Alcohol in pregnancy | moderate | Page does not mention it |
| [C04-004](#c04-004) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Very preterm birth: does the link survive sibling comparison? | moderate | Page does not mention it |
| [C04-005](#c04-005) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Screens and ADHD symptoms | moderate | Page reports one side only |
| [C05-002](#c05-002) | [Addiction and ADHD: is risk higher, and do medicines raise it?](../05-what-often-comes-with-it/alcohol-drugs-and-addiction.md) | Does ADHD itself lead to substance use, or is the link confounded? | moderate | Page does not mention it |
| [C05-003](#c05-003) | [Physical health problems and ADHD: is there a link?](../05-what-often-comes-with-it/physical-health.md) | ADHD and obesity: shared genes, cause, or both directions? | moderate | Page does not mention it |
| [C06-008](#c06-008) | [Neurofeedback, diet, supplements, exercise: do they help ADHD?](../06-treatment-what-works/lifestyle-and-other-approaches.md) | Neurofeedback: blinded null vs sustained effects at follow-up | moderate | Page reports one side only |
| [C06-010](#c06-010) | [Neurofeedback, diet, supplements, exercise: do they help ADHD?](../06-treatment-what-works/lifestyle-and-other-approaches.md) | Exercise: moderate-to-large vs small effects on core symptoms | moderate | Page reports one side only |
| [C06-003](#c06-003) | [Is ADHD medication safe? Heart, growth, psychosis and misuse](../06-treatment-what-works/medication-safety.md) | Long-term cardiovascular risk: registry signal vs pooled observational studies | moderate | Page reports one side only |
| [C06-007](#c06-007) | [Pregnancy, breastfeeding and ADHD medication: is it safe?](../06-treatment-what-works/pregnancy-and-breastfeeding.md) | Modafinil in pregnancy and birth defects | moderate | Page reports one side only |
| [C06-015](#c06-015) | [Real-life outcomes on ADHD medication: what do registries show?](../06-treatment-what-works/what-registries-show.md) | Suicidal thoughts: atomoxetine trial signal vs registry reassurance | moderate | Page does not mention it |
| [C07-001](#c07-001) | [Parent training and school support for ADHD: do they help?](../07-family-work-and-other-people/parenting-and-what-helps.md) | Parent training and children's core ADHD symptoms | moderate | Page reports one side only |
| [C07-003](#c07-003) | [ADHD, work and study: does treatment or support help?](../07-family-work-and-other-people/work-and-study.md) | Does structured support help university students with ADHD? | moderate | Page does not mention it |
| [C08-004](#c08-004) | [ADHD myths: which popular claims are wrong or half right?](../08-reading-this-well/myths-and-corrections.md) | Life-expectancy gap: modelled 13 years vs life-table estimates | moderate | Page reports one side only |
| [C08-005](#c08-005) | [ADHD myths: which popular claims are wrong or half right?](../08-reading-this-well/myths-and-corrections.md) | Paracetamol in pregnancy: sibling designs vs Navigation Guide review | moderate | Page reports one side only |
| [C08-006](#c08-006) | [ADHD myths: which popular claims are wrong or half right?](../08-reading-this-well/myths-and-corrections.md) | Do childhood stimulants change later addiction risk? | moderate | Page reports one side only |
| [C08-001](#c08-001) | [Where does the information on these pages come from?](../08-reading-this-well/sources-and-guidelines.md) | First-line medicine: NICE vs AADPA vs CADDRA vs network meta-analysis | moderate | Page reports one side only |
| [C01-007](#c01-007) | [Why are girls and women with ADHD so often missed?](../01-is-this-real/women-and-girls.md) | Sex ratio in adulthood and adult-onset cases | minor | Page reports one side only |
| [C03-006](#c03-006) | [Sleep and ADHD: why can't I fall asleep, and is sleep the cause?](../03-why-i-think-and-feel-this-way/sleep-and-the-body-clock.md) | Does shifting the body clock improve ADHD symptoms? | minor | Page does not mention it |
| [C03-007](#c03-007) | [Time and waiting in ADHD: why do I lose track and hate waiting?](../03-why-i-think-and-feel-this-way/time-waiting-and-rewards.md) | Why people with ADHD choose 'now' over 'later' | minor | Page reports one side only |
| [C04-006](#c04-006) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Diet beyond sugar: food colours and elimination diets | minor | Page does not mention it |
| [C04-007](#c04-007) | [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md) | Can extreme early adversity cause ADHD? | minor | Page does not mention it |
| [C05-008](#c05-008) | [Is it ADHD, or could it be something else?](../05-what-often-comes-with-it/is-it-adhd-or-something-else.md) | PTSD and ADHD: both directions, or mainly ADHD to PTSD? | minor | Page does not mention it |
| [C06-005](#c06-005) | [Real-life outcomes on ADHD medication: what do registries show?](../06-treatment-what-works/what-registries-show.md) | Mortality and medication: absolute figures now available | minor | Page does not mention it |
| [C07-002](#c07-002) | [ADHD stigma and shame: should I tell people?](../07-family-work-and-other-people/stigma-and-telling-people.md) | Trials of interventions to reduce ADHD stigma | minor | Page does not mention it |

## All conflicts, by page

### [Diagnosed as an adult: how was my ADHD missed, and is it the same?](../01-is-this-real/diagnosed-as-an-adult.md)

#### C01-003

**Late-onset (adult-onset) ADHD** · major · method/measurement · Page reports both sides

**In dispute:** Follow-up studies find most 'late' cases began in adolescence or had earlier signs, and true adult onset is rare or unproven ('the current consensus is mostly adolescent onset, or missed').

- **Position A:** Several population birth cohorts found that most young adults meeting ADHD criteria had not met criteria in childhood (Dunedin 90%; E-Risk 67.5% of 166; Pelotas only 12.6% had childhood ADHD), with comparable impairment, leading authors to propose late onset as real and possibly a distinct syndrome.
  - Moffitt TE, et al. Is adult ADHD a childhood-onset neurodevelopmental disorder? Evidence from a four-decade longitudinal cohort study. Am J Psychiatry. 2015. — [DOI 10.1176/appi.ajp.2015.14101266](https://doi.org/10.1176/appi.ajp.2015.14101266) · [PMID 25998281](https://pubmed.ncbi.nlm.nih.gov/25998281/); birth cohort, n = 1,037; cited on page; checked: PubMed record + abstract
  - Agnew-Blais JC, et al. Evaluation of the persistence, remission, and emergence of attention-deficit/hyperactivity disorder in young adulthood. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0465](https://doi.org/10.1001/jamapsychiatry.2016.0465) · [PMID 27192174](https://pubmed.ncbi.nlm.nih.gov/27192174/); birth cohort (twins), n = 2,040; **not yet cited on page**; checked: PubMed record + abstract
  - Caye A, et al. Attention-deficit/hyperactivity disorder trajectories from childhood to young adulthood: evidence from a birth cohort supporting a late-onset syndrome. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0383](https://doi.org/10.1001/jamapsychiatry.2016.0383) · [PMID 27192050](https://pubmed.ncbi.nlm.nih.gov/27192050/); birth cohort, n = 5,249 born; 81.3% retained; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** With repeated, multi-informant assessment, about 95% of apparent late cases were excluded (substance use, other conditions), remaining cases began in adolescence; a cohort analysis found parent-rated late-onset ADHD resembled child-onset ADHD in polygenic risk and cognition, suggesting delayed emergence (perhaps due to childhood resources) rather than a different disorder.
  - Sibley MH, et al. Late-onset ADHD reconsidered with comprehensive repeated assessments between ages 10 and 25. Am J Psychiatry. 2018. — [DOI 10.1176/appi.ajp.2017.17030298](https://doi.org/10.1176/appi.ajp.2017.17030298) · [PMID 29050505](https://pubmed.ncbi.nlm.nih.gov/29050505/); cohort (comparison group of MTA), n = 239; cited on page; checked: PubMed record + abstract
  - Asherson P, et al. Annual Research Review: Does late-onset attention-deficit/hyperactivity disorder exist? J Child Psychol Psychiatry. 2019. — [DOI 10.1111/jcpp.13020](https://doi.org/10.1111/jcpp.13020) · [PMID 30843223](https://pubmed.ncbi.nlm.nih.gov/30843223/); narrative review; cited on page; checked: PubMed record + abstract
  - Riglin L, et al. "Late-onset" ADHD symptoms in young adulthood: is this ADHD? J Atten Disord. 2022. — [DOI 10.1177/10870547211066486](https://doi.org/10.1177/10870547211066486) · [PMID 35034501](https://pubmed.ncbi.nlm.nih.gov/35034501/); population cohort (ALSPAC), n = 4,224-9,764; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Cohorts that measured ADHD at few time points, with screening tools, single informants or self-report in adulthood (Dunedin, E-Risk, Pelotas) find much more 'late onset'; studies with dense repeated assessments and exclusion of substance use and other disorders (MTA comparison group) find little. Self-report versus parent report changes the picture (Riglin). The Pelotas childhood screen used a questionnaire subscale. Samples also differ in country and era.

**Next step:** Add the E-Risk and Pelotas cohorts (and Riglin 2022) so the page shows that three of four large population cohorts found large late-onset groups; tabulate each cohort by assessment density, informant and exclusion rules to show how method drives the estimate; consider softening 'current consensus' to 'the leading interpretation'.

#### C01-004

**How often childhood ADHD persists into adulthood** · moderate · method/measurement · Page reports both sides

**In dispute:** About 15% still meet full criteria at 25 (65% counting partial remission); most MTA participants fluctuate; other cohorts find fluctuation less often.

- **Position A:** Meta-analysis of older follow-up studies: about 15% persist with full criteria at age 25, about 65% if impairing subthreshold symptoms are counted.
  - Faraone SV, et al. The age-dependent decline of attention deficit hyperactivity disorder: a meta-analysis of follow-up studies. Psychol Med. 2006. — [DOI 10.1017/S003329170500471X](https://doi.org/10.1017/S003329170500471X) · [PMID 16420712](https://pubmed.ncbi.nlm.nih.gov/16420712/); meta-analysis; cited on page; checked: PubMed record + abstract
- **Position B:** In the MTA cohort (8 assessments to age 25) 63.8% fluctuated in and out of threshold and only 9.1% fully recovered; three other US cohorts found fluctuation in 17-29% and never as the largest group.
  - Sibley MH, et al. Variable patterns of remission from ADHD in the Multimodal Treatment Study of ADHD. Am J Psychiatry. 2022. — [DOI 10.1176/appi.ajp.2021.21010032](https://doi.org/10.1176/appi.ajp.2021.21010032) · [PMID 34384227](https://pubmed.ncbi.nlm.nih.gov/34384227/); cohort, n = 558; cited on page; checked: PubMed record + abstract
  - Norman LJ, et al. Longitudinal trajectories of childhood and adolescent attention deficit hyperactivity disorder diagnoses in three cohorts. EClinicalMedicine. 2023. — [DOI 10.1016/j.eclinm.2023.102021](https://doi.org/10.1016/j.eclinm.2023.102021) · [PMID 37333663](https://pubmed.ncbi.nlm.nih.gov/37333663/); three cohorts, n = >10,000; cited on page; checked: PubMed record + abstract

**Why they may differ:** Persistence rates depend on how many times people are assessed (more assessments reveal fluctuation), who reports (self versus parent), whether impairment and subthreshold symptoms count, and whether samples are clinic-referred (MTA) or population-based (ABCD). The Faraone figures pool older studies with mostly two time points.

**Next step:** Present persistence as a range conditioned on definition and number of assessments; check for a newer pooled persistence meta-analysis (post-2015) to update the 2006 figures.

### [How is ADHD diagnosed, and why is there no test?](../01-is-this-real/how-diagnosis-works.md)

#### C01-008

**Ethnic differences: missed diagnoses or different measurement?** · moderate · method/measurement · Page reports both sides

**In dispute:** Lower diagnosis rates in Asian, Black and Hispanic US children look partly like missed diagnoses; but a meta-analysis estimated higher ADHD prevalence in Black Americans.

- **Position A:** Insurance-claims and survey cohorts found minority children less likely to be diagnosed and treated, interpreted as under-diagnosis of minority children rather than over-diagnosis of White children.
  - Shi Y, et al. Racial disparities in diagnosis of attention-deficit/hyperactivity disorder in a US national birth cohort. JAMA Netw Open. 2021. — [DOI 10.1001/jamanetworkopen.2021.0321](https://doi.org/10.1001/jamanetworkopen.2021.0321) · [PMID 33646315](https://pubmed.ncbi.nlm.nih.gov/33646315/); claims cohort, n = 238,011; cited on page; checked: PubMed record + abstract
  - Coker TR, et al. Racial and ethnic disparities in ADHD diagnosis and treatment. Pediatrics. 2016. — [DOI 10.1542/peds.2016-0407](https://doi.org/10.1542/peds.2016-0407) · [PMID 27553219](https://pubmed.ncbi.nlm.nih.gov/27553219/); longitudinal survey, n = 4,297; cited on page; checked: PubMed record + abstract
- **Position B:** A meta-analysis of 21 US studies estimated ADHD at about 14.5% among Black individuals, higher than general US estimates.
  - Cénat JM, et al. Prevalence and risk factors associated with attention-deficit/hyperactivity disorder among US Black individuals: a systematic review and meta-analysis. JAMA Psychiatry. 2021. — [DOI 10.1001/jamapsychiatry.2020.2788](https://doi.org/10.1001/jamapsychiatry.2020.2788) · [PMID 32902608](https://pubmed.ncbi.nlm.nih.gov/32902608/); meta-analysis, n = 21 studies; >150,000; cited on page; checked: PubMed record + abstract

**Why they may differ:** A uses recorded diagnoses in insured populations; B pools symptom-based estimates, many from disadvantaged samples, where adversity raises symptom scores and rating scales may not be measurement-invariant across groups. Both can be true: higher symptom levels in some samples and lower access to diagnosis.

**Next step:** Look for measurement-invariance studies of ADHD rating scales across US ethnic groups, and for a non-US (UK/Australia) registry study of ethnicity and ADHD diagnosis, which the page says is missing.

### [Why are ADHD diagnoses rising, and is it a fad?](../01-is-this-real/more-diagnoses-than-ever.md)

#### C01-002

**Is the rise filling a gap or overdiagnosis?** · major · causal interpretation · Page reports both sides

**In dispute:** The same system over-diagnoses some groups (young-for-year, milder cases) and under-diagnoses others (older adults, minority children, girls).

- **Position A:** Evidence consistent with overdiagnosis in children: rising diagnosis and prescribing, extra cases tending to be milder, and a few studies suggesting diminishing returns where harms may outweigh benefits for mild cases.
  - Kazda L, et al. Overdiagnosis of attention-deficit/hyperactivity disorder in children and adolescents: a systematic scoping review. JAMA Netw Open. 2021. — [DOI 10.1001/jamanetworkopen.2021.5335](https://doi.org/10.1001/jamanetworkopen.2021.5335) · [PMID 33843998](https://pubmed.ncbi.nlm.nih.gov/33843998/); scoping review, n = 334 studies; cited on page; checked: PubMed record + abstract
- **Position B:** Recorded ADHD in England in 2025 (1.19% of patients) was still well below expected prevalence in every age group, from about 29% shortfall in young men to about 94% in people over 65, read by the authors as continued under-recognition. A 2026 multi-author UK commentary concluded there is no evidence of UK overdiagnosis (while noting rigorous post-pandemic data are lacking and some low-quality assessments may misdiagnose), and an editorial by the chair of the NHS-England ADHD taskforce noted UK administrative prevalence is below population rates.
  - John A, et al. Attention-deficit/hyperactivity disorder in children and adults in England, 2000-2025: recorded prevalence and diagnostic trends. Lancet Reg Health Eur. 2026. — [DOI 10.1016/j.lanepe.2026.101740](https://doi.org/10.1016/j.lanepe.2026.101740) · [PMID 42577275](https://pubmed.ncbi.nlm.nih.gov/42577275/); primary-care records cohort, n = 3.5 million; cited on page; checked: PubMed record + abstract
  - Cortese S, et al. ADHD (over) diagnosis: fiction, fashion and failure. Br J Psychiatry. 2026. — [DOI 10.1192/bjp.2026.10546](https://doi.org/10.1192/bjp.2026.10546) · [PMID 41787830](https://pubmed.ncbi.nlm.nih.gov/41787830/); expert commentary (multi-author); **not yet cited on page**; checked: PubMed record + abstract
  - Thapar A. Editorial Perspective: Overdiagnosis of ADHD? Here we go again. Child Adolesc Ment Health. 2026. — [DOI 10.1111/camh.70075](https://doi.org/10.1111/camh.70075) · [PMID 41725142](https://pubmed.ncbi.nlm.nih.gov/41725142/); editorial; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Kazda's evidence is mostly from children and from high-diagnosing systems (US, Australia) before 2020; John compares coded GP diagnoses in England against prevalence benchmarks from other studies, and GP coding may miss specialist or private diagnoses (understating recorded prevalence). 'Milder' new cases can be read either as overdiagnosis or as legitimate diagnoses of a dimensional condition. Both may be true in different groups.

**Next step:** Add the 2026 UK commentaries (Cortese; Thapar) so the page shows the current UK expert position as well as Kazda; weigh against direct outcome evidence: find studies comparing outcomes (benefit and harm) of diagnosis/treatment in near-threshold cases; check whether John et al. adjust for private-sector diagnoses not coded in GP records; add any newer overdiagnosis/underdiagnosis estimates for adults.

#### C01-001

**Stable prevalence versus rising diagnoses** · moderate · method/measurement · Page reports both sides

**In dispute:** The share of children who meet ADHD criteria has not risen over three decades, while recorded diagnoses have risen sharply (US, Sweden, England).

- **Position A:** When standardised criteria are applied in community samples, the proportion of children meeting ADHD criteria is stable across decades and regions; in Swedish twins, diagnosis-level parent-rated symptoms did not change 2004-2014.
  - Polanczyk GV, et al. ADHD prevalence estimates across three decades: an updated systematic review and meta-regression analysis. Int J Epidemiol. 2014. — [DOI 10.1093/ije/dyt261](https://doi.org/10.1093/ije/dyt261) · [PMID 24464188](https://pubmed.ncbi.nlm.nih.gov/24464188/); meta-regression, n = 135 studies; cited on page; checked: PubMed record + abstract
  - Rydell M, et al. Has the attention deficit hyperactivity disorder phenotype become more common in children between 2004 and 2014? Trends over 10 years from a Swedish general population sample. J Child Psychol Psychiatry. 2018. — [DOI 10.1111/jcpp.12882](https://doi.org/10.1111/jcpp.12882) · [PMID 29484650](https://pubmed.ncbi.nlm.nih.gov/29484650/); twin cohort linked to registers, n = 19,271; cited on page; checked: PubMed record + abstract
- **Position B:** Diagnosed ADHD has risen substantially: parent-reported US diagnoses from 6.1% to 10.2% (1997-2016), Swedish register diagnoses more than fivefold, and English GP-recorded new diagnoses accelerating after 2020.
  - Xu G, et al. Twenty-year trends in diagnosed attention-deficit/hyperactivity disorder among US children and adolescents, 1997-2016. JAMA Netw Open. 2018. — [DOI 10.1001/jamanetworkopen.2018.1471](https://doi.org/10.1001/jamanetworkopen.2018.1471) · [PMID 30646132](https://pubmed.ncbi.nlm.nih.gov/30646132/); repeated national survey, n = 186,457; cited on page; checked: PubMed record + abstract
  - John A, et al. Attention-deficit/hyperactivity disorder in children and adults in England, 2000-2025: recorded prevalence and diagnostic trends. Lancet Reg Health Eur. 2026. — [DOI 10.1016/j.lanepe.2026.101740](https://doi.org/10.1016/j.lanepe.2026.101740) · [PMID 42577275](https://pubmed.ncbi.nlm.nih.gov/42577275/); primary-care records cohort, n = 3.5 million (prevalence); 42 million (trends); cited on page; checked: PubMed record + abstract

**Why they may differ:** These are not strictly contradictory: A measures how many children meet criteria when everyone is assessed the same way; B measures who reaches a clinician and gets a recorded diagnosis. The gap is filled by changes in awareness, access, thresholds and recording. The open dispute is how much of the gap is catching previously missed cases versus adding milder or borderline ones. Polanczyk's series ends in about 2013, before the post-2020 surge, so 'stable true prevalence' is an extrapolation for the most recent period.

**Next step:** Look for community prevalence surveys using standardised criteria conducted after 2020 (for example, repeated national child mental-health surveys) to test whether true prevalence is still flat during the post-pandemic diagnosis surge; state on the page that the stable-prevalence series predates 2020.

### [What is ADHD, actually?](../01-is-this-real/what-adhd-is.md)

#### C01-009

**How common is ADHD in children: 5-8% or about 2.7%?** · moderate · method/measurement · Page does not mention it

**In dispute:** Pooled studies put ADHD in roughly 5-8% of children and adolescents (WFADHD 5.9%; Salari 7.6% for ages 3-12 and 5.6% for 12-18).

- **Position A:** Meta-analyses of community studies give child/adolescent prevalence around 5-8%; Cortese's re-analysis of the GBD's own input data (pre-2013) gave 5.41%.
  - Faraone SV, et al. The World Federation of ADHD International Consensus Statement: 208 evidence-based conclusions about the disorder. Neurosci Biobehav Rev. 2021. — [DOI 10.1016/j.neubiorev.2021.01.022](https://doi.org/10.1016/j.neubiorev.2021.01.022) · [PMID 33549739](https://pubmed.ncbi.nlm.nih.gov/33549739/); consensus statement; cited on page; checked: PubMed record + abstract
  - Salari N, et al. The global prevalence of ADHD in children and adolescents: a systematic review and meta-analysis. Ital J Pediatr. 2023. — [DOI 10.1186/s13052-023-01456-1](https://doi.org/10.1186/s13052-023-01456-1) · [PMID 37081447](https://pubmed.ncbi.nlm.nih.gov/37081447/); meta-analysis, n = 61 studies; cited on page; checked: PubMed record + abstract
  - Cortese S, et al. Incidence, prevalence, and global burden of ADHD from 1990 to 2019 across 204 countries: data, with critical re-analysis, from the Global Burden of Disease study. Mol Psychiatry. 2023. — [DOI 10.1038/s41380-023-02228-3](https://doi.org/10.1038/s41380-023-02228-3) · [PMID 37684322](https://pubmed.ncbi.nlm.nih.gov/37684322/); re-analysis of GBD data; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** The Global Burden of Disease study, widely used in policy, modelled child/adolescent prevalence at 2.68% and lifespan prevalence at 1.13% in 2019, with a slight fall (-8.75%) in age-standardised prevalence since 1990.
  - Cortese S, et al. Incidence, prevalence, and global burden of ADHD from 1990 to 2019 across 204 countries: data, with critical re-analysis, from the Global Burden of Disease study. Mol Psychiatry. 2023. — [DOI 10.1038/s41380-023-02228-3](https://doi.org/10.1038/s41380-023-02228-3) · [PMID 37684322](https://pubmed.ncbi.nlm.nih.gov/37684322/); GBD modelled estimates (reported), n = 204 countries; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** GBD imputes prevalence for countries with no data and applies its own case definitions, which Cortese et al. argue underestimate ADHD; meta-analyses pool heterogeneous surveys, often with screening tools that can overestimate (Salari's 7.6% is high). Readers will meet the GBD figure in news and policy documents, so the gap needs explaining.

**Next step:** Add one sentence on what-adhd-is.md noting the much lower GBD modelled estimate and why it differs; check whether GBD 2023 (Lancet 2026, PMID 42167272) revised the ADHD figure.

#### C01-005

**Adult prevalence: 2.6% versus 6.8%** · minor · method/measurement · Page reports both sides

**In dispute:** About 2.6% of adults have persistent childhood-onset ADHD; about 6.8% have current symptoms meeting criteria.

- **Position A:** Adult ADHD with childhood onset: about 2.58% globally (Song), close to the WFADHD consensus figure of 2.5%.
  - Song P, et al. The prevalence of adult attention-deficit hyperactivity disorder: a global systematic review and meta-analysis. J Glob Health. 2021. — [DOI 10.7189/jogh.11.04009](https://doi.org/10.7189/jogh.11.04009) · [PMID 33692893](https://pubmed.ncbi.nlm.nih.gov/33692893/); meta-analysis; cited on page; checked: PubMed record + abstract
  - Faraone SV, et al. The World Federation of ADHD International Consensus Statement: 208 evidence-based conclusions about the disorder. Neurosci Biobehav Rev. 2021. — [DOI 10.1016/j.neubiorev.2021.01.022](https://doi.org/10.1016/j.neubiorev.2021.01.022) · [PMID 33549739](https://pubmed.ncbi.nlm.nih.gov/33549739/); consensus statement; cited on page; checked: PubMed record + abstract
- **Position B:** Symptomatic adult ADHD without checking childhood onset: about 6.76%, more than double.
  - Song P, et al. The prevalence of adult attention-deficit hyperactivity disorder: a global systematic review and meta-analysis. J Glob Health. 2021. — [DOI 10.7189/jogh.11.04009](https://doi.org/10.7189/jogh.11.04009) · [PMID 33692893](https://pubmed.ncbi.nlm.nih.gov/33692893/); meta-analysis; cited on page; checked: PubMed record + abstract

**Why they may differ:** The difference is mostly definitional: requiring documented childhood onset and full criteria versus counting current symptoms with impairment. It interacts with the late-onset debate (C01-003): which figure is 'right' depends on whether adult-onset cases count as ADHD.

**Next step:** Cross-link the two figures to the late-onset record; keep both figures with their definitions wherever adult prevalence is quoted on the site.

### [Why are girls and women with ADHD so often missed?](../01-is-this-real/women-and-girls.md)

#### C01-006

**Sex differences in symptom presentation** · moderate · method/measurement · Page reports one side only

**In dispute:** On full clinical interviews, core symptom severity looks similar across sexes; separately, expert consensus says girls tend to present with more inattention and less disruptive behaviour.

- **Position A:** A 2024 meta-analysis of 52 studies found no significant sex difference in core symptom severity on clinical interviews, in children or adults.
  - Young S, et al. A systematic review and meta-analysis comparing the severity of core symptoms of attention-deficit hyperactivity disorder in females and males. Psychol Med. 2024. — [DOI 10.1017/S0033291724001600](https://doi.org/10.1017/S0033291724001600) · [PMID 39494848](https://pubmed.ncbi.nlm.nih.gov/39494848/); meta-analysis, n = 52 studies; 8,423 females, 9,985 males; cited on page; checked: PubMed record + abstract
- **Position B:** Earlier meta-analyses of diagnosed youth found boys rated more hyperactive than girls (and, in the older review, girls rated lower on all symptom domains), with boys showing more motor-inhibition and flexibility difficulties; the expert consensus also describes a more inattentive, less disruptive female presentation.
  - Loyer Carbonneau M, et al. Meta-analysis of sex differences in ADHD symptoms and associated cognitive deficits. J Atten Disord. 2021. — [DOI 10.1177/1087054720923736](https://doi.org/10.1177/1087054720923736) · [PMID 32495675](https://pubmed.ncbi.nlm.nih.gov/32495675/); meta-analysis, n = studies 1997-2017; **not yet cited on page**; checked: PubMed record + abstract
  - Gershon J. A meta-analytic review of gender differences in ADHD. J Atten Disord. 2002. — [DOI 10.1177/108705470200500302](https://doi.org/10.1177/108705470200500302) · [PMID 11911007](https://pubmed.ncbi.nlm.nih.gov/11911007/); meta-analysis; **not yet cited on page**; checked: PubMed record + abstract
  - Young S, et al. Females with ADHD: an expert consensus statement taking a lifespan approach providing guidance for the identification and treatment of attention-deficit/hyperactivity disorder in girls and women. BMC Psychiatry. 2020. — [DOI 10.1186/s12888-020-02707-9](https://doi.org/10.1186/s12888-020-02707-9) · [PMID 32787804](https://pubmed.ncbi.nlm.nih.gov/32787804/); expert consensus; cited on page; checked: PubMed record + abstract

**Why they may differ:** Young 2024 restricted to clinical interviews, which may standardise ratings; the other meta-analyses pooled rating scales from parents and teachers, where rater expectation and referral bias (more severely hyperactive girls are referred) operate. 'No difference in severity among those diagnosed' and 'girls present differently in the population' can both be true because diagnosed girls are a selected group.

**Next step:** Add the Loyer Carbonneau 2021 meta-analysis (hyperactivity higher in boys) alongside Young 2024, and explain that diagnosed samples are selected; check whether Young 2024 analysed hyperactivity and inattention separately by measure.

#### C01-007

**Sex ratio in adulthood and adult-onset cases** · minor · population/age · Page reports one side only

**In dispute:** In adulthood the sex difference is smaller; the Dunedin cohort found adult ADHD roughly balanced between men and women.

- **Position A:** Boys outnumber girls in childhood studies; the gap narrows in adults (Dunedin roughly balanced).
  - Willcutt EG. The prevalence of DSM-IV attention-deficit/hyperactivity disorder: a meta-analytic review. Neurotherapeutics. 2012. — [DOI 10.1007/s13311-012-0135-8](https://doi.org/10.1007/s13311-012-0135-8) · [PMID 22976615](https://pubmed.ncbi.nlm.nih.gov/22976615/); meta-analysis, n = 86 child studies; 11 adult studies; cited on page; checked: PubMed record + abstract
  - Moffitt TE, et al. Is adult ADHD a childhood-onset neurodevelopmental disorder? Evidence from a four-decade longitudinal cohort study. Am J Psychiatry. 2015. — [DOI 10.1176/appi.ajp.2015.14101266](https://doi.org/10.1176/appi.ajp.2015.14101266) · [PMID 25998281](https://pubmed.ncbi.nlm.nih.gov/25998281/); birth cohort, n = 1,037; cited on page; checked: PubMed record + abstract
- **Position B:** In the Pelotas birth cohort, childhood ADHD was male-predominant but young-adult ADHD (mostly without childhood ADHD) was female-predominant (39% male versus 50% in those without ADHD).
  - Caye A, et al. Attention-deficit/hyperactivity disorder trajectories from childhood to young adulthood: evidence from a birth cohort supporting a late-onset syndrome. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0383](https://doi.org/10.1001/jamapsychiatry.2016.0383) · [PMID 27192050](https://pubmed.ncbi.nlm.nih.gov/27192050/); birth cohort, n = 5,249; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Whether the adult sex ratio balances or reverses depends on whether adult cases are counted without requiring childhood onset; adult self-report, higher help-seeking by women and late-emerging cases (C01-003) all push female representation up. This is tangled with the late-onset question, so the adult ratio cannot be read simply as 'girls finally recognised'.

**Next step:** Note that the adult sex balance depends on case definition and cross-reference the late-onset record; look for adult registry incidence by sex after 2020 (e.g., John 2026 full text) to see whether recorded new adult diagnoses now favour women.

### [Does ADHD mean my brain is damaged or "three years behind"?](../02-whats-happening-in-my-brain/brain-structure-and-development.md)

#### C02-002

**Does stimulant medication change brain structure?** · moderate · causal interpretation · Page reports both sides

**In dispute:** ENIGMA found no medication effect on subcortical volumes; smaller VBM meta-analyses linked stimulant use to more typical brain measures; 'no randomised trial has settled it'.

- **Position A:** In the largest mega-analysis (3,242 scans), subcortical differences were the same with or without stimulant history; a 1-year placebo-controlled trial in adults found no grey-matter volume loss with methylphenidate (a trend to cerebellar grey-matter increase).
  - Hoogman M, et al. Subcortical brain volume differences in participants with attention deficit hyperactivity disorder in children and adults: a cross-sectional mega-analysis. Lancet Psychiatry. 2017. — [DOI 10.1016/S2215-0366(17)30049-4](https://doi.org/10.1016/S2215-0366(17)30049-4) · [PMID 28219628](https://pubmed.ncbi.nlm.nih.gov/28219628/); mega-analysis, n = 3,242; cited on page; checked: PubMed record + abstract
  - Tebartz van Elst L, et al. The effect of methylphenidate intake on brain structure in adults with ADHD in a placebo-controlled randomized trial. J Psychiatry Neurosci. 2016. — [DOI 10.1503/jpn.150320](https://doi.org/10.1503/jpn.150320) · [PMID 27575717](https://pubmed.ncbi.nlm.nih.gov/27575717/); RCT, n = 131 at baseline; 76 at 1 year; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** VBM meta-analyses found samples with more stimulant-treated participants had more typical basal ganglia values; a 16-week randomised placebo-controlled trial found methylphenidate increased white-matter FA in several tracts in boys aged 10-12 but not in adult men, suggesting age-dependent medication effects.
  - Nakao T, et al. Gray matter volume abnormalities in ADHD: voxel-based meta-analysis exploring the effects of age and stimulant medication. Am J Psychiatry. 2011. — [DOI 10.1176/appi.ajp.2011.11020281](https://doi.org/10.1176/appi.ajp.2011.11020281) · [PMID 21865529](https://pubmed.ncbi.nlm.nih.gov/21865529/); meta-analysis, n = 14 datasets; 722; cited on page; checked: PubMed record + abstract
  - Frodl T, Skokauskas N. Meta-analysis of structural MRI studies in children and adults with attention deficit hyperactivity disorder indicates treatment effects. Acta Psychiatr Scand. 2012. — [DOI 10.1111/j.1600-0447.2011.01786.x](https://doi.org/10.1111/j.1600-0447.2011.01786.x) · [PMID 22118249](https://pubmed.ncbi.nlm.nih.gov/22118249/); meta-analysis; cited on page; checked: PubMed record + abstract
  - Bouziane C, et al. White matter by diffusion MRI following methylphenidate treatment: a randomized control trial in males with attention-deficit/hyperactivity disorder. Radiology. 2019. — [DOI 10.1148/radiol.2019182528](https://doi.org/10.1148/radiol.2019182528) · [PMID 31407970](https://pubmed.ncbi.nlm.nih.gov/31407970/); RCT (ePOD-MPH), n = 50 boys, 48 men; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Cross-study associations (meta-regression on % medicated) are confounded by severity and age; ENIGMA's medication data are lifetime yes/no histories from mixed sites. The two trials are small, short and measure different things (grey-matter volume in adults versus white-matter FA in boys), and they actually agree that adults show little change; Bouziane's region-of-interest analysis was null and only a voxel-wise age interaction was significant.

**Next step:** Update the page's 'No randomised trial has settled it': add the two small RCTs (Tebartz van Elst 2016; Bouziane 2019) and explain they suggest possible age-dependent white-matter effects in children and no volume loss in adults, without settling long-term effects. Check for further ePOD-MPH outputs (grey matter, dopamine).

#### C02-003

**"Three years behind": cortical maturation delay** · moderate · method/measurement · Page reports both sides

**In dispute:** Half the cortex reached peak thickness about 3 years later in children with ADHD (Shaw 2007); ENIGMA found mostly no thickness differences.

- **Position A:** A longitudinal cohort found a delay in the age of peak cortical thickness (10.5 versus 7.5 years); a 2026 systematic review of 32 longitudinal MRI studies concluded that delayed peaks in thickness, surface area and gyrification are a recurring finding.
  - Shaw P, et al. Attention-deficit/hyperactivity disorder is characterized by a delay in cortical maturation. PNAS. 2007. — [DOI 10.1073/pnas.0707741104](https://doi.org/10.1073/pnas.0707741104) · [PMID 18024590](https://pubmed.ncbi.nlm.nih.gov/18024590/); longitudinal cohort, n = 223 + 223 children; 824 scans; cited on page; checked: PubMed record + abstract
  - Ishii-Takahashi A, et al. Longitudinal MRI studies of children with attention-deficit/hyperactivity disorder: a systematic review. Psychiatry Clin Neurosci. 2026. — [DOI 10.1111/pcn.70100](https://doi.org/10.1111/pcn.70100) · [PMID 42503306](https://pubmed.ncbi.nlm.nih.gov/42503306/); systematic review (+ small meta-analysis), n = 32 studies; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** The large ENIGMA cortical analysis found thickness differences in only two regions in children and none in adolescents or adults; the 2026 review's own meta-analysis found no difference in longitudinal change of total grey matter; an ABCD brain-age study found 'younger-looking' regional brain age in ADHD but tiny effects (d -0.08 to -0.12).
  - Hoogman M, et al. Brain imaging of the cortex in ADHD: a coordinated analysis of large-scale clinical and population-based samples. Am J Psychiatry. 2019. — [DOI 10.1176/appi.ajp.2019.18091033](https://doi.org/10.1176/appi.ajp.2019.18091033) · [PMID 31014101](https://pubmed.ncbi.nlm.nih.gov/31014101/); mega-analysis, n = 4,180; cited on page; checked: PubMed record + abstract
  - Gagnon A, et al. Regional brain age deviations reveal divergent developmental pathways in youth. Biol Psychiatry Cogn Neurosci Neuroimaging. 2026. — [DOI 10.1016/j.bpsc.2026.03.010](https://doi.org/10.1016/j.bpsc.2026.03.010) · [PMID 41905477](https://pubmed.ncbi.nlm.nih.gov/41905477/); cohort (ABCD), normative brain-age model; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Shaw measured timing of a peak with repeated scans in one NIMH sample; ENIGMA compares thickness at a single time point across sites, which cannot detect a shifted trajectory if curves cross. Delay may be large in timing but small in magnitude at any one age. Single-site longitudinal studies also have selection bias, which the 2026 review flags.

**Next step:** Add the 2026 longitudinal review as the current summary of trajectory studies and note its null pooled grey-matter result; distinguish 'delayed timing' from 'smaller differences at a single scan' in plain language.

#### C02-006

**White-matter (DTI) differences: robust or fragile?** · moderate · direct contradiction · Page reports one side only

**In dispute:** Lower FA in the corpus callosum in pooled studies is fragile: not in children analysed alone, null in high-quality studies, and possibly due to head motion.

- **Position A:** The largest review (129 studies) found the high-quality-only analysis null and no effect in children; a meta-analysis showed most motion-matched studies found no FA difference.
  - Parlatini V, et al. White matter alterations in attention-deficit/hyperactivity disorder (ADHD): a systematic review of 129 diffusion imaging studies with meta-analysis. Mol Psychiatry. 2023. — [DOI 10.1038/s41380-023-02173-1](https://doi.org/10.1038/s41380-023-02173-1) · [PMID 37479785](https://pubmed.ncbi.nlm.nih.gov/37479785/); systematic review and meta-analysis, n = 6,739 + 6,476; cited on page; checked: PubMed record + abstract
  - Aoki Y, et al. Research Review: Diffusion tensor imaging studies of attention-deficit/hyperactivity disorder: meta-analyses and reflections on head motion. J Child Psychol Psychiatry. 2018. — [DOI 10.1111/jcpp.12778](https://doi.org/10.1111/jcpp.12778) · [PMID 28671333](https://pubmed.ncbi.nlm.nih.gov/28671333/); meta-analysis, n = 27 datasets; cited on page; checked: PubMed record + abstract
- **Position B:** A mega-analysis of raw DTI from 6,993 youths aged 6-18 in five cohorts found ADHD associated with lower FA in the inferior longitudinal and left uncinate fasciculi (largest d -0.3), specific to ADHD versus mood/anxiety/externalising problems, and holding after matching on in-scanner motion.
  - Sudre G, et al. A mega-analytic study of white matter microstructural differences across 5 cohorts of youths with attention-deficit/hyperactivity disorder. Biol Psychiatry. 2023. — [DOI 10.1016/j.biopsych.2022.09.021](https://doi.org/10.1016/j.biopsych.2022.09.021) · [PMID 36609028](https://pubmed.ncbi.nlm.nih.gov/36609028/); mega-analysis, n = 6,993; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Literature meta-analyses pool small studies with varied scanners and tract definitions; the mega-analysis harmonised raw data and controlled motion, giving power to detect small effects. The tracts also differ (corpus callosum in meta-analyses versus inferior longitudinal/uncinate in the mega-analysis), so 'fragile' may apply to the callosal finding but not to white-matter differences in children generally.

**Next step:** Add Sudre 2023 to the white-matter section and the summary table; revise 'not robust in children' to say a motion-matched mega-analysis in children found small differences in different tracts.

#### C02-005

**Population (ABCD) versus clinic (ENIGMA) brain differences** · minor · size of effect · Page reports both sides

**In dispute:** Population samples such as ABCD found smaller structural differences (d -0.06 to -0.11) than clinic samples (ENIGMA d up to -0.19 in children).

- **Position A:** ENIGMA mega-analyses of mostly clinic-recruited samples: subcortical d -0.11 to -0.19 and total surface area d -0.21 in children.
  - Hoogman M, et al. Subcortical brain volume differences in participants with attention deficit hyperactivity disorder in children and adults: a cross-sectional mega-analysis. Lancet Psychiatry. 2017. — [DOI 10.1016/S2215-0366(17)30049-4](https://doi.org/10.1016/S2215-0366(17)30049-4) · [PMID 28219628](https://pubmed.ncbi.nlm.nih.gov/28219628/); mega-analysis, n = 3,242; cited on page; checked: PubMed record + abstract
  - Hoogman M, et al. Brain imaging of the cortex in ADHD: a coordinated analysis of large-scale clinical and population-based samples. Am J Psychiatry. 2019. — [DOI 10.1176/appi.ajp.2019.18091033](https://doi.org/10.1176/appi.ajp.2019.18091033) · [PMID 31014101](https://pubmed.ncbi.nlm.nih.gov/31014101/); mega-analysis, n = 4,180; cited on page; checked: PubMed record + abstract
- **Position B:** In about 10,700 ABCD 9-10-year-olds only 11 of 79 measures differed, with d -0.06 to -0.11; an ABCD brain-age study likewise found d -0.08 to -0.12.
  - Bernanke J, et al. Structural brain measures among children with and without ADHD in the Adolescent Brain and Cognitive Development Study cohort: a cross-sectional US population-based study. Lancet Psychiatry. 2022. — [DOI 10.1016/S2215-0366(21)00505-8](https://doi.org/10.1016/S2215-0366(21)00505-8) · [PMID 35143759](https://pubmed.ncbi.nlm.nih.gov/35143759/); population cohort, n = 10,736; cited on page; checked: PubMed record + abstract
  - Gagnon A, et al. Regional brain age deviations reveal divergent developmental pathways in youth. Biol Psychiatry Cogn Neurosci Neuroimaging. 2026. — [DOI 10.1016/j.bpsc.2026.03.010](https://doi.org/10.1016/j.bpsc.2026.03.010) · [PMID 41905477](https://pubmed.ncbi.nlm.nih.gov/41905477/); population cohort (ABCD); **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** ABCD identifies ADHD by parent-report questionnaires in a general-population sample (milder, more misclassification, narrow age band); ENIGMA pools clinic cases across ages and sites with harmonised processing but site and selection heterogeneity. Small effects in big samples are more precise, so the true clinical-population effect is probably at the low end of ENIGMA's range.

**Next step:** Keep both; consider stating in the short answer that the largest and most population-representative sample found the smallest differences.

#### C02-009

**Do brain differences fade in adults?** · minor · causal interpretation · Page reports both sides

**In dispute:** Structural differences were in children, not adults (no significant adult differences in ENIGMA); a machine-learning study found features shared by children and adults.

- **Position A:** ENIGMA found subcortical and cortical differences only in children; none significant in adults.
  - Hoogman M, et al. Subcortical brain volume differences in participants with attention deficit hyperactivity disorder in children and adults: a cross-sectional mega-analysis. Lancet Psychiatry. 2017. — [DOI 10.1016/S2215-0366(17)30049-4](https://doi.org/10.1016/S2215-0366(17)30049-4) · [PMID 28219628](https://pubmed.ncbi.nlm.nih.gov/28219628/); mega-analysis, n = 3,242; cited on page; checked: PubMed record + abstract
  - Hoogman M, et al. Brain imaging of the cortex in ADHD: a coordinated analysis of large-scale clinical and population-based samples. Am J Psychiatry. 2019. — [DOI 10.1176/appi.ajp.2019.18091033](https://doi.org/10.1176/appi.ajp.2019.18091033) · [PMID 31014101](https://pubmed.ncbi.nlm.nih.gov/31014101/); mega-analysis, n = 4,180; cited on page; checked: PubMed record + abstract
- **Position B:** A classifier trained on ENIGMA scans separated ADHD from controls above chance in adults as well as children, and found similar structural anomalies across ages.
  - Zhang-James Y, et al. Evidence for similar structural brain anomalies in youth and adult attention-deficit/hyperactivity disorder: a machine learning analysis. Transl Psychiatry. 2021. — [DOI 10.1038/s41398-021-01201-4](https://doi.org/10.1038/s41398-021-01201-4) · [PMID 33526765](https://pubmed.ncbi.nlm.nih.gov/33526765/); machine-learning analysis of ENIGMA data, n = about 4,000; cited on page; checked: PubMed record + abstract

**Why they may differ:** Univariate region-by-region tests can be null in adults while a multivariate pattern remains detectable; adult samples are smaller and adults who still meet criteria are a selected group. Cross-sectional data cannot show convergence within people.

**Next step:** Check the Zhang-James full text for adult AUC to say how far above chance; the page's 'What this means for you' ('the largest adult scan comparisons found no reliable differences') should mention the multivariate result.

### [Is ADHD caused by low dopamine?](../02-whats-happening-in-my-brain/dopamine-noradrenaline-and-myths.md)

#### C02-004

**Dopamine transporter: lower or higher in ADHD?** · moderate · direct contradiction · Page reports both sides

**In dispute:** Dopamine scans disagree on direction: lower DAT in never-medicated adults (Volkow) versus 14% higher pooled striatal DAT (Fusar-Poli), with the medication explanation disputed.

- **Position A:** Never-medicated adults show lower DAT (and D2/D3) availability in reward regions; a 2024 SPECT study of 20 drug-naive adults also found lower DAT in the nucleus accumbens, with inattention linked to lower caudate DAT.
  - Volkow ND, et al. Evaluating dopamine reward pathway in ADHD: clinical implications. JAMA. 2009. — [DOI 10.1001/jama.2009.1308](https://doi.org/10.1001/jama.2009.1308) · [PMID 19738093](https://pubmed.ncbi.nlm.nih.gov/19738093/); PET case-control, n = 53 + 44; cited on page; checked: PubMed record + abstract
  - Itagaki S, et al. Reduced dopamine transporter availability in drug-naive adult attention-deficit/hyperactivity disorder. PCN Rep. 2024. — [DOI 10.1002/pcn5.177](https://doi.org/10.1002/pcn5.177) · [PMID 38868484](https://pubmed.ncbi.nlm.nih.gov/38868484/); SPECT case-control, n = 20 + 20; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Pooled across 9 PET/SPECT studies, striatal DAT was on average 14% higher in ADHD, higher in previously medicated and lower in drug-naive samples, suggesting upregulation as an adaptation to stimulants; a letter disputed the medication coding.
  - Fusar-Poli P, et al. Striatal dopamine transporter alterations in ADHD: pathophysiology or adaptation to psychostimulants? A meta-analysis. Am J Psychiatry. 2012. — [DOI 10.1176/appi.ajp.2011.11060940](https://doi.org/10.1176/appi.ajp.2011.11060940) · [PMID 22294258](https://pubmed.ncbi.nlm.nih.gov/22294258/); meta-analysis, n = 9 studies; 169 + 173; cited on page; checked: PubMed record + abstract
  - Spencer TJ, et al. Striatal dopamine transporter binding in adults with ADHD. Am J Psychiatry. 2012. — [DOI 10.1176/appi.ajp.2012.12020232](https://doi.org/10.1176/appi.ajp.2012.12020232) · [PMID 22684601](https://pubmed.ncbi.nlm.nih.gov/22684601/); letter/critique; cited on page; checked: PubMed record only

**Why they may differ:** Tracers differ in selectivity (e.g., beta-CIT also binds serotonin transporters), regions differ (whole striatum versus accumbens), samples are tiny, and prior medication may up-regulate DAT. The newer drug-naive study fits Fusar-Poli's own suggestion that drug-naive samples show lower DAT, so the medication-adaptation explanation and the 'lower in untreated ADHD' finding are compatible. No pooled analysis since 2012 was found.

**Next step:** Add Itagaki 2024 as a further drug-naive data point; note tracer differences in the table; search for any post-2012 DAT meta-analysis or longitudinal PET before/after stimulant exposure to test the adaptation hypothesis directly.

#### C02-007

**Resting-state connectivity: any consistent pattern?** · minor · method/measurement · Page reports both sides

**In dispute:** Meta-analyses disagree (null convergence versus reduced default-mode connectivity versus frontoparietal-default over-connection); the largest mega-analysis found tiny striato-cortical differences.

- **Position A:** A preregistered meta-analysis of 30 studies found no location where connectivity differences converged.
  - Cortese S, et al. Systematic review and meta-analysis: resting-state functional magnetic resonance imaging studies of attention-deficit/hyperactivity disorder. J Am Acad Child Adolesc Psychiatry. 2021. — [DOI 10.1016/j.jaac.2020.08.014](https://doi.org/10.1016/j.jaac.2020.08.014) · [PMID 32946973](https://pubmed.ncbi.nlm.nih.gov/32946973/); meta-analysis (preregistered), n = 30 studies; 1,094 + 884; cited on page; checked: PubMed record + abstract
- **Position B:** Two other meta-analyses reported (different) network-level patterns; a 2024 voxel-wise mega-analysis of 8,433 youths found stronger striatum-cortex connectivity in ADHD (largest d 0.15).
  - Sutcubasi B, et al. Resting-state network dysconnectivity in ADHD: a system-neuroscience-based meta-analysis. World J Biol Psychiatry. 2020. — [DOI 10.1080/15622975.2020.1775889](https://doi.org/10.1080/15622975.2020.1775889) · [PMID 32468880](https://pubmed.ncbi.nlm.nih.gov/32468880/); meta-analysis, n = 20 studies; cited on page; checked: PubMed record + abstract
  - Gao Y, et al. Impairments of large-scale functional networks in attention-deficit/hyperactivity disorder: a meta-analysis of resting-state functional connectivity. Psychol Med. 2019. — [DOI 10.1017/S003329171900237X](https://doi.org/10.1017/S003329171900237X) · [PMID 31500674](https://pubmed.ncbi.nlm.nih.gov/31500674/); meta-analysis, n = 21 studies; cited on page; checked: PubMed record + abstract
  - Norman LJ, et al. Subcortico-cortical dysconnectivity in ADHD: a voxel-wise mega-analysis across multiple cohorts. Am J Psychiatry. 2024. — [DOI 10.1176/appi.ajp.20230026](https://doi.org/10.1176/appi.ajp.20230026) · [PMID 38476041](https://pubmed.ncbi.nlm.nih.gov/38476041/); mega-analysis, n = 1,696 + 6,737; cited on page; checked: PubMed record + abstract

**Why they may differ:** Coordinate-based meta-analysis of seed-based studies depends on which seeds authors chose and on reporting; network-level meta-analyses aggregate differently; mega-analysis of raw data can detect tiny but consistent effects. Motion and global-signal handling differ across studies.

**Next step:** No action beyond keeping both; a later analysis could check whether any resting-state mega-analysis has replicated the striatal finding in an independent cohort.

#### C02-008

**EEG theta/beta ratio as an ADHD marker** · minor · guideline disagreement · Page reports both sides

**In dispute:** The theta/beta ratio difference has shrunk and is not a reliable diagnostic measure, though the FDA cleared one device (NEBA) as an aid.

- **Position A:** Regulator: the FDA cleared the NEBA theta/beta-based system in 2013 as an aid to clinical evaluation in 6-17-year-olds.
  - US Food and Drug Administration. De novo classification of the Neuropsychiatric EEG-Based ADHD Assessment Aid (NEBA) System, DEN110019. 2013. — regulatory decision; cited on page; checked: search result only
- **Position B:** Meta-analysis found the pooled effect an overestimate that shrank over time and judged the ratio not a reliable diagnostic measure; a large sample found no difference in youth and a lower ratio in adults with ADHD.
  - Arns M, et al. A decade of EEG theta/beta ratio research in ADHD: a meta-analysis. J Atten Disord. 2013. — [DOI 10.1177/1087054712460087](https://doi.org/10.1177/1087054712460087) · [PMID 23086616](https://pubmed.ncbi.nlm.nih.gov/23086616/); meta-analysis, n = 9 studies; cited on page; checked: PubMed record + abstract
  - Loo SK, et al. Characterization of the theta to beta ratio in ADHD: identifying potential sources of heterogeneity. J Atten Disord. 2013. — [DOI 10.1177/1087054712468050](https://doi.org/10.1177/1087054712468050) · [PMID 23264365](https://pubmed.ncbi.nlm.nih.gov/23264365/); case-control, n = 871; cited on page; checked: PubMed record + abstract

**Why they may differ:** Regulatory clearance under the de novo pathway assesses safety and a narrow intended use (adjunct), not diagnostic validity in general; later research found the effect declining, possibly due to changes in control-group sleep/age and publication bias in early studies.

**Next step:** None needed beyond confirming the FDA record directly (only search summaries were seen).

### [Is ADHD genetic, and will my children have it?](../02-whats-happening-in-my-brain/genes-and-inheritance.md)

#### C02-001

**Twin heritability versus measured DNA and indirect genetic effects** · major · size of effect · Page reports one side only

**In dispute:** About 74% of variation in ADHD is genetic (twin studies); 'about a third' of heritability comes from common variants; ADHD runs in families 'mostly through genes'.

- **Position A:** Pooled twin studies give heritability of about 74%; a Swedish clinical-diagnosis twin register gives 0.88 overall and 0.72 in adults; family clustering tracks genetic relatedness.
  - Faraone SV, et al. Genetics of attention deficit hyperactivity disorder. Mol Psychiatry. 2019. — [DOI 10.1038/s41380-018-0070-0](https://doi.org/10.1038/s41380-018-0070-0) · [PMID 29892054](https://pubmed.ncbi.nlm.nih.gov/29892054/); review of 37 twin studies; cited on page; checked: PubMed record + abstract
  - Larsson H, et al. The heritability of clinically diagnosed attention deficit hyperactivity disorder across the lifespan. Psychol Med. 2014. — [DOI 10.1017/S0033291713002493](https://doi.org/10.1017/S0033291713002493) · [PMID 24107258](https://pubmed.ncbi.nlm.nih.gov/24107258/); twin register, n = 59,514 twins; cited on page; checked: PubMed record + abstract
  - Chen Q, et al. Familial aggregation of attention-deficit/hyperactivity disorder. J Child Psychol Psychiatry. 2017. — [DOI 10.1111/jcpp.12616](https://doi.org/10.1111/jcpp.12616) · [PMID 27545745](https://pubmed.ncbi.nlm.nih.gov/27545745/); national register, n = 1,656,943; cited on page; checked: PubMed record + abstract
- **Position B:** Measured common DNA explains much less; in Norwegian parent-offspring trios, genetic effects acting through parents (indirect genetic effects, i.e. the family environment parents' genes create) explained more variance than the child's own (direct) genes for hyperactivity at age 3 (9.6% versus 1.3%) and inattention (6.7% versus 4.8%).
  - Hegemann L, et al. Direct and indirect genetic effects on early neurodevelopmental traits. J Child Psychol Psychiatry. 2025. — [DOI 10.1111/jcpp.14122](https://doi.org/10.1111/jcpp.14122) · [PMID 39887701](https://pubmed.ncbi.nlm.nih.gov/39887701/); trio genomic (Trio-GCTA) cohort, n = up to 24,692 trios; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Twin designs assume equal environments for identical and non-identical twins and can be inflated by rater contrast effects in parent ratings; SNP-based methods capture only common variants and are confounded by indirect effects and population structure, which within-family designs remove. The 'about a third' figure is from a 2019 review summarising earlier GWAS; the 2023 GWAS's own SNP-heritability figure was not confirmed from its abstract for this register. Hegemann measured mother-rated traits at age 3, not diagnosed ADHD.

**Next step:** Confirm the SNP heritability reported in the full text of Demontis 2023 (DOI 10.1038/s41588-022-01285-8) and update 'about a third' if it is lower; add within-family/trio evidence on indirect genetic effects to the 'missing heritability' bullet; soften 'mostly through genes' on what-adhd-is.md to make clear heritability includes gene-environment interplay.

### [ADHD and hyperfocus: why can I focus for hours on some things?](../03-why-i-think-and-feel-this-way/attention-regulation-and-hyperfocus.md)

#### C03-004

**Is hyperfocus more common in diagnosed ADHD?** · moderate · population/age · Page reports one side only

**In dispute:** People with more ADHD symptoms report hyperfocus more often; there are 'no studies of how common it is in diagnosed adults'.

- **Position A:** In online adult samples (pilot n = 251, replication n = 372), higher ADHD symptoms went with more frequent hyperfocus in school, hobbies and screen time; a 12-item dispositional scale correlated r = 0.53 with an ADHD rating scale.
  - Hupfeld KE, et al. Living "in the zone": hyperfocus in adult ADHD. Atten Defic Hyperact Disord. 2019. — [DOI 10.1007/s12402-018-0272-y](https://doi.org/10.1007/s12402-018-0272-y) · [PMID 30267329](https://pubmed.ncbi.nlm.nih.gov/30267329/); cross-sectional survey, n = 251 + 372; cited on page; checked: PubMed record + abstract
  - Hupfeld KE, et al. Validation of the dispositional adult hyperfocus questionnaire (AHQ-D). Sci Rep. 2024. — [DOI 10.1038/s41598-024-70028-y](https://doi.org/10.1038/s41598-024-70028-y) · [PMID 39169147](https://pubmed.ncbi.nlm.nih.gov/39169147/); psychometric validation, n = 347; cited on page; checked: PubMed record + abstract
- **Position B:** In a study that included 78 diagnosed adults compared with matched controls, patients and controls did not differ in occurrence, frequency, duration or pervasiveness of hyperfocus (hyperfocus was less likely in educational and social settings in ADHD), although ADHD traits correlated with hyperfocus frequency in 1,124 healthy adults. The authors concluded hyperfocus is not specific to ADHD patients.
  - Groen Y, et al. Testing the relation between ADHD and hyperfocus experiences. Res Dev Disabil. 2020. — [DOI 10.1016/j.ridd.2020.103789](https://doi.org/10.1016/j.ridd.2020.103789) · [PMID 33126147](https://pubmed.ncbi.nlm.nih.gov/33126147/); case-control + population survey, n = 78 patients; 1,124 healthy adults; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Trait correlations in online community samples can arise from shared self-report style (people endorsing many experiences), while a diagnosed clinical group compared with matched controls tests the clinical claim directly. Questionnaires differ, and 'hyperfocus' has no agreed definition.

**Next step:** Add Groen 2020 to the page and remove or revise 'no studies of how common it is in diagnosed adults'; the page already says hyperfocus is not unique to ADHD, which Groen supports more strongly than the current sources.

### [Emotions and rejection in ADHD: why do they hit so hard?](../03-why-i-think-and-feel-this-way/emotions-and-rejection.md)

#### C03-002

**Is emotion dysregulation a core part of ADHD?** · moderate · causal interpretation · Page reports both sides

**In dispute:** Emotion dysregulation is common but not a listed symptom; experts disagree whether it should be (core, separate-but-related, or a subgroup).

- **Position A:** Emotional impulsivity and deficient emotional self-regulation may be specific enough to ADHD to serve as diagnostic criteria; a 2026 meta-analysis of 75 studies (63 on ADHD) found emotion dysregulation correlated with externalising symptoms (r = 0.35; lability r = 0.47) regardless of age, sex, informant, subtype, comorbidity or medication.
  - Faraone SV, et al. Practitioner Review: Emotional dysregulation in attention-deficit/hyperactivity disorder - implications for clinical recognition and intervention. J Child Psychol Psychiatry. 2019. — [DOI 10.1111/jcpp.12899](https://doi.org/10.1111/jcpp.12899) · [PMID 29624671](https://pubmed.ncbi.nlm.nih.gov/29624671/); practitioner review; **not yet cited on page**; checked: PubMed record + abstract
  - Njardvik U, et al. Emotion dysregulation in children and adolescents with externalizing disorders: a systematic review and meta-analysis. Eur Child Adolesc Psychiatry. 2026. — [DOI 10.1007/s00787-026-03090-8](https://doi.org/10.1007/s00787-026-03090-8) · [PMID 42301280](https://pubmed.ncbi.nlm.nih.gov/42301280/); meta-analysis, n = 75 studies; 11,913; **not yet cited on page**; checked: PubMed record + abstract
  - Soler-Gutiérrez AM, et al. Evidence of emotion dysregulation as a core symptom of adult ADHD: a systematic review. PLoS One. 2023. — [DOI 10.1371/journal.pone.0280131](https://doi.org/10.1371/journal.pone.0280131) · [PMID 36608036](https://pubmed.ncbi.nlm.nih.gov/36608036/); systematic review, n = 22 studies; cited on page; checked: PubMed record + abstract
- **Position B:** Emotion dysregulation affects only a portion of children with ADHD in clinic studies and is best seen as a dimension; competing models treat it as a separate correlated problem or the mark of a subgroup; emotional symptoms are non-specific across disorders and there is no agreed definition.
  - Shaw P, et al. Emotion dysregulation in attention deficit hyperactivity disorder. Am J Psychiatry. 2014. — [DOI 10.1176/appi.ajp.2013.13070966](https://doi.org/10.1176/appi.ajp.2013.13070966) · [PMID 24480998](https://pubmed.ncbi.nlm.nih.gov/24480998/); review; cited on page; checked: PubMed record + abstract

**Why they may differ:** A moderate correlation (r about 0.35) means emotion dysregulation travels with ADHD symptoms but is far from identical to them, which each camp reads differently. Much of the adult evidence is self-report, and overlap with mood, anxiety and trauma conditions makes specificity hard to test. The definitional problem (lability, irritability, emotional impulsivity) is acknowledged by both sides.

**Next step:** Add the 2026 meta-analysis (r = 0.35, lability 0.47) as the best current estimate of strength of association in young people; note Faraone 2019 as the 'core symptom' side so the debate has a named source on each side.

#### C03-003

**Rejection sensitive dysphoria (RSD) as a concept** · minor · causal interpretation · Page reports both sides

**In dispute:** RSD is not established as a condition; where the term came from was not checked for this page.

- **Position A:** Lived-experience research describes intense, embodied responses to rejection that people with ADHD name as RSD; rejection sensitivity is associated with ADHD symptoms in adolescents.
  - Rowney-Smith A, et al. The lived experience of rejection sensitivity in ADHD - a qualitative exploration. PLoS One. 2026. — [DOI 10.1371/journal.pone.0314669](https://doi.org/10.1371/journal.pone.0314669) · [PMID 41564005](https://pubmed.ncbi.nlm.nih.gov/41564005/); qualitative, n = 5; cited on page; checked: PubMed record + abstract
  - Babinski DE, et al. Sensitivity to peer feedback in young adolescents with symptoms of ADHD: examination of neurophysiological and self-report measures. J Abnorm Child Psychol. 2019. — [DOI 10.1007/s10802-018-0470-2](https://doi.org/10.1007/s10802-018-0470-2) · [PMID 30155685](https://pubmed.ncbi.nlm.nih.gov/30155685/); correlational; cited on page; checked: PubMed record + abstract
- **Position B:** A 2026 critical reflection traces RSD to the US psychiatrist William Dodson's clinical experience and spread via social media, and argues its use in professional communication is problematic (terminological fragmentation, environmental factors under-emphasised, limited evidence), recommending the established rejection-sensitivity construct instead.
  - van Asselt A. [Rejection sensitivity dysphoria: a critical reflection]. Tijdschr Psychiatr. 2026. — [PMID 41944472](https://pubmed.ncbi.nlm.nih.gov/41944472/); expert commentary (Dutch); **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The sides largely agree on the experience but differ on whether a new label adds anything beyond rejection sensitivity and emotion dysregulation. Neither side has a validated RSD measure, so the dispute is conceptual rather than empirical.

**Next step:** Fill the page's 'where the term first came from was not checked' using van Asselt 2026 (confirm in the full text that Dodson is named as originator); recheck for any RSD questionnaire validation in 2026.

### [Executive function and ADHD: why can't I plan or get started?](../03-why-i-think-and-feel-this-way/executive-function-and-working-memory.md)

#### C03-001

**Executive deficits: a subgroup or nearly everyone?** · moderate · method/measurement · Page reports both sides

**In dispute:** Executive weaknesses are 'neither necessary nor sufficient'; older estimates put executive impairment at a third to a half of children with ADHD, while one study found 89%.

- **Position A:** Medium average effects with heavy overlap mean many people with ADHD test in the normal range; executive deficit may mark only a subgroup (roughly a third to a half).
  - Willcutt EG, et al. Validity of the executive function theory of attention-deficit/hyperactivity disorder: a meta-analytic review. Biol Psychiatry. 2005. — [DOI 10.1016/j.biopsych.2005.02.006](https://doi.org/10.1016/j.biopsych.2005.02.006) · [PMID 15950006](https://pubmed.ncbi.nlm.nih.gov/15950006/); meta-analysis, n = 83 studies; 3,734 + 2,969; cited on page; checked: PubMed record + abstract
  - Nigg JT, et al. Causal heterogeneity in attention-deficit/hyperactivity disorder: do we need neuropsychologically impaired subtypes? Biol Psychiatry. 2005. — [DOI 10.1016/j.biopsych.2004.08.025](https://doi.org/10.1016/j.biopsych.2004.08.025) · [PMID 15949992](https://pubmed.ncbi.nlm.nih.gov/15949992/); review; cited on page; checked: PubMed record + abstract
- **Position B:** Using several tests per skill and latent modelling to remove test unreliability, 89% of children with ADHD were impaired on at least one executive domain (working memory 62%).
  - Kofler MJ, et al. Executive functioning heterogeneity in pediatric ADHD. J Abnorm Child Psychol. 2019. — [DOI 10.1007/s10802-018-0438-2](https://doi.org/10.1007/s10802-018-0438-2) · [PMID 29705926](https://pubmed.ncbi.nlm.nih.gov/29705926/); case-control, n = 136; cited on page; checked: PubMed record + abstract

**Why they may differ:** Single tests are unreliable and capture one skill, so they under-detect impairment; aggregating multiple tests raises detection but also the chance of finding 'impairment' in one of several domains (the 89% is 'any of three'), and the comparison-group impairment rate matters. The cut-off for 'impaired' varies.

**Next step:** Find the comparison-group rate of 'impaired on at least one domain' in Kofler 2019 so the 89% can be read against a baseline; look for a replication of multi-indicator estimates in a larger or adult sample.

### [Sleep and ADHD: why can't I fall asleep, and is sleep the cause?](../03-why-i-think-and-feel-this-way/sleep-and-the-body-clock.md)

#### C03-005

**Does poor sleep cause ADHD, or the reverse?** · moderate · direct contradiction · Page does not mention it

**In dispute:** Which causes which is not settled; research is mostly cross-sectional and cannot tell the directions apart.

- **Position A:** A bidirectional Mendelian randomisation study (genetic variants as natural experiments) estimated that genetically predicted insomnia raised ADHD risk (OR 1.33, 95% CI 1.22-1.45), with a suggestive link from ADHD to shorter sleep.
  - Sun X, et al. Sleep disturbance and psychiatric disorders: a bidirectional Mendelian randomisation study. Epidemiol Psychiatr Sci. 2022. — [DOI 10.1017/S2045796021000810](https://doi.org/10.1017/S2045796021000810) · [PMID 35465862](https://pubmed.ncbi.nlm.nih.gov/35465862/); Mendelian randomisation, n = GWAS summary data; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** An earlier Mendelian randomisation study found insomnia causally linked to autism and bipolar disorder, but no significant causal estimate in either direction for ADHD.
  - Gao X, et al. The bidirectional causal relationships of insomnia with five major psychiatric disorders: a Mendelian randomization study. Eur Psychiatry. 2019. — [DOI 10.1016/j.eurpsy.2019.05.004](https://doi.org/10.1016/j.eurpsy.2019.05.004) · [PMID 31234011](https://pubmed.ncbi.nlm.nih.gov/31234011/); Mendelian randomisation, n = GWAS summary data; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Different insomnia GWAS instruments, different (older versus newer) ADHD GWAS, and different pleiotropy filters (HEIDI versus multiple robust estimators). Insomnia variants overlap with general psychiatric liability, which can mimic causation. MR estimates lifelong genetic tendency, not the effect of a bad night or of treating sleep.

**Next step:** Add a sentence that genetic (Mendelian randomisation) studies exist and disagree; check for newer MR using the 2023 ADHD GWAS and for prospective cohort studies testing whether early sleep problems predict later ADHD symptoms.

#### C03-006

**Does shifting the body clock improve ADHD symptoms?** · minor · size of effect · Page does not mention it

**In dispute:** Whether shifting the body clock also improves daytime ADHD symptoms 'has hardly been tested'.

- **Position A:** A three-arm RCT in 51 adults with ADHD and delayed sleep phase found low-dose melatonin advanced melatonin onset by about 1.5 hours and reduced self-rated ADHD symptoms by 14%; a pilot found that correcting delayed phase with bright light predicted ADHD symptom improvement.
  - van Andel E, et al. Effects of chronotherapy on circadian rhythm and ADHD symptoms in adults with attention-deficit/hyperactivity disorder and delayed sleep phase syndrome: a randomized clinical trial. Chronobiol Int. 2021. — [DOI 10.1080/07420528.2020.1835943](https://doi.org/10.1080/07420528.2020.1835943) · [PMID 33121289](https://pubmed.ncbi.nlm.nih.gov/33121289/); RCT, n = 51; **not yet cited on page**; checked: PubMed record + abstract
  - Fargason RE, et al. Correcting delayed circadian phase with bright light therapy predicts improvement in ADHD symptoms: a pilot study. J Psychiatr Res. 2017. — [DOI 10.1016/j.jpsychires.2017.03.004](https://doi.org/10.1016/j.jpsychires.2017.03.004) · [PMID 28327443](https://pubmed.ncbi.nlm.nih.gov/28327443/); pilot study; **not yet cited on page**; checked: PubMed record only
- **Position B:** In the same RCT, melatonin plus bright light advanced the clock more but did not change ADHD symptoms, and both clock and symptom changes were gone two weeks after treatment; the earlier systematic review found few treatment trials.
  - van Andel E, et al. Effects of chronotherapy on circadian rhythm and ADHD symptoms in adults with attention-deficit/hyperactivity disorder and delayed sleep phase syndrome: a randomized clinical trial. Chronobiol Int. 2021. — [DOI 10.1080/07420528.2020.1835943](https://doi.org/10.1080/07420528.2020.1835943) · [PMID 33121289](https://pubmed.ncbi.nlm.nih.gov/33121289/); RCT, n = 51; **not yet cited on page**; checked: PubMed record + abstract
  - Coogan AN, et al. A systematic review of circadian function, chronotype and chronotherapy in attention deficit hyperactivity disorder. Atten Defic Hyperact Disord. 2017. — [DOI 10.1007/s12402-016-0214-5](https://doi.org/10.1007/s12402-016-0214-5) · [PMID 28064405](https://pubmed.ncbi.nlm.nih.gov/28064405/); systematic review, n = 62 studies; cited on page; checked: PubMed record + abstract

**Why they may differ:** Small, short trials with self-rated outcomes; the arm that shifted the clock most did not improve symptoms, so the link between phase shift and symptom change is unclear. The reviews that say 'hardly tested' predate the RCT.

**Next step:** Revise 'has hardly been tested' to describe the one small RCT and its mixed result; report findings only, consistent with the no-advice rule.

### [Time and waiting in ADHD: why do I lose track and hate waiting?](../03-why-i-think-and-feel-this-way/time-waiting-and-rewards.md)

#### C03-007

**Why people with ADHD choose 'now' over 'later'** · minor · causal interpretation · Page reports one side only

**In dispute:** Steeper delay discounting is robust (d = 0.43) and the same in young people and adults; delay aversion is one route in the dual pathway model.

- **Position A:** Meta-analyses find medium effects for monetary delay discounting with minimal heterogeneity and no age moderation; in children, choice impulsivity g = 0.47.
  - Jackson JN, MacKillop J. Attention-deficit/hyperactivity disorder and monetary delay discounting: a meta-analysis of case-control studies. Biol Psychiatry Cogn Neurosci Neuroimaging. 2016. — [DOI 10.1016/j.bpsc.2016.01.007](https://doi.org/10.1016/j.bpsc.2016.01.007) · [PMID 27722208](https://pubmed.ncbi.nlm.nih.gov/27722208/); meta-analysis, n = 21 studies; 3,913; cited on page; checked: PubMed record + abstract
  - Patros CH, et al. Choice-impulsivity in children and adolescents with attention-deficit/hyperactivity disorder (ADHD): a meta-analytic review. Clin Psychol Rev. 2016. — [DOI 10.1016/j.cpr.2015.11.001](https://doi.org/10.1016/j.cpr.2015.11.001) · [PMID 26602954](https://pubmed.ncbi.nlm.nih.gov/26602954/); meta-analysis, n = 26 studies; 4,320; cited on page; checked: PubMed record + abstract
- **Position B:** Effects are only small-to-medium, inflated in single-informant studies and those excluding girls; in a comparative meta-analysis, offering real rather than hypothetical rewards almost doubled the odds of impulsive choice in ADHD, which the authors read as delay aversion interacting with demotivation by hypothetical rewards rather than a pure discounting trait.
  - Marx I, et al. ADHD and the choice of small immediate over larger delayed rewards: a comparative meta-analysis of performance on simple choice-delay and temporal discounting paradigms. J Atten Disord. 2021. — [DOI 10.1177/1087054718772138](https://doi.org/10.1177/1087054718772138) · [PMID 29806533](https://pubmed.ncbi.nlm.nih.gov/29806533/); meta-analysis, n = 37 comparisons; 3,763; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Temporal-discounting questionnaires with hypothetical money and choice-delay tasks with real waits measure different things; real waits engage delay aversion, hypothetical tasks engage valuation and motivation. Diagnostic rigour and sex composition shift effect sizes.

**Next step:** Add Marx 2021 to show that task type (real waits versus hypothetical money) changes the effect, which bears on the page's interpretation of deadlines; align the evidence grade for Sonuga-Barke 2003 across pages ('Expert review' here, 'Moderate' on why-no-two-adhd-brains-are-alike.md).

### [Do periods, pregnancy and menopause make ADHD worse?](../04-did-i-cause-this-and-where-is-it-going/hormones-cycles-and-menopause.md)

#### C04-013

**After giving birth: is the evidence only two uncontrolled surveys?** · major · method/measurement · Page does not mention it

**In dispute:** After giving birth the evidence is two surveys of women with ADHD, neither with a comparison group.

- **Position A:** The page's sources: a Dutch clinic survey (57.6% above a postnatal depression cut-off) and a 2026 online survey (70% reported worsening), both without comparison groups and both relying on recall.
  - Dorani F, et al. Prevalence of hormone-related mood disorder symptoms in women with ADHD. J Psychiatr Res. 2021. — [DOI 10.1016/j.jpsychires.2020.12.005](https://doi.org/10.1016/j.jpsychires.2020.12.005) · [PMID 33302160](https://pubmed.ncbi.nlm.nih.gov/33302160/); clinic survey, no control, n = 209; cited on page; checked: PubMed record
  - Osianlis E, et al. ADHD in females: survey findings on symptoms across hormonal life stages. J Psychiatr Res. 2026. — [DOI 10.1016/j.jpsychires.2025.11.035](https://doi.org/10.1016/j.jpsychires.2025.11.035) · [PMID 41330200](https://pubmed.ncbi.nlm.nih.gov/41330200/); online survey, no control, n = 600; cited on page; checked: PubMed record
- **Position B:** Controlled studies now exist. In Ontario health records (about 1.05 million pregnancies), perinatal mental illness was diagnosed in 50.2% of those with ADHD against 24.0% without (adjusted relative risk 1.35; perinatal depression 14.4% against 5.0%). A Canadian national survey found mothers with possible ADHD had about 1.7 times the odds of postpartum depression and anxiety.
  - Vigod SN, et al. Attention-deficit hyperactivity disorder and perinatal mental illness: a population-based study. Soc Psychiatry Psychiatr Epidemiol. 2026. — [DOI 10.1007/s00127-026-03206-0](https://doi.org/10.1007/s00127-026-03206-0) · [PMID 42663665](https://pubmed.ncbi.nlm.nih.gov/42663665/); population health-records cohort, n = 22,995 with ADHD; 1,028,038 without; **not yet cited on page**; checked: PubMed record + abstract
  - Johnson D, et al. Associations between self-reported ADHD symptoms and depression and anxiety in mothers and fathers during the postpartum period: A Canadian nationwide longitudinal study. J Affect Disord. 2025. — [DOI 10.1016/j.jad.2025.02.113](https://doi.org/10.1016/j.jad.2025.02.113) · [PMID 40044079](https://pubmed.ncbi.nlm.nih.gov/40044079/); national longitudinal survey; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The page's statement reflects its own source set, not the field. The newer studies measure perinatal mental illness (largely depression and anxiety) rather than whether ADHD symptoms themselves worsen, so they answer a related but different question. Health-record diagnoses miss untreated cases but avoid recall bias; women with ADHD may also be more often in contact with services and so more often diagnosed.

**Next step:** Update the 'After giving birth' bullet and short answer: large controlled data (Vigod 2026, with absolute figures) show raised perinatal depression and anxiety in women with ADHD, while whether ADHD symptoms themselves worsen still rests on uncontrolled surveys. Keep the help-now link next to the perinatal depression figures. Cross-check with 06-treatment-what-works/pregnancy-and-breastfeeding.md.

#### C04-012

**Do menopausal symptoms differ in women with ADHD?** · moderate · direct contradiction · Page reports both sides

**In dispute:** Two 2025 menopause studies comparing women with and without ADHD disagreed: Iceland found more perimenopausal symptoms, a UK survey found no difference by diagnosis.

- **Position A:** Women with ADHD report more menopausal symptoms: in Iceland, severe perimenopausal symptoms in 54% with ADHD against 30% without; an Irish 2026 survey of 602 women (377 with self-reported ADHD) also found greater menopausal symptom severity.
  - Jakobsdóttir Smári U, et al. Perimenopausal symptoms in women with and without ADHD: a population-based cohort study. Eur Psychiatry. 2025. — [DOI 10.1192/j.eurpsy.2025.10101](https://doi.org/10.1192/j.eurpsy.2025.10101) · [PMID 40903825](https://pubmed.ncbi.nlm.nih.gov/40903825/); population cohort, cross-sectional self-report (SAGA), n = 5,392 women (535 with ADHD); cited on page; checked: PubMed record
  - Boyd C, et al. ADHD and the female reproductive stages: menstruation, perinatal and menopause. Arch Womens Ment Health. 2026. — [DOI 10.1007/s00737-026-01718-x](https://doi.org/10.1007/s00737-026-01718-x) · [PMID 42207323](https://pubmed.ncbi.nlm.nih.gov/42207323/); cross-sectional online survey with comparison group, n = 602 (377 with self-reported ADHD, 225 without); **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** In 656 UK women aged 45-60, a diagnosis of ADHD was not linked to worse menopausal symptoms at any stage, although more ADHD traits were linked to more complaints.
  - Chapman L, et al. Examining the link between ADHD symptoms and menopausal experiences. J Atten Disord. 2025. — [DOI 10.1177/10870547251355006](https://doi.org/10.1177/10870547251355006) · [PMID 40738484](https://pubmed.ncbi.nlm.nih.gov/40738484/); cross-sectional survey, n = 656 (245 with ADHD); cited on page; checked: PubMed record

**Why they may differ:** All are cross-sectional self-report studies with self-reported diagnosis. The UK study excluded hormone-therapy and pill users (who may be the most symptomatic) and recruited women 45-60; Iceland's sample was younger (35-55) and found the largest gap at 35-39, before most women's transition; the Irish survey recruited partly via ADHD support groups, which may select more symptomatic women. Trait-based analyses in the UK study point the same direction as the other two, so the disagreement may be about diagnosis versus traits more than about whether a link exists.

**Next step:** Add Boyd 2026 as a third comparison study (noting its support-group recruitment), so the balance is visible as two-to-one on diagnosis with all three agreeing on traits. Watch for any longitudinal study through the menopause transition, which would settle whether symptoms change rather than differ.

#### C04-014

**Hormonal contraception and mood in ADHD** · moderate · method/measurement · Page does not mention it

**In dispute:** The effects of hormonal contraception and hormone therapy on ADHD have not been studied well enough to summarise.

- **Position A:** The page treats hormonal contraception as unstudied in ADHD.
- **Position B:** A Swedish register study of 29,767 young women with ADHD aged 15-24 and 763,146 without found women with ADHD had higher depression risk overall, and a larger excess when using oral hormonal contraception (combined pill hazard ratio 5.19 against non-users without ADHD).
  - Lundin C, et al. Hormonal Contraceptive Use and Risk of Depression Among Young Women With Attention-Deficit/Hyperactivity Disorder. J Am Acad Child Adolesc Psychiatry. 2023. — [DOI 10.1016/j.jaac.2022.07.847](https://doi.org/10.1016/j.jaac.2022.07.847) · [PMID 36332846](https://pubmed.ncbi.nlm.nih.gov/36332846/); national register cohort, n = 29,767 with ADHD; 763,146 without; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The page's statement is about effects on ADHD symptoms, which remain unstudied; the registry addresses depression during contraceptive use. It is observational, so women prescribed the pill may differ from non-users, and depression diagnoses in records may reflect contact with services. Relative figures need absolute rates added.

**Next step:** Revise the bullet to say that effects on ADHD symptoms are unstudied, but a large Swedish registry found higher depression risk in young women with ADHD using oral contraception; obtain absolute depression rates from the full text before quoting, and frame contraception choices as decisions with a clinician.

#### C04-015

**Recalled versus measured symptom change across hormonal stages; strength of expert claims** · moderate · method/measurement · Page reports both sides

**In dispute:** An expert review states hormonal transitions worsen ADHD symptoms and mood; the systematic review calls evidence 'largely suggestive'; a 2026 survey found large recalled worsening but similar measured severity across stages.

- **Position A:** Hormonal transitions worsen ADHD: the Eunethydis expert review states this, and most women in surveys recall worsening (98% around menopause, 89% across the cycle). A 2026 three-group study found women with ADHD more often screened positive for PMDD than women without ADHD.
  - Kooij JJS, et al. Research advances and future directions in female ADHD: the lifelong interplay of hormonal fluctuations with mood, cognition, and disease. Front Glob Womens Health. 2025. — [DOI 10.3389/fgwh.2025.1613628](https://doi.org/10.3389/fgwh.2025.1613628) · [PMID 40692967](https://pubmed.ncbi.nlm.nih.gov/40692967/); expert review; cited on page; checked: PubMed record
  - Groenman AP, et al. The monthly spectrum: Premenstrual symptoms across ADHD and autism. Womens Health (Lond). 2026. — [DOI 10.1177/17455057261476912](https://doi.org/10.1177/17455057261476912) · [PMID 42617113](https://pubmed.ncbi.nlm.nih.gov/42617113/); cross-sectional survey with comparison group, n = 199 (89 ADHD, 39 autism, 71 neither); **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** The best syntheses and measured data are weaker: the systematic review found 11 mostly small studies and 'largely suggestive' evidence, and when current symptoms were scored with a standard questionnaire, severity was similar across life stages despite recalled worsening.
  - Osianlis E, et al. ADHD and sex hormones in females: a systematic review. J Atten Disord. 2025. — [DOI 10.1177/10870547251332319](https://doi.org/10.1177/10870547251332319) · [PMID 40251875](https://pubmed.ncbi.nlm.nih.gov/40251875/); systematic review, n = 11 studies; cited on page; checked: PubMed record
  - Osianlis E, et al. ADHD in females: survey findings on symptoms across hormonal life stages. J Psychiatr Res. 2026. — [DOI 10.1016/j.jpsychires.2025.11.035](https://doi.org/10.1016/j.jpsychires.2025.11.035) · [PMID 41330200](https://pubmed.ncbi.nlm.nih.gov/41330200/); online survey, n = 600; cited on page; checked: PubMed record

**Why they may differ:** Recall of change is shaped by expectation and by the worst periods, while a single current-symptom score cannot capture within-person change across stages; neither design follows the same women through a transition. The expert review draws on clinical experience and women's accounts, which are valuable for generating hypotheses but go beyond the systematic evidence. The PMDD finding concerns premenstrual mood, not ADHD core symptoms.

**Next step:** Page handles this well. Optionally add Groenman 2026 as the first PMDD study with a non-ADHD comparison group (strengthening the cycle-mood point while noting small numbers). Prioritise any prospective daily-tracking study when it appears.

### [ADHD over a lifetime: will it get better or worse as I age?](../04-did-i-cause-this-and-where-is-it-going/how-adhd-changes-over-life.md)

#### C04-008

**How many children still have ADHD as adults** · moderate · method/measurement · Page reports both sides

**In dispute:** About 15% still meet full criteria at 25 and about 65% if partial remission is counted (Faraone 2006); about 90% of the MTA cohort still had some symptoms.

- **Position A:** Low persistence on strict criteria: 15% at full criteria in the 2006 meta-analysis; in population cohorts, 21.9% of children with ADHD in England (E-Risk) and 17.2% in Brazil (Pelotas) still met criteria at 18-19, and 3 of 61 in Dunedin at 38.
  - Faraone SV, et al. The age-dependent decline of attention deficit hyperactivity disorder: a meta-analysis of follow-up studies. Psychol Med. 2006. — [DOI 10.1017/S003329170500471X](https://doi.org/10.1017/S003329170500471X) · [PMID 16420712](https://pubmed.ncbi.nlm.nih.gov/16420712/); meta-analysis of follow-up studies; cited on page; checked: PubMed record
  - Agnew-Blais JC, et al. Evaluation of the Persistence, Remission, and Emergence of Attention-Deficit/Hyperactivity Disorder in Young Adulthood. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0465](https://doi.org/10.1001/jamapsychiatry.2016.0465) · [PMID 27192174](https://pubmed.ncbi.nlm.nih.gov/27192174/); population twin birth cohort (E-Risk), n = 2,040; **not yet cited on page**; checked: PubMed record + abstract
  - Caye A, et al. Attention-Deficit/Hyperactivity Disorder Trajectories From Childhood to Young Adulthood: Evidence From a Birth Cohort Supporting a Late-Onset Syndrome. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0383](https://doi.org/10.1001/jamapsychiatry.2016.0383) · [PMID 27192050](https://pubmed.ncbi.nlm.nih.gov/27192050/); population birth cohort (Pelotas 1993), n = about 4,000 (393 with childhood ADHD); **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** High persistence in clinical cohorts with repeated, multi-informant assessment: in the MTA, combining parent and self-reports, 60% showed symptom persistence and 41% met symptom and impairment criteria in young adulthood, and about 90% had residual symptoms over the whole follow-up.
  - Sibley MH, et al. Defining ADHD symptom persistence in adulthood: optimizing sensitivity and specificity. J Child Psychol Psychiatry. 2017. — [DOI 10.1111/jcpp.12620](https://doi.org/10.1111/jcpp.12620) · [PMID 27642116](https://pubmed.ncbi.nlm.nih.gov/27642116/); clinical cohort (MTA), comparison of persistence definitions; **not yet cited on page**; checked: PubMed record + abstract
  - Sibley MH, et al. Variable patterns of remission from ADHD in the Multimodal Treatment Study of ADHD. Am J Psychiatry. 2022. — [DOI 10.1176/appi.ajp.2021.21010032](https://doi.org/10.1176/appi.ajp.2021.21010032) · [PMID 34384227](https://pubmed.ncbi.nlm.nih.gov/34384227/); clinical cohort, 8 assessments over 16 years, n = 558; cited on page; checked: PubMed record

**Why they may differ:** Persistence depends on who reports (self-reports by young adults give much lower rates than parent reports), the threshold (DSM's six symptoms, which were written for children, versus age-adjusted norms), whether impairment is required, and the sample (clinic-referred, more severe children in MTA versus community cases, some milder, in birth cohorts). Single snapshots also miss people who are between episodes.

**Next step:** The page handles the definitional point well. Add the informant effect (Sibley 2017: parent versus self-report) to the existing 'self-report versus others' report' bullet with a citation, and cite at least one population cohort (E-Risk or Pelotas) so the low-persistence end does not rest on a 2006 meta-analysis and Dunedin alone. Mirror any change on 01-is-this-real/diagnosed-as-an-adult.md, which repeats the 15%/65% figures.

#### C04-010

**Adult-onset ADHD** · moderate · direct contradiction · Page reports both sides

**In dispute:** Adult onset is contested; the usual view now is that most 'late' ADHD began in adolescence or was missed, with true adult onset unresolved.

- **Position A:** Three population birth cohorts found most young-adult or adult ADHD had no childhood diagnosis: 90% in Dunedin (age 38), 67.5% in E-Risk (age 18) and 87.4% in Pelotas (age 18-19), and the Pelotas authors proposed two distinct syndromes.
  - Moffitt TE, et al. Is adult ADHD a childhood-onset neurodevelopmental disorder? Evidence from a four-decade longitudinal cohort study. Am J Psychiatry. 2015. — [DOI 10.1176/appi.ajp.2015.14101266](https://doi.org/10.1176/appi.ajp.2015.14101266) · [PMID 25998281](https://pubmed.ncbi.nlm.nih.gov/25998281/); birth cohort (Dunedin), n = 1,037; cited on page; checked: PubMed record
  - Agnew-Blais JC, et al. Evaluation of the Persistence, Remission, and Emergence of Attention-Deficit/Hyperactivity Disorder in Young Adulthood. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0465](https://doi.org/10.1001/jamapsychiatry.2016.0465) · [PMID 27192174](https://pubmed.ncbi.nlm.nih.gov/27192174/); population twin birth cohort (E-Risk), n = 2,040; **not yet cited on page**; checked: PubMed record + abstract
  - Caye A, et al. Attention-Deficit/Hyperactivity Disorder Trajectories From Childhood to Young Adulthood: Evidence From a Birth Cohort Supporting a Late-Onset Syndrome. JAMA Psychiatry. 2016. — [DOI 10.1001/jamapsychiatry.2016.0383](https://doi.org/10.1001/jamapsychiatry.2016.0383) · [PMID 27192050](https://pubmed.ncbi.nlm.nih.gov/27192050/); population birth cohort (Pelotas), n = about 4,000; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Careful, repeated assessment shrinks late onset: in the MTA about 95% of apparent late-onset cases were excluded; in a later Pelotas follow-up at 22, latent-trajectory analysis found 78% of adults with ADHD had persistent symptoms from childhood and 67% a neurodevelopmental course, with the remainder rising after puberty.
  - Sibley MH, et al. Late-onset ADHD reconsidered with comprehensive repeated assessments between ages 10 and 25. Am J Psychiatry. 2018. — [DOI 10.1176/appi.ajp.2017.17030298](https://doi.org/10.1176/appi.ajp.2017.17030298) · [PMID 29050505](https://pubmed.ncbi.nlm.nih.gov/29050505/); clinical cohort (MTA local normative comparison group); cited on page; checked: PubMed record
  - Breda V, et al. The neurodevelopmental nature of attention-deficit hyperactivity disorder in adults. Br J Psychiatry. 2021. — [DOI 10.1192/bjp.2020.200](https://doi.org/10.1192/bjp.2020.200) · [PMID 33263274](https://pubmed.ncbi.nlm.nih.gov/33263274/); population birth cohort (Pelotas), trajectory analysis; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Birth cohorts used brief childhood assessments (and in some cases few informants), so subthreshold or missed childhood ADHD looks like 'new' adult ADHD; adult diagnoses were often made without excluding substance use, depression or anxiety. The MTA reassessment used full clinical evaluation and multiple informants but studied a smaller comparison group. Breda's reanalysis of the same Pelotas cohort reached a more continuous picture using symptom trajectories rather than diagnostic cut-offs, showing the definition largely drives the answer.

**Next step:** Cite E-Risk and Pelotas alongside Dunedin, since three independent cohorts carry more weight than one, and add Breda 2021 to show the Pelotas team's own later, more continuous finding. Check that 01-is-this-real/diagnosed-as-an-adult.md frames the debate the same way.

#### C04-009

**How common is a fluctuating course** · minor · method/measurement · Page reports both sides

**In dispute:** In the MTA most people's course fluctuated (63.8%); three other cohorts found fluctuation in 17-29%.

- **Position A:** MTA: 63.8% moved between remission and recurrence across eight assessments from about age 10 to 25.
  - Sibley MH, et al. Variable patterns of remission from ADHD in the Multimodal Treatment Study of ADHD. Am J Psychiatry. 2022. — [DOI 10.1176/appi.ajp.2021.21010032](https://doi.org/10.1176/appi.ajp.2021.21010032) · [PMID 34384227](https://pubmed.ncbi.nlm.nih.gov/34384227/); clinical cohort, n = 558; cited on page; checked: PubMed record
- **Position B:** Three US cohorts with more than 10,000 young people found a fluctuating course (two or more switches) in 17-29%, never the largest group.
  - Norman LJ, et al. Longitudinal trajectories of childhood and adolescent attention deficit hyperactivity disorder diagnoses in three cohorts. EClinicalMedicine. 2023. — [DOI 10.1016/j.eclinm.2023.102021](https://doi.org/10.1016/j.eclinm.2023.102021) · [PMID 37333663](https://pubmed.ncbi.nlm.nih.gov/37333663/); three cohorts (ABCD, NCR, NKI-Rockland), n = >10,000; cited on page; checked: PubMed record

**Why they may differ:** The MTA followed clinic-referred children into adulthood with eight assessments and counted any remission-recurrence as fluctuation; Norman's cohorts were mostly community samples followed over shorter, mainly childhood and adolescent windows, with fewer assessment points and a stricter 'two switches' definition. More assessments and a longer window mechanically find more switches.

**Next step:** No change needed beyond perhaps naming the age window and number of assessments for each so readers see why they differ. The short answer's '(studies disagree how many)' is accurate.

#### C04-011

**Does ADHD decline in older adults or go unrecognised?** · minor · method/measurement · Page reports both sides

**In dispute:** Adult prevalence falls with age (5.1% at 18-24 to 0.8% at 60+ for childhood-onset ADHD), but lower rates may partly reflect under-assessment; in over-50s, 2.18% by rating scales against 0.23% diagnosed.

- **Position A:** Real decline: the global meta-analysis shows falling prevalence across adult age bands, and five birth cohorts spanning ages 3 to 45 found ADHD trait scores fall steadily with age in the general population.
  - Song P, et al. The prevalence of adult attention-deficit hyperactivity disorder: a global systematic review and meta-analysis. J Glob Health. 2021. — [DOI 10.7189/jogh.11.04009](https://doi.org/10.7189/jogh.11.04009) · [PMID 33692893](https://pubmed.ncbi.nlm.nih.gov/33692893/); meta-analysis; cited on page; checked: PubMed record
  - Wootton RE, et al. Decline in attention-deficit hyperactivity disorder traits over the life course in the general population: trajectories across five population birth cohorts spanning ages 3 to 45 years. Int J Epidemiol. 2022. — [DOI 10.1093/ije/dyac049](https://doi.org/10.1093/ije/dyac049) · [PMID 35403686](https://pubmed.ncbi.nlm.nih.gov/35403686/); five population birth cohorts; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Under-recognition: in over-50s, symptom-scale prevalence (2.18%) is about ten times the diagnosed rate (0.23%), and treated ADHD is rarer still, which the authors read as missed cases rather than disappearance.
  - Dobrosavljevic M, et al. Prevalence of attention-deficit/hyperactivity disorder in older adults: a systematic review and meta-analysis. Neurosci Biobehav Rev. 2020. — [DOI 10.1016/j.neubiorev.2020.07.042](https://doi.org/10.1016/j.neubiorev.2020.07.042) · [PMID 32798966](https://pubmed.ncbi.nlm.nih.gov/32798966/); meta-analysis, n = 20 studies; cited on page; checked: PubMed record

**Why they may differ:** Both can be true: traits fall on average with age while diagnosis in older people lags far behind symptoms. Symptom scales in older adults also pick up sleep problems, depression, medication effects and early cognitive decline, which can inflate the 2.18% figure.

**Next step:** Optionally add Wootton 2022 as general-population evidence that average trait decline is real, independent of diagnosis rates, and note that symptom scales in older people overlap with ageing-related problems.

### [Will ADHD shorten my life? The hard statistics in context](../04-did-i-cause-this-and-where-is-it-going/the-hard-statistics-in-context.md)

#### C04-019

**Dementia risk** · major · size of effect · Page reports both sides

**In dispute:** Dementia: a real registry link, much weaker than headlines suggest; it weakens considerably after accounting for other psychiatric conditions (Swedish HR 2.92 to 1.62), and a 2023 review judged evidence too varied to combine.

- **Position A:** Weaker or confounded: in 3.6 million Swedes, the hazard ratio fell from 2.92 to 1.62 after accounting for depression, anxiety, substance use and bipolar disorder; part of the link runs in families; reverse causation (early dementia mislabelled as ADHD) is possible; a 2023 systematic review could not pool studies.
  - Dobrosavljevic M, et al. Attention-deficit/hyperactivity disorder as a risk factor for dementia and mild cognitive impairment: a population-based register study. Eur Psychiatry. 2022. — [DOI 10.1192/j.eurpsy.2021.2261](https://doi.org/10.1192/j.eurpsy.2021.2261) · [PMID 34924079](https://pubmed.ncbi.nlm.nih.gov/34924079/); national registry, n = 3.6 million; cited on page; checked: PubMed record
  - Becker S, et al. Risk of neurodegenerative disease or dementia in adults with attention-deficit/hyperactivity disorder: a systematic review. Front Psychiatry. 2023. — [DOI 10.3389/fpsyt.2023.1158546](https://doi.org/10.3389/fpsyt.2023.1158546) · [PMID 37663597](https://pubmed.ncbi.nlm.nih.gov/37663597/); systematic review, n = 7 studies; cited on page; checked: PubMed record
- **Position B:** Newer evidence points to a sizeable, partly genetic link: a 2026 meta-analysis of five studies pooled a hazard ratio of 2.52 for all-cause dementia; in 187,341 US adults aged 50+ (All of Us), cognitive impairment developed in 6.7% with ADHD against 3.4% without (HR 4.60, attenuated but not removed by adjustment), and a higher ADHD polygenic score also predicted impairment (HR 1.35), as it did in a separate multicohort study (10-year incidence 33.8% against 23.4% by score tertile).
  - Levine SZ, et al. Adult attention-deficit/hyperactivity disorder and the risk of dementia. JAMA Netw Open. 2023. — [DOI 10.1001/jamanetworkopen.2023.38088](https://doi.org/10.1001/jamanetworkopen.2023.38088) · [PMID 37847497](https://pubmed.ncbi.nlm.nih.gov/37847497/); health-insurance cohort, n = 109,218 (730 with adult ADHD); cited on page; checked: PubMed record
  - Baiamonte L, et al. Attention Deficit/Hyperactivity Disorder and Risk of Dementia: A Systematic Review and Meta-Analysis. Brain Sci. 2026. — [DOI 10.3390/brainsci16060646](https://doi.org/10.3390/brainsci16060646) · [PMID 42352655](https://pubmed.ncbi.nlm.nih.gov/42352655/); meta-analysis, n = 4 cohorts (3,703,877) and 1 case-control (400); **not yet cited on page**; checked: PubMed record + abstract
  - Bauer-Negrini G, et al. Attention-Deficit/Hyperactivity Disorder and Late-Life Cognitive Impairment. JAMA Psychiatry. 2026. — [DOI 10.1001/jamapsychiatry.2026.3165](https://doi.org/10.1001/jamapsychiatry.2026.3165) · [PMID 42842281](https://pubmed.ncbi.nlm.nih.gov/42842281/); cohort with EHR and polygenic scores (All of Us), n = 187,341 (3,026 with ADHD); **not yet cited on page**; checked: PubMed record + abstract
  - Leffa DT, et al. Attention-deficit/hyperactivity disorder polygenic risk score and incidence of cognitive impairment in older adults: A prospective multicohort study. Alzheimers Dement. 2026. — [DOI 10.1002/alz.71770](https://doi.org/10.1002/alz.71770) · [PMID 42878194](https://pubmed.ncbi.nlm.nih.gov/42878194/); prospective multicohort, polygenic score; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Studies differ in whether they adjust for psychiatric conditions that may lie on the pathway, in the outcome (dementia versus the broader 'cognitive impairment'), and in how ADHD is identified late in life, where new attention complaints can be early dementia (reverse causation). Polygenic-score links are less prone to reverse causation but can reflect shared genetics with education, vascular risk or psychiatric illness; the meta-analysis pooled only five studies, likely including the Swedish and Israeli ones already cited, so it does not add independent data so much as summarise them.

**Next step:** Revisit the heading 'much weaker than headlines suggest': it remains fair for the Swedish adjusted estimate but sits awkwardly beside a 2026 pooled HR of 2.52 and the All of Us HR of 4.60 with genetic support. Add the 2026 meta-analysis and All of Us study with absolute figures (6.7% against 3.4% over about 10 years), keep the reverse-causation and confounding caveats, and note that 'cognitive impairment' includes mild cognitive impairment, not only dementia. Check overlap of studies in the meta-analysis before treating it as independent.

#### C04-016

**Life expectancy: counted versus modelled** · moderate · method/measurement · Page reports both sides

**In dispute:** The '13 years' figure is a calculator estimate; a UK study that counted deaths found life expectancy 6.8 (men) and 8.6 (women) years shorter in diagnosed adults, probably more than for everyone with ADHD.

- **Position A:** Counted from deaths in UK primary-care records of 30,039 diagnosed adults: 6.8 and 8.6 years less life expectancy, which the authors say probably overstates the gap for all people with ADHD.
  - O'Nions E, et al. Life expectancy and years of life lost for adults with diagnosed ADHD in the UK: matched cohort study. Br J Psychiatry. 2025. — [DOI 10.1192/bjp.2024.199](https://doi.org/10.1192/bjp.2024.199) · [PMID 39844532](https://pubmed.ncbi.nlm.nih.gov/39844532/); matched primary-care cohort, n = 30,039 with ADHD; cited on page; checked: PubMed record
- **Position B:** Modelled with an actuarial calculator from risk-factor answers in a Milwaukee clinical cohort, with no deaths counted: 8.4 fewer total years for the childhood group and about 12.7 years (healthy life) for those whose ADHD persisted.
  - Barkley RA, et al. Hyperactive child syndrome and estimated life expectancy at young adult follow-up: the role of ADHD persistence and other potential predictors. J Atten Disord. 2019. — [DOI 10.1177/1087054718816164](https://doi.org/10.1177/1087054718816164) · [PMID 30526189](https://pubmed.ncbi.nlm.nih.gov/30526189/); clinical cohort with actuarial estimate, n = 131 cases, 71 controls; cited on page; checked: PubMed record

**Why they may differ:** One counts actual deaths in diagnosed adults (who are more severely affected than the wider ADHD population, and whose deaths may reflect co-occurring conditions); the other predicts lifespan from present-day risk factors in a small, severe, mostly male clinic sample. Calculators assume risk factors persist and add up, which may not hold. Neither represents undiagnosed adults. Several published commentaries on the UK paper and an author reply exist (Br J Psychiatry 2025-26, e.g. PMIDs 40685928, 40904184, 40910173, 41178080) but have no abstracts, so their arguments were not checked.

**Next step:** Page handles this carefully and follows safe messaging. Read the UK commentaries and author reply in full; if they raise substantive critiques (for example about matching, coding of ADHD in GP records, or life-table methods), add one line to the 'what is uncertain' section.

#### C04-017

**Size of the raised risk of suicide death** · moderate · size of effect · Page reports both sides

**In dispute:** Suicide deaths: odds ratio 6.7 in a 2019 meta-analysis (four datasets, interval 3.24-17.39); the 2026 meta-analysis found death from suicide about 90% higher.

- **Position A:** A 2019 meta-analysis pooled four datasets and found about 6.7 times the odds of suicide death, with very wide uncertainty.
  - Septier M, et al. Association between suicidal spectrum behaviors and attention-deficit/hyperactivity disorder: a systematic review and meta-analysis. Neurosci Biobehav Rev. 2019. — [DOI 10.1016/j.neubiorev.2019.05.022](https://doi.org/10.1016/j.neubiorev.2019.05.022) · [PMID 31129238](https://pubmed.ncbi.nlm.nih.gov/31129238/); meta-analysis, n = 4 datasets for suicide death; cited on page; checked: PubMed record
- **Position B:** A 2026 meta-analysis of 19 studies (about 16 million people) found a hazard ratio of roughly 1.9 for suicide death, a much smaller relative increase.
  - Corrigan L, et al. Mortality among people with attention-deficit/hyperactivity disorder: a systematic review and meta-analysis. JAMA Netw Open. 2026. — [DOI 10.1001/jamanetworkopen.2026.39448](https://doi.org/10.1001/jamanetworkopen.2026.39448) · [PMID 42895743](https://pubmed.ncbi.nlm.nih.gov/42895743/); meta-analysis, n = 19 studies, about 16 million people; cited on page; checked: PubMed record

**Why they may differ:** The 2019 estimate rests on four datasets and mixes odds ratios from case-control and cohort designs, which inflate when outcomes are rare and samples are selected; the 2026 estimate pools more and larger cohort studies with hazard ratios and is more precise. Different adjustment for co-occurring depression and substance use, and different eras, also matter. The page gives both numbers in separate paragraphs without saying they disagree or which is more reliable.

**Next step:** In the suicide paragraph, state that the larger, newer meta-analysis gives a smaller relative increase (about 1.9) and that the 6.7 figure rests on four datasets; lead with the more reliable figure. Keep absolute framing ('raised, and still uncommon') and the crisis-contacts link; avoid any method detail, per safe-messaging guidance. Seek an absolute suicide-death rate per 10,000 from a registry source (for example the Danish cohort's cause-specific data).

#### C04-018

**How much is all-cause mortality raised, and how much is due to co-occurring conditions** · minor · size of effect · Page reports both sides

**In dispute:** Death rates are about twice as high (Danish rate ratio 2.07; 2022 meta-analysis 2.13), about 70% higher in the 2026 meta-analysis (1.71), and fall to 1.50 once conduct and substance use disorders are excluded.

- **Position A:** About double: Danish registry rate ratio 2.07 and a 2022 meta-analysis relative risk of 2.13 (8 studies, interval 1.13-4.02).
  - Dalsgaard S, et al. Mortality in children, adolescents, and adults with attention deficit hyperactivity disorder: a nationwide cohort study. Lancet. 2015. — [DOI 10.1016/S0140-6736(14)61684-6](https://doi.org/10.1016/S0140-6736(14)61684-6) · [PMID 25726514](https://pubmed.ncbi.nlm.nih.gov/25726514/); national registry cohort, n = 1.92 million (32,061 with ADHD); cited on page; checked: PubMed record
  - Catalá-López F, et al. Mortality in persons with autism spectrum disorder or attention-deficit/hyperactivity disorder: a systematic review and meta-analysis. JAMA Pediatr. 2022. — [DOI 10.1001/jamapediatrics.2021.6401](https://doi.org/10.1001/jamapediatrics.2021.6401) · [PMID 35157020](https://pubmed.ncbi.nlm.nih.gov/35157020/); meta-analysis, n = 8 studies for ADHD; cited on page; checked: PubMed record
- **Position B:** Smaller once more studies are pooled or co-occurring conditions removed: 1.71 across 19 studies, and 1.50 in Denmark after excluding conduct and substance use disorders, with the male estimate (1.27) not distinguishable from no difference.
  - Corrigan L, et al. Mortality among people with attention-deficit/hyperactivity disorder: a systematic review and meta-analysis. JAMA Netw Open. 2026. — [DOI 10.1001/jamanetworkopen.2026.39448](https://doi.org/10.1001/jamanetworkopen.2026.39448) · [PMID 42895743](https://pubmed.ncbi.nlm.nih.gov/42895743/); meta-analysis, n = 19 studies; cited on page; checked: PubMed record

**Why they may differ:** Estimates differ by age of cohort (Danish cohort aged 32 or under, where accidents dominate), by adjustment for co-occurring conditions, and by which studies are pooled. Whether to adjust for conduct and substance disorders is itself debated: they may be pathways from ADHD rather than confounders, so the 1.50 figure may understate ADHD-related risk.

**Next step:** Consider adding a sentence that excluding co-occurring conditions can remove part of ADHD's own effect if ADHD leads to them, so 1.50 and 2.07 bracket the plausible range rather than one being 'true'. The short answer's 'about 6 in 10,000 against 2' is consistent with the sources.

### [What causes ADHD, and is it my fault or my parents'?](../04-did-i-cause-this-and-where-is-it-going/what-does-and-doesnt-cause-adhd.md)

#### C04-001

**Paracetamol (acetaminophen) in pregnancy** · major · causal interpretation · Page reports both sides

**In dispute:** Paracetamol in pregnancy does not appear to cause ADHD; there is no link once families are accounted for.

- **Position A:** Sibling-comparison studies and reviews that weight them find the small whole-population association disappears within families, pointing to shared family factors (for example the mother's own genes or the illnesses that lead to taking paracetamol).
  - Ahlqvist VH, et al. Acetaminophen use during pregnancy and children's risk of autism, ADHD, and intellectual disability. JAMA. 2024. — [DOI 10.1001/jama.2024.3172](https://doi.org/10.1001/jama.2024.3172) · [PMID 38592388](https://pubmed.ncbi.nlm.nih.gov/38592388/); registry with full-sibling comparison, n = 2.48 million children; cited on page; checked: PubMed record + abstract
  - Sheikh J, et al. Maternal paracetamol (acetaminophen) use during pregnancy and risk of autism spectrum disorder and attention deficit/hyperactivity disorder in offspring: umbrella review of systematic reviews. BMJ. 2025. — [DOI 10.1136/bmj-2025-088141](https://doi.org/10.1136/bmj-2025-088141) · [PMID 41207796](https://pubmed.ncbi.nlm.nih.gov/41207796/); umbrella review, n = 9 reviews, 40 studies; cited on page; checked: PubMed record
  - Gustavson K, et al. Acetaminophen use during pregnancy and offspring attention deficit hyperactivity disorder - a longitudinal sibling control study. JCPP Adv. 2021. — [DOI 10.1002/jcv2.12020](https://doi.org/10.1002/jcv2.12020) · [PMID 37431475](https://pubmed.ncbi.nlm.nih.gov/37431475/); prospective cohort with sibling control (MoBa), n = 26,613 children from 12,902 families; **not yet cited on page**; checked: PubMed record + abstract
  - Okubo Y, et al. Maternal Acetaminophen Use and Offspring's Neurodevelopmental Outcome: A Nationwide Birth Cohort Study. Paediatr Perinat Epidemiol. 2026. — [DOI 10.1111/ppe.70071](https://doi.org/10.1111/ppe.70071) · [PMID 40898607](https://pubmed.ncbi.nlm.nih.gov/40898607/); nationwide administrative birth cohort (Japan) with sibling comparison, bias analysis and negative controls, n = 217,602 children; 23,593 in sibling analysis; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Some reviews and biomarker studies read the evidence as consistent with a real effect, especially for long or heavy use, and argue sibling designs can hide true effects. A Navigation Guide review of 46 studies concluded the evidence supports an association and called for limiting use; a cord-blood study found a dose-response pattern; the Norwegian study found long-term use (29+ days) doubled risk between families before the sibling analysis removed it.
  - Prada D, et al. Evaluation of the evidence on acetaminophen use and neurodevelopmental disorders using the Navigation Guide methodology. Environ Health. 2025. — [DOI 10.1186/s12940-025-01208-0](https://doi.org/10.1186/s12940-025-01208-0) · [PMID 40804730](https://pubmed.ncbi.nlm.nih.gov/40804730/); systematic review (Navigation Guide, qualitative synthesis), n = 46 studies; **not yet cited on page**; checked: PubMed record + abstract
  - Ji Y, et al. Association of Cord Plasma Biomarkers of In Utero Acetaminophen Exposure With Risk of Attention-Deficit/Hyperactivity Disorder and Autism Spectrum Disorder in Childhood. JAMA Psychiatry. 2020. — [DOI 10.1001/jamapsychiatry.2019.3259](https://doi.org/10.1001/jamapsychiatry.2019.3259) · [PMID 31664451](https://pubmed.ncbi.nlm.nih.gov/31664451/); prospective cohort with cord-plasma biomarkers (Boston Birth Cohort), n = 996 mother-infant pairs; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Side B relies mainly on whole-population comparisons, which cannot separate paracetamol from the reasons for taking it (fever, infection, pain) or from the mother's genes; the cord-blood study measured exposure well but was a small, high-risk clinic sample with little control for family factors. Side A's sibling designs remove fixed family factors but lose precision, depend on mothers whose use differed between pregnancies, and are biased towards no effect when exposure is misrecorded, which Prada and colleagues argue can hide a small or dose-dependent effect. The Japanese study's bias analyses suggested misclassification and confounding inflate, rather than hide, the observed link.

**Next step:** Add one sentence acknowledging that a 2025 Navigation Guide review (Prada et al.) reached the opposite reading and why it differs (no sibling weighting, qualitative synthesis), and consider citing the Norwegian and Japanese sibling studies as independent replications of the Swedish null. Check whether long-duration use has been tested specifically in sibling designs beyond Gustavson 2021, and soften 'no link' to 'no link within families' in the heading if long-term-use data stay thin.

#### C04-002

**Smoking in pregnancy** · moderate · causal interpretation · Page reports one side only

**In dispute:** The smoking-in-pregnancy link with ADHD largely disappears when siblings are compared, so it is mostly about families.

- **Position A:** Sibling and negative-control designs find the association is explained by family factors: the Swedish sibling estimate was about 0.85, and a three-cohort triangulation study using fathers' smoking as a control and genetic scores found no causal intrauterine effect.
  - Skoglund C, et al. Familial confounding of the association between maternal smoking during pregnancy and ADHD in offspring. J Child Psychol Psychiatry. 2014. — [DOI 10.1111/jcpp.12124](https://doi.org/10.1111/jcpp.12124) · [PMID 25359172](https://pubmed.ncbi.nlm.nih.gov/25359172/); registry with sibling and cousin comparisons; cited on page; checked: PubMed record
  - Haan E, et al. Prenatal smoking, alcohol and caffeine exposure and maternal-reported attention deficit hyperactivity disorder symptoms in childhood: triangulation of evidence using negative control and polygenic risk score analyses. Addiction. 2022. — [DOI 10.1111/add.15746](https://doi.org/10.1111/add.15746) · [PMID 34791750](https://pubmed.ncbi.nlm.nih.gov/34791750/); negative-control (paternal) and polygenic score triangulation across ALSPAC, Generation R and MoBa, n = up to about 42,000 children per cohort; **not yet cited on page**; checked: PubMed record + abstract
  - Tsegay L, et al. Maternal and paternal smoking during pregnancy and the risk of ADHD in offspring: An umbrella review of systematic reviews and meta-analyses. J Psychiatr Res. 2026. — [DOI 10.1016/j.jpsychires.2025.12.010](https://doi.org/10.1016/j.jpsychires.2025.12.010) · [PMID 41385914](https://pubmed.ncbi.nlm.nih.gov/41385914/); umbrella review, n = 6 meta-analyses; about 2.2 million participants for maternal smoking; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Pooled observational studies consistently find raised odds (about 1.7 for maternal smoking), and a 2024 two-sample Mendelian randomisation study reported a causal effect (odds ratio 2.54), though a published comment judged that evidence inconclusive.
  - Xie T, et al. The causal impact of maternal smoking around birth on offspring ADHD: A two-sample Mendelian randomization study. J Affect Disord. 2024. — [DOI 10.1016/j.jad.2024.01.196](https://doi.org/10.1016/j.jad.2024.01.196) · [PMID 38266926](https://pubmed.ncbi.nlm.nih.gov/38266926/); two-sample Mendelian randomisation; **not yet cited on page**; checked: PubMed record + abstract
  - Sorjonen K, et al. Inconclusive evidence for a causal impact of maternal smoking on offspring ADHD in a Mendelian randomization study by Xie and Mao (2024). J Affect Disord. 2024. — [DOI 10.1016/j.jad.2024.03.140](https://doi.org/10.1016/j.jad.2024.03.140) · [PMID 38554877](https://pubmed.ncbi.nlm.nih.gov/38554877/); critical comment; **not yet cited on page**; checked: PubMed record (comment, no abstract)

**Why they may differ:** Whole-population studies cannot separate smoking from the mother's own ADHD-linked genes and circumstances. The umbrella review found fathers' smoking was linked to ADHD almost as strongly as mothers', which is hard to explain by a direct effect in the womb and points to family confounding. The Mendelian randomisation study used variants for the mother's smoking measured in adults' own genomes ('maternal smoking around birth' as reported by UK Biobank participants), which also partly measure the child's inherited liability, so it may not isolate the pregnancy exposure; its critics made this kind of point.

**Next step:** Keep the page's conclusion but strengthen it with the paternal-smoking negative control (Tsegay 2026, Haan 2022), which is easier for readers to follow than sibling designs. If the Xie MR result is mentioned anywhere on the site, pair it with the critique. Confirm the Skoglund sample size from the full record before quoting it.

#### C04-003

**Alcohol in pregnancy** · moderate · population/age · Page does not mention it

**In dispute:** Not covered on the page: whether drinking alcohol in pregnancy causes ADHD.

- **Position A:** Heavy prenatal alcohol exposure causes fetal alcohol spectrum disorder (FASD), and ADHD is among the most common diagnoses in people with prenatal alcohol exposure; ADHD-like symptoms in FASD can be mistaken for ADHD.
  - Clark CA, et al. Prevalence of co-occurring diagnoses in people exposed to alcohol prenatally: Findings from a meta-analysis. J Affect Disord. 2024. — [DOI 10.1016/j.jad.2024.05.035](https://doi.org/10.1016/j.jad.2024.05.035) · [PMID 38718944](https://pubmed.ncbi.nlm.nih.gov/38718944/); meta-analysis; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** For the light-to-moderate drinking that most pregnant drinkers report, sibling and negative-control designs find at most a very weak link with ADHD symptoms and none with an ADHD diagnosis.
  - Eilertsen EM, et al. Maternal alcohol use during pregnancy and offspring attention-deficit hyperactivity disorder (ADHD): a prospective sibling control study. Int J Epidemiol. 2017. — [DOI 10.1093/ije/dyx067](https://doi.org/10.1093/ije/dyx067) · [PMID 28449133](https://pubmed.ncbi.nlm.nih.gov/28449133/); prospective cohort with sibling control and negative control (MoBa); **not yet cited on page**; checked: PubMed record + abstract
  - Haan E, et al. Prenatal smoking, alcohol and caffeine exposure and maternal-reported attention deficit hyperactivity disorder symptoms in childhood: triangulation of evidence using negative control and polygenic risk score analyses. Addiction. 2022. — [DOI 10.1111/add.15746](https://doi.org/10.1111/add.15746) · [PMID 34791750](https://pubmed.ncbi.nlm.nih.gov/34791750/); negative-control and polygenic score triangulation, three cohorts, n = up to about 42,000 children per cohort; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The two sides concern different doses. Heavy or binge exposure has well-established effects on the developing brain; the cohort studies mostly capture low, self-reported drinking, where familial confounding dominates and true effects, if any, are small. Self-report of drinking in pregnancy is also under-reported, which biases towards no effect.

**Next step:** Add a short alcohol paragraph to the causes page (a common parental worry), separating heavy exposure and FASD from light drinking, and link to any FASD differential-diagnosis content on is-it-adhd-or-something-else. Avoid wording that implies drinking in pregnancy is safe; national guidance advises none.

#### C04-004

**Very preterm birth: does the link survive sibling comparison?** · moderate · causal interpretation · Page does not mention it

**In dispute:** Very preterm birth is consistently linked to ADHD (odds ratio 3.04) but cause is not established; whether it holds in sibling comparisons was not checked for this page.

- **Position A:** Meta-analysis of 12 studies: very or extremely preterm or very low birth weight children have about three times the odds of ADHD; the page treats causation as open.
  - Franz AP, et al. Attention-deficit/hyperactivity disorder and very preterm/very low birth weight: a meta-analysis. Pediatrics. 2018. — [DOI 10.1542/peds.2017-1645](https://doi.org/10.1542/peds.2017-1645) · [PMID 29255083](https://pubmed.ncbi.nlm.nih.gov/29255083/); meta-analysis, n = 12 studies, 1,787 people; cited on page; checked: PubMed record
- **Position B:** Sibling designs show the link largely survives: in Norway, early-preterm children scored about 0.24 SD higher on ADHD symptoms after accounting for family factors, and a systematic review of 140 twin and sibling studies listed low birth weight and gestational age among the few early factors still linked to ADHD after familial adjustment.
  - Ask H, et al. Association of Gestational Age at Birth With Symptoms of Attention-Deficit/Hyperactivity Disorder in Children. JAMA Pediatr. 2018. — [DOI 10.1001/jamapediatrics.2018.1315](https://doi.org/10.1001/jamapediatrics.2018.1315) · [PMID 29946656](https://pubmed.ncbi.nlm.nih.gov/29946656/); prospective cohort with sibling comparison (MoBa), n = 113,227 children incl. 33,081 siblings; **not yet cited on page**; checked: PubMed record + abstract
  - Carlsson T, et al. Early environmental risk factors for neurodevelopmental disorders - a systematic review of twin and sibling studies. Dev Psychopathol. 2021. — [DOI 10.1017/S0954579420000620](https://doi.org/10.1017/S0954579420000620) · [PMID 32703331](https://pubmed.ncbi.nlm.nih.gov/32703331/); systematic review of twin and sibling studies, n = 140 articles; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** This is less a contradiction than a gap the page itself flags. The meta-analysis pooled ordinary comparisons; the sibling studies remove shared family factors and still find a link, which makes a causal contribution of very early birth more plausible than for smoking or paracetamol. Sibling effects were modest (around a quarter of a standard deviation) and stronger for inattention.

**Next step:** Replace 'whether this holds in sibling comparisons was not checked' with the Ask 2018 and Carlsson 2021 findings, and adjust the short answer: preterm birth is the one exposure on the page whose link survives sibling comparison. Look for absolute ADHD rates by gestational age in a registry source to meet the absolute-risk rule.

#### C04-005

**Screens and ADHD symptoms** · moderate · causal interpretation · Page reports one side only

**In dispute:** Screens are linked with later ADHD symptoms, but cause is unproven (based on one US cohort of 2,587 teenagers).

- **Position A:** Some longitudinal and genetic studies suggest digital media may raise later ADHD symptoms: the US cohort found 9.5% against 4.6%; a review of 28 longitudinal studies found effects in both directions, more consistent for problematic use; one Mendelian randomisation study reported that genetically predicted phone and TV time raised childhood ADHD risk.
  - Ra CK, et al. Association of digital media use with subsequent symptoms of attention-deficit/hyperactivity disorder among adolescents. JAMA. 2018. — [DOI 10.1001/jama.2018.8931](https://doi.org/10.1001/jama.2018.8931) · [PMID 30027248](https://pubmed.ncbi.nlm.nih.gov/30027248/); prospective cohort, n = 2,587 adolescents; cited on page; checked: PubMed record
  - Thorell LB, et al. Longitudinal associations between digital media use and ADHD symptoms in children and adolescents: a systematic literature review. Eur Child Adolesc Psychiatry. 2024. — [DOI 10.1007/s00787-022-02130-3](https://doi.org/10.1007/s00787-022-02130-3) · [PMID 36562860](https://pubmed.ncbi.nlm.nih.gov/36562860/); systematic review of longitudinal studies, n = 28 studies; **not yet cited on page**; checked: PubMed record + abstract
  - Meng Z, et al. Relationships between screen time and childhood attention deficit hyperactivity disorder: a Mendelian randomization study. Front Psychiatry. 2024. — [DOI 10.3389/fpsyt.2024.1441191](https://doi.org/10.3389/fpsyt.2024.1441191) · [PMID 39376970](https://pubmed.ncbi.nlm.nih.gov/39376970/); two-sample Mendelian randomisation; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Other designs find the link is small or largely genetic: a meta-analysis of 87 studies found only a small correlation of screen time with behaviour problems (r 0.11); in 4,262 US children, shared genetic risk accounted for most or all of the screen time-attention link; and a second Mendelian randomisation study found genetically predicted leisure screen time associated with lower ADHD risk.
  - Eirich R, et al. Association of Screen Time With Internalizing and Externalizing Behavior Problems in Children 12 Years or Younger: A Systematic Review and Meta-analysis. JAMA Psychiatry. 2022. — [DOI 10.1001/jamapsychiatry.2022.0155](https://doi.org/10.1001/jamapsychiatry.2022.0155) · [PMID 35293954](https://pubmed.ncbi.nlm.nih.gov/35293954/); meta-analysis, n = 87 studies, 159,425 children; **not yet cited on page**; checked: PubMed record + abstract
  - Zhang Y, et al. Shared Genetic Risk in the Association of Screen Time With Psychiatric Problems in Children. JAMA Netw Open. 2023. — [DOI 10.1001/jamanetworkopen.2023.41502](https://doi.org/10.1001/jamanetworkopen.2023.41502) · [PMID 37930702](https://pubmed.ncbi.nlm.nih.gov/37930702/); cohort with polygenic scores (ABCD), n = 4,262 children; **not yet cited on page**; checked: PubMed record + abstract
  - Cai C, et al. Leisure Screen Time and the Risk of Six Neurodevelopmental Disorders: A Two-Sample Mendelian Randomization Study. Brain Behav. 2025. — [DOI 10.1002/brb3.70884](https://doi.org/10.1002/brb3.70884) · [PMID 40977001](https://pubmed.ncbi.nlm.nih.gov/40977001/); two-sample Mendelian randomisation; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Screen time is self- or parent-reported and bundled with sleep, family conflict and genes that also shape attention. Polygenic designs suggest the same inherited tendencies drive both, while the two Mendelian randomisation studies, using adult screen-time variants from the same UK Biobank-type data, reached opposite conclusions, which suggests the genetic instruments are not specific to screen use. Reciprocal effects mean children with attention problems may drift towards heavier or more problematic use.

**Next step:** Replace or supplement the single 2018 cohort with the Eirich meta-analysis (small effect) and Thorell review (reciprocal effects), and mention genetic confounding (Zhang 2023). Do not cite either MR study alone; if cited, cite both as showing the method gives contradictory answers here.

#### C04-006

**Diet beyond sugar: food colours and elimination diets** · minor · size of effect · Page does not mention it

**In dispute:** Sugar has no effect in blinded trials, and the evidence does not support that a parent caused ADHD through sugar; myths page groups 'sugar, screens' together as myths.

- **Position A:** Blinded sugar challenge trials found no effect on behaviour or thinking, though a small effect in a subgroup could not be ruled out.
  - Wolraich ML, et al. The effect of sugar on behavior or cognition in children: a meta-analysis. JAMA. 1995. — [DOI 10.1001/jama.1995.03530200053037](https://doi.org/10.1001/jama.1995.03530200053037) · [PMID 7474248](https://pubmed.ncbi.nlm.nih.gov/7474248/); meta-analysis of blinded within-person trials, n = 23 studies; cited on page; checked: PubMed record
- **Position B:** For other parts of the diet, blinded trials do show small effects in some children: removing artificial food colours had an effect that survived probably blinded ratings (SMD 0.42, mostly in children selected for food sensitivity), and a review of meta-analyses found few-foods (elimination) diet effects that were larger on parent ratings but uncertain on others' ratings.
  - Sonuga-Barke EJ, et al. Nonpharmacological interventions for ADHD: systematic review and meta-analyses of randomized controlled trials of dietary and psychological treatments. Am J Psychiatry. 2013. — [DOI 10.1176/appi.ajp.2012.12070991](https://doi.org/10.1176/appi.ajp.2012.12070991) · [PMID 23360949](https://pubmed.ncbi.nlm.nih.gov/23360949/); meta-analysis of RCTs, n = 54 trials; **not yet cited on page**; checked: PubMed record + abstract
  - Pelsser LM, et al. Diet and ADHD, Reviewing the Evidence: A Systematic Review of Meta-Analyses of Double-Blind Placebo-Controlled Trials Evaluating the Efficacy of Diet Interventions on the Behavior of Children with ADHD. PLoS One. 2017. — [DOI 10.1371/journal.pone.0169277](https://doi.org/10.1371/journal.pone.0169277) · [PMID 28121994](https://pubmed.ncbi.nlm.nih.gov/28121994/); systematic review of meta-analyses; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** These are different questions: sugar versus food additives or broad elimination diets, and 'causes ADHD' versus 'worsens symptoms in a subgroup of children who already have it'. Unblinded parent ratings inflate diet effects, and children selected for suspected food sensitivity are not typical. The site's lifestyle page already reports the food-colour findings (Sonuga-Barke 2013; Nigg 2012), so the gap is a cross-page framing one.

**Next step:** Add one sentence on the causes page noting that food colours are a separate question with small effects in some children, linking to 06-treatment-what-works/lifestyle-and-other-approaches.md, so readers do not read 'diet doesn't matter' from the sugar finding. Check the myths page wording for the same issue.

#### C04-007

**Can extreme early adversity cause ADHD?** · minor · population/age · Page does not mention it

**In dispute:** Parenting style does not appear to cause ADHD; the arrow often runs from child to parent.

- **Position A:** Adoption data show a child's inherited traits draw out harsher parenting, rather than ordinary parenting causing ADHD.
  - Harold GT, et al. Biological and rearing mother influences on child ADHD symptoms: revisiting the developmental interface between nature and nurture. J Child Psychol Psychiatry. 2013. — [DOI 10.1111/jcpp.12100](https://doi.org/10.1111/jcpp.12100) · [PMID 24007415](https://pubmed.ncbi.nlm.nih.gov/24007415/); adoption study, n = two adoption samples; cited on page; checked: PubMed record
- **Position B:** Severe early deprivation does appear to cause an ADHD-like condition: Romanian children who spent more than six months in extreme institutional care were about seven times as likely to meet adult ADHD criteria (29.3% against 3.8%), a deprivation-related variant that persisted despite good adoptive homes.
  - Kennedy M, et al. Early severe institutional deprivation is associated with a persistent variant of adult attention-deficit/hyperactivity disorder: clinical presentation, developmental continuities and life circumstances in the English and Romanian Adoptees study. J Child Psychol Psychiatry. 2016. — [DOI 10.1111/jcpp.12576](https://doi.org/10.1111/jcpp.12576) · [PMID 27264475](https://pubmed.ncbi.nlm.nih.gov/27264475/); natural-experiment adoption cohort (ERA); **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Not a contradiction about ordinary parenting: the ERA study concerns extreme global neglect in institutions, far outside normal family variation, and the resulting presentation was unusual (mostly inattentive, high autistic and social-disinhibition features). It does show that the environment can cause ADHD-like problems in extreme cases, which qualifies 'genes explain most' as a population average under ordinary conditions.

**Next step:** Consider one sentence in the uncertainty section that extreme early deprivation is an established exception, worded so parents do not read it as about ordinary parenting. Confirm the exact cohort size from the full text before quoting numbers.

### [Addiction and ADHD: is risk higher, and do medicines raise it?](../05-what-often-comes-with-it/alcohol-drugs-and-addiction.md)

#### C05-001

**Does childhood ADHD medication protect against later substance problems?** · moderate · causal interpretation · Page reports both sides

**In dispute:** Prescribed medication has not been found to raise later addiction risk; in observational studies medicated periods had fewer substance-related problems ('if anything, medicated periods are associated with fewer substance problems').

- **Position A:** Protective association: within-person US insurance data found 31-35% lower odds of substance-related events in medicated months; a Swedish registry found 31% lower substance-related outcomes after stimulant use; a 2025 target-trial emulation found 15% lower substance misuse over two years.
  - Quinn PD, et al. ADHD medication and substance-related problems. Am J Psychiatry. 2017. — [DOI 10.1176/appi.ajp.2017.16060686](https://doi.org/10.1176/appi.ajp.2017.16060686) · [PMID 28659039](https://pubmed.ncbi.nlm.nih.gov/28659039/); within-person insurance-claims cohort, n = about 3 million; cited on page; checked: PubMed record
  - Chang Z, et al. Stimulant ADHD medication and risk for substance abuse. J Child Psychol Psychiatry. 2014. — [DOI 10.1111/jcpp.12164](https://doi.org/10.1111/jcpp.12164) · [PMID 25158998](https://pubmed.ncbi.nlm.nih.gov/25158998/); national registry; cited on page; checked: PubMed record
  - Zhang L, et al. ADHD drug treatment and risk of suicidal behaviours, substance misuse, accidental injuries, transport accidents, and criminality: emulation of target trials. BMJ. 2025. — [DOI 10.1136/bmj-2024-083658](https://doi.org/10.1136/bmj-2024-083658) · [PMID 40803836](https://pubmed.ncbi.nlm.nih.gov/40803836/); target-trial emulation, national registry, n = 148,581; cited on page; checked: PubMed record
- **Position B:** Neutral in the long run: a meta-analysis of 15 studies found childhood stimulant treatment neither raised nor lowered later substance outcomes, and the MTA's 16-year follow-up of 579 children, using models that adjust for changing confounders, found no evidence that current, prior, longer or continuous stimulant treatment was linked to adult substance use or substance use disorder in either direction.
  - Humphreys KL, et al. Stimulant medication and substance use outcomes: a meta-analysis. JAMA Psychiatry. 2013. — [DOI 10.1001/jamapsychiatry.2013.1273](https://doi.org/10.1001/jamapsychiatry.2013.1273) · [PMID 23754458](https://pubmed.ncbi.nlm.nih.gov/23754458/); meta-analysis of observational studies, n = 15 studies; cited on page; checked: PubMed record
  - Molina BSG, et al. Association Between Stimulant Treatment and Substance Use Through Adolescence Into Early Adulthood. JAMA Psychiatry. 2023. — [DOI 10.1001/jamapsychiatry.2023.2157](https://doi.org/10.1001/jamapsychiatry.2023.2157) · [PMID 37405756](https://pubmed.ncbi.nlm.nih.gov/37405756/); clinical cohort with marginal structural models (MTA), n = 579; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The protective findings are short-term (month-by-month or two-year windows) and concern acute substance-related events such as emergency visits, which medication might reduce through less impulsive behaviour while it is being taken; the neutral findings concern long-term use patterns years later. Registry estimates may also reflect healthy-adherer effects (people stable enough to take medication regularly). The two sides agree that medication does not raise risk.

**Next step:** Add Molina 2023 as the best long-term evidence that childhood stimulant treatment neither increases nor prevents adult substance use, and qualify 'if anything, medicated periods are associated with fewer substance problems' as a short-term finding about acute events. Mirror on 06-treatment-what-works/what-registries-show.md if it makes the same claim.

#### C05-002

**Does ADHD itself lead to substance use, or is the link confounded?** · moderate · causal interpretation · Page does not mention it

**In dispute:** Shared genetic influences, impulsivity, reward differences and social factors probably all contribute; the self-medication idea is a hypothesis with no good test found.

- **Position A:** Prospective cohorts and meta-analyses show children with ADHD go on to higher nicotine use (odds ratio 2.36) and alcohol use disorder (1.35), and the page treats mechanism as open.
  - Charach A, et al. Childhood attention-deficit/hyperactivity disorder and future substance use disorders: comparative meta-analyses. J Am Acad Child Adolesc Psychiatry. 2011. — [DOI 10.1016/j.jaac.2010.09.019](https://doi.org/10.1016/j.jaac.2010.09.019) · [PMID 21156266](https://pubmed.ncbi.nlm.nih.gov/21156266/); meta-analysis of prospective cohorts, n = 13 cohorts; cited on page; checked: PubMed record + abstract
- **Position B:** Mendelian randomisation suggests genetic liability to ADHD has a causal effect on starting and continuing smoking (and on smoking heaviness), and on cannabis initiation, with weaker evidence for alcohol dependence; a second study also supported a causal effect of ADHD liability on substance use disorder alongside a shared genetic background.
  - Treur JL, et al. Investigating causality between liability to ADHD and substance use, and liability to substance use and ADHD risk, using Mendelian randomization. Addict Biol. 2021. — [DOI 10.1111/adb.12849](https://doi.org/10.1111/adb.12849) · [PMID 31733098](https://pubmed.ncbi.nlm.nih.gov/31733098/); bidirectional two-sample Mendelian randomisation; **not yet cited on page**; checked: PubMed record + abstract
  - Vilar-Ribó L, et al. Genetic overlap and causality between substance use disorder and attention-deficit and hyperactivity disorder. Am J Med Genet B Neuropsychiatr Genet. 2021. — [DOI 10.1002/ajmg.b.32827](https://doi.org/10.1002/ajmg.b.32827) · [PMID 33244849](https://pubmed.ncbi.nlm.nih.gov/33244849/); genetic correlation and Mendelian randomisation, n = 989 clinical sample plus GWAS summary data; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Not a contradiction but a gap: the page presents causation as unknown, while genetic causal-inference studies offer moderate support for a path from ADHD liability to smoking and cannabis. MR assumes the variants affect substance use only through ADHD; ADHD variants overlap with education and risk-taking, so pleiotropy could inflate estimates. MR also cannot say whether the path runs through self-medication, impulsivity or social disadvantage.

**Next step:** Add a sentence in 'Why the link exists' that genetic (Mendelian randomisation) studies support ADHD liability raising smoking and cannabis initiation, with the usual MR caveats; it still does not test self-medication specifically. Consider linking to genes-and-inheritance for shared genetics.

### [Anxiety and depression with ADHD: why are they so common?](../05-what-often-comes-with-it/anxiety-and-depression.md)

#### C05-005

**Direction of the ADHD-depression link** · moderate · causal interpretation · Page reports both sides

**In dispute:** Genetic studies suggest ADHD modestly raises later depression risk (MR odds ratio 1.21; 1.09 in a larger study), and depression liability may raise ADHD risk more (1.76).

- **Position A:** ADHD leads to depression: childhood ADHD predicted recurrent depression in ALSPAC and MR gave odds ratio 1.21; a 2024 Swedish study triangulating sibling and twin comparisons (HR 4.12 for later depression after adjusting for shared family factors), twin-cohort score associations and MR (odds ratio 1.15) concluded ADHD is causally related to major depression.
  - Riglin L, et al. ADHD and depression: investigating a causal explanation. Psychol Med. 2021. — [DOI 10.1017/S0033291720000665](https://doi.org/10.1017/S0033291720000665) · [PMID 32249726](https://pubmed.ncbi.nlm.nih.gov/32249726/); birth cohort plus Mendelian randomisation; cited on page; checked: PubMed record
  - Garcia-Argibay M, et al. Attention-Deficit/Hyperactivity Disorder and Major Depressive Disorder: Evidence From Multiple Genetically Informed Designs. Biol Psychiatry. 2024. — [DOI 10.1016/j.biopsych.2023.07.017](https://doi.org/10.1016/j.biopsych.2023.07.017) · [PMID 37562520](https://pubmed.ncbi.nlm.nih.gov/37562520/); sibling and twin comparisons plus Mendelian randomisation (Sweden); **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** Effect may run mainly the other way: a network MR with larger datasets found a small ADHD-to-depression effect (1.09) and a larger depression-to-ADHD effect (1.76), and no causal link with anxiety.
  - Meisinger C, et al. Understanding the causal relationships of attention-deficit/hyperactivity disorder with mental disorders and suicide attempt: a network Mendelian randomisation study. BMJ Ment Health. 2023. — [DOI 10.1136/bmjment-2022-300642](https://doi.org/10.1136/bmjment-2022-300642) · [PMID 37669871](https://pubmed.ncbi.nlm.nih.gov/37669871/); network Mendelian randomisation; cited on page; checked: PubMed record

**Why they may differ:** MR estimates in the depression-to-ADHD direction are vulnerable because depression variants are weak, heterogeneous instruments and overlap with general psychopathology; ADHD-to-depression estimates are consistently positive but small across MR studies. Sibling designs address time order (ADHD diagnosed before depression) and shared family factors, but not factors that differ between siblings, so the large sibling HR measures association after family adjustment rather than a causal size. All approaches agree there is at least a modest ADHD-to-depression path.

**Next step:** Add Garcia-Argibay 2024 as the strongest triangulated evidence for an ADHD-to-depression path, and note that the reverse MR estimate (1.76) has not been replicated with sibling or time-ordered designs. Keep the page's caveat about untestable MR assumptions.

#### C05-006

**How much more common are depression and anxiety: 4-5 times or about 9 times?** · minor · method/measurement · Page reports both sides

**In dispute:** Adults with ADHD have about four to five times the odds of anxiety or depression (Hartman 2023); in Swedish records 42% against 4.7% had depression recorded (prevalence ratio about 9).

- **Position A:** Pooled large studies (surveys, claims and registers): odds ratios of 5.0 for anxiety and 4.5 for major depression.
  - Hartman CA, et al. Anxiety, mood, and substance use disorders in adult men and women with and without attention-deficit/hyperactivity disorder: a substantive and methodological overview. Neurosci Biobehav Rev. 2023. — [DOI 10.1016/j.neubiorev.2023.105209](https://doi.org/10.1016/j.neubiorev.2023.105209) · [PMID 37149075](https://pubmed.ncbi.nlm.nih.gov/37149075/); meta-analysis of studies with >10,000 participants, n = 550,748 with ADHD; cited on page; checked: PubMed record + abstract
- **Position B:** Swedish national registers: recorded depression in 42% of adults with diagnosed ADHD against 4.7% without, and anxiety 45% against 4.9%, a ratio of about 9.
  - Chen Q, et al. Common psychiatric and metabolic comorbidity of adult attention-deficit/hyperactivity disorder: a population-based cross-sectional study. PLoS One. 2018. — [DOI 10.1371/journal.pone.0204516](https://doi.org/10.1371/journal.pone.0204516) · [PMID 30256837](https://pubmed.ncbi.nlm.nih.gov/30256837/); national register, cross-sectional, n = 5.55 million (61,129 with ADHD); cited on page; checked: PubMed record

**Why they may differ:** Prevalence ratios and odds ratios are different measures (odds ratios exceed risk ratios when outcomes are common, so this would push the other way), so the gap is mainly about samples: registers count only diagnosed ADHD, which in Sweden in that era captured the most severe adults who are in frequent contact with services where depression is also recorded (surveillance bias), while surveys capture milder, undiagnosed cases. The page notes the records caveat but presents the two figures side by side in the short answer without explaining why they differ.

**Next step:** Add one sentence explaining that registry figures for diagnosed adults are higher than survey-based estimates because diagnosed adults are more severely affected and more often assessed; consider leading the short answer with the pooled 4-5 times figure and giving the Swedish absolute figures as one example.

### [Autism and ADHD: can you have both?](../05-what-often-comes-with-it/autism-and-adhd.md)

#### C05-007

**How often autistic people have ADHD** · minor · method/measurement · Page reports both sides

**In dispute:** Between about one in four and two in five autistic people have ADHD (28% in Lai 2019; 38.5% current, 40.2% lifetime in Rong 2021); adult data were not found for the ADHD-to-autism direction.

- **Position A:** Higher figure: 38.5% current and 40.2% lifetime across 63 articles with high heterogeneity.
  - Rong Y, et al. Prevalence of attention-deficit/hyperactivity disorder in individuals with autism spectrum disorder: a meta-analysis. Res Autism Spectr Disord. 2021. — [DOI 10.1016/j.rasd.2021.101759](https://doi.org/10.1016/j.rasd.2021.101759); meta-analysis, n = 63 articles; cited on page; checked: Crossref record
- **Position B:** Lower figure using confirmed clinical diagnoses: 28% across 96 studies. A 2023 meta-analysis of 340 publications (about 590,000 participants) found ADHD among the most frequent co-occurring conditions in children and adults, with prevalence differing by age group and study design (pooled figures not in the abstract).
  - Lai MC, et al. Prevalence of co-occurring mental health diagnoses in the autism population: a systematic review and meta-analysis. Lancet Psychiatry. 2019. — [DOI 10.1016/S2215-0366(19)30289-5](https://doi.org/10.1016/S2215-0366(19)30289-5) · [PMID 31447415](https://pubmed.ncbi.nlm.nih.gov/31447415/); meta-analysis, n = 96 studies; cited on page; checked: PubMed record
  - Micai M, et al. Prevalence of co-occurring conditions in children and adults with autism spectrum disorder: A systematic review and meta-analysis. Neurosci Biobehav Rev. 2023. — [DOI 10.1016/j.neubiorev.2023.105436](https://doi.org/10.1016/j.neubiorev.2023.105436) · [PMID 37913872](https://pubmed.ncbi.nlm.nih.gov/37913872/); meta-analysis with age and design subgroups, n = 340 publications, about 590,000 participants; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Rong included symptom-based and research-assessed ADHD and many clinic samples; Lai restricted to confirmed diagnoses, which undercount in older studies done under DSM-IV's exclusion rule. Clinic samples, children and people without intellectual disability tend to give higher rates.

**Next step:** Obtain Micai 2023's ADHD point-prevalence figures by age group and design from the full text; if they include adults, they fill the page's stated gap on adult data and offer a third, larger estimate to sit between 28% and 38.5%.

### [Is it ADHD, or could it be something else?](../05-what-often-comes-with-it/is-it-adhd-or-something-else.md)

#### C05-008

**PTSD and ADHD: both directions, or mainly ADHD to PTSD?** · minor · causal interpretation · Page does not mention it

**In dispute:** Trauma and PTSD overlap in both directions: PTSD about 2.9 times as common with ADHD and ADHD about 1.7 times as common with PTSD; smaller (1.6) when the comparison group had also been through trauma.

- **Position A:** Meta-analysis of 22 studies: association in both directions, smaller against trauma-exposed controls, consistent with symptom overlap and with trauma's own effects.
  - Spencer AE, et al. Examining the association between posttraumatic stress disorder and attention-deficit/hyperactivity disorder: a systematic review and meta-analysis. J Clin Psychiatry. 2016. — [DOI 10.4088/JCP.14r09479](https://doi.org/10.4088/JCP.14r09479) · [PMID 26114394](https://pubmed.ncbi.nlm.nih.gov/26114394/); meta-analysis, n = 22 studies; cited on page; checked: PubMed record
- **Position B:** Genetic and sibling evidence points mainly one way: genetic liability to ADHD was causally linked to PTSD but not the reverse, and people diagnosed with ADHD had about 2.4 times the risk of later PTSD compared with their own undiagnosed siblings.
  - Wendt FR, et al. The Relationship of Attention-Deficit/Hyperactivity Disorder With Posttraumatic Stress Disorder: A Two-Sample Mendelian Randomization and Population-Based Sibling Comparison Study. Biol Psychiatry. 2023. — [DOI 10.1016/j.biopsych.2022.08.012](https://doi.org/10.1016/j.biopsych.2022.08.012) · [PMID 36335070](https://pubmed.ncbi.nlm.nih.gov/36335070/); Mendelian randomisation plus Swedish sibling comparison; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Co-occurrence 'in both directions' describes prevalence, which can arise even if causation runs one way (ADHD raises exposure to accidents and adversity, and thus PTSD) or if trauma symptoms are mistaken for ADHD. MR tests genetic liability, not trauma-induced ADHD-like symptoms, so it cannot rule out that trauma produces ADHD-like presentations; the page's clinical point about timing relative to trauma remains valid.

**Next step:** Add a sentence that genetic and sibling evidence suggests ADHD raises the later risk of PTSD (Wendt 2023), while trauma can still produce ADHD-like symptoms, which is why timing matters in assessment.

#### C05-009

**Treating sleep apnoea: behaviour improves, measured attention may not** · minor · method/measurement · Page reports both sides

**In dispute:** In a randomised trial, adenotonsillectomy for childhood sleep apnoea improved caregiver- and teacher-rated behaviour but not formal attention or executive-function tests; this shows a sleep disorder can produce ADHD-like behaviour.

- **Position A:** Before-after and pooled studies suggest real ADHD-symptom improvement: a 2014 meta-analysis found a medium link between sleep-disordered breathing and ADHD symptoms (g 0.57) and medium symptom reductions after surgery (g 0.43 across 12 studies); a 2026 meta-analysis found moderate parent-rated behavioural and small executive-function improvement.
  - Sedky K, et al. Attention deficit hyperactivity disorder and sleep disordered breathing in pediatric populations: a meta-analysis. Sleep Med Rev. 2014. — [DOI 10.1016/j.smrv.2013.12.003](https://doi.org/10.1016/j.smrv.2013.12.003) · [PMID 24581717](https://pubmed.ncbi.nlm.nih.gov/24581717/); meta-analysis (incl. pre-post studies), n = 18 studies; 12 surgery studies (529 children); **not yet cited on page**; checked: PubMed record + abstract
  - Lee YC, et al. Neurobehavioral outcomes after adenotonsillectomy for pediatric sleep-disordered breathing: A systematic review and meta-analysis. Am J Otolaryngol. 2026. — [DOI 10.1016/j.amjoto.2026.104886](https://doi.org/10.1016/j.amjoto.2026.104886) · [PMID 42456309](https://pubmed.ncbi.nlm.nih.gov/42456309/); meta-analysis, n = 8 studies; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** In the one large randomised trial and in the 2026 pooled data, objective attention and ADHD-specific measures did not improve significantly; the behaviour gains rest on raters who knew whether the child had surgery.
  - Marcus CL, et al. A randomized trial of adenotonsillectomy for childhood sleep apnea. N Engl J Med. 2013. — [DOI 10.1056/NEJMoa1215881](https://doi.org/10.1056/NEJMoa1215881) · [PMID 23692173](https://pubmed.ncbi.nlm.nih.gov/23692173/); RCT (CHAT), n = 464; cited on page; checked: PubMed record

**Why they may differ:** Uncontrolled before-after studies overstate change through expectation and regression to the mean; in CHAT, parents and teachers were not blinded to surgery. Objective tests may be insensitive to day-to-day behaviour. The page's inference ('a sleep disorder can produce ADHD-like behaviour that improves when sleep is treated') is reasonable but rests on unblinded ratings.

**Next step:** Note that the behaviour ratings were unblinded and that pooled studies show the same pattern (behaviour improves, objective attention measures less clearly), so the trial shows sleep problems can worsen behaviour rather than proving they mimic ADHD.

### [Physical health problems and ADHD: is there a link?](../05-what-often-comes-with-it/physical-health.md)

#### C05-003

**ADHD and obesity: shared genes, cause, or both directions?** · moderate · causal interpretation · Page does not mention it

**In dispute:** Obesity is moderately more common (28.2% against 16.4% in adults); for metabolic conditions shared genetic factors explained 60-69% of the overlap; whether changing habits lowers the risk has barely been tested.

- **Position A:** Much of the overlap is shared genetic liability: the Swedish sibling-based study attributed most of the ADHD-metabolic overlap to shared genes, and the meta-analysis shows an association, not a direction.
  - Du Rietz E, et al. Mapping phenotypic and aetiological associations between ADHD and physical conditions in adulthood in Sweden: a genetically informed register study. Lancet Psychiatry. 2021. — [DOI 10.1016/S2215-0366(21)00171-1](https://doi.org/10.1016/S2215-0366(21)00171-1) · [PMID 34242595](https://pubmed.ncbi.nlm.nih.gov/34242595/); national registry with sibling-based genetic modelling, n = 4.8 million adults; cited on page; checked: PubMed record + abstract
  - Cortese S, et al. Association between ADHD and obesity: a systematic review and meta-analysis. Am J Psychiatry. 2016. — [DOI 10.1176/appi.ajp.2015.15020266](https://doi.org/10.1176/appi.ajp.2015.15020266) · [PMID 26315982](https://pubmed.ncbi.nlm.nih.gov/26315982/); meta-analysis, n = 42 studies; cited on page; checked: PubMed record
- **Position B:** Mendelian randomisation studies find causal effects in both directions: genetic liability to ADHD raises obesity-related traits, and higher BMI raises ADHD risk, with stronger effects for childhood obesity, according to a review of ADHD MR studies and two primary analyses.
  - Karhunen V, et al. The link between attention deficit hyperactivity disorder (ADHD) symptoms and obesity-related traits: genetic and prenatal explanations. Transl Psychiatry. 2021. — [DOI 10.1038/s41398-021-01584-4](https://doi.org/10.1038/s41398-021-01584-4) · [PMID 34482360](https://pubmed.ncbi.nlm.nih.gov/34482360/); bidirectional Mendelian randomisation plus birth-cohort polygenic scores, n = 2,984 (NFBC1986) plus GWAS summary data; **not yet cited on page**; checked: PubMed record + abstract
  - Chen W, et al. Mendelian randomization analyses identify bidirectional causal relationships of obesity with psychiatric disorders. J Affect Disord. 2023. — [DOI 10.1016/j.jad.2023.07.044](https://doi.org/10.1016/j.jad.2023.07.044) · [PMID 37474010](https://pubmed.ncbi.nlm.nih.gov/37474010/); two-sample Mendelian randomisation; **not yet cited on page**; checked: PubMed record + abstract
  - Riglin L, et al. Mendelian randomisation studies of Attention Deficit Hyperactivity Disorder. JCPP Adv. 2022. — [DOI 10.1002/jcv2.12117](https://doi.org/10.1002/jcv2.12117) · [PMID 37431426](https://pubmed.ncbi.nlm.nih.gov/37431426/); review of Mendelian randomisation studies; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** 'Shared genes' (sibling modelling) and 'causal effect' (MR) are not mutually exclusive: MR treats the same variants as instruments, and a variant that raises both ADHD and BMI through a common pathway (pleiotropy) can look like a causal effect. Sibling models partition overlap into genetic and environmental parts but cannot show direction. The page's framing ('shared biology, which is no one's fault') is fair, but it omits the genetic evidence that each may partly lead to the other, which bears on its point that habits and sleep may be modifiable routes.

**Next step:** Add one sentence that genetic causal-inference studies suggest effects in both directions between ADHD and higher body weight (Riglin 2022 review), with MR caveats; this supports, rather than contradicts, the page's point that weight-related pathways may be modifiable.

#### C05-004

**ADHD and cardiovascular disease in adults** · moderate · direct contradiction · Page reports both sides

**In dispute:** Reviews differ: an earlier systematic review noted one large registry study had found no link with cardiovascular disease, whereas the later Swedish sibling study found modestly raised odds for heart and circulation conditions.

- **Position A:** No clear link: an earlier systematic review of 126 mostly small studies noted a large registry study had found no association with cardiovascular disease.
  - Instanes JT, et al. Adult ADHD and comorbid somatic disease: a systematic literature review. J Atten Disord. 2018. — [DOI 10.1177/1087054716669589](https://doi.org/10.1177/1087054716669589) · [PMID 27664125](https://pubmed.ncbi.nlm.nih.gov/27664125/); systematic review, n = 126 studies; cited on page; checked: PubMed record
- **Position B:** Raised risk: in 5.4 million Swedish adults followed for about 12 years, 38.05% of those with ADHD against 23.57% without had a cardiovascular diagnosis (HR 2.05, falling to 1.65 after adjusting for metabolic, lifestyle and psychiatric factors); the sibling study also found modestly raised odds; MR studies give some evidence of causal effects on coronary artery disease and stroke.
  - Li L, et al. Attention-deficit/hyperactivity disorder as a risk factor for cardiovascular diseases: a nationwide population-based cohort study. World Psychiatry. 2022. — [DOI 10.1002/wps.21020](https://doi.org/10.1002/wps.21020) · [PMID 36073682](https://pubmed.ncbi.nlm.nih.gov/36073682/); national registry cohort, n = 5,389,519 adults; **not yet cited on page**; checked: PubMed record + abstract
  - Du Rietz E, et al. Mapping phenotypic and aetiological associations between ADHD and physical conditions in adulthood in Sweden: a genetically informed register study. Lancet Psychiatry. 2021. — [DOI 10.1016/S2215-0366(21)00171-1](https://doi.org/10.1016/S2215-0366(21)00171-1) · [PMID 34242595](https://pubmed.ncbi.nlm.nih.gov/34242595/); national registry with sibling modelling, n = 4.8 million; cited on page; checked: PubMed record + abstract
  - Riglin L, et al. Mendelian randomisation studies of Attention Deficit Hyperactivity Disorder. JCPP Adv. 2022. — [DOI 10.1002/jcv2.12117](https://doi.org/10.1002/jcv2.12117) · [PMID 37431426](https://pubmed.ncbi.nlm.nih.gov/37431426/); review of Mendelian randomisation studies; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The older null registry finding likely came from a younger cohort with few cardiovascular events; Li 2022 followed adults born 1941-83 for over a decade, with ADHD as a time-varying exposure. Long-term ADHD medication is itself linked to modestly higher cardiovascular risk (covered on the medication-safety page), so part of the association may run through treatment, and part through smoking, weight and sleep, which registries measure imperfectly.

**Next step:** Add Li 2022 as the main cardiovascular source, with its absolute figures (38.05% against 23.57% over about 12 years, all cardiovascular diagnoses) and the attenuation to HR 1.65 after adjustment; this resolves the 'reviews differ' sentence in favour of a raised risk. Update the 'absolute risks are mostly missing' bullet accordingly and link to medication-safety for the medication part.

### [How well does ADHD medication work?](../06-treatment-what-works/how-well-medication-works.md)

#### C06-001

**Certainty of methylphenidate evidence in children (Cochrane vs umbrella/network reviews)** · major · method/measurement · Page reports both sides

**In dispute:** Reviews agree on the short-term size of methylphenidate's effect in children (SMD about 0.74-0.78) but disagree on its certainty: Cochrane rates it very low, the 2025 BMJ umbrella review moderate or high.

- **Position A:** Cochrane finds a teacher-rated SMD of 0.74 but judges almost every trial at high risk of bias (unblinding through side effects, industry funding), so rates all outcomes very low certainty. Its authors defended these judgements against critics.
  - Storebø OJ, et al. Methylphenidate for children and adolescents with attention deficit hyperactivity disorder (ADHD). Cochrane Database Syst Rev. 2025 (CD009885.pub4). — [DOI 10.1002/14651858.CD009885.pub4](https://doi.org/10.1002/14651858.CD009885.pub4) · [PMID 41342306](https://pubmed.ncbi.nlm.nih.gov/41342306/); systematic review and meta-analysis (Cochrane), n = 21 trials, 1,728 participants for teacher-rated symptoms; cited on page; checked: PubMed record + abstract
  - Storebø OJ, et al. Response to "Trust, but verify" by Banaschewski et al. Z Kinder Jugendpsychiatr Psychother. 2016. — [DOI 10.1024/1422-4917/a000472](https://doi.org/10.1024/1422-4917/a000472) · [PMID 27658627](https://pubmed.ncbi.nlm.nih.gov/27658627/); reply to critique; **not yet cited on page**; checked: PubMed record
- **Position B:** Network and umbrella reviews find the same or slightly larger effect and grade it moderate to high certainty; the European ADHD Guidelines Group argued Cochrane's risk-of-bias calls were too severe and that high- and low-risk trials gave similar results.
  - Gosling CJ, et al. Benefits and harms of ADHD interventions: umbrella review and platform for shared decision making. BMJ. 2025;391:e085875. — [DOI 10.1136/bmj-2025-085875](https://doi.org/10.1136/bmj-2025-085875) · [PMID 41297970](https://pubmed.ncbi.nlm.nih.gov/41297970/); umbrella review, n = 221 treatment-comparison-outcome combinations; cited on page; checked: PubMed record
  - Cortese S, et al. Comparative efficacy and tolerability of medications for ADHD in children, adolescents, and adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2018;5(9):727-38. — [DOI 10.1016/S2215-0366(18)30269-4](https://doi.org/10.1016/S2215-0366(18)30269-4) · [PMID 30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/); network meta-analysis, n = 133 trials; cited on page; checked: PubMed record
  - Banaschewski T, et al. Methylphenidate for ADHD in children and adolescents: throwing the baby out with the bathwater. Evid Based Ment Health. 2016. — [DOI 10.1136/eb-2016-102461](https://doi.org/10.1136/eb-2016-102461) · [PMID 27935807](https://pubmed.ncbi.nlm.nih.gov/27935807/); expert commentary; cited on page; checked: PubMed record

**Why they may differ:** Both sides use GRADE, but GRADE needs judgement at the risk-of-bias step. Cochrane treats possible unblinding through side effects and industry funding as high risk and marks the whole body of evidence down; the other groups weigh the fact that high- and low-risk trials give similar results and do not mark down as far. The numbers barely differ; the confidence label does.

**Next step:** Cite the Cochrane authors' 2016 reply (PMID 27658627) so both sides are represented by primary text, and tabulate the risk-of-bias decisions of each review side by side for the same trials, including any sensitivity analysis restricted to low-risk trials in the 2025 Cochrane update.

#### C06-011

**Does medication improve quality of life in adults?** · major · direct contradiction · Page reports one side only

**In dispute:** In adults, symptom relief did not bring measurable quality-of-life gains; medicines were not efficacious on quality of life.

- **Position A:** A 2025 component network meta-analysis of 113 adult trials found medicines reduced core symptoms but were not efficacious on other outcomes such as quality of life; a withdrawal-trial meta-analysis found a quality-of-life drop after stopping only in children.
  - Ostinelli EG, et al. Comparative efficacy and acceptability of pharmacological, psychological, and neurostimulatory interventions for ADHD in adults: a systematic review and component network meta-analysis. Lancet Psychiatry. 2025;12(1):32-43. — [DOI 10.1016/S2215-0366(24)00360-2](https://doi.org/10.1016/S2215-0366(24)00360-2) · [PMID 39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/); component network meta-analysis, n = 113 trials, 14,887; cited on page; checked: PubMed record
  - Tsujii N, et al. Effect of continuing and discontinuing medications on quality of life after symptomatic remission in ADHD: a systematic review and meta-analysis. J Clin Psychiatry. 2020;81(3):19r13015. — [DOI 10.4088/JCP.19r13015](https://doi.org/10.4088/JCP.19r13015) · [PMID 32237294](https://pubmed.ncbi.nlm.nih.gov/32237294/); meta-analysis of withdrawal RCTs, n = 5 trials, 1,463; **not yet cited on page**; checked: PubMed record
- **Position B:** A 2025 meta-analysis of 17 placebo-controlled RCTs (5,388 people) found amphetamines (g 0.51), methylphenidate (0.38) and atomoxetine (0.30) improved quality of life more than placebo; for atomoxetine the effect did not differ between children and adults.
  - Bellato A, et al. Systematic review and meta-analysis: effects of pharmacological treatment for ADHD on quality of life. J Am Acad Child Adolesc Psychiatry. 2025. — [DOI 10.1016/j.jaac.2024.05.023](https://doi.org/10.1016/j.jaac.2024.05.023) · [PMID 38823477](https://pubmed.ncbi.nlm.nih.gov/38823477/); meta-analysis of RCTs, n = 17 RCTs, 5,388; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Different trial sets, quality-of-life scales and analytic models: Ostinelli's component network model across many interventions may have had few quality-of-life data points per comparison and wide intervals, while Bellato pooled placebo-controlled medication trials directly. Effects in Bellato are smaller than for symptoms and quality of life is often self-rated by participants who may guess their allocation. The abstract does not split stimulant effects by age, so the adult-specific stimulant estimate needs the full text.

**Next step:** Add Bellato 2025 and change the short answer from 'did not bring measurable quality-of-life gains' to 'evidence on quality of life is mixed: one large adult network analysis found no clear benefit, while a meta-analysis of 17 trials found small-to-moderate gains'. Extract adult-only estimates from Bellato's full text. Also update the matching sentence on 07/when-your-partner-has-adhd.md.

### [Neurofeedback, diet, supplements, exercise: do they help ADHD?](../06-treatment-what-works/lifestyle-and-other-approaches.md)

#### C06-008

**Neurofeedback: blinded null vs sustained effects at follow-up** · moderate · method/measurement · Page reports one side only

**In dispute:** Neurofeedback shows no meaningful effect when raters are blinded (SMD 0.04); trials do not support it as a stand-alone treatment.

- **Position A:** Meta-analyses separating rater blinding find essentially no effect on probably blinded ratings, with a small effect (0.21) only for standard protocols.
  - Westwood SJ, et al. Neurofeedback for ADHD: a systematic review and meta-analysis. JAMA Psychiatry. 2025;82(2):118-29. — [DOI 10.1001/jamapsychiatry.2024.3702](https://doi.org/10.1001/jamapsychiatry.2024.3702) · [PMID 39661381](https://pubmed.ncbi.nlm.nih.gov/39661381/); meta-analysis of RCTs, n = 38 trials, 2,472; cited on page; checked: PubMed record
  - Cortese S, et al. Neurofeedback for ADHD: meta-analysis of clinical and neuropsychological outcomes from randomized controlled trials. J Am Acad Child Adolesc Psychiatry. 2016;55(6):444-55. — [DOI 10.1016/j.jaac.2016.03.007](https://doi.org/10.1016/j.jaac.2016.03.007) · [PMID 27238063](https://pubmed.ncbi.nlm.nih.gov/27238063/); meta-analysis of RCTs, n = 13 trials, 520; cited on page; checked: PubMed record
- **Position B:** A meta-analysis of 10 RCTs with 2-12-month follow-up found neurofeedback's parent-rated effects held or grew (inattention SMD 0.64 to 0.80 within-group) and beat non-active controls at follow-up (0.57), while non-active control effects faded; the lead authors include neurofeedback providers.
  - Van Doren J, et al. Sustained effects of neurofeedback in ADHD: a systematic review and meta-analysis. Eur Child Adolesc Psychiatry. 2019;28(3):293-305. — [DOI 10.1007/s00787-018-1121-4](https://doi.org/10.1007/s00787-018-1121-4) · [PMID 29445867](https://pubmed.ncbi.nlm.nih.gov/29445867/); meta-analysis of RCT follow-ups, n = 10 trials, 506; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The sustained-effects review uses parent ratings (unblinded) and compares mostly against non-active controls; it does not address blinding. Its authors declare commercial neurofeedback interests. Proponents argue learning-based effects need time to show and that standard protocols matter, which Westwood partly supports (0.21). Active controls (mostly methylphenidate) still did better at post-treatment.

**Next step:** Mention the follow-up claim and why it does not overturn the blinded result (unblinded parent ratings, non-active controls, declared interests); check whether Westwood 2025 analysed follow-up time points with blinded raters.

#### C06-010

**Exercise: moderate-to-large vs small effects on core symptoms** · moderate · size of effect · Page reports one side only

**In dispute:** In children, a 2015 meta-analysis of a small number of small trials reported moderate to large effects of aerobic exercise on attention, hyperactivity and impulsivity.

- **Position A:** A 2015 meta-analysis and recent executive-function meta-analyses report moderate effects (for example inhibitory control g about 0.60 and working memory 0.51 in 16 RCTs of school-aged children).
  - Cerrillo-Urbina AJ, et al. The effects of physical exercise in children with ADHD: a systematic review and meta-analysis of randomized control trials. Child Care Health Dev. 2015;41(6):779-88. — [DOI 10.1111/cch.12255](https://doi.org/10.1111/cch.12255) · [PMID 25988743](https://pubmed.ncbi.nlm.nih.gov/25988743/); meta-analysis of RCTs, n = small number of small trials; cited on page; checked: PubMed record
  - Liu R, et al. Effects of exercise interventions on executive function in school-aged children with ADHD: a systematic review and meta-analysis. BMC Public Health. 2025. — [DOI 10.1186/s12889-025-24335-2](https://doi.org/10.1186/s12889-025-24335-2) · [PMID 41034843](https://pubmed.ncbi.nlm.nih.gov/41034843/); meta-analysis of RCTs, n = 16 RCTs; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** A 2022 meta-analysis restricted to RCTs in clinically diagnosed children using valid ADHD rating scales found only a small effect of regular moderate-to-vigorous activity on total core symptoms (g -0.33, 11 trials, with a confidence interval reaching -0.02).
  - Seiffer B, et al. The efficacy of physical activity for children with ADHD: a meta-analysis of randomized controlled trials. J Atten Disord. 2022;26(5):656-73. — [DOI 10.1177/10870547211017982](https://doi.org/10.1177/10870547211017982) · [PMID 34041952](https://pubmed.ncbi.nlm.nih.gov/34041952/); meta-analysis of RCTs, n = 11 trials; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Executive-function tests are not ADHD symptoms, and the 2025 review notes its effects depend on test paradigm and scoring direction. Symptom ratings in exercise trials are rarely blinded. Stricter inclusion (clinical diagnosis, validated symptom scales) gives smaller effects.

**Next step:** Replace or supplement the 2015 'moderate to large' headline with the 2022 RCT-only symptom estimate (small, imprecise), separate test-based executive-function outcomes from symptom outcomes, and check whether any exercise meta-analysis split blinded and unblinded ratings.

#### C06-009

**Omega-3 supplements: small benefit vs no difference** · minor · size of effect · Page reports both sides

**In dispute:** Omega-3 and other fatty acids have small or no effect; a 2023 Cochrane review found high-certainty evidence of no difference on parent-rated symptoms.

- **Position A:** Earlier meta-analyses found small-to-moderate benefits in children: SMD 0.31 (10 trials) and g 0.38 on clinical symptoms (7 RCTs, 534 youths), plus larger effects on attention tests in 3 RCTs; children with ADHD had lower blood omega-3 levels.
  - Bloch MH, et al. Omega-3 fatty acid supplementation for the treatment of children with ADHD symptomatology: systematic review and meta-analysis. J Am Acad Child Adolesc Psychiatry. 2011;50(10):991-1000. — [DOI 10.1016/j.jaac.2011.06.008](https://doi.org/10.1016/j.jaac.2011.06.008) · [PMID 21961774](https://pubmed.ncbi.nlm.nih.gov/21961774/); meta-analysis of RCTs, n = 10 trials, 699; cited on page; checked: PubMed record
  - Chang JP, et al. Omega-3 polyunsaturated fatty acids in youths with ADHD: a systematic review and meta-analysis of clinical trials and biological studies. Neuropsychopharmacology. 2018. — [DOI 10.1038/npp.2017.160](https://doi.org/10.1038/npp.2017.160) · [PMID 28741625](https://pubmed.ncbi.nlm.nih.gov/28741625/); meta-analysis of RCTs and case-control studies, n = 7 RCTs, 534; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** The 2023 Cochrane review of 37 trials found high-certainty evidence of no difference on parent-rated total symptoms over the medium term (SMD -0.08); probably blinded ratings in 2013 gave only 0.16.
  - Gillies D, et al. Polyunsaturated fatty acids (PUFA) for ADHD in children and adolescents. Cochrane Database Syst Rev. 2023;CD007986.pub3. — [DOI 10.1002/14651858.CD007986.pub3](https://doi.org/10.1002/14651858.CD007986.pub3) · [PMID 37058600](https://pubmed.ncbi.nlm.nih.gov/37058600/); systematic review and meta-analysis (Cochrane), n = 37 trials; cited on page; checked: PubMed record
  - Sonuga-Barke EJS, et al. Nonpharmacological interventions for ADHD: systematic review and meta-analyses of RCTs of dietary and psychological treatments. Am J Psychiatry. 2013;170(3):275-89. — [DOI 10.1176/appi.ajp.2012.12070991](https://doi.org/10.1176/appi.ajp.2012.12070991) · [PMID 23360949](https://pubmed.ncbi.nlm.nih.gov/23360949/); meta-analysis of RCTs, n = 54 trials; cited on page; checked: PubMed record

**Why they may differ:** Smaller, earlier pools of trials give larger effects; the Cochrane review has far more trials and grades risk of bias. Chang 2018 combines monotherapy trials and mixes clinical and cognitive outcomes; possible subgroup effects (children with low baseline omega-3, higher EPA doses) may be diluted in whole-population averages.

**Next step:** Optionally cite Chang 2018 as the strongest positive meta-analysis and state why the larger Cochrane review is weighted more; check whether any trial stratified by baseline omega-3 level.

### [Is ADHD medication safe? Heart, growth, psychosis and misuse](../06-treatment-what-works/medication-safety.md)

#### C06-002

**How often psychosis or mania follows stimulant treatment** · major · size of effect · Page reports one side only

**In dispute:** Psychosis is rare: about 1 in 660 young people starting a stimulant (0.10% methylphenidate, 0.21% amphetamine) developed new psychosis treated with an antipsychotic.

- **Position A:** US insurance and hospital case-control data put new psychosis at about 1 to 2 per 1,000 starters, higher with amphetamine and with high amphetamine doses; methylphenidate was not linked in the case-control study.
  - Moran LV, et al. Psychosis with methylphenidate or amphetamine in patients with ADHD. N Engl J Med. 2019;380:1128-38. — [DOI 10.1056/NEJMoa1813751](https://doi.org/10.1056/NEJMoa1813751) · [PMID 30893533](https://pubmed.ncbi.nlm.nih.gov/30893533/); cohort (two US insurance databases), n = 221,846; cited on page; checked: PubMed record
  - Moran LV, et al. Risk of incident psychosis and mania with prescription amphetamines. Am J Psychiatry. 2024;181(10):901-9. — [DOI 10.1176/appi.ajp.20230329](https://doi.org/10.1176/appi.ajp.20230329) · [PMID 39262211](https://pubmed.ncbi.nlm.nih.gov/39262211/); case-control (single hospital), n = 1,374 cases, 2,748 controls; cited on page; checked: PubMed record
- **Position B:** A 2025 meta-analysis of 16 studies (391,043 people) found 2.3% of stimulant-treated people developed a psychotic disorder, 2.8% psychotic symptoms and 3.7% bipolar disorder, about ten times the page's headline rate, with amphetamines worse than methylphenidate (OR 1.57).
  - Salazar de Pablo G, et al. Occurrence of psychosis and bipolar disorder in individuals with ADHD treated with stimulants: a systematic review and meta-analysis. JAMA Psychiatry. 2025. — [DOI 10.1001/jamapsychiatry.2025.2311](https://doi.org/10.1001/jamapsychiatry.2025.2311) · [PMID 40900605](https://pubmed.ncbi.nlm.nih.gov/40900605/); systematic review and meta-analysis (proportions), n = 16 studies, 391,043; **not yet cited on page**; checked: PubMed record + abstract
- **Position C:** Within-person register studies find no rise in psychotic events after starting methylphenidate (IRR 1.04, even in people with past psychosis), and no rise in mania when methylphenidate is taken with a mood stabiliser, though mania rose sharply with methylphenidate alone in bipolar disorder (HR 6.7).
  - Hollis C, et al. Methylphenidate and the risk of psychosis in adolescents and young adults: a population-based cohort study. Lancet Psychiatry. 2019. — [DOI 10.1016/S2215-0366(19)30189-0](https://doi.org/10.1016/S2215-0366(19)30189-0) · [PMID 31221557](https://pubmed.ncbi.nlm.nih.gov/31221557/); registry, within-individual, n = 23,898; **not yet cited on page**; checked: PubMed record + abstract
  - Viktorin A, et al. The risk of treatment-emergent mania with methylphenidate in bipolar disorder. Am J Psychiatry. 2017. — [DOI 10.1176/appi.ajp.2016.16040467](https://doi.org/10.1176/appi.ajp.2016.16040467) · [PMID 27690517](https://pubmed.ncbi.nlm.nih.gov/27690517/); registry, within-individual; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** They measure different things. The US cohort counts new psychosis serious enough for antipsychotic treatment in a fixed window; the meta-analysis pools any psychotic symptoms over long and variable follow-up, has no unexposed comparison group, and is very heterogeneous (I2 above 95%), with higher rates in small, North American and long-follow-up studies. Within-person designs ask whether risk rises after starting compared with before, which removes background risk that people with ADHD already carry.

**Next step:** Add the 2025 meta-analysis and the Swedish within-person studies, separate 'how many treated people ever develop psychosis' (prevalence, no comparator) from 'does starting medication raise risk' (comparative), and state that the 1-in-660 figure is a short-window incidence in US 13-25-year-olds. Mention the bipolar/mood-stabiliser finding as a reported study result, without advice.

#### C06-003

**Long-term cardiovascular risk: registry signal vs pooled observational studies** · moderate · size of effect · Page reports one side only

**In dispute:** Long-term use is linked to modestly higher odds of cardiovascular disease (about 4% per year of use; hypertension and arterial disease clearest).

- **Position A:** A Swedish nested case-control study found cumulative use linked to higher odds of cardiovascular disease, mainly hypertension and arterial disease, and trials show small average rises in blood pressure and pulse.
  - Zhang L, et al. ADHD medications and long-term risk of cardiovascular diseases. JAMA Psychiatry. 2024;81(2):178-87. — [DOI 10.1001/jamapsychiatry.2023.4294](https://doi.org/10.1001/jamapsychiatry.2023.4294) · [PMID 37991787](https://pubmed.ncbi.nlm.nih.gov/37991787/); registry, nested case-control, n = 278,027 cohort; 10,388 cases; cited on page; checked: PubMed record
  - Farhat LC, et al. Comparative cardiovascular safety of medications for ADHD in children, adolescents, and adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2025;12(5):355-65. — [DOI 10.1016/S2215-0366(25)00062-8](https://doi.org/10.1016/S2215-0366(25)00062-8) · [PMID 40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/); network meta-analysis of RCTs, n = 102 trials, >22,700; cited on page; checked: PubMed record
- **Position B:** A 2022 meta-analysis of 19 observational studies (3.9 million people) by the same research group found no statistically significant link between ADHD medication and any cardiovascular disease in children (RR 1.18), younger adults (1.04) or older adults (1.59), while saying a modest rise, especially in arrhythmia or cardiac arrest, could not be ruled out.
  - Zhang L, et al. Risk of cardiovascular diseases associated with medications used in ADHD: a systematic review and meta-analysis. JAMA Netw Open. 2022. — [DOI 10.1001/jamanetworkopen.2022.43597](https://doi.org/10.1001/jamanetworkopen.2022.43597) · [PMID 36416824](https://pubmed.ncbi.nlm.nih.gov/36416824/); meta-analysis of observational studies, n = 19 studies, 3,931,532; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The meta-analysis pools mostly short follow-up studies (median 1.5 years) with wide, heterogeneous estimates, so it has little power to see a slow, dose-accumulating effect; the 2024 study looks specifically at cumulative years of use over up to 14 years. The two are not strictly contradictory (no significant pooled effect vs a small duration-dependent effect), but they lead to different headlines. Both are observational and exposed to confounding by smoking, weight and stress.

**Next step:** Add the 2022 meta-analysis and explain that 'no significant association over short follow-up' and 'small rise with many years of use' can both be true. Look for absolute risk differences by duration in the 2024 paper's full text or supplement.

#### C06-006

**Growth: how much adult height difference, if any** · moderate · size of effect · Page reports both sides

**In dispute:** One follow-up linked consistent childhood use with about 2.5 cm less adult height; another found no difference.

- **Position A:** MTA follow-up reports consistent users about 2.4-2.6 cm shorter in young adulthood; a later MTA growth-trajectory analysis put the gap at about 4.1 cm vs the negligibly medicated subgroup (and 3.3 cm vs non-ADHD classmates), with higher weight and BMI in adulthood.
  - Swanson JM, et al. Young adult outcomes in the follow-up of the multimodal treatment study of ADHD. J Child Psychol Psychiatry. 2017;58(6):663-78. — [DOI 10.1111/jcpp.12684](https://doi.org/10.1111/jcpp.12684) · [PMID 28295312](https://pubmed.ncbi.nlm.nih.gov/28295312/); observational follow-up of RCT cohort, n = MTA cohort (579 randomised); cited on page; checked: PubMed record
  - Greenhill LL, et al. Trajectories of growth associated with long-term stimulant medication in the Multimodal Treatment Study of ADHD. J Am Acad Child Adolesc Psychiatry. 2020. — [DOI 10.1016/j.jaac.2019.06.019](https://doi.org/10.1016/j.jaac.2019.06.019) · [PMID 31421233](https://pubmed.ncbi.nlm.nih.gov/31421233/); observational follow-up of RCT cohort, n = MTA cohort; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** A US birth cohort found neither ADHD nor stimulant treatment linked to final adult height; a meta-analysis found small height deficits (SMD 0.27) concentrated in the first two years, of possibly minimal clinical impact.
  - Harstad EB, et al. ADHD, stimulant treatment, and growth: a longitudinal study. Pediatrics. 2014;134(4):e935-44. — [DOI 10.1542/peds.2014-0428](https://doi.org/10.1542/peds.2014-0428) · [PMID 25180281](https://pubmed.ncbi.nlm.nih.gov/25180281/); population birth cohort, n = 340 ADHD, 680 controls; cited on page; checked: PubMed record
  - Carucci S, et al. Long term methylphenidate exposure and growth in children and adolescents with ADHD. Neurosci Biobehav Rev. 2021;120:509-25. — [DOI 10.1016/j.neubiorev.2020.09.031](https://doi.org/10.1016/j.neubiorev.2020.09.031) · [PMID 33080250](https://pubmed.ncbi.nlm.nih.gov/33080250/); meta-analysis of observational studies, n = 18 studies, 4,868; cited on page; checked: PubMed record

**Why they may differ:** MTA subgroups were self-selected after the trial (families chose whether to continue), so consistent users may differ in ways linked to growth; the 2020 analysis uses the extreme comparison (consistent vs negligible). The Rochester cohort had adult height for only a subset and more varied, often lower, exposure. Dose, duration and continuity differ across studies.

**Next step:** Add the 2020 MTA trajectory paper so readers see that the same cohort's estimate ranges from about 2.5 to 4 cm depending on comparison group; check the full text for whether the authors treat it as hypothesis-generating, and keep children-and-medication.md consistent with the home figure.

### [Pregnancy, breastfeeding and ADHD medication: is it safe?](../06-treatment-what-works/pregnancy-and-breastfeeding.md)

#### C06-007

**Modafinil in pregnancy and birth defects** · moderate · direct contradiction · Page reports one side only

**In dispute:** A 2025 systematic review singled out modafinil (sometimes used off-label for ADHD) as significantly increasing the risk of birth defects.

- **Position A:** A 2025 systematic review and a Danish register study reported more major malformations after first-trimester modafinil exposure.
  - Tai S, et al. Maternal and offspring outcomes associated with prescribed ADHD medication in pregnancy: a systematic review. Arch Womens Ment Health. 2025;28(6):1425-46. — [DOI 10.1007/s00737-025-01621-x](https://doi.org/10.1007/s00737-025-01621-x) · [PMID 41083615](https://pubmed.ncbi.nlm.nih.gov/41083615/); systematic review (no pooling), n = 12 cohort studies; cited on page; checked: PubMed record
  - Damkier P, Broe A. First-trimester pregnancy exposure to modafinil and risk of congenital malformations. JAMA. 2020;323(4):374-6. — [DOI 10.1001/jama.2019.20008](https://doi.org/10.1001/jama.2019.20008) · [PMID 31990303](https://pubmed.ncbi.nlm.nih.gov/31990303/); registry (research letter); **not yet cited on page**; checked: PubMed record (research letter, no abstract)
- **Position B:** A Swedish-Norwegian register study published later the same year examined malformation incidence after early-pregnancy modafinil exposure and did not replicate a clear increase (figures corrected by a 2021 erratum).
  - Cesta CE, et al. Incidence of malformations after early pregnancy exposure to modafinil in Sweden and Norway. JAMA. 2020;324(9):895-7. Erratum JAMA 2021;325(1):90. — [DOI 10.1001/jama.2020.9840](https://doi.org/10.1001/jama.2020.9840) · [PMID 32870289](https://pubmed.ncbi.nlm.nih.gov/32870289/); registry (research letter); **not yet cited on page**; checked: PubMed record (research letter, no abstract)

**Why they may differ:** Both studies have very few exposed pregnancies, so a handful of cases moves the estimate a lot; modafinil is mostly prescribed for sleep disorders, so the exposed women differ from women taking ADHD stimulants. The Nordic letter's direction is recalled from the literature and needs confirming from its full text and erratum.

**Next step:** Read both JAMA letters and the 2021 erratum in full, record exposed counts and malformation rates, and report the modafinil signal as small-sample and not consistently replicated if confirmed. Note that modafinil is not an ADHD-licensed medicine in most places.

#### C06-013

**Methylphenidate in early pregnancy and heart defects** · minor · size of effect · Page reports both sides

**In dispute:** No overall rise in birth defects, with a possible small increase in heart defects with methylphenidate (RR about 1.28-1.33).

- **Position A:** A US-Nordic cohort (pooled RR 1.28, 1.00-1.64) and a 2026 meta-analysis of 25 studies (adjusted RR 1.33, 1.01-1.74) find a small, borderline rise in heart defects with methylphenidate but not amphetamines.
  - Huybrechts KF, et al. Association between methylphenidate and amphetamine use in pregnancy and risk of congenital malformations. JAMA Psychiatry. 2018;75(2):167-75. — [DOI 10.1001/jamapsychiatry.2017.3644](https://doi.org/10.1001/jamapsychiatry.2017.3644) · [PMID 29238795](https://pubmed.ncbi.nlm.nih.gov/29238795/); cohort (US Medicaid + Nordic registers), n = 1.8 million + 2.6 million pregnancies; cited on page; checked: PubMed record
  - Komargodski R, et al. Pregnancy and offspring outcomes after prenatal stimulant or atomoxetine exposure: a systematic review and meta-analysis. Am J Obstet Gynecol MFM. 2026;8:102165. — [DOI 10.1016/j.ajogmf.2026.102165](https://doi.org/10.1016/j.ajogmf.2026.102165) · [PMID 42887725](https://pubmed.ncbi.nlm.nih.gov/42887725/); meta-analysis of observational studies, n = 25 studies; cited on page; checked: PubMed record
- **Position B:** A 2024 meta-analysis of 10 studies (about 16.6 million pregnancies) found no significant link between methylphenidate or atomoxetine and congenital anomalies (corrected April 2025, conclusions unchanged).
  - di Giacomo E, et al. Methylphenidate and atomoxetine in pregnancy and possible adverse fetal outcomes: a systematic review and meta-analysis. JAMA Netw Open. 2024;7(11):e2443648. — [DOI 10.1001/jamanetworkopen.2024.43648](https://doi.org/10.1001/jamanetworkopen.2024.43648); meta-analysis of observational studies, n = 10 studies; cited on page; checked: Crossref record

**Why they may differ:** Estimates sit at the edge of statistical significance, so different study sets and whether heart defects are analysed separately from all anomalies tip the conclusion either way; the studies overlap heavily, so they are not independent confirmations. Confounding by maternal conditions remains possible.

**Next step:** Obtain the corrected di Giacomo estimates and check whether it analysed cardiac defects separately; note study overlap between the meta-analyses.

### [Stopping ADHD medication: do benefits fade, and is it for life?](../06-treatment-what-works/staying-on-or-stopping-medication.md)

#### C06-012

**Long-term benefit: withdrawal trials vs naturalistic MTA follow-up** · major · causal interpretation · Page reports both sides

**In dispute:** After two years methylphenidate still helped children on average (40% vs 16% worsened on placebo), while in the MTA follow-up early differences faded and extended use was not linked to fewer adult symptoms.

- **Position A:** Randomised discontinuation trials show more worsening after switching to placebo in children treated for over two years and in adults stable on lisdexamfetamine (75% vs 9% relapse).
  - Matthijssen AM, et al. Continued benefits of methylphenidate in ADHD after 2 years in clinical practice: a randomized placebo-controlled discontinuation study. Am J Psychiatry. 2019;176(9):754-62. — [DOI 10.1176/appi.ajp.2019.18111296](https://doi.org/10.1176/appi.ajp.2019.18111296) · [PMID 31109200](https://pubmed.ncbi.nlm.nih.gov/31109200/); RCT (discontinuation), n = 94; cited on page; checked: PubMed record
  - Brams M, et al. Maintenance of efficacy of lisdexamfetamine dimesylate in adults with ADHD: randomized withdrawal design. J Clin Psychiatry. 2012;73(7):977-83. — [DOI 10.4088/JCP.11m07430](https://doi.org/10.4088/JCP.11m07430) · [PMID 22780921](https://pubmed.ncbi.nlm.nih.gov/22780921/); RCT (randomised withdrawal, industry-funded), n = 116; cited on page; checked: PubMed record
- **Position B:** In the MTA, original group differences were gone by 3 years; by 8 years medication in the previous year was not linked to better functioning, and at 16 years consistent use was linked to shorter height but not fewer symptoms.
  - Molina BSG, et al. The MTA at 8 years: prospective follow-up of children treated for combined-type ADHD in a multisite study. J Am Acad Child Adolesc Psychiatry. 2009;48(5):484-500. — [DOI 10.1097/CHI.0b013e31819c23d0](https://doi.org/10.1097/CHI.0b013e31819c23d0) · [PMID 19318991](https://pubmed.ncbi.nlm.nih.gov/19318991/); observational follow-up of RCT cohort, n = about three-quarters of 579; cited on page; checked: PubMed record
  - Swanson JM, et al. Young adult outcomes in the follow-up of the multimodal treatment study of ADHD. J Child Psychol Psychiatry. 2017;58(6):663-78. — [DOI 10.1111/jcpp.12684](https://doi.org/10.1111/jcpp.12684) · [PMID 28295312](https://pubmed.ncbi.nlm.nih.gov/28295312/); observational follow-up of RCT cohort, n = MTA cohort; cited on page; checked: PubMed record

**Why they may differ:** Withdrawal trials enrol people who already respond and tolerate the drug (enriched), run for weeks, and can mistake rebound or unblinding for relapse. The MTA follow-up is non-randomised after 14 months, so families of more impaired children may have kept medicating (confounding by indication), which hides benefit. They answer different questions: 'does it still work for current responders now' vs 'does a childhood treatment strategy change the adult course'.

**Next step:** Keep both, and add a one-line explanation that the designs answer different questions; consider adding the 2025 target-trial emulations (Zhang 2025, Li 2024) as a third, intermediate design for longer-term outcomes.

### [Therapy, coaching and skills training: do they work for ADHD?](../06-treatment-what-works/therapy-and-skills.md)

#### C06-014

**Adult CBT: moderate-certainty benefit vs clinician-only effect** · moderate · method/measurement · Page reports both sides

**In dispute:** CBT has the best evidence among talking treatments for adults, with moderate-certainty short-term benefit against waiting lists; in a 2025 analysis it beat controls only on clinician ratings.

- **Position A:** Cochrane found CBT reduced self-reported symptoms vs waiting list (SMD 0.84, moderate certainty); the 2025 BMJ umbrella review rates adult CBT at least moderate certainty; a 250-student RCT of a CBT-plus-mentoring programme found medium-to-large self-reported improvements.
  - Lopez PL, et al. Cognitive-behavioural interventions for ADHD in adults. Cochrane Database Syst Rev. 2018;CD010840. — [DOI 10.1002/14651858.CD010840.pub2](https://doi.org/10.1002/14651858.CD010840.pub2) · [PMID 29566425](https://pubmed.ncbi.nlm.nih.gov/29566425/); systematic review and meta-analysis (Cochrane), n = 14 trials, about 700; cited on page; checked: PubMed record
  - Gosling CJ, et al. Benefits and harms of ADHD interventions: umbrella review and platform for shared decision making. BMJ. 2025;391:e085875. — [DOI 10.1136/bmj-2025-085875](https://doi.org/10.1136/bmj-2025-085875) · [PMID 41297970](https://pubmed.ncbi.nlm.nih.gov/41297970/); umbrella review; cited on page; checked: PubMed record
  - Anastopoulos AD, et al. A randomized controlled trial examining CBT for college students with ADHD. J Consult Clin Psychol. 2021. — [DOI 10.1037/ccp0000553](https://doi.org/10.1037/ccp0000553) · [PMID 33507774](https://pubmed.ncbi.nlm.nih.gov/33507774/); RCT (delayed-treatment control), n = 250; **not yet cited on page**; checked: PubMed record + abstract
- **Position B:** A 2025 component network meta-analysis found CBT (SMD about 0.76) beat controls only on clinician ratings, which were often unblinded, not on adults' own ratings.
  - Ostinelli EG, et al. Comparative efficacy and acceptability of pharmacological, psychological, and neurostimulatory interventions for ADHD in adults. Lancet Psychiatry. 2025;12(1):32-43. — [DOI 10.1016/S2215-0366(24)00360-2](https://doi.org/10.1016/S2215-0366(24)00360-2) · [PMID 39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/); component network meta-analysis, n = 113 trials; cited on page; checked: PubMed record

**Why they may differ:** Self-reports against a waiting list (Cochrane) are generous because waiting can worsen scores; the network analysis compares against a range of controls and finds self-rated effects do not separate. Neither rater is blinded in a meaningful way for therapy. The two disagree on which rater shows the effect, which is itself a sign that expectation and comparator choice drive part of it.

**Next step:** Point out explicitly that Cochrane's benefit was self-rated while Ostinelli found self-ratings did not separate, and look in Ostinelli's supplement for CBT-vs-waitlist self-rated estimates to see whether comparator explains the gap.

### [Real-life outcomes on ADHD medication: what do registries show?](../06-treatment-what-works/what-registries-show.md)

#### C06-004

**Size of registry benefits: within-person designs vs target-trial emulation** · major · size of effect · Page does not mention it

**In dispute:** During medicated periods the same people had roughly a third fewer criminal convictions, crash-related emergency visits and substance-related emergencies; injuries were also less common.

- **Position A:** Within-person register and claims studies find reductions of about 30-40% in convictions, crash emergencies and substance-related emergencies during medicated periods, and a protective effect on injuries in self-controlled studies.
  - Lichtenstein P, et al. Medication for attention deficit-hyperactivity disorder and criminality. N Engl J Med. 2012;367:2006-14. — [DOI 10.1056/NEJMoa1203241](https://doi.org/10.1056/NEJMoa1203241) · [PMID 23171097](https://pubmed.ncbi.nlm.nih.gov/23171097/); registry, within-individual, n = 25,656; cited on page; checked: PubMed record
  - Chang Z, et al. Association between medication use for ADHD and risk of motor vehicle crashes. JAMA Psychiatry. 2017;74(6):597-603. — [DOI 10.1001/jamapsychiatry.2017.0659](https://doi.org/10.1001/jamapsychiatry.2017.0659) · [PMID 28492937](https://pubmed.ncbi.nlm.nih.gov/28492937/); claims, within-individual, n = 2,319,450; cited on page; checked: PubMed record
  - Quinn PD, et al. ADHD medication and substance-related problems. Am J Psychiatry. 2017;174(9):877-85. — [DOI 10.1176/appi.ajp.2017.16060686](https://doi.org/10.1176/appi.ajp.2017.16060686) · [PMID 28659039](https://pubmed.ncbi.nlm.nih.gov/28659039/); claims, within-individual, n = about 3 million; cited on page; checked: PubMed record
- **Position B:** A 2025 Swedish target-trial emulation (148,581 people) comparing starting vs not starting medication found smaller first-event reductions: suicidal behaviour 17%, substance misuse 15%, transport accidents 12%, criminality 13%, and no clear reduction in accidental injuries (IRR 0.98). It also reports absolute rates, e.g. criminality 65.1 vs 76.1 per 1,000 person-years.
  - Zhang L, et al. ADHD drug treatment and risk of suicidal behaviours, substance misuse, accidental injuries, transport accidents, and criminality: emulation of target trials. BMJ. 2025. — [DOI 10.1136/bmj-2024-083658](https://doi.org/10.1136/bmj-2024-083658) · [PMID 40803836](https://pubmed.ncbi.nlm.nih.gov/40803836/); registry, target trial emulation, n = 148,581; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Within-person designs compare on- and off-medication months, so time-varying factors (crises before starting, stopping during chaotic periods) can enlarge the apparent benefit; they also answer a different question (being on vs off at a given time). Target-trial emulation compares people who start with similar people who do not, over a fixed period, using an intention-to-treat style analysis that dilutes effects when people stop. The newer design suggests the same direction with smaller effects and, for first injuries, no clear effect.

**Next step:** Add the 2025 target-trial emulation with its absolute rates per 1,000 person-years, which fills the page's stated gap on absolute numbers; soften 'injuries were also less common' to note that the newest design found no clear reduction in first injuries (recurrent injuries fell slightly, IRR 0.96).

#### C06-015

**Suicidal thoughts: atomoxetine trial signal vs registry reassurance** · moderate · population/age · Page does not mention it

**In dispute:** Suicidal behaviour was not higher during treatment; within-person rates were slightly lower (HR 0.89 overall, 0.81 for stimulants).

- **Position A:** Swedish and US within-person studies find suicide-related events or attempts no higher, and somewhat lower, during medicated periods; a Hong Kong study shows risk already raised before methylphenidate began.
  - Chen Q, et al. Drug treatment for ADHD and suicidal behaviour: register based study. BMJ. 2014;348:g3769. — [DOI 10.1136/bmj.g3769](https://doi.org/10.1136/bmj.g3769) · [PMID 24942388](https://pubmed.ncbi.nlm.nih.gov/24942388/); registry, within-individual, n = 37,936; cited on page; checked: PubMed record
  - Chang Z, et al. Medication for ADHD and risk for suicide attempts. Biol Psychiatry. 2020;88(6):452-8. — [DOI 10.1016/j.biopsych.2019.12.003](https://doi.org/10.1016/j.biopsych.2019.12.003) · [PMID 31987492](https://pubmed.ncbi.nlm.nih.gov/31987492/); claims, within-individual; cited on page; checked: PubMed record
- **Position B:** Pooled placebo-controlled atomoxetine trials found suicidal ideation in 0.37% of children on atomoxetine vs 0% on placebo (5/1,357 vs 0/851; risk difference significant, number needed to harm 227), the basis of regulatory warnings; a later, larger pooled dataset found the paediatric difference no longer significant (0.37% vs 0.07%) and none in adults.
  - Bangs ME, et al. Meta-analysis of suicide-related behavior events in patients treated with atomoxetine. J Am Acad Child Adolesc Psychiatry. 2008. — [DOI 10.1097/chi.0b013e31815d88b2](https://doi.org/10.1097/chi.0b013e31815d88b2) · [PMID 18176331](https://pubmed.ncbi.nlm.nih.gov/18176331/); pooled analysis of RCTs (manufacturer), n = 2,208 children; **not yet cited on page**; checked: PubMed record + abstract
  - Bangs ME, et al. Meta-analysis of suicide-related behavior or ideation in child, adolescent, and adult patients treated with atomoxetine. J Child Adolesc Psychopharmacol. 2014. — [DOI 10.1089/cap.2014.0005](https://doi.org/10.1089/cap.2014.0005) · [PMID 25019647](https://pubmed.ncbi.nlm.nih.gov/25019647/); pooled analysis of RCTs (manufacturer); **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Trials capture rare, mostly ideation-level events reported spontaneously in children over weeks; registries capture recorded suicide attempts and are dominated by stimulant use, so a non-stimulant-specific signal could be hidden in the overall estimate. Both trial analyses are manufacturer-led, and their sizes are tiny in absolute terms.

**Next step:** Add a sentence (following safe-messaging rules) that atomoxetine carries a trial-based warning about suicidal thoughts in young people, with the absolute figures, and check whether Chen 2014 reported a non-stimulant estimate separately.

#### C06-005

**Mortality and medication: absolute figures now available** · minor · size of effect · Page does not mention it

**In dispute:** People taking medication had a lower death rate, but the evidence is thin; the medication estimate was seen only in press coverage and absolute numbers are on another page.

- **Position A:** A 2026 meta-analysis found a lower death rate with medication, but the estimate rests on three observational studies and cannot show causation.
  - Corrigan L, et al. Mortality among people with ADHD: a systematic review and meta-analysis. JAMA Netw Open. 2026;9(10):e2639448. — [DOI 10.1001/jamanetworkopen.2026.39448](https://doi.org/10.1001/jamanetworkopen.2026.39448) · [PMID 42895743](https://pubmed.ncbi.nlm.nih.gov/42895743/); meta-analysis of observational studies, n = 19 studies (3 for medication); cited on page; checked: PubMed record
- **Position B:** A Swedish target-trial emulation found starting medication linked to lower 2-year all-cause mortality (39.1 vs 48.1 per 10,000; HR 0.79), driven by unnatural causes (25.9 vs 33.3 per 10,000), with no clear difference in natural-cause deaths.
  - Li L, et al. ADHD pharmacotherapy and mortality in individuals with ADHD. JAMA. 2024. — [DOI 10.1001/jama.2024.0851](https://doi.org/10.1001/jama.2024.0851) · [PMID 38470385](https://pubmed.ncbi.nlm.nih.gov/38470385/); registry, target trial emulation, n = 148,578; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Not a contradiction in direction: the page leans on a meta-analysis whose medication estimate it could not confirm, while a single large emulated trial gives confirmed relative and absolute figures. The disagreement is about how thin the evidence is; the emulation still cannot exclude unmeasured confounding.

**Next step:** Cite Li 2024 on this page (it is already cited on 04/the-hard-statistics-in-context.md) for confirmed absolute risk differences, and keep the caveat that only unnatural-cause deaths differed.

### [Parent training and school support for ADHD: do they help?](../07-family-work-and-other-people/parenting-and-what-helps.md)

#### C07-001

**Parent training and children's core ADHD symptoms** · moderate · method/measurement · Page reports one side only

**In dispute:** On blinded ratings, parent training improves parenting and slightly reduces behaviour problems; effects on core ADHD symptoms shrink to little or nothing.

- **Position A:** On probably blinded measures, behavioural interventions show no significant effect on core ADHD symptoms, though parenting and conduct effects hold (SMD 0.63, 0.43, 0.31); in preschoolers only negative parenting held on independent assessment.
  - Sonuga-Barke EJS, et al. Nonpharmacological interventions for ADHD. Am J Psychiatry. 2013;170(3):275-89. — [DOI 10.1176/appi.ajp.2012.12070991](https://doi.org/10.1176/appi.ajp.2012.12070991) · [PMID 23360949](https://pubmed.ncbi.nlm.nih.gov/23360949/); meta-analysis of RCTs, n = 54 trials; cited on page; checked: PubMed record
  - Daley D, et al. Behavioral interventions in ADHD: a meta-analysis of randomized controlled trials across multiple outcome domains. J Am Acad Child Adolesc Psychiatry. 2014;53(8):835-47. — [DOI 10.1016/j.jaac.2014.05.013](https://doi.org/10.1016/j.jaac.2014.05.013) · [PMID 25062591](https://pubmed.ncbi.nlm.nih.gov/25062591/); meta-analysis of RCTs; cited on page; checked: PubMed record
- **Position B:** Newer syntheses find small-to-moderate between-group effects on ADHD symptoms sustained about 5 months after parent training (27 RCTs), robust parental-outcome effects on both blinded and unblinded measures, and, in an individual-participant analysis of 19 RCTs (1,720 children), that improvements in parenting go together with improvements in children's ADHD severity.
  - Doffer DPA, et al. Sustained improvements by behavioural parent training for children with ADHD: a meta-analytic review of longer-term child and parental outcomes. JCPP Adv. 2023. — [DOI 10.1002/jcv2.12196](https://doi.org/10.1002/jcv2.12196) · [PMID 37720584](https://pubmed.ncbi.nlm.nih.gov/37720584/); meta-analysis of RCTs, n = 27 studies; **not yet cited on page**; checked: PubMed record + abstract
  - Dekkers TJ, et al. Meta-analysis: which components of parent training work for children with ADHD? J Am Acad Child Adolesc Psychiatry. 2022. — [DOI 10.1016/j.jaac.2021.06.015](https://doi.org/10.1016/j.jaac.2021.06.015) · [PMID 34224837](https://pubmed.ncbi.nlm.nih.gov/34224837/); meta-analysis of RCTs; **not yet cited on page**; checked: PubMed record + abstract
  - Psyllou C, et al. Research Review: Mechanisms of change and between-family differences in parenting interventions for children with ADHD - an individual participant data meta-analysis. J Child Psychol Psychiatry. 2025;66(9):1304-19. — [DOI 10.1111/jcpp.14120](https://doi.org/10.1111/jcpp.14120) · [PMID 39910778](https://pubmed.ncbi.nlm.nih.gov/39910778/); individual participant data meta-analysis, n = 19 RCTs, 1,720; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Position B relies mostly on parent reports, which the parents receiving training make with full knowledge, so expectation can inflate symptom change; Position A restricts to probably blinded raters, who see the child briefly or in another setting and may miss change at home. The abstracts of the newer reviews do not say whether the sustained ADHD-symptom effect survives blinded rating.

**Next step:** Add the 2022-2025 syntheses as the current evidence on maintenance and mechanism, and check their full texts for blinded-only ADHD-symptom estimates; keep the page's framing that blinded evidence for core-symptom change is weak unless those estimates say otherwise.

### [ADHD stigma and shame: should I tell people?](../07-family-work-and-other-people/stigma-and-telling-people.md)

#### C07-002

**Trials of interventions to reduce ADHD stigma** · minor · direct contradiction · Page does not mention it

**In dispute:** No trial of an intervention to reduce public or self-stigma about ADHD was found.

- **Position A:** Systematic reviews of community attitudes found no trials showing that better public knowledge reduces stigma.
  - Bisset M, et al. Recent attitudes toward ADHD in the broader community: a systematic review. J Atten Disord. 2022;26(4):537-48. — [DOI 10.1177/10870547211003671](https://doi.org/10.1177/10870547211003671); systematic review, n = 10 studies; cited on page; checked: Crossref record
- **Position B:** A 2026 randomised controlled study of 145 children with ADHD found an 8-session nurse-led CBT-based psychoeducation programme reduced internalised stigma and raised hope compared with a wait-list control.
  - Yılmaz R, et al. The effect of cognitive behavioural therapy-based psychoeducation provided to children with ADHD on internalized stigma and hope. Psychol Health Med. 2026. — [DOI 10.1080/13548506.2026.2714468](https://doi.org/10.1080/13548506.2026.2714468) · [PMID 42554334](https://pubmed.ncbi.nlm.nih.gov/42554334/); RCT (wait-list control, single clinic), n = 145; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The page's search predates or missed this trial; it is small, single-site, unblinded, self-reported and in children (Turkey), so it does not show effects on public stigma or in adults.

**Next step:** Revise 'no trial found' to 'one small trial in children found reduced self-stigma after a psychoeducation programme (Limited)'; search for adult and public-stigma intervention trials (e.g. teacher or workplace programmes).

### [ADHD, work and study: does treatment or support help?](../07-family-work-and-other-people/work-and-study.md)

#### C07-003

**Does structured support help university students with ADHD?** · moderate · direct contradiction · Page does not mention it

**In dispute:** Support is barely tested: it is plausible that coaching, mentoring or flexible deadlines help, but plausible is not tested.

- **Position A:** Reviews find workplace interventions almost untested and educational accommodations mostly without ADHD-specific benefit.
  - Lovett BJ, et al. Systematic review: educational accommodations for children and adolescents with ADHD. J Am Acad Child Adolesc Psychiatry. 2021. — [PMID 32745597](https://pubmed.ncbi.nlm.nih.gov/32745597/); systematic review; cited on page; checked: cited on page; record not rechecked here
  - Lauder, et al. A systematic review of interventions to support adults with ADHD at work. Front Psychol. 2022. — [DOI 10.3389/fpsyg.2022.893469](https://doi.org/10.3389/fpsyg.2022.893469); realist systematic review; cited on page; checked: Crossref record
- **Position B:** A two-site RCT of 250 college students found a two-semester CBT group plus individual mentoring programme (ACCESS) improved ADHD symptoms, executive functioning and use of disability accommodations more than delayed treatment (d 0.39-1.21).
  - Anastopoulos AD, et al. A randomized controlled trial examining CBT for college students with ADHD. J Consult Clin Psychol. 2021. — [DOI 10.1037/ccp0000553](https://doi.org/10.1037/ccp0000553) · [PMID 33507774](https://pubmed.ncbi.nlm.nih.gov/33507774/); RCT (delayed-treatment control), n = 250; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The page's claim is about workplace adjustments and accommodations, where evidence really is thin; ACCESS is a study-support programme with mentoring, tested against delayed treatment with self-report outcomes, so it supports 'some structured support helps students' rather than any specific adjustment. Grades and retention were not primary outcomes in the abstract.

**Next step:** Add ACCESS as the main controlled evidence for university support, with its limits (unblinded self-report, waitlist control, US public universities), and check later ACCESS papers for grades and retention.

#### C07-004

**Medication and work outcomes: unemployment vs work disability** · minor · size of effect · Page reports both sides

**In dispute:** Registry studies find slightly less long-term unemployment during medicated periods.

- **Position A:** Swedish within-person data: long-term unemployment about 11% less common during medicated periods (RR 0.89), clearer in women.
  - Li L, et al. Association between pharmacological treatment of ADHD and long-term unemployment among working-age individuals in Sweden. JAMA Netw Open. 2022;5(4):e226815. — [DOI 10.1001/jamanetworkopen.2022.6815](https://doi.org/10.1001/jamanetworkopen.2022.6815) · [PMID 35476068](https://pubmed.ncbi.nlm.nih.gov/35476068/); registry, within-individual, n = 12,875; cited on page; checked: PubMed record
- **Position B:** A larger Swedish within-person study found lower sickness absence or disability pension only during atomoxetine use (HR 0.89), not with stimulants.
  - Taipale H, et al. ADHD medications and work disability and mental health outcomes. JAMA Netw Open. 2024. — [DOI 10.1001/jamanetworkopen.2024.2859](https://doi.org/10.1001/jamanetworkopen.2024.2859) · [PMID 38506810](https://pubmed.ncbi.nlm.nih.gov/38506810/); registry, within-individual, n = 221,714; cited on page; checked: PubMed record

**Why they may differ:** Different outcomes (unemployment vs sickness absence/disability pension), age ranges and exposure definitions; work disability was a secondary outcome in Taipale. Within-person designs are vulnerable to people starting or stopping medication around job changes.

**Next step:** No change needed beyond noting that the two outcomes differ; a later analysis could check whether stimulant periods were shorter or more often interrupted in Taipale.

### [ADHD myths: which popular claims are wrong or half right?](../08-reading-this-well/myths-and-corrections.md)

#### C08-003

**Is ADHD overdiagnosed?** · moderate · causal interpretation · Page reports both sides

**In dispute:** 'ADHD is a fad, or overdiagnosed' is partly true: true prevalence has not risen over three decades, though diagnoses have, with some milder cases and relative-age effects.

- **Position A:** With the same methods, the share of children meeting ADHD criteria has not changed over three decades; rising diagnoses largely reflect recognition.
  - Polanczyk GV, et al. ADHD prevalence estimates across three decades: an updated systematic review and meta-regression analysis. Int J Epidemiol. 2014;43(2):434-42. — [DOI 10.1093/ije/dyt261](https://doi.org/10.1093/ije/dyt261) · [PMID 24464188](https://pubmed.ncbi.nlm.nih.gov/24464188/); meta-regression; cited on page; checked: PubMed record
- **Position B:** A scoping review of 334 studies concluded there is evidence of overdiagnosis and overtreatment in children: diagnoses and prescribing rose, added cases were often milder, and the few studies of milder cases suggested diminishing returns where harms may outweigh benefits.
  - Kazda L, et al. Overdiagnosis of attention-deficit/hyperactivity disorder in children and adolescents: a systematic scoping review. JAMA Netw Open. 2021. — [DOI 10.1001/jamanetworkopen.2021.5335](https://doi.org/10.1001/jamanetworkopen.2021.5335) · [PMID 33843998](https://pubmed.ncbi.nlm.nih.gov/33843998/); systematic scoping review, n = 334 studies; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** Stable prevalence of meeting criteria in surveys does not settle whether clinical diagnoses track true need; a 'reservoir' of undiagnosed cases can coexist with over-labelling of milder or younger children. 'Overdiagnosis' in Kazda's sense means diagnosis that does more harm than good, a different question from prevalence. Under-diagnosis in adults (e.g. English primary care) runs the other way.

**Next step:** Cite Kazda 2021 as the main overdiagnosis evidence on the myths page or its target page (01/more-diagnoses-than-ever.md), and state that only five studies examined benefits and harms in milder cases.

#### C08-004

**Life-expectancy gap: modelled 13 years vs life-table estimates** · moderate · size of effect · Page reports one side only

**In dispute:** 'People with ADHD die 13 years earlier' is a model-based estimate from one Milwaukee group; studies of actual deaths among diagnosed adults find a smaller and still uncertain gap.

- **Position A:** The Milwaukee follow-up estimated 12.7 fewer years for persistent ADHD and 8.4 for the whole childhood-diagnosed group, using a life-expectancy calculator.
  - Barkley RA, et al. Hyperactive child syndrome and estimated life expectancy at young adult follow-up: the role of ADHD persistence and other potential predictors. J Atten Disord. 2019;23(9):907-23. — [DOI 10.1177/1087054718816164](https://doi.org/10.1177/1087054718816164) · [PMID 30526189](https://pubmed.ncbi.nlm.nih.gov/30526189/); cohort with modelled life expectancy, n = 131 hyperactive, 71 controls; cited on page; checked: PubMed record
- **Position B:** A UK primary-care matched cohort (30,039 diagnosed adults) using life tables from observed deaths estimated life expectancy 6.78 years shorter for men and 8.64 years for women; the authors note diagnosed adults are a minority of all adults with ADHD.
  - O'Nions E, et al. Life expectancy and years of life lost for adults with diagnosed ADHD in the UK: matched cohort study. Br J Psychiatry. 2025;226(5):261-8. — [DOI 10.1192/bjp.2024.199](https://doi.org/10.1192/bjp.2024.199) · [PMID 39844532](https://pubmed.ncbi.nlm.nih.gov/39844532/); matched cohort, life tables, n = 30,039 ADHD; 300,390 comparison; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The 13-year figure is modelled from risk factors in a small clinical sample; the UK figures come from observed deaths in a large diagnosed sample but still reflect a selected (diagnosed, often multimorbid) group. For women, the UK estimate (8.6 years) is close to Barkley's whole-group 8.4, so 'smaller gap' is only partly right.

**Next step:** On the myths page, give the UK life-table figures (already on 04/the-hard-statistics-in-context.md) alongside the 13-year figure, and replace 'a smaller ... gap' with wording that says observed-death estimates are about 7-9 years in diagnosed UK adults, with wide uncertainty and selection caveats. Use safe-messaging wording.

#### C08-005

**Paracetamol in pregnancy: sibling designs vs Navigation Guide review** · moderate · causal interpretation · Page reports one side only

**In dispute:** The links with paracetamol in pregnancy largely disappear when siblings are compared, pointing to shared family factors.

- **Position A:** In 2.48 million Swedish children the small raw link vanished in full-sibling comparisons (HR 0.98).
  - Ahlqvist VH, et al. Acetaminophen use during pregnancy and children's risk of autism, ADHD, and intellectual disability. JAMA. 2024;331(14):1205-14. — [DOI 10.1001/jama.2024.3172](https://doi.org/10.1001/jama.2024.3172) · [PMID 38592388](https://pubmed.ncbi.nlm.nih.gov/38592388/); registry with sibling comparison, n = 2.48 million; **not yet cited on page**; checked: PubMed record
- **Position B:** A 2025 Navigation Guide review of 46 studies found most (27) reported positive associations, rated higher-quality studies as more likely to be positive, and called for advising pregnant women to limit use; one author declared work as an expert witness for plaintiffs.
  - Prada D, et al. Evaluation of the evidence on acetaminophen use and neurodevelopmental disorders using the Navigation Guide methodology. Environ Health. 2025. — [DOI 10.1186/s12940-025-01208-0](https://doi.org/10.1186/s12940-025-01208-0) · [PMID 40804730](https://pubmed.ncbi.nlm.nih.gov/40804730/); systematic review (qualitative, Navigation Guide), n = 46 studies; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** The Navigation Guide review weighs studies with detailed exposure measurement (often smaller cohorts) as higher quality and does not privilege sibling designs; sibling analyses remove family confounding but can be biased toward null by exposure misclassification and discordant-sibling selection. The myths page cites neither source directly (its home page, 04/what-does-and-doesnt-cause-adhd.md, carries the detail and the FDA notice).

**Next step:** Add a clause to the myth correction that one 2025 review and a 2025 US FDA notice took a different view, linking to the home page; the full weighing belongs on the 04 page (see the folder-04 register).

#### C08-006

**Do childhood stimulants change later addiction risk?** · moderate · causal interpretation · Page reports one side only

**In dispute:** Correction to 'stimulants lead to addiction': within-person studies find fewer substance-related problems during medicated periods (about a third lower odds).

- **Position A:** US claims within-person data show 31-35% lower odds of substance-related emergencies in medicated months, and lower odds two years later.
  - Quinn PD, et al. ADHD medication and substance-related problems. Am J Psychiatry. 2017;174(9):877-85. — [DOI 10.1176/appi.ajp.2017.16060686](https://doi.org/10.1176/appi.ajp.2017.16060686) · [PMID 28659039](https://pubmed.ncbi.nlm.nih.gov/28659039/); claims, within-individual, n = about 3 million; cited on page; checked: PubMed record
- **Position B:** A meta-analysis of prospective studies found children with and without a stimulant treatment history had comparable later substance use, abuse and dependence: treatment neither protected nor increased risk.
  - Humphreys KL, et al. Stimulant medication and substance use outcomes: a meta-analysis. JAMA Psychiatry. 2013. — [DOI 10.1001/jamapsychiatry.2013.1273](https://doi.org/10.1001/jamapsychiatry.2013.1273) · [PMID 23754458](https://pubmed.ncbi.nlm.nih.gov/23754458/); meta-analysis of longitudinal studies, n = 3-11 studies per outcome; **not yet cited on page**; checked: PubMed record + abstract

**Why they may differ:** They measure different things: acute emergencies during current treatment vs long-term substance use disorders after childhood treatment. Both reject 'stimulants cause addiction', but the myth correction could be read as 'stimulants protect against addiction', which the long-term evidence does not support.

**Next step:** Add to the myth correction that long-term follow-ups find neither increased nor reduced later substance use disorders (Humphreys 2013 is already cited on 05/alcohol-drugs-and-addiction.md).

### [Where does the information on these pages come from?](../08-reading-this-well/sources-and-guidelines.md)

#### C08-001

**First-line medicine: NICE vs AADPA vs CADDRA vs network meta-analysis** · moderate · guideline disagreement · Page reports one side only

**In dispute:** Guidelines mostly agree on the basics and differ on details such as which medicine to offer first.

- **Position A:** NICE NG87 (England): methylphenidate as first-line medicine for children aged 5 and over and young people, after environmental modifications and support; lisdexamfetamine after an inadequate 6-week methylphenidate trial; for adults, lisdexamfetamine or methylphenidate.
  - National Institute for Health and Care Excellence. Attention deficit hyperactivity disorder: diagnosis and management (NG87). 2018, updated 2019. — guideline; cited on page; checked: search result only
- **Position B:** AADPA (Australia): methylphenidate, dexamfetamine or lisdexamfetamine equally as first-line for children 5 and over, adolescents and adults, citing minimal differences in efficacy and tolerability; each graded low certainty.
  - May T, et al. The Australian evidence-based clinical practice guideline for attention deficit hyperactivity disorder. Aust N Z J Psychiatry. 2023;57(8):1101-16. — [DOI 10.1177/00048674231166329](https://doi.org/10.1177/00048674231166329) · [PMID 37254562](https://pubmed.ncbi.nlm.nih.gov/37254562/); guideline; cited on page; checked: PubMed record + PMC full text
- **Position C:** CADDRA (Canada, 4.1): long-acting stimulants of either class (methylphenidate or amphetamine) as first-line, with a trial of both classes before second-line options; short-acting stimulants and atomoxetine second-line (from secondary descriptions).
  - Canadian ADHD Resource Alliance. Canadian ADHD Practice Guidelines, 4.1 edition. 2020/2021. — guideline; cited on page; checked: search result only
- **Position D:** The 2018 network meta-analysis favoured methylphenidate in children but amphetamines in adults, weighing efficacy against tolerability.
  - Cortese S, et al. Comparative efficacy and tolerability of medications for ADHD in children, adolescents, and adults: a systematic review and network meta-analysis. Lancet Psychiatry. 2018;5(9):727-38. — [DOI 10.1016/S2215-0366(18)30269-4](https://doi.org/10.1016/S2215-0366(18)30269-4) · [PMID 30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/); network meta-analysis, n = 133 trials; **not yet cited on page**; checked: PubMed record

**Why they may differ:** Same trial base, different decisions: NICE adds cost-effectiveness and a stepped NHS pathway; AADPA judged the stimulants interchangeable on low-certainty evidence; CADDRA prioritises long-acting formulations for adherence and diversion reasons. The guidelines predate the 2025 network and umbrella reviews. Licensing (for example dexamfetamine availability) also differs by country.

**Next step:** Add a short side-by-side table of each guideline's first-line wording, verified against the full NICE recommendations (1.7.x / adult section) and the CADDRA 4.1 PDF, and note where Cortese 2018 differs for adults. Frame as what each guideline says, not as advice.

#### C08-002

**WFADHD 2026 update vs the 2021 statement the pages anchor on** · moderate · guideline disagreement · Page reports both sides

**In dispute:** The 2021 World Federation of ADHD consensus statement is the anchor for 'what is established'; the 2026 update says most conclusions stand, and pages have not been checked against it.

- **Position A:** 2021 statement: 208 evidence-based conclusions from meta-analyses or studies of more than 2,000 people.
  - Faraone SV, et al. The World Federation of ADHD International Consensus Statement: 208 evidence-based conclusions about the disorder. Neurosci Biobehav Rev. 2021;128:789-818. — [DOI 10.1016/j.neubiorev.2021.01.022](https://doi.org/10.1016/j.neubiorev.2021.01.022) · [PMID 33549739](https://pubmed.ncbi.nlm.nih.gov/33549739/); consensus statement; cited on page; checked: PubMed record
- **Position B:** 2026 update: 252 statements from 2021-2025 studies; supports many 2021 conclusions but adds nuance and says the balance of findings has shifted in a few areas. The abstract does not name which.
  - Faraone SV, et al. The World Federation of ADHD International Consensus Statement: 2026 update. Neurosci Biobehav Rev. 2026;193:107083. — [DOI 10.1016/j.neubiorev.2026.107083](https://doi.org/10.1016/j.neubiorev.2026.107083) · [PMID 43044899](https://pubmed.ncbi.nlm.nih.gov/43044899/); consensus statement, n = 118 authors; cited on page; checked: PubMed record + abstract

**Why they may differ:** New evidence 2021-2025 (for example target-trial emulations, umbrella reviews, pregnancy meta-analyses) may have moved specific conclusions. Both statements share authors, inclusion rules and declared industry links, so they are not independent checks of each other.

**Next step:** Read the 2026 full text, list every statement marked as changed or nuanced, and map each to the site's home pages (especially medication safety, registry outcomes, pregnancy and non-drug treatments). Until then, avoid calling the 2021 statement the anchor without that caveat.
