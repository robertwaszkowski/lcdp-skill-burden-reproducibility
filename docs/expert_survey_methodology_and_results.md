# Expert Survey Protocol and Delphi-Based Consensus Analysis for the IT Skill Burden Framework

**Working document version:** 1.0  
**Prepared for:** LCDP IT Skill Burden / Total ISBI research package  
**Survey round:** Round 1 and targeted Round 2 Delphi refinement  
**Date:** 2026-06-03  

---

## Abstract

This document describes the expert survey protocol used to determine skill-level weights for the Two-Level IT Skill Burden Framework, a multi-criteria model designed to quantify the technical burden imposed by low-code development platforms (LCDPs) on citizen developers. The expert survey was conducted to estimate two constructs for each IT skill included in the framework: (1) *Usage Intensity*, representing how often and how centrally a skill is required in a given application lifecycle phase, and (2) *Difficulty of Acquisition*, representing how difficult it is for a business user without formal IT education to acquire sufficient practical competence in the skill.

In Round 1, fifteen experts assessed 209 IT skills, producing 3,135 expert-skill observations. Each skill was evaluated using closed, subject-specific five-level linguistic scales mapped to numerical values from 1 to 5. The synthetic expert-level burden weight was defined as the product of usage intensity and difficulty of acquisition. The Round 1 dataset was validated for completeness, invalid entries, and duplicate responses. No missing or invalid ratings were detected. Reliability analysis showed strong average-expert reliability for Usage Intensity and Difficulty of Acquisition, and acceptable-to-good average-expert reliability for the Synthetic Weight.

A targeted Round 2 Delphi refinement was then conducted for 46 low-consensus skills identified in Round 1. Experts were shown their original ratings, anonymized panel means, and panel standard deviations for the disputed items, and were asked to reconsider only those ratings. Round 2 produced 690 additional expert-skill observations. All 46 targeted skills showed reduced dispersion in synthetic weight after the second round, with a mean reduction in standard deviation of 1.414. Final reliability improved relative to Round 1, with the average-expert ICC increasing from 0.8759 to 0.8925 for Usage Intensity, from 0.9425 to 0.9468 for Difficulty of Acquisition, and from 0.7897 to 0.8335 for Synthetic Weight. These results indicate that the expert survey produced a reliable and reproducible set of consensus skill weights suitable for use in the final IT Skill Burden model.

---

## Keywords

Citizen Development; low-code development platforms; expert survey; Delphi method; IT skill burden; multi-criteria decision-making; reliability analysis; intraclass correlation; consensus weights; reproducibility.

---

# 1. Introduction

Low-code development platforms (LCDPs) are widely promoted as tools that reduce the technical barriers to software development and enable business users to participate directly in application creation. This premise is central to the Citizen Development paradigm. However, different LCDPs impose different technical demands on users. Some platforms may allow business users to create applications mainly through visual configuration, whereas others may still require knowledge of databases, APIs, scripting, authentication mechanisms, deployment concepts, or software integration patterns.

The Two-Level IT Skill Burden Framework was developed to quantify this burden systematically. Its core assumption is that the suitability of an LCDP for Citizen Development depends not only on the number of technical skills required, but also on the difficulty of those skills, the intensity with which they are used, and the lifecycle phase in which they appear. The framework therefore requires a validated skill-weighting procedure.

This document describes the expert survey used to derive those skill weights. It is intended to serve as a reproducibility and methodological supplement. It explains the aim of the survey, the expert rating framework, the structure of the questionnaire, the Delphi-style consensus procedure, data validation rules, reliability statistics, Round 1 results, Round 2 refinement, final outcomes, and recommended use of the expert-derived weights in the main manuscript and public repository.

---

# 2. Aim of the Expert Survey

The primary aim of the expert survey was to obtain reliable, expert-derived weights for IT skills used in the Two-Level IT Skill Burden Framework.

For each skill `c_j`, the survey estimated two constructs:

```math
u_{j,e}
```

where `u_{j,e}` denotes the Usage Intensity assigned to skill `c_j` by expert `e`, and

```math
d_{j,e}
```

where `d_{j,e}` denotes the Difficulty of Acquisition assigned to skill `c_j` by expert `e`.

The expert-level synthetic skill burden was then calculated as:

```math
w_{j,e}=u_{j,e}\times d_{j,e}.
```

The final consensus weight for each skill was calculated from the expert panel, typically using the mean or median across experts:

