from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class FrontierPoint:
    budget: float
    reward: float
    strategy: Mapping[str, float]


def upper_envelope(
    strategies: Iterable[Mapping[str, float]],
    budgets: Sequence[float],
    cost_key: str,
    reward_key: str = "reward",
) -> list[FrontierPoint]:
    rows = list(strategies)
    out: list[FrontierPoint] = []
    for budget in budgets:
        feasible = [r for r in rows if float(r[cost_key]) <= float(budget) + 1e-12]
        if not feasible:
            out.append(FrontierPoint(float(budget), float("-inf"), {}))
            continue
        best = max(feasible, key=lambda r: (float(r[reward_key]), -float(r[cost_key])))
        out.append(FrontierPoint(float(budget), float(best[reward_key]), dict(best)))
    return out


def joint_frontier(
    strategies: Iterable[Mapping[str, float]],
    peak_budgets: Sequence[float],
    workload_budgets: Sequence[float],
    reward_key: str = "reward",
) -> list[dict[str, float]]:
    rows = list(strategies)
    out: list[dict[str, float]] = []
    for peak in peak_budgets:
        for work in workload_budgets:
            feasible = [
                r for r in rows
                if float(r["peak_cost"]) <= float(peak) + 1e-12
                and float(r["workload"]) <= float(work) + 1e-12
            ]
            if feasible:
                best = max(feasible, key=lambda r: float(r[reward_key]))
                out.append({
                    "peak_budget": float(peak),
                    "workload_budget": float(work),
                    "reward": float(best[reward_key]),
                    "p_hard": float(best.get("p_hard", 0.0)),
                    "queries": float(best.get("queries", 0.0)),
                })
            else:
                out.append({
                    "peak_budget": float(peak),
                    "workload_budget": float(work),
                    "reward": float("nan"),
                    "p_hard": float("nan"),
                    "queries": float("nan"),
                })
    return out
