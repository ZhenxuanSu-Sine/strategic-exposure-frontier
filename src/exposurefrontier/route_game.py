from __future__ import annotations

from .majority import majority_success_probability


def enumerate_route_strategies(
    n_bits: int = 21,
    safe_reward: float = 0.65,
    p_steps: int = 101,
) -> list[dict[str, float]]:
    if p_steps < 2:
        raise ValueError("p_steps must be >= 2")
    rows: list[dict[str, float]] = []
    for i in range(p_steps):
        p_hard = i / (p_steps - 1)
        for q in range(n_bits + 1):
            hard_reward = majority_success_probability(n_bits, q)
            reward = (1.0 - p_hard) * safe_reward + p_hard * hard_reward
            rows.append({
                "p_hard": float(p_hard),
                "queries": float(q),
                "hard_reward": float(hard_reward),
                "reward": float(reward),
                "peak_cost": float(q if p_hard > 0.0 else 0.0),
                "workload": float(p_hard * q),
            })
    return rows
