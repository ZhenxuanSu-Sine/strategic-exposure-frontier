from __future__ import annotations

from .majority import majority_success_probability


def challenge_rows(
    theta: float,
    n_bits: int = 21,
    easy_reward: float = 1.0,
    easy_cost: float = 0.0,
) -> list[dict[str, float]]:
    if not 0.0 <= theta <= 1.0:
        raise ValueError("theta must be in [0,1]")
    rows: list[dict[str, float]] = []
    for q in range(n_bits + 1):
        hard_reward = majority_success_probability(n_bits, q)
        reward = (1.0 - theta) * easy_reward + theta * hard_reward
        workload = (1.0 - theta) * easy_cost + theta * q
        rows.append({
            "theta": float(theta),
            "queries": float(q),
            "reward": float(reward),
            "workload": float(workload),
            "peak_cost": float(q),
        })
    return rows
