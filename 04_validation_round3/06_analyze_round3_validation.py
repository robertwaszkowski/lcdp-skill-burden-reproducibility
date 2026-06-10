#!/usr/bin/env python3
"""Reproduce Round 3 direct pairwise platform-ranking validation results.

This script reads the anonymized Round 3 pairwise comparison data and reproduces
the agreement rates reported in the manuscript.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "output"
OUT = ROOT / "output"

pairwise_path = DATA / "round3_pairwise_comparisons_anonymized.csv"
if not pairwise_path.exists():
    raise FileNotFoundError(f"Missing input file: {pairwise_path}")

df = pd.read_csv(pairwise_path)

sub = df[df["is_substantive"] == 1].copy()
cannot = int(df["is_cannot_judge"].sum())
ties = int(df["is_tie"].sum())
consistent = int(sub["is_framework_consistent"].astype(int).sum())

both = sub[sub["both_familiarity_ge_2"] == 1].copy()
both_consistent = int(both["is_framework_consistent"].astype(int).sum())

n_experts = df["expert_id"].nunique()
total_rows = len(df)
substantive = len(sub)
agreement = consistent / substantive
both_n = len(both)
both_agreement = both_consistent / both_n

output_text = [
    "Round 3 direct pairwise platform-ranking validation\n",
    f"experts: {n_experts}",
    f"total pairwise rows: {total_rows}",
    f"substantive comparisons: {substantive}",
    f"cannot judge responses: {cannot}",
    f"tie / no clear difference responses: {ties}",
    f"framework-consistent substantive comparisons: {consistent}",
    f"pairwise agreement: {agreement:.4f} ({agreement*100:.2f}%)\n",
    "Familiarity-filtered subset",
    f"substantive comparisons with both familiarity scores >= 2: {both_n}",
    f"framework-consistent comparisons in subset: {both_consistent}",
    f"agreement in subset: {both_agreement:.4f} ({both_agreement*100:.2f}%)\n",
]

for line in output_text:
    print(line)

OUT.mkdir(parents=True, exist_ok=True)
with open(OUT / "validation_summary.txt", "w") as f:
    f.write("\n".join(output_text))

expected = {
    "experts": 15,
    "total_rows": 225,
    "substantive": 187,
    "cannot": 28,
    "ties": 10,
    "consistent": 144,
    "both_n": 88,
    "both_consistent": 72,
}

actual = {
    "experts": n_experts,
    "total_rows": total_rows,
    "substantive": substantive,
    "cannot": cannot,
    "ties": ties,
    "consistent": consistent,
    "both_n": both_n,
    "both_consistent": both_consistent,
}

for key, expected_value in expected.items():
    actual_value = actual[key]
    if actual_value != expected_value:
        raise AssertionError(f"{key}: expected {expected_value}, got {actual_value}")

print("ROUND 3 VALIDATION REPRODUCTION PASS")
