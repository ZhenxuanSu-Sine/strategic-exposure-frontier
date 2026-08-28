from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from exposurefrontier.frontier import upper_envelope
from exposurefrontier.games.tictactoe import (
    EMPTY,
    future_x_exposure_under_br_force,
    future_x_exposure_under_lex_minimax,
    minimax_value,
    trace_o_policy,
)
from exposurefrontier.majority import majority_success_probability
from exposurefrontier.route_game import enumerate_route_strategies


def main() -> None:
    vals = [majority_success_probability(21, q) for q in range(22)]
    assert abs(vals[0] - 0.5) < 1e-12
    assert abs(vals[-1] - 1.0) < 1e-12
    assert all(b + 1e-12 >= a for a, b in zip(vals, vals[1:]))

    rows = enumerate_route_strategies(p_steps=31)
    budgets = [float(x) for x in range(22)]
    for key in ("peak_cost", "workload"):
        rewards = [p.reward for p in upper_envelope(rows, budgets, key)]
        assert all(b + 1e-12 >= a for a, b in zip(rewards, rewards[1:]))

    for n in (2, 8, 64, 1024):
        assert (1.0 / n) * n == 1.0

    assert minimax_value(EMPTY * 9) == 0
    _, lex_value = trace_o_policy("lex_minimax")
    _, force_value = trace_o_policy("br_force")
    assert lex_value == force_value == 0
    assert future_x_exposure_under_br_force(EMPTY * 9) == future_x_exposure_under_lex_minimax(EMPTY * 9)
    print("selftest: all checks passed")


if __name__ == "__main__":
    main()