```math
\bar{w}_j = \frac{1}{E}\sum_{e=1}^{E} w_{j,e},
```

where `E = 15` is the number of experts.

The survey was designed to support four methodological goals:

1. **Weight estimation** — derive skill-level weights that reflect both skill difficulty and practical usage intensity.
2. **Consensus measurement** — quantify the degree of expert agreement for each skill.
3. **Reliability assessment** — evaluate whether the expert panel produces stable aggregate judgments.
4. **Reproducibility** — generate transparent, analyzable, and citable expert-level data for inclusion in the research repository.

---

# 3. Relationship to the Two-Level IT Skill Burden Framework

The expert survey provides the skill weights used in the Two-Level IT Skill Burden Framework. In the framework, each LCDP is represented by a phase-specific platform-skill matrix:

```math
x_{ijk}\in\{0,1\},
```

where:

- `i` denotes the platform,
- `j` denotes the IT skill,
- `k` denotes the lifecycle phase,
- `x_{ijk}=1` means that platform `y^i` requires skill `c_j` in phase `P_k`,
- `x_{ijk}=0` means that the skill is not required in that phase.

The lifecycle phases are:

```math
P_k\in\{P_A,P_D,P_I\},
```

where:

- `P_A` = Design / Analysis,
- `P_D` = Development,
- `P_I` = Implementation.

For each phase, the phase-specific IT Skill Burden Index is computed as:

```math
F_{P_k}(y^i)=\sum_{c_j\in C_{IT,P_k}} w_jx_{ijk}
```

under the baseline configuration `p = 1`. The total burden index is then obtained as:

```math
F_{\mathrm{Total}}(y^i)=F_{P_A}(y^i)+F_{P_D}(y^i)+F_{P_I}(y^i).
```

Thus, the quality of the final platform ranking depends on the validity and reliability of `w_j`. The expert survey was therefore designed as a structured, reproducible procedure for estimating `w_j`.

---

# 4. Survey Constructs

## 4.1 Usage Intensity

Usage Intensity measures how often and how centrally a skill is required when using an LCDP in the relevant lifecycle phase. It does not measure whether the skill is generally important in software engineering; rather, it measures how important the skill is in the specific context of low-code platform use.

Formally, Usage Intensity is represented as:

```math
u_{j,e}\in\{1,2,3,4,5\}.
```

The expert survey used the following closed linguistic scale.

| Numerical value | Linguistic label | Operational meaning |
|---:|---|---|
| 1 | Rare / avoidable | The skill is rarely needed and can usually be avoided through platform features, templates, or alternative workflows. |
| 2 | Occasional / peripheral | The skill is needed only in limited cases or for non-core tasks. |
| 3 | Moderate / recurring | The skill is used in several typical tasks but is not continuously required. |
| 4 | Frequent / important | The skill is required in many typical tasks and has a clear effect on successful platform use. |
| 5 | Essential / continuous | The skill is central to the phase and is required for most relevant tasks or for completing the phase effectively. |

## 4.2 Difficulty of Acquisition

Difficulty of Acquisition measures how difficult it is for a business user without formal IT education to acquire sufficient practical competence in a given skill. The construct does not require expert mastery; it concerns the practical level needed to use the skill reliably in the low-code context.

Formally, Difficulty of Acquisition is represented as:

```math
d_{j,e}\in\{1,2,3,4,5\}.
```

The expert survey used the following closed linguistic scale.

| Numerical value | Linguistic label | Operational meaning |
|---:|---|---|
| 1 | Very easy | Can be learned quickly by a non-IT user with minimal instruction or self-guided exploration. |
| 2 | Easy | Requires limited training or practice, but no significant technical background. |
| 3 | Moderate | Requires structured learning and repeated practice; some technical concepts may be unfamiliar. |
| 4 | Difficult | Requires substantial training, technical reasoning, or prior exposure to IT concepts. |
| 5 | Very difficult | Requires advanced technical knowledge, formal IT background, or extended practice to apply reliably. |

## 4.3 Synthetic Skill Weight

The synthetic skill weight combines the two constructs:

```math
w_{j,e}=u_{j,e}\times d_{j,e}.
```

The product formulation was used because a skill imposes a high burden when it is both difficult to acquire and frequently or centrally required. Conversely, a difficult but rarely used skill, or an easy but frequently used skill, imposes a lower burden than a skill that is both difficult and essential.

