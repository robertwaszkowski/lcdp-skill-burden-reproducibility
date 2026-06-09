#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parents[1]
pkg = ROOT / "data" / "platform_score_package"
dataset_path = pkg / "lcdp_skill_burden_dataset.xlsx"
final_weights_path = ROOT / "data" / "processed" / "final_consensus_weights_after_round2.csv"

platforms = [
    "Aurea",
    "Google AppSheet",
    "OutSystems",
    "Zoho Creator",
    "Microsoft Power Apps",
    "Mendix",
]

def norm_skill_id(x):
    if pd.isna(x):
        return ""
    s = str(x).strip()
    if s.upper().startswith("SK"):
        digits = "".join(ch for ch in s if ch.isdigit())
        return f"SK{int(digits):03d}" if digits else s
    if s.replace(".", "", 1).isdigit():
        return f"SK{int(float(s)):03d}"
    return s

def main():
    matrix = pd.read_excel(dataset_path, sheet_name="Platform_Skill_Matrix")
    weights = pd.read_excel(dataset_path, sheet_name="Skill_Taxonomy_Weights")
    final = pd.read_csv(final_weights_path)

    matrix["Skill_ID_norm"] = matrix["Skill_ID"].map(norm_skill_id)
    weights["Skill_ID_norm"] = weights["Skill_ID"].map(norm_skill_id)
    final["Skill_ID_norm"] = final["skill_id"].map(norm_skill_id)

    for p in platforms:
        matrix[p] = matrix[p].fillna(0).astype(float)

    check = weights[["Skill_ID_norm", "Usage_Intensity", "Difficulty_of_Acquisition", "Synthetic_Weight"]].merge(
        final[["Skill_ID_norm", "usage_mean", "difficulty_mean", "weight_mean"]],
        on="Skill_ID_norm",
        how="outer",
        indicator=True,
    )

    check["Usage_Diff"] = check["Usage_Intensity"] - check["usage_mean"]
    check["Difficulty_Diff"] = check["Difficulty_of_Acquisition"] - check["difficulty_mean"]
    check["Synthetic_Diff"] = check["Synthetic_Weight"] - check["weight_mean"]

    if set(check["_merge"]) != {"both"} or check[["Usage_Diff", "Difficulty_Diff", "Synthetic_Diff"]].abs().max().max() > 1e-9:
        print("ERROR: Skill_Taxonomy_Weights does not match final 15-expert consensus weights.")
        print(check.sort_values("Synthetic_Diff", key=lambda s: s.abs(), ascending=False).head(20).to_string(index=False))
        return 1

    df = matrix[matrix["Skill_ID_norm"] != ""].merge(
        weights[["Skill_ID_norm", "Synthetic_Weight"]],
        on="Skill_ID_norm",
        how="left",
        validate="many_to_one",
    )

    rows = []
    for p in platforms:
        tmp = df.assign(weighted=df[p] * df["Synthetic_Weight"].fillna(0))
        phase = tmp.groupby("Project_Stage")["weighted"].sum().to_dict()
        rows.append({
            "Platform": p,
            "Design": phase.get("Design", 0.0),
            "Development": phase.get("Development", 0.0),
            "Implementation": phase.get("Implementation", 0.0),
        })

    phase_scores = pd.DataFrame(rows)
    phase_scores["Total_Score"] = phase_scores[["Design", "Development", "Implementation"]].sum(axis=1)
    phase_scores["Rank"] = phase_scores["Total_Score"].rank(method="min", ascending=True).astype(int)
    phase_scores = phase_scores.sort_values("Rank").reset_index(drop=True)

    print("Final 15-expert phase scores:")
    print(phase_scores.to_string(index=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
