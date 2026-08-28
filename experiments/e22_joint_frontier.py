from __future__ import annotations

import csv
import json
from pathlib import Path

from exposurefrontier.frontier import joint_frontier
from exposurefrontier.route_game import enumerate_route_strategies


def run(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = enumerate_route_strategies(n_bits=21, safe_reward=0.65, p_steps=101)
    peak_budgets = list(range(0, 22))
    workload_budgets = [float(x) for x in range(0, 22)]
    surface = joint_frontier(rows, peak_budgets, workload_budgets)
    with (output_dir / "e22_joint_frontier.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(surface[0]))
        w.writeheader(); w.writerows(surface)
    distinct_strategies = sorted({(r["p_hard"], r["queries"]) for r in surface if r["reward"] == r["reward"]})
    summary = {
        "experiment": "E22",
        "grid_points": len(surface),
        "distinct_optimal_strategies": len(distinct_strategies),
        "strategy_examples": distinct_strategies[:20],
    }
    (output_dir / "e22_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(run(Path("results")))