The resulting expert-level synthetic weight can range from:

```math
1\times1=1
```

to:

```math
5\times5=25.
```

---

# 5. Expert Panel

The expert panel consisted of fifteen respondents. Each respondent completed a structured Excel-based survey independently. The survey files were anonymized using expert identifiers:

```math
E01,E02,\ldots,E15.
```

The expert survey was designed to avoid direct collection of personally identifiable information in the analytical dataset. The public analytical files should use anonymized expert IDs rather than personal names. The auxiliary expert-summary file records only role category, organizational context, and organization-size class. These descriptors are sufficient to document panel composition without revealing individual identities.

## 5.1 Expert Selection Rationale

The panel was constructed to include practitioners who could evaluate IT skills from the perspective of real low-code platform implementation, process automation, digital transformation, and enterprise application delivery. The respondents were selected because their professional roles require them to assess both the technical complexity of IT skills and the practical conditions under which such skills are used in low-code or workflow-oriented projects.

The panel intentionally includes both architecture-oriented and analysis-oriented profiles. Architecture-oriented experts are expected to have strong insight into platform integration, deployment, software structure, and technical feasibility. Analysis-oriented experts are expected to have strong insight into business-process interpretation, user requirements, workflow design, and the practical capabilities of non-IT users. This combination is appropriate for assessing IT skill burden in Citizen Development, because the framework concerns both technical competencies and their practical usability by business users.

## 5.2 Expert Inclusion Criteria

The expert panel was based on the following inclusion logic:

- professional involvement in software engineering, low-code development, business process automation, workflow management, data-driven digital transformation, or enterprise application delivery;
- practical familiarity with low-code development platforms, workflow automation tools, or related digital-platform implementation environments;
- ability to judge the difficulty of technical skills from the perspective of a business user without formal IT education;
- ability to judge how frequently or centrally a skill may be required in application lifecycle phases;
- senior or decision-influencing role, such as architect, analyst, team leader, department director, or board member.

Experts currently employed by evaluated platform vendors should be excluded from the panel to reduce vendor-specific bias. If this exclusion criterion was applied during recruitment, it should be reported explicitly in the manuscript.

## 5.3 Panel Composition

The final expert panel contained 15 experts. The panel included 11 architecture-oriented experts and 4 analysis-oriented experts:

| Broad professional profile | Number of experts |
|---|---:|
| Architect | 11 |
| Analyst | 4 |

The experts also held senior organizational or project roles:

| Seniority / responsibility profile | Number of experts |
|---|---:|
| Board Member | 8 |
| Team Leader | 5 |
| Department Director | 2 |

The detailed role distribution was:

| Professional role | Number of experts |
|---|---:|
| Architect / Board Member | 5 |
| Analyst / Board Member | 3 |
| Architect / Team Leader | 4 |
| Analyst / Team Leader | 1 |
| Architect / Department Director | 2 |

The panel represented organizations of different size classes, from small and medium-sized organizations to large public-sector or enterprise-scale institutions:

| Organization size class | Number of experts |
|---|---:|
| 50+ | 4 |
| 100+ | 1 |
| 200+ | 3 |
| 250+ | 1 |
| 400+ | 3 |
| 1000+ | 2 |
| 5000+ | 1 |

This diversity is important because the interpretation of low-code skill burden may depend on organizational scale. Smaller organizations may emphasize practical delivery speed and limited technical specialization, whereas larger organizations may emphasize integration, governance, deployment controls, and operational reliability.

## 5.4 Expert Characteristics

The expert-level descriptors used for methodological documentation are summarized below. Organization names are not reported. Instead, each organization is described by its general technology and business profile.

