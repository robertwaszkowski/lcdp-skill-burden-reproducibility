# LCDP Skill Burden Dataset and Calculation Package

This package supports reproducibility for the manuscript:

**Extending the CD Score for Low-Code Platform Evaluation: A Two-Level Multi-Criteria Model of IT Skill Burden in Citizen Development**

## Files

### lcdp_skill_burden_dataset.xlsx
Curated input dataset. It contains:
- `Platform_Review`: original documentation-based review of the evaluated LCDPs.
- `Skill_Taxonomy_Weights`: extracted IT skills with expert-survey-based Usage Intensity, Difficulty of Acquisition, and Synthetic Weight.
- `Platform_Skill_Matrix`: normalized binary platform-skill requirement matrix, where `1` means that a skill is required and `0` means that it is not required.
- `Sources`: source URLs used in the platform review.
- `Data_Dictionary`: definitions of fields and variables.

### lcdp_skill_burden_calculations.xlsx
Derived calculation workbook. It contains:
- `Phase_Scores`: phase-specific and total IT skill-burden scores for each LCDP.
- `Final_Ranking`: final ranking by the Phase-Aware Weighted CD Score.
- `Sensitivity_Skill_Weights`: ranking under ±20% perturbation of selected skill weights.
- `Sensitivity_Phase_Weights`: ranking under alternative phase-priority scenarios.
- `Sensitivity_Aggregation`: ranking under alternative Minkowski parameters.
- `Switching_Points`: numerical details of the OutSystems vs. Zoho Creator switching-point analysis.
- `Top_10_Skills` and `Expensive_Categories`: additional diagnostic summaries.

## Reproduction workflow

1. Start with `lcdp_skill_burden_dataset.xlsx`.
2. Review the source platform documentation mapping in `Platform_Review`.
3. Use the normalized skill requirement indicators in `Platform_Skill_Matrix`.
4. Use `Usage_Intensity` and `Difficulty_of_Acquisition` from `Skill_Taxonomy_Weights` to calculate `Synthetic_Weight = Usage_Intensity × Difficulty_of_Acquisition`.
5. Reproduce the phase-specific burden indices and total ranking using the tables in `lcdp_skill_burden_calculations.xlsx`.

## Notes

The original working files contained duplicated intermediate transformations and working-copy filenames. This cleaned package consolidates those materials into a publication-oriented dataset and a separate calculation workbook.
