"""Check IT catalogue coverage, including the documented SK113 label correction."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def main():
    matrix = read(ROOT / "02_platform_burden/input/platform_skill_matrix.csv")
    weights = read(ROOT / "01_expert_surveys/output/final_consensus_weights_after_round2.csv")
    expected = {f"SK{int(row['skill_id']):03d}" for row in weights
                if not row['skill_name'].startswith('+') or int(row['skill_id']) == 113}
    actual = [row['Skill_ID'] for row in matrix]
    if len(actual) != len(set(actual)) or set(actual) != expected:
        raise ValueError(f"Matrix coverage mismatch: missing={expected-set(actual)}, extra={set(actual)-expected}; duplicates={len(actual)-len(set(actual))}")
    print(f"Validated {len(actual)} unique IT entries; {len(weights)-len(expected)} domain entries excluded from {len(weights)} survey items.")

if __name__ == '__main__':
    main()