| Expert ID | Expert code | Professional role | Organization profile | Organization size |
|---|---|---|---|---:|
| E01 | RW | Architect / Board Member | The organization specializes in business process automation, digital transformation, and workflow management. It delivers solutions to clients using both proprietary and third-party low-code development platforms, enabling the rapid development and automation of business applications with minimal traditional programming. | 50+ |
| E02 | AC | Analyst / Board Member | The company focuses on process automation, workflow optimization, and digital transformation initiatives. It leverages both in-house and third-party low-code development platforms to design, implement, and maintain business applications that reduce development effort and accelerate delivery. | 50+ |
| E03 | PO | Architect / Board Member | The company helps clients improve operational efficiency through business process automation and digital solutions. To deliver these solutions, it utilizes a combination of proprietary and external low-code platforms, enabling faster application development with limited reliance on traditional coding. | 50+ |
| E04 | JS | Architect / Team Leader | The organization provides consulting and implementation services in the areas of business process management, workflow automation, and enterprise digitalization. It uses both proprietary and third-party low-code development platforms to rapidly deliver process-centric applications and tailored digital solutions for its clients. | 50+ |
| E05 | WD | Analyst / Board Member | The organization specializes in custom software development, digital transformation, and business process optimization. It delivers tailored solutions using a combination of low-code platforms, proprietary tools, and traditional software engineering approaches to meet client requirements. | 200+ |
| E06 | PM | Architect / Board Member | The company supports organizations in developing and modernizing digital products and business applications. It leverages both third-party low-code platforms and custom development technologies to accelerate solution delivery and drive business innovation. | 200+ |
| E07 | BK | Architect / Team Leader | The organization provides technology consulting and software development services focused on digitalization and process improvement. To deliver client solutions, it combines low-code development platforms with custom-built software and agile development practices. | 200+ |
| E08 | JA | Architect / Board Member | The organization specializes in data management, analytics, digital transformation, and business process optimization. It delivers technology solutions using a combination of proprietary applications, low-code platforms, and custom development approaches tailored to client needs. | 400+ |
| E09 | MM | Analyst / Team Leader | The company helps organizations modernize operations through data-driven solutions, process automation, and digital transformation initiatives. It leverages both internally developed solutions and third-party low-code platforms to accelerate application delivery and support business innovation. | 400+ |
| E10 | MW | Architect / Team Leader | The organization provides consulting and technology services focused on data, analytics, and enterprise transformation. To deliver business applications and automation solutions, it combines proprietary technologies with external low-code development platforms and traditional software engineering practices. | 400+ |
| E11 | SS | Analyst / Board Member | The organization specializes in software engineering, digital transformation, and enterprise technology solutions. It delivers business applications and process automation initiatives using a combination of low-code platforms, cloud technologies, and custom software development. | 1000+ |
| E12 | MK | Architect / Department Director | The company helps organizations modernize and scale their digital capabilities through application development, automation, and technology consulting services. It utilizes both low-code development platforms and traditional engineering approaches to accelerate solution delivery and support client-specific requirements. | 1000+ |
| E13 | MMA | Architect / Board Member | The company helps organizations improve decision-making and business performance through data integration, analytics, and digital solutions. It leverages both low-code development platforms and traditional software engineering methods to accelerate the delivery of client-focused applications and automation initiatives. | 100+ |
| E14 | PMA | Architect / Department Director | The company supports clients through equipment sales, maintenance services, and operational support solutions. To enhance efficiency and digitalize internal and customer-facing processes, it employs a range of enterprise technologies, including low-code platforms and workflow automation tools. | 250+ |
| E15 | KR | Architect / Team Leader | The organization is a public-sector institution responsible for administering agricultural support programs, rural development initiatives, and financial assistance schemes. It uses digital platforms, workflow automation, and low-code-based solutions to support service delivery, process management, and interactions with beneficiaries. | 5000+ |

## 5.5 Relevance of the Expert Panel to the Survey Aim

The composition of the panel is appropriate for the survey aim for three reasons.

First, the experts represent roles directly involved in translating business requirements into digital applications, workflows, integrations, and implementation decisions. This makes them suitable judges of the practical burden imposed by individual IT skills.

Second, the panel includes both strategic decision-makers and delivery-oriented leaders. Board-level respondents bring perspective on technology adoption and organizational feasibility, while team leaders and department directors bring operational experience with implementation challenges.

Third, the represented organizations use combinations of low-code platforms, proprietary technologies, third-party platforms, workflow automation tools, cloud technologies, data platforms, and traditional software engineering practices. This reduces the risk that the ratings reflect only one technological ecosystem or one platform vendor.

## 5.6 Anonymization and Data-Protection Approach

For reproducibility, the analytical dataset should retain only anonymized expert identifiers, such as `E01` to `E15`. Expert codes such as initials may be retained in private working files but should be removed or replaced with anonymous IDs in the public repository if there is any possibility of identification.

The recommended public expert metadata fields are:

- anonymized expert ID,
- broad role category,
- seniority or responsibility category,
- organization size class,
- generalized organization profile.

