# Two-Level IT Skill Burden Framework for Low-Code Platform Selection

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20529987.svg)](https://doi.org/10.5281/zenodo.20529987)

This repository contains the reproducibility package for the study introducing the **Two-Level IT Skill Burden Framework** for evaluating low-code development platforms in the context of **Citizen Development**.

The framework quantifies the IT skill burden imposed by low-code development platforms using expert-derived skill weights, lifecycle-phase decomposition, reliability analysis, Delphi refinement, and sensitivity analysis. It extends prior count-based assessment of IT competency requirements by introducing validated weights that reflect both the usage intensity and difficulty of acquisition of individual IT skills.

## Repository contents

```text
.
├── analysis/
│   ├── reproduce_expert_survey_round1_analysis.py
│   ├── reproduce_expert_survey_round2_analysis.py
│   └── requirements.txt
│
├── data/
│   ├── raw/
│   │   ├── completed_expert_surveys_round1_FINAL.zip
│   │   └── completed_expert_surveys_round2_FINAL.zip
│   │
│   └── processed/
│       ├── final_expert_survey_long_format_after_round2.csv
│       ├── final_consensus_weights_after_round2.csv
│       ├── expert_reliability_round2_and_final.csv
│       └── round2_convergence_by_skill.csv
│
├── outputs/
│   └── reproduced analysis outputs
│
├── README.md
├── LICENSE
└── CITATION.cff
```

The repository includes raw expert-survey archives, processed datasets, reproducible Python scripts, reliability outputs, convergence-analysis results, and documentation needed to reproduce the expert-survey validation package.

## Study overview

The study evaluates IT skill burden in low-code development platforms using a platform-skill-phase matrix and expert-derived skill weights.

The framework distinguishes three lifecycle phases:

1. Design/Analysis
2. Development
3. Implementation

For each IT skill, expert ratings were collected for:

* **Usage Intensity**: how often or strongly a skill is required;
* **Difficulty of Acquisition**: how difficult the skill is for non-IT-trained users to acquire.

The synthetic skill weight is calculated as:

```text
Synthetic Weight = Usage Intensity × Difficulty of Acquisition
```

These weights are then used to calculate phase-specific IT Skill Burden Indices and a Total IT Skill Burden Index.

## Expert survey design

The validation package is based on a two-round expert survey.

### Round 1

Round 1 included:

* 15 experts;
* 209 IT skills;
* 3,135 expert-skill observations;
* no missing or invalid ratings;
* no duplicate expert-response pairs.

Round 1 reliability results:

| Measure                   | Cronbach’s alpha | ICC, average experts |
| ------------------------- | ---------------: | -------------------: |
| Usage Intensity           |           0.8994 |               0.8759 |
| Difficulty of Acquisition |           0.9507 |               0.9425 |
| Synthetic Weight          |           0.8434 |               0.7897 |

### Round 2 Delphi refinement

Round 2 targeted 46 low-consensus skills identified from high dispersion in synthetic weights.

Round 2 included:

* 46 low-consensus skills;
* 15 experts;
* 690 expert-skill observations;
* no missing or invalid ratings.

All 46 targeted skills showed reduced synthetic-weight standard deviation after Delphi refinement. The mean change in synthetic-weight standard deviation was approximately `-1.414`.

Final reliability after Round 2:

| Measure                   | ICC, average experts |
| ------------------------- | -------------------: |
| Usage Intensity           |               0.8925 |
| Difficulty of Acquisition |               0.9468 |
| Synthetic Weight          |               0.8335 |

## Reproducing the analysis

### 1. Clone the repository

```bash
git clone https://github.com/robertwaszkowski/lcdp-skill-burden-reproducibility.git
cd lcdp-skill-burden-reproducibility
```

### 2. Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r analysis/requirements.txt
```

### 4. Reproduce Round 1 analysis

```bash
python analysis/reproduce_expert_survey_round1_analysis.py
```

### 5. Reproduce Round 2 and final analysis

```bash
python analysis/reproduce_expert_survey_round2_analysis.py
```

The scripts reproduce the expert-survey reliability analysis, Delphi convergence outputs, final consensus weights, and processed datasets.

## Data description

The main processed datasets are:

| File                                               | Description                                                       |
| -------------------------------------------------- | ----------------------------------------------------------------- |
| `final_expert_survey_long_format_after_round2.csv` | Final long-format expert-survey dataset after Round 2 refinement  |
| `final_consensus_weights_after_round2.csv`         | Final consensus skill weights after Delphi refinement             |
| `expert_reliability_round2_and_final.csv`          | Reliability statistics for Round 2 and final expert-weight set    |
| `round2_convergence_by_skill.csv`                  | Skill-level convergence results for the 46 targeted Delphi skills |

The raw survey archives are stored in:

```text
data/raw/
```

## Citation

Please cite this repository using the Zenodo DOI:

```text
Waszkowski, R. Two-Level IT Skill Burden Framework for Low-Code Platform Selection: Reproducibility Package. Zenodo. https://doi.org/10.5281/zenodo.20529856
```

A machine-readable citation file is provided in `CITATION.cff`.

## Related publication

This repository supports the manuscript on the Two-Level IT Skill Burden Framework for low-code platform selection in Citizen Development.

The study builds on prior work introducing the CD Score for evaluating low-code development platforms in terms of Citizen Development assumptions, and advances it by operationalizing and validating expert-derived IT skill burden weights.

## License

This repository is distributed under the license specified in the `LICENSE` file.

## Contact

Robert Waszkowski
Military University of Technology
Email: [robert.waszkowski@wat.edu.pl](mailto:robert.waszkowski@wat.edu.pl)
