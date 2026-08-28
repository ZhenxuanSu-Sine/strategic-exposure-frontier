from __future__ import annotations

import csv
import json
from pathlib import Path


def run(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    ns = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    rows = []
    for n in ns:
        p_hard = 1.0 / n
        peak = float(n)
        workload = p_hard * peak
        rows.append({
            "n": n,
            "p_hard": p_hard,
            "peak_capability": peak,
            "on_policy_workload": workload,
            "gap_ratio": peak / workload,
        })
    csv_path = output_dir / "e18_rare_hard_gap.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    summary = {
        "experiment": "E18",
        "claim": "on-policy expected workload remains 1 while peak capability grows with n",
        "max_peak": rows[-1]["peak_capability"],
        "max_workload_deviation_from_1": max(abs(r["on_policy_workload"] - 1.0) for r in rows),
    }
    (output_dir / "e18_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(run(Path("results")))