The public dataset should not include names, email addresses, organization names, signatures, or free-text comments that could identify an expert.

# 6. Survey Instrument

## 6.1 Format

The survey was implemented as an Excel workbook. Each expert received an individual file with a unique expert ID. The Round 1 workbook contained all 209 IT skills.

Each row corresponded to one skill, with the following conceptual fields:

- Project Stage,
- Project Task,
- Skill ID,
- Skill Name,
- Usage Intensity,
- Difficulty of Acquisition,
- optional comments.

The answer cells used closed-list dropdown scales to reduce entry errors and standardize responses. The workbook also included a missing-ratings counter and a completion status field.

## 6.2 Number of Items

Round 1 included:

```math
N=209
```

IT skills.

Each expert provided two ratings per skill:

```math
u_{j,e}
```

and

```math
d_{j,e}.
```

Therefore, the total number of expected Round 1 expert-skill observations was:

```math
15\times209=3135.
```

Because each observation includes both usage and difficulty, the number of individual rating values was:

```math
3135\times2=6270.
```

---

# 7. Round 1 Procedure

Each expert completed the Round 1 survey independently. Experts were instructed to evaluate each skill in relation to its expected relevance in low-code development and Citizen Development contexts. They were asked not to rank platforms directly. Instead, the purpose was to assess the burden associated with the IT skill itself.

Experts selected values from predefined linguistic scales. After all 15 files were collected, the files were processed using a reproducibility script that extracted the ratings, mapped linguistic labels to numerical values, calculated synthetic weights, and generated validation and reliability reports.

---

# 8. Round 1 Data Validation

The Round 1 validation procedure checked the following:

1. number of uploaded files,
2. unique expert identifiers,
3. number of skill rows per file,
4. presence of Round 1 metadata,
5. missing Usage Intensity values,
6. missing Difficulty of Acquisition values,
7. invalid values outside the closed scale,
8. duplicated or near-duplicated expert response profiles,
9. completeness of the extracted long-format dataset.

The final validated Round 1 dataset contained:

```math
15\times209=3135
```

expert-skill observations.

No missing ratings and no invalid ratings were detected. The dataset was therefore suitable for reliability and consensus analysis.

---

# 9. Round 1 Reliability Analysis

## 9.1 Reliability Metrics

Reliability was evaluated separately for:

- Usage Intensity,
- Difficulty of Acquisition,
- Synthetic Weight.

Three reliability indicators were computed:

1. Cronbach’s alpha,
2. ICC for a single expert,
3. ICC for the average expert panel.

Cronbach’s alpha measures internal consistency across expert raters. The intraclass correlation coefficient (ICC) evaluates the degree of agreement or consistency among raters. The average-expert ICC is particularly important for this study because the final model uses aggregated expert consensus rather than the rating of a single expert.

## 9.2 Round 1 Reliability Results

The Round 1 reliability statistics were:

| Measure | Cronbach’s alpha | ICC single expert | ICC average experts |
|---|---:|---:|---:|
| Usage Intensity | 0.8994 | 0.3200 | 0.8759 |
| Difficulty of Acquisition | 0.9507 | 0.5223 | 0.9425 |
| Synthetic Weight | 0.8434 | 0.2002 | 0.7897 |

These results indicate that the expert panel produced reliable aggregate judgments. Single-expert ICC values were lower, which is expected because individual experts may differ in their professional experience and interpretation of skill burden. However, the average-expert ICC values were strong for Usage Intensity and Difficulty of Acquisition, and acceptable-to-good for Synthetic Weight.

The lower reliability for Synthetic Weight is expected because `w_{j,e}` is a product of two separate judgments. Multiplicative variables naturally amplify differences between experts.

---

# 10. Identification of Low-Consensus Skills

Round 1 consensus was assessed for each skill using the dispersion of expert-level synthetic weights:

```math
SD(w_{j,e}).
```

A skill was flagged as low-consensus if the standard deviation of the synthetic weight exceeded the predefined threshold used in the analysis script:

```math
SD(w_{j,e})>5.
```

This threshold identified 46 low-consensus skills. These skills were selected for targeted Round 2 Delphi refinement.

The use of targeted refinement was intended to reduce expert fatigue. Rather than asking experts to re-score all 209 skills, Round 2 focused only on the subset of items where expert disagreement was highest.

---

# 11. Round 2 Delphi Refinement

