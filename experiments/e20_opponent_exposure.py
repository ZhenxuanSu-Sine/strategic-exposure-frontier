from __future__ import annotations

import csv
import json
from pathlib import Path

from exposurefrontier.challenge_game import challenge_rows
from exposurefrontier.frontier import upper_envelope


def linspace(start: float, stop: float, count: int) -> list[float]:
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def maybe_plot(frontiers: dict[float, list], output_dir: Path) -> bool:
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return False
    plt.figure(figsize=(7, 4.5))
    for theta, front in frontiers.items():
        plt.plot([fp.budget for fp in front], [fp.reward for fp in front], label=f"hard exposure θ={theta}")
    plt.xlabel("expected workload budget")
    plt.ylabel("max expected reward")
    plt.title("E20: occupancy controlled by opponent/environment")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "e20_opponent_exposure.png", dpi=160)
    plt.close()
    return True


def run(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    thetas = [0.1, 0.5, 1.0]
    budgets = linspace(0.0, 21.0, 211)
    all_rows = []
    summaries = {}
    frontiers = {}

    for theta in thetas:
        rows = challenge_rows(theta=theta, n_bits=21)
        front = upper_envelope(rows, budgets, "workload")
        frontiers[theta] = front
        for fp in front:
            all_rows.append({
                "theta": theta,
                "budget": fp.budget,
                "reward": fp.reward,
                "queries": fp.strategy.get("queries", float("nan")),
            })
        q_full = rows[-1]
        summaries[str(theta)] = {
            "full_solver_peak": q_full["peak_cost"],
            "full_solver_workload": q_full["workload"],
            "full_solver_reward": q_full["reward"],
        }

    with (output_dir / "e20_opponent_exposure.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0]))
        w.writeheader(); w.writerows(all_rows)

    plotted = maybe_plot(frontiers, output_dir)
    summary = {"experiment": "E20", "theta_summaries": summaries, "plot_generated": plotted}
    (output_dir / "e20_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(run(Path("results")))
