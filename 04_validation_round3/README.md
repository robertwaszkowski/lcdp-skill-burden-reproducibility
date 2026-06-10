# Phase 4: Round 3 Validation

This directory contains the scripts and anonymized data for the Phase 3 pairwise validation of the IT Skill Burden platform ranking.

## Purpose

Round 3 validates the final Total IT Skill Burden Index (Total ISBI) platform ranking using independent expert judgments. Unlike Rounds 1 and 2, it does not estimate or refine skill weights. Instead, experts compare platform pairs and indicate which platform imposes a lower expected IT skill burden for citizen developers.

## Pipeline Scripts

- `05_process_expert_surveys_round3.py`: Processes the raw (anonymized) Round 3 survey responses.
- `06_analyze_round3_validation.py`: Analyzes the pairwise comparisons against the reference ISBI ranking and computes agreement percentages.

## Reference Ranking

The reference ranking produced by Phase 2 (lower Total ISBI means lower expected IT skill burden):
1. Aurea
2. Google AppSheet
3. OutSystems
4. Zoho Creator
5. Microsoft Power Apps
6. Mendix

## Input Data (`input/`)

Contains anonymized reproducibility data for the Round 3 experiment:
- `round3_pairwise_comparisons_anonymized.csv` — one row per expert/platform-pair comparison.
- `round3_platform_familiarity_anonymized.csv` — expert self-rated familiarity for each platform.
- `round3_pairwise_agreement_summary.csv` — agreement summary by platform pair.
- `round3_expert_summary_anonymized.csv` — anonymized expert-level response summary.
- `round3_validation_summary.txt` — plain-text summary of the validation results.

*(Raw expert identifiers are anonymized as `R3E01` to `R3E15`.)*

## Reproduction

To reproduce this phase, run the scripts sequentially:
```bash
python 05_process_expert_surveys_round3.py
python 06_analyze_round3_validation.py
```

Expected validation output includes:
- 15 experts, 225 total pairwise rows
- 187 substantive comparisons
- 77.01% pairwise agreement
- 81.82% agreement when both familiarity scores are >= 2