## 11.1 Aim of Round 2

The aim of Round 2 was to improve consensus for skills that showed high dispersion in Round 1.

The Round 2 procedure followed a targeted Delphi logic:

1. identify low-consensus items after Round 1,
2. provide experts with structured anonymized panel feedback,
3. ask experts to reconsider only the disputed items,
4. measure whether dispersion decreased after the second round.

## 11.2 Round 2 Instrument

Each expert received an individual Round 2 workbook containing only the 46 low-consensus skills. For each skill, the workbook presented:

- the expert’s own Round 1 Usage Intensity rating,
- the expert’s own Round 1 Difficulty of Acquisition rating,
- the expert’s own Round 1 synthetic weight,
- anonymized panel mean for Usage Intensity,
- anonymized panel standard deviation for Usage Intensity,
- anonymized panel mean for Difficulty of Acquisition,
- anonymized panel standard deviation for Difficulty of Acquisition,
- anonymized panel mean for Synthetic Weight,
- anonymized panel standard deviation for Synthetic Weight,
- blank Round 2 Usage Intensity field,
- blank Round 2 Difficulty of Acquisition field,
- optional comment field.

The Round 2 answer cells used the same closed linguistic scales as Round 1.

## 11.3 Round 2 Dataset

Round 2 included:

```math
46
```

skills and:

```math
15
```

experts.

The expected number of Round 2 observations was therefore:

```math
15\times46=690.
```

All expected Round 2 observations were extracted successfully. No missing or invalid Round 2 ratings were detected.

---

# 12. Round 2 Convergence Results

Round 2 substantially improved expert consensus.

All 46 targeted low-consensus skills showed reduced synthetic-weight dispersion after Round 2:

```math
46/46
```

skills improved.

The mean change in synthetic-weight standard deviation was:

```math
\Delta SD_w=-1.414.
```

The negative value indicates a reduction in dispersion. Therefore, the targeted Delphi refinement successfully increased consensus for all disputed items.

This result is methodologically important because it demonstrates that the second round was not merely procedural. It produced measurable convergence in expert judgment.

---

# 13. Final Reliability After Round 2

The final dataset was constructed by retaining Round 1 ratings for skills that were not targeted in Round 2 and replacing Round 1 ratings with Round 2 ratings for the 46 low-consensus skills.

The average-expert ICC values improved after Round 2:

| Measure | Round 1 average-expert ICC | Final average-expert ICC |
|---|---:|---:|
| Usage Intensity | 0.8759 | 0.8925 |
| Difficulty of Acquisition | 0.9425 | 0.9468 |
| Synthetic Weight | 0.7897 | 0.8335 |

These results show that the targeted Delphi refinement improved the reliability of the final expert-derived weights.

The strongest improvement occurred for Synthetic Weight:

```math
0.7897 \rightarrow 0.8335.
```

This is meaningful because Synthetic Weight is the final input used by the Two-Level IT Skill Burden Framework. The improvement therefore directly strengthens the methodological foundation of the platform-ranking model.

---

# 14. Final Consensus Weight Calculation

The final expert-level dataset after Round 2 is denoted as:

```math
u^{*}_{j,e}, \quad d^{*}_{j,e}, \quad w^{*}_{j,e}.
```

For skills not included in Round 2:

```math
u^{*}_{j,e}=u^{R1}_{j,e},
```

```math
d^{*}_{j,e}=d^{R1}_{j,e}.
```

For the 46 low-consensus skills included in Round 2:

```math
u^{*}_{j,e}=u^{R2}_{j,e},
```

```math
d^{*}_{j,e}=d^{R2}_{j,e}.
```

The final expert-level synthetic weight was calculated as:

```math
w^{*}_{j,e}=u^{*}_{j,e}\times d^{*}_{j,e}.
```

The final consensus synthetic weight for skill `c_j` was calculated as:

```math
\bar{w}^{*}_j = \frac{1}{15}\sum_{e=1}^{15} w^{*}_{j,e}.
```

The final consensus table therefore provides, for each skill:

- mean Usage Intensity,
- median Usage Intensity,
- standard deviation of Usage Intensity,
- mean Difficulty of Acquisition,
- median Difficulty of Acquisition,
- standard deviation of Difficulty of Acquisition,
- mean Synthetic Weight,
- median Synthetic Weight,
- standard deviation of Synthetic Weight,
- final consensus flag.

