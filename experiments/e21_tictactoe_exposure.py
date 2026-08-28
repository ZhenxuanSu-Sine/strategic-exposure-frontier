from __future__ import annotations

import csv
import json
from pathlib import Path

from exposurefrontier.games.tictactoe import (
    EMPTY,
    expected_value_x_vs_random_o,
    future_x_exposure_under_br_force,
    future_x_exposure_under_lex_minimax,
    future_x_exposure_under_random_o,
    minimax_value,
    naive_minimax_node_count,
    trace_o_policy,
)


def run(output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    empty = EMPTY * 9
    lex_trace, lex_value = trace_o_policy("lex_minimax")
    force_trace, force_value = trace_o_policy("br_force")

    rows = [
        {
            "opponent": "random",
            "x_game_value": expected_value_x_vs_random_o(empty),
            "x_expected_search_nodes": future_x_exposure_under_random_o(empty),
        },
        {
            "opponent": "lex_minimax_best_response",
            "x_game_value": float(lex_value),
            "x_expected_search_nodes": future_x_exposure_under_lex_minimax(empty),
        },
        {
            "opponent": "minimax_then_exposure_best_response",
            "x_game_value": float(force_value),
            "x_expected_search_nodes": future_x_exposure_under_br_force(empty),
        },
    ]

    with (output_dir / "e21_tictactoe_exposure.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

    with (output_dir / "e21_lex_trace.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(lex_trace[0]))
        w.writeheader(); w.writerows(lex_trace)
    with (output_dir / "e21_force_trace.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(force_trace[0]))
        w.writeheader(); w.writerows(force_trace)

    summary = {
        "experiment": "E21",
        "empty_board_naive_minimax_nodes": naive_minimax_node_count(empty),
        "minimax_value": minimax_value(empty),
        "rows": rows,
        "payoff_preserved": lex_value == force_value,
        "extra_nodes_for_br_force": future_x_exposure_under_br_force(empty) - future_x_exposure_under_lex_minimax(empty),
    }
    (output_dir / "e21_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


if __name__ == "__main__":
    print(run(Path("results")))
