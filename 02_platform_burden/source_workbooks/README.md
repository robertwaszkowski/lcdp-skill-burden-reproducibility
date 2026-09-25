# Source workbook for keyword classification

[`table__it_skills_updated_20241021_RW.xlsx`](table__it_skills_updated_20241021_RW.xlsx) preserves the original workbook documenting the extraction and generalization of technical terms from LCDP documentation. The workbook is provided unchanged, including its formulas and cached values.

## Relevant worksheets

- **Platform review** records the platform, project stage, task, documentation URL(s), and extracted keywords. Its 127 rows match `../input/platform_review.csv`, apart from a trailing space in one keyword cell (E54).
- **CLASSIFICATION** records source keywords and their classification into generalized concepts, with project-stage and functional-scope context. Columns C and D contain `Keyword` and `Classification (Generalized keyword)`. For example, `Foreign Key`, `Primary Key`, and `One-to-Many` are mapped to `Relational Database`. These are distinct technical concepts grouped into a broader category, not synonyms.
- **TABELA_UNIQUE** includes generalized and original keywords and platform assignments. The workbook also retains intermediate tables and LaTeX export worksheets.

## Relation to the current reproducibility pipeline

This is a historical source workbook documenting how the terminology was classified. It contains earlier importance weights and intermediate calculations. Some derived cells, including cells in the `TABELA_UNIQUE` and LaTeX export worksheets, retain cached formula errors. The `Platform review` and `CLASSIFICATION` worksheets contain no cached Excel error values in the inspected copy.

Use the curated CSV files in `../input/`, the final consensus weights in `../../01_expert_surveys/output/`, and the repository scripts to reproduce the current study results. The workbook is supporting provenance and is not a replacement for those calculation inputs.

SHA-256 of the unchanged workbook:

```text
6a14c270446ddac107494c64b8083829ff825016e7488c2c5e92c568a33d5242
```