---

# 15. Interpretation of the Expert Survey Results

The survey results support several conclusions.

First, the expert panel produced stable aggregate assessments. While individual experts varied, the average-expert reliability was strong, which is appropriate because the framework uses aggregated consensus weights rather than individual judgments.

Second, Difficulty of Acquisition showed the highest reliability. This suggests that experts agreed more strongly on which IT skills are easy or difficult for non-IT business users to learn.

Third, Usage Intensity also showed strong reliability, although slightly lower than Difficulty of Acquisition. This is expected because usage intensity may depend more on platform context, implementation scenario, and organizational assumptions.

Fourth, Synthetic Weight showed the lowest initial reliability because it combines two ratings multiplicatively. However, after targeted Round 2 refinement, the average-expert ICC for Synthetic Weight improved substantially to 0.8335.

Fifth, the targeted Delphi process was effective. All 46 low-consensus skills showed reduced dispersion, demonstrating convergence of expert judgment.

---

# 16. Recommended Manuscript Reporting

The following concise methodological statement can be adapted for the main manuscript:

> Skill weights were derived through a two-round expert survey involving fifteen independent experts. In Round 1, experts evaluated 209 IT skills using two five-level linguistic scales: Usage Intensity and Difficulty of Acquisition. The synthetic burden weight for each skill was calculated as the product of these two ratings. Round 1 produced 3,135 expert-skill observations and no missing or invalid ratings. Reliability analysis showed strong panel-level agreement, with average-expert ICC values of 0.8759 for Usage Intensity, 0.9425 for Difficulty of Acquisition, and 0.7897 for Synthetic Weight. A targeted Round 2 Delphi refinement was conducted for 46 low-consensus skills identified by high dispersion in synthetic weights. All targeted skills showed reduced dispersion after Round 2, with a mean reduction in synthetic-weight standard deviation of 1.414. Final average-expert ICC values increased to 0.8925 for Usage Intensity, 0.9468 for Difficulty of Acquisition, and 0.8335 for Synthetic Weight.

---

# 17. Reproducibility

The expert survey analysis is reproducible from the following files:

1. Round 1 completed expert survey ZIP,
2. Round 2 completed expert survey ZIP,
3. Round 1 reproduction script,
4. Round 2 reproduction script,
5. final analysis output CSV files,
6. final consensus weights file,
7. final long-format expert dataset.

The reproducibility workflow consists of:

1. extracting expert responses from Excel files,
2. mapping linguistic labels to numerical values,
3. validating survey completeness,
4. calculating expert-level weights,
5. generating long-format data,
6. computing consensus statistics,
7. identifying low-consensus skills,
8. processing targeted Round 2 responses,
9. constructing the final post-Delphi dataset,
10. calculating final reliability statistics,
11. exporting CSV and Excel reports.

The recommended public repository structure is:

```text
data/
  raw/
    completed_expert_surveys_round1_FINAL.zip
    completed_expert_surveys_round2_FINAL.zip
  processed/
    final_expert_survey_long_format_after_round2.csv
    final_consensus_weights_after_round2.csv
    expert_reliability_round2_and_final.csv
    round2_convergence_by_skill.csv

analysis/
  reproduce_expert_survey_round1_analysis.py
  reproduce_expert_survey_round2_analysis.py

reports/
  expert_survey_round1_analysis_report_FINAL.xlsx
  expert_survey_round2_analysis_report_FINAL.xlsx

README.md
LICENSE
CITATION.cff
```

For publication, the repository should be archived using a persistent identifier, preferably through Zenodo.

---

# 18. Limitations

Several limitations should be acknowledged.

First, the survey relies on expert judgment. Although the Delphi refinement and reliability analysis improve confidence in the results, the weights remain expert-derived estimates rather than direct behavioral measurements.

Second, expert ratings may depend on the assumed profile of the citizen developer. Some experts may imagine a technically advanced business analyst, while others may imagine a non-technical domain specialist. The survey instructions attempted to reduce this ambiguity by defining the target user as a business user without formal IT education.

Third, Usage Intensity may vary across specific platforms and implementation contexts. A skill may be central in one LCDP but peripheral in another. The framework partially addresses this issue by combining skill weights with platform-specific skill requirement variables `x_{ijk}`, but some contextual variation remains unavoidable.

