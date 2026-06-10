#!/usr/bin/env python3
"""Process raw Round 3 validation survey Excel files.

Reads all Direct_Platform_Ranking_*.xlsx files, extracts familiarity and pairwise
comparisons, and outputs the anonymized intermediate datasets.
"""

from pathlib import Path
import sys
import pandas as pd
import glob
import zipfile
import shutil

ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"
EXTRACT_DIR = INPUT_DIR / "_extract"
ZIP_PATH = INPUT_DIR / "completed_expert_surveys_round3_FINAL.zip"

FRAMEWORK_RANKING = [
    "Aurea",
    "Google AppSheet",
    "OutSystems",
    "Zoho Creator",
    "Microsoft Power Apps",
    "Mendix"
]

def get_framework_preferred(platform_a, platform_b):
    try:
        idx_a = FRAMEWORK_RANKING.index(platform_a)
        idx_b = FRAMEWORK_RANKING.index(platform_b)
        return platform_a if idx_a < idx_b else platform_b
    except ValueError:
        return ""

def process_expert_file(file_path, expert_id_anonymized):
    xlsx = pd.ExcelFile(file_path)
    
    # 1. Parse Familiarity
    df_fam = pd.read_excel(xlsx, "Platform_Familiarity")
    fam_dict = {}
    for _, row in df_fam.iterrows():
        fam_dict[row["Platform"]] = row["Familiarity_0_3"]
        
    # 2. Parse Pairwise Comparisons
    df_pairs = pd.read_excel(xlsx, "Pairwise_Comparisons")
    
    # Filter out empty rows and summary stats at the bottom
    df_pairs = df_pairs[df_pairs["Pair_ID"].astype(str).str.startswith("P")]
    
    parsed_rows = []
    for _, row in df_pairs.iterrows():
        platform_a = row["Platform_A"]
        platform_b = row["Platform_B"]
        expert_choice = row["Expert_choice"]
        
        fam_a = fam_dict.get(platform_a, 0)
        fam_b = fam_dict.get(platform_b, 0)
        
        expert_preferred = ""
        is_substantive = 0
        is_tie = 0
        is_cannot_judge = 0
        is_framework_consistent = None
        
        if pd.isna(expert_choice):
            is_cannot_judge = 1
        elif expert_choice == "Tie / no clear difference":
            is_tie = 1
        elif expert_choice == "Cannot judge":
            is_cannot_judge = 1
        elif str(expert_choice).endswith(" lower burden"):
            is_substantive = 1
            expert_preferred = str(expert_choice).replace(" lower burden", "")
        
        framework_preferred = get_framework_preferred(platform_a, platform_b)
        
        if is_substantive == 1:
            is_framework_consistent = 1 if expert_preferred == framework_preferred else 0
            
        both_familiarity_ge_2 = 1 if (fam_a >= 2 and fam_b >= 2) else 0
        
        parsed_rows.append({
            "expert_id": expert_id_anonymized,
            "pair_id": row["Pair_ID"],
            "platform_a": platform_a,
            "platform_b": platform_b,
            "fam_a": fam_a,
            "fam_b": fam_b,
            "expert_choice": expert_choice if pd.notna(expert_choice) else "",
            "expert_preferred": expert_preferred,
            "framework_preferred": framework_preferred,
            "is_substantive": is_substantive,
            "is_tie": is_tie,
            "is_cannot_judge": is_cannot_judge,
            "is_framework_consistent": is_framework_consistent,
            "both_familiarity_ge_2": both_familiarity_ge_2
        })
        
    return pd.DataFrame(parsed_rows), fam_dict

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    if EXTRACT_DIR.exists():
        shutil.rmtree(EXTRACT_DIR)
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"Extracting {ZIP_PATH.name}...")
    with zipfile.ZipFile(ZIP_PATH) as archive:
        archive.extractall(EXTRACT_DIR)
    
    files = sorted(glob.glob(str(EXTRACT_DIR / "Direct_Platform_Ranking_*.xlsx")))
    if not files:
        print(f"No Excel files found in {EXTRACT_DIR}")
        return 1
        
    all_pairs = []
    
    expert_idx = 1
    for file_path in files:
        anonymized_id = f"R3E{expert_idx:02d}"
        
        df_pairs, _ = process_expert_file(file_path, anonymized_id)
        all_pairs.append(df_pairs)
        
        expert_idx += 1
        
    final_df = pd.concat(all_pairs, ignore_index=True)
    
    out_csv = OUTPUT_DIR / "round3_pairwise_comparisons_anonymized.csv"
    final_df.to_csv(out_csv, index=False)
    
    if EXTRACT_DIR.exists():
        shutil.rmtree(EXTRACT_DIR)
    
    print(f"Processed {len(files)} files.")
    print(f"Output saved to {out_csv}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
