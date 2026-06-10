# Round 3 pairwise platform-ranking validation data

This directory contains anonymized reproducibility data for the Round 3 direct pairwise platform-ranking validation experiment.

## Purpose

Round 3 validates the final Total IT Skill Burden Index (Total ISBI) platform ranking using independent expert judgments. Unlike Rounds 1 and 2, it does not estimate or refine skill weights. Instead, experts compare platform pairs and indicate which platform imposes a lower expected IT skill burden for citizen developers.

## Reference ranking

Lower Total ISBI means lower expected IT skill burden:

1. Aurea
2. Google AppSheet
3. OutSystems
4. Zoho Creator
5. Microsoft Power Apps
6. Mendix

## Files

- `round3_pairwise_comparisons_anonymized.csv` — one row per expert/platform-pair comparison.
- `round3_platform_familiarity_anonymized.csv` — expert self-rated familiarity for each platform.
- `round3_pairwise_agreement_summary.csv` — agreement summary by platform pair.
- `round3_expert_summary_anonymized.csv` — anonymized expert-level response summary.
- `round3_validation_summary.txt` — plain-text summary of the validation results.

Raw expert identifiers and original filenames are not included in the public dataset. Public expert IDs are anonymized as `R3E01` to `R3E15`.

## Reproduction

Run:

    python analysis/analyze_round3_pairwise_validation.py

Expected output:

- 15 experts
- 225 total pairwise rows
- 187 substantive comparisons
- 28 cannot judge responses
- 10 tie / no clear difference responses
- 144 framework-consistent substantive comparisons
- 77.01% pairwise agreement
- 72/88 = 81.82% agreement when both familiarity scores are >= 2