Fourth, the product formulation `w_j=d_j\times u_j` is transparent and interpretable, but it assumes multiplicative interaction between difficulty and usage. Alternative formulations, such as additive weighting or fuzzy aggregation, could be explored in future work.

Fifth, the Round 2 refinement targeted only low-consensus skills. This was intentional to reduce expert fatigue, but it means that high- and moderate-consensus skills were not re-evaluated in the second round.

---

# 19. Ethical and Data-Protection Considerations

The analytical dataset uses anonymized expert identifiers. No personal names are required for reproducing the analysis. If expert metadata are included in the public repository, they should be reported only in aggregated or categorical form, such as years-of-experience bands or role categories.

The public data release should avoid disclosing information that could identify individual experts. The recommended public dataset should contain:

- anonymized expert ID,
- round number,
- skill ID,
- skill name,
- stage,
- task,
- usage rating,
- difficulty rating,
- synthetic weight.

If comments contain identifying information, they should be reviewed and anonymized before publication.

---

# 20. Conclusion

The expert survey provides a reliable and reproducible empirical foundation for the skill-weighting component of the Two-Level IT Skill Burden Framework. A structured Round 1 survey of 15 experts produced complete ratings for 209 IT skills. Reliability analysis showed strong panel-level consistency for the two primary rating constructs and acceptable-to-good reliability for the derived synthetic weights.

A targeted Round 2 Delphi refinement was conducted for 46 low-consensus skills. This refinement improved consensus for all targeted skills and increased the reliability of the final synthetic weights. The resulting final consensus-weight dataset is suitable for use in the Total IT Skill Burden Index and strengthens the methodological credibility of the LCDP platform assessment.

The survey protocol, expert-level datasets, scripts, and output reports should be included in the public reproducibility repository and cited in the final manuscript.

---

# Appendix A. Usage Intensity Scale

| Value | Label | Definition |
|---:|---|---|
| 1 | Rare / avoidable | The skill is rarely needed and can usually be avoided through platform features, templates, or alternative workflows. |
| 2 | Occasional / peripheral | The skill is needed only in limited cases or for non-core tasks. |
| 3 | Moderate / recurring | The skill is used in several typical tasks but is not continuously required. |
| 4 | Frequent / important | The skill is required in many typical tasks and has a clear effect on successful platform use. |
| 5 | Essential / continuous | The skill is central to the phase and is required for most relevant tasks or for completing the phase effectively. |

# Appendix B. Difficulty of Acquisition Scale

| Value | Label | Definition |
|---:|---|---|
| 1 | Very easy | Can be learned quickly by a non-IT user with minimal instruction or self-guided exploration. |
| 2 | Easy | Requires limited training or practice, but no significant technical background. |
| 3 | Moderate | Requires structured learning and repeated practice; some technical concepts may be unfamiliar. |
| 4 | Difficult | Requires substantial training, technical reasoning, or prior exposure to IT concepts. |
| 5 | Very difficult | Requires advanced technical knowledge, formal IT background, or extended practice to apply reliably. |

# Appendix C. Core Equations

Expert-level synthetic weight:

```math
w_{j,e}=u_{j,e}\times d_{j,e}.
```

Final consensus weight:

```math
\bar{w}^{*}_j = \frac{1}{15}\sum_{e=1}^{15} w^{*}_{j,e}.
```

Phase-specific burden:

```math
F_{P_k}(y^i)=\sum_{c_j\in C_{IT,P_k}} \bar{w}^{*}_jx_{ijk}.
```

Total IT Skill Burden Index:

```math
F_{\mathrm{Total}}(y^i)=F_{P_A}(y^i)+F_{P_D}(y^i)+F_{P_I}(y^i).
```

# Appendix D. Key Numerical Results

| Result | Value |
|---|---:|
| Experts | 15 |
| Skills in Round 1 | 209 |
| Round 1 expert-skill observations | 3,135 |
| Low-consensus skills selected for Round 2 | 46 |
| Round 2 expert-skill observations | 690 |
| Missing or invalid Round 1 ratings | 0 |
| Missing or invalid Round 2 ratings | 0 |
| Skills with reduced `SD_w` after Round 2 | 46 / 46 |
| Mean change in `SD_w` after Round 2 | -1.414 |
| Final average-expert ICC, Usage Intensity | 0.8925 |
| Final average-expert ICC, Difficulty of Acquisition | 0.9468 |
| Final average-expert ICC, Synthetic Weight | 0.8335 |
