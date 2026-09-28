# Source workbook for keyword classification

[`table__it_skills_updated_20241021_RW.xlsx`](table__it_skills_updated_20241021_RW.xlsx) contains the historical workbook documenting the extraction and generalization of technical terms from LCDP documentation. The 2026-09-28 correction unifies `Enumeration` with the source label `Enumerations` (SK015) and updates its directly affected cached assignments and database-model counts. All formula expressions and package parts are preserved; Excel is instructed to recalculate on opening. Unrelated historical cached formula errors have not been repaired. SK185 (`.NET Framework`, OutSystems client installation) was already present in this workbook; its correction applies to the CSV matrix.

## Relevant worksheets

- **Platform review** records the platform, project stage, task, documentation URL(s), and extracted keywords. Its 127 rows match `../input/platform_review.csv`, apart from a trailing space in one keyword cell (E54).
- **CLASSIFICATION** records source keywords and their classification into generalized concepts, with project-stage and functional-scope context. Columns C and D contain `Keyword` and `Classification (Generalized keyword)`. For example, `Foreign Key`, `Primary Key`, and `One-to-Many` are mapped to `Relational Database`. These are distinct technical concepts grouped into a broader category, not synonyms.
- **TABELA_UNIQUE** includes generalized and original keywords and platform assignments. The workbook also retains intermediate tables and LaTeX export worksheets.

## Relation to the current reproducibility pipeline

This is a historical source workbook documenting how the terminology was classified. It contains earlier importance weights and intermediate calculations. Some derived cells, including cells in the `TABELA_UNIQUE` and LaTeX export worksheets, retain cached formula errors. The `Platform review` and `CLASSIFICATION` worksheets contain no cached Excel error values in the inspected copy.

Use the curated CSV files in `../input/`, the final consensus weights in `../../01_expert_surveys/output/`, and the repository scripts to reproduce the current study results. The workbook is supporting provenance and is not a replacement for those calculation inputs.

SHA-256 of the corrected workbook:

```text
029aa768a775a3faa0c36831c9b9d3bc73eafcf997fee466217fb0ce4f3e7ea9
```

The original workbook remains available at commit `bb6c082e6388da3bb3cb5127b1ff3275bc99bbbb` (SHA-256 `6a14c270446ddac107494c64b8083829ff825016e7488c2c5e92c568a33d5242`). The historical Important-skills subset is unaffected: SK015 is excluded by its Importance filter, and SK185 was already included.
