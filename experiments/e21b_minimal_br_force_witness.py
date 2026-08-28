from __future__ import annotations

import csv
import json
from pathlib import Path


def run(output_dir: Path) -> dict:
    """Minimal exact witness for payoff-preserving best-response exposure.

    O chooses EASY or HARD. X has a fixed correct policy in both branches.
    Both branches end in the same zero-sum payoff for X (+1), so both are
    payoff-best responses for O (O cannot improve payoff). Under the declared
    implementation, EASY requires 1 query and HARD requires n parity queries.
    Hence a best-response tie can be broken to maximize X workload.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    n = 16
    rows = [
        {"o_move": "EASY", "x_payoff": 1.0, "x_local_query_cost": 1.0, "is_o_best_response": True},
        {"o_move": "HARD", "x_payoff": 1.0, "x_local_query_cost": float(n), "is_o_best_response": True},
    ]
    with (output_dir / "e21b_minimal_br_force_witness.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    summary = {
        "experiment": "E21b",
        "payoff_preserving": rows[0]["x_payoff"] == rows[1]["x_payoff"],
        "reference_best_response_cost": rows[0]["x_local_query_cost"],
        "exposure_maximizing_best_response_cost": rows[1]["x_local_query_cost"],
        "exposure_gap": rows[1]["x_local_query_cost"] - rows[0]["x_local_query_cost"],
        "interpretation": "existence witness only; intentionally minimal/degenerate, not evidence about natural games",
    }
    (output_dir / "e21b_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(run(Path("results")))
