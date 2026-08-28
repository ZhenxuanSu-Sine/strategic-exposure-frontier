from __future__ import annotations

import csv
import json
from pathlib import Path

from exposurefrontier.frontier import upper_envelope
from exposurefrontier.route_game import enumerate_route_strategies


def linspace(start: float, stop: float, count: int) -> list[float]:
    if count <= 1:
        return [start]
    step = (stop - start) / (count - 1)
    return [start + i * step for i in range(count)]


def maybe_plot(out_rows: list[dict[str, float]], output_dir: Path) -> bool:
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return False
    plt.figure(figsize=(7, 4.5))
    plt.plot([r["budget"] for r in out_rows], [r["peak_reward"] for r in out_rows], label="peak-capability budget")
    plt.plot([r["budget"] for r in out_rows], [r["work_reward"] for r in out_rows], label="on-policy workload budget")
    plt.xlabel("budget")
    plt.ylabel("max expected reward")
    plt.title("E19: route-game frontiers")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "e19_route_frontiers.png", dpi=160)
    plt.close()
    return True


def run(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = enumerate_route_strategies(n_bits=21, safe_reward=0.65, p_steps=201)
    budgets = linspace(0.0, 21.0, 211)
    peak_front = upper_envelope(rows, budgets, "peak_cost")
    work_front = upper_envelope(rows, budgets, "workload")

    out_rows = []
    for p, w in zip(peak_front, work_front):
        out_rows.append({
            "budget": p.budget,
            "peak_reward": p.reward,
            "peak_p_hard": p.strategy.get("p_hard", float("nan")),
            "peak_queries": p.strategy.get("queries", float("nan")),
            "work_reward": w.reward,
            "work_p_hard": w.strategy.get("p_hard", float("nan")),
            "work_queries": w.strategy.get("queries", float("nan")),
        })

    csv_path = output_dir / "e19_route_frontiers.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0]))
        writer.writeheader(); writer.writerows(out_rows)

    plotted = maybe_plot(out_rows, output_dir)
    max_gap = max(float(r["work_reward"] - r["peak_reward"]) for r in out_rows)
    gap_row = max(out_rows, key=lambda r: float(r["work_reward"] - r["peak_reward"]))
    summary = {
        "experiment": "E19",
        "max_work_minus_peak_reward_gap": max_gap,
        "gap_budget": float(gap_row["budget"]),
        "work_strategy_at_gap": {"p_hard": gap_row["work_p_hard"], "queries": gap_row["work_queries"]},
        "peak_strategy_at_gap": {"p_hard": gap_row["peak_p_hard"], "queries": gap_row["peak_queries"]},
        "plot_generated": plotted,
    }
    (output_dir / "e19_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(run(Path("results")))
