# LCDP Skill Burden Dataset and Calculation Package

This package supports reproducibility for the manuscript on the Two-Level IT Skill Burden Framework for low-code platform selection in Citizen Development.

## Files

### lcdp_skill_burden_dataset.xlsx

Curated input dataset. It contains:
- README: dataset-level notes.
- Platform_Review: documentation-based platform review of the evaluated LCDPs.
- Skill_Taxonomy_Weights: extracted IT skills with final 15-expert Round 2 consensus weights.
- Platform_Skill_Matrix: normalized binary platform-skill requirement matrix, where 1 means that a skill is required and 0 means that it is not required.
- Data_Dictionary: definitions of fields and variables.

Important: in the repaired final version, Synthetic_Weight is the final consensus weight_mean from final_consensus_weights_after_round2.csv. It is the mean of expert-level Usage x Difficulty values after Round 2. It is not recomputed as Usage_Intensity mean multiplied by Difficulty_of_Acquisition mean.

### lcdp_skill_burden_calculations.xlsx

Corrected derived calculation workbook generated from the final 15-expert Round 2 consensus weights. It contains:
- README: calculation notes.
- Phase_Scores: phase-specific and total IT skill-burden scores for each LCDP.
- Final_Ranking: final ranking by Total ISBI.
- Weight_Set_Check: verification that the workbook weights match the final 15-expert consensus weights.
- Phase8I_Ablation_Diagnostic: diagnostic comparison showing that the unweighted requirement-count ranking is identical to the weighted Total ISBI ranking.

Previous sensitivity and switching-point sheets based on the older weight set were intentionally removed. They must be recomputed before being cited or used in the manuscript.

## Reproduction workflow

1. Start with lcdp_skill_burden_dataset.xlsx.
2. Review the source platform documentation mapping in Platform_Review.
3. Use the normalized skill requirement indicators in Platform_Skill_Matrix.
4. Use the final Round 2 consensus weights from Skill_Taxonomy_Weights.
5. Reproduce phase-specific burden indices and total ranking from lcdp_skill_burden_calculations.xlsx.

## Current final 15-expert Total ISBI ranking

| Rank | Platform | Total ISBI |
| ---: | --- | ---: |
| 1 | Aurea | 301.5333 |
| 2 | Google AppSheet | 478.2667 |
| 3 | OutSystems | 510.6667 |
| 4 | Zoho Creator | 531.5333 |
| 5 | Microsoft Power Apps | 562.0000 |
| 6 | Mendix | 718.7333 |

## Phase 8I diagnostic decision

The unweighted requirement-count ranking is identical to the weighted Total ISBI ranking. Therefore, the ablation diagnostic is retained as a reproducibility check but is not recommended as an additional manuscript table or subsection.

## Notes

This package verifies the curated dataset and derived calculation outputs. It does not claim automatic regeneration of the platform-skill matrix from raw vendor documentation.
