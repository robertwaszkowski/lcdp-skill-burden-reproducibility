# Phase 1: Expert Surveys (Delphi Method)

This directory contains the scripts and data for calculating expert-derived skill weights and establishing reliability for the IT Skill Burden framework.

## Purpose
Phase 1 uses a two-round expert Delphi survey to derive synthetic weights for each of the 209 IT skills. These weights are based on:
1. **Usage Intensity**: How often/strongly a skill is required.
2. **Difficulty of Acquisition**: How difficult the skill is for non-IT-trained users to acquire.

## Pipeline Scripts
- `01_process_expert_surveys_round1.py`: Processes the first round of expert surveys to establish initial synthetic weights and identify low-consensus skills.
- `02_process_expert_surveys_round2.py`: Processes the second round of surveys targeting the low-consensus skills to refine the weights via the Delphi method.

## Data Directories
- `input/`: Contains the raw expert survey data.
- `output/`: Stores the generated consensus weights, descriptive statistics, and reliability metrics (e.g., Cronbach's alpha, ICC).

## Reproduction
Run the scripts sequentially to reproduce Phase 1:
```bash
python 01_process_expert_surveys_round1.py
python 02_process_expert_surveys_round2.py
```
