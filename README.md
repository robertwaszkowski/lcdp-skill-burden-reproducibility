# Two-Level IT Skill Burden Framework for Low-Code Platform Selection

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20682925.svg)](https://doi.org/10.5281/zenodo.20682925)

This repository contains the reproducibility package for the study introducing the **Two-Level IT Skill Burden Framework** for evaluating low-code development platforms in the context of **Citizen Development**.

The framework quantifies the IT skill burden imposed by low-code development platforms using expert-derived skill weights, lifecycle-phase decomposition, reliability analysis, Delphi refinement, and sensitivity analysis. It extends prior count-based assessment of IT competency requirements by introducing validated weights that reflect both the usage intensity and difficulty of acquisition of individual IT skills.

## Repository contents

To clearly reflect the sequence of analytical steps, the repository is organized into pipeline phases. **Each phase has its own detailed README:**

* **[Phase 1: Expert Surveys](01_expert_surveys/README.md)** (`01_expert_surveys/`)
* **[Phase 2: Platform Burden](02_platform_burden/README.md)** (`02_platform_burden/`)
* **[Phase 3: Sensitivity Analysis](03_sensitivity/README.md)** (`03_sensitivity/`)
* **[Phase 4: Round 3 Validation](04_validation_round3/README.md)** (`04_validation_round3/`)

```text
.
├── 01_expert_surveys/
│   ├── input/     # Raw expert survey ZIP archives
│   ├── output/    # Consensus weights and reliability metrics
│   ├── 01_process_expert_surveys_round1.py
│   └── 02_process_expert_surveys_round2.py
│
├── 02_platform_burden/
│   ├── input/     # Platform-skill matrix CSVs
│   ├── output/    # Phase scores and final ranking
│   └── 03_calculate_platform_scores.py
│
├── 03_sensitivity/
│   ├── output/    # Sensitivity and robustness metrics
│   └── 04_run_sensitivity_analysis.py
│
├── 04_validation_round3/
│   ├── input/     # Round 3 pairwise validation datasets
│   ├── output/    # Validation summary metrics
│   └── 05_analyze_round3_validation.py
│
├── .venv/         # Python virtual environment (if created)
├── README.md
├── LICENSE
└── CITATION.cff
```

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

The validation package is based on a two-round expert Delphi survey, followed by a third-round validation.

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

### 2. Create a Python environment and Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas openpyxl scipy
```

### 3. Run the complete pipeline

The scripts are sequentially numbered. You can reproduce the entire pipeline by running:

```bash
# Phase 1: Delphi expert consensus
python 01_expert_surveys/01_process_expert_surveys_round1.py
python 01_expert_surveys/02_process_expert_surveys_round2.py

# Phase 2: Platform Burden Calculations
python 02_platform_burden/03_calculate_platform_scores.py

# Phase 2b: Sensitivity Analysis
python 03_sensitivity/04_run_sensitivity_analysis.py

# Phase 3: Pairwise Validation
python 04_validation_round3/05_process_expert_surveys_round3.py
python 04_validation_round3/06_analyze_round3_validation.py
```

The expected Total ISBI ranking (found in `02_platform_burden/output/final_ranking.csv`) is:

| Rank | Platform | Total ISBI |
| ---: | --- | ---: |
| 1 | Aurea | 301.5333 |
| 2 | Google AppSheet | 478.2666 |
| 3 | OutSystems | 510.6666 |
| 4 | Zoho Creator | 531.5333 |
| 5 | Microsoft Power Apps | 562.0000 |
| 6 | Mendix | 718.7333 |


## Citation

Please cite this repository using the Zenodo DOI:

```text
Waszkowski, R. Two-Level IT Skill Burden Framework for Low-Code Platform Selection: Reproducibility Package. Zenodo. https://doi.org/10.5281/zenodo.20682925
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
