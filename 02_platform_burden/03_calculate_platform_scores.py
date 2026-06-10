#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import sys

ROOT = Path(__file__).resolve().parents[1]
matrix_path = ROOT / "02_platform_burden" / "input" / "platform_skill_matrix.csv"
final_weights_path = ROOT / "01_expert_surveys" / "output" / "final_consensus_weights_after_round2.csv"
output_dir = ROOT / "02_platform_burden" / "output"

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
    output_dir.mkdir(parents=True, exist_ok=True)
    matrix = pd.read_csv(matrix_path)
    final = pd.read_csv(final_weights_path)

    matrix["Skill_ID_norm"] = matrix["Skill_ID"].map(norm_skill_id)
    final["Skill_ID_norm"] = final["skill_id"].map(norm_skill_id)

    for p in platforms:
        matrix[p] = matrix[p].fillna(0).astype(float)

    # Use weight_mean as the Synthetic_Weight
    df = matrix[matrix["Skill_ID_norm"] != ""].merge(
        final[["Skill_ID_norm", "weight_mean"]],
        on="Skill_ID_norm",
        how="left",
        validate="many_to_one",
    )

    rows = []
    for p in platforms:
        tmp = df.assign(weighted=df[p] * df["weight_mean"].fillna(0))
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
    
    phase_scores.to_csv(output_dir / "phase_scores.csv", index=False)
    phase_scores[["Rank", "Platform", "Total_Score"]].to_csv(output_dir / "final_ranking.csv", index=False)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
