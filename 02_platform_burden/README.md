# Phase 2: Platform Burden Calculations

This directory contains the scripts and data required to compute the IT Skill Burden for the selected low-code development platforms.

## Purpose
Phase 2 applies the expert-derived skill weights (from Phase 1) to the platform-skill-phase matrix. This determines how much IT skill burden each platform imposes during three lifecycle phases:
1. Design/Analysis
2. Development
3. Implementation

## Pipeline Scripts
- `03_calculate_platform_scores.py`: Calculates phase-specific IT Skill Burden Indices and aggregates them into the final Total IT Skill Burden Index (Total ISBI).

## Data Directories
- `input/`: Contains the platform-skill matrix CSV files detailing the required skills for each platform across the three lifecycle phases.
- `output/`: Stores the computed phase scores and the final Total ISBI ranking of the platforms.
- [`source_workbooks/`](source_workbooks/): Original Excel workbook documenting documentation-derived keywords and their classification into generalized concepts. See its README for worksheet descriptions and its relationship to the current calculation inputs.

## Reproduction
Ensure Phase 1 is completed first, then run:
```bash
python 03_calculate_platform_scores.py
```

## Skill label correction (SK113)

The canonical label for SK113 (Development / Data validation development) is
`Column Expressions`. The leading `+` in the historical label
`+Column Expressions` has been removed from `input/platform_skill_matrix.csv`
to match this item's existing treatment as an IT skill in the calculation.
AppSheet column expressions specify column behavior through expressions;
see [AppSheet expressions documentation](https://support.google.com/appsheet/answer/10104642).

This is a label correction: Skill_ID SK113, platform indicators, expert ratings,
weights, and numerical results are unchanged. Historical source workbooks,
submitted survey archives, and the previously generated expert-survey outputs
retain their original labels for traceability. When joining those records to
the current matrix, use Skill_ID (113 / SK113); both labels refer to the same item.
This correction does not reclassify other entries prefixed with `+` and does not
resolve the separate distinction between the full survey catalogue and its IT-skill subset.
