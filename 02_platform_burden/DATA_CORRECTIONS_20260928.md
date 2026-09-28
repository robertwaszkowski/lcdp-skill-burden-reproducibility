# Correction of SK015 and SK185 — 2026-09-28

## Input changes

- SK015 (Design / Database model): unified `Enumeration` with `Enumerations` in the historical workbook. Restored Google AppSheet and Aurea assignments from `Platform review`. CSV row MK009 now carries SK015 and these two indicators.
- SK185 (Implementation / Client module installation / .NET Framework): restored the missing CSV row as MK163, with OutSystems=1. This assignment was already present in the workbook and source review. The historical cause of its omission from the CSV has not been established.
- The corrected matrix contains 163 distinct survey IDs: all 209 catalogue entries except 46 domain-skill entries. SK113 follows the previously documented canonical classification. Survey ratings and consensus weights are unchanged.

## Recomputed results

The scripts `02_platform_burden/03_calculate_platform_scores.py` and `03_sensitivity/04_run_sensitivity_analysis.py` regenerate the committed outputs.

| Platform | Previous total | Corrected total |
|---|---:|---:|
| Aurea | 301.533333 | 312.200000 |
| Google AppSheet | 478.266667 | 488.933333 |
| OutSystems | 510.666667 | 522.400000 |

Other totals and baseline ranks are unchanged. The baseline ordering used in Round 3 validation is therefore unchanged.

- Reducing the selected Application Logic & Programming weights by 20% now exchanges OutSystems and Zoho Creator; increasing them by 20% preserves the baseline order. Spearman correlations: 0.942857 and 1.0 respectively. The selected subset has 66 rows because its existing keyword rule includes .NET Framework. First changes on the existing grid occur at -15% and +50%.
- In the Design-dominant scenario, Aurea ranks fourth, Zoho Creator second, Microsoft Power Apps third.
- For p=2, q=1, OutSystems ranks fifth and Microsoft Power Apps third; Zoho Creator remains fourth.
- The OutSystems–Zoho Creator baseline gap falls to 9.133333; the average-weight error diagnostic becomes 1. This average is calculated over the full survey catalogue, not only the IT subset, as in the existing script.

## Workbook preservation and historical records

All original worksheet formula expressions, worksheet dimensions, and ZIP package members were preserved. Only the SK015 label and directly affected cached assignments/counts/LaTeX row were changed; full recalculation is requested on opening in Excel. Native Excel recalculation was not run. Pre-existing unrelated cached errors were retained. The filtered Important-skills table is unchanged: SK015 has Importance=-1 and is excluded, while SK185 was already included.

Earlier repository commits and the previously archived Zenodo release retain the former data and results. This correction does not modify that archive or any submitted manuscript. Cite the corrected GitHub commit when reproducing the revised results.
