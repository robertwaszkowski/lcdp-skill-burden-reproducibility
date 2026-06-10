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

## Reproduction
Ensure Phase 1 is completed first, then run:
```bash
python 03_calculate_platform_scores.py
```
