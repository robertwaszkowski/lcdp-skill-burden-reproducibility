# Phase 3: Sensitivity Analysis

This directory contains the scripts and results for the sensitivity and robustness analysis of the IT Skill Burden framework.

## Purpose
Phase 3 validates the stability of the platform ranking produced in Phase 2. It assesses how sensitive the final Total IT Skill Burden Index (Total ISBI) is to:
- Perturbations in the expert-derived skill weights.
- Changes to the aggregation assumptions or lifecycle-phase priorities.

## Pipeline Scripts
- `04_run_sensitivity_analysis.py`: Executes the sensitivity scenarios and calculates robustness metrics for the rankings.

## Data Directories
- `output/`: Stores the sensitivity results, robustness metrics, and any generated plots or summary tables.

## Reproduction
Ensure Phase 2 is completed first, then run:
```bash
python 04_run_sensitivity_analysis.py
```
