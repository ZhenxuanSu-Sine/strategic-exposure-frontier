#!/usr/bin/env python3
"""Exact epsilon-forceability scan for a small deterministic OpenSpiel game.

Declared architecture/cost proxy:
- focal player: player 0;
- focal policy: lexicographic exact minimax policy;
- local focal computation cost: number of nodes expanded by a *naive full-tree*
  minimax invocation from the focal decision state (no cache / alpha-beta);
- opponent: player 1;
- chance nodes are rejected in this starter.

This is deliberately solver-relative. It is not an intrinsic game complexity.
"""
from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pyspiel


@dataclass(frozen=True)
class Pair:
    value: float
    workload: int


def child(state, action):
    s = state.clone()
    s.apply_action(action)
    return s


def require_supported(game, state) -> None:
    if game.num_players() != 2:
        raise ValueError("starter supports exactly two players")
    if state.is_chance_node():
        raise ValueError("starter rejects chance nodes; extend explicitly if needed")
    gt = game.get_type()
    if gt.dynamics != pyspiel.GameType.Dynamics.SEQUENTIAL:
        raise ValueError("starter requires sequential games")


def exact_value(state) -> float:
    if state.is_terminal():
        return float(state.returns()[0])
    if state.is_chance_node():
        raise ValueError("chance nodes not supported")
    vals = [exact_value(child(state, a)) for a in state.legal_actions()]
    p = state.current_player()
    if p == 0:
        return max(vals)
    if p == 1:
        return min(vals)
    raise ValueError(f"unexpected current player {p}")


def naive_subtree_nodes(state) -> int:
    """Count nodes in a naive full recursion rooted at state, including root."""
    if state.is_terminal():
        return 1
    if state.is_chance_node():
        raise ValueError("chance nodes not supported")
    return 1 + sum(naive_subtree_nodes(child(state, a)) for a in state.legal_actions())


def focal_action(state) -> int:
    """Lexicographic exact minimax action for player 0."""
    assert state.current_player() == 0
    scored = [(exact_value(child(state, a)), a) for a in state.legal_actions()]
    best = max(v for v, _ in scored)
    return min(a for v, a in scored if v == best)


def realized_pairs(state) -> list[Pair]:
    """All payoff/workload pairs player 1 can induce against fixed focal policy."""
    if state.is_terminal():
        return [Pair(float(state.returns()[0]), 0)]
    if state.is_chance_node():
        raise ValueError("chance nodes not supported")

    p = state.current_player()
    if p == 0:
        local = naive_subtree_nodes(state)
        a = focal_action(state)
        return [Pair(x.value, x.workload + local) for x in realized_pairs(child(state, a))]
    if p == 1:
        out: list[Pair] = []
        for a in state.legal_actions():
            out.extend(realized_pairs(child(state, a)))
        # Deduplicate identical pairs; retaining all strategies is unnecessary for F/L.
        return sorted(set(out), key=lambda x: (x.value, x.workload))
    raise ValueError(f"unexpected current player {p}")


def force_curve(pairs: Iterable[Pair]) -> list[dict]:
    pairs = list(pairs)
    v = min(p.value for p in pairs)
    breakpoints = sorted(set(max(0.0, p.value - v) for p in pairs))
    rows = []
    for eps in breakpoints:
        feasible = [p for p in pairs if p.value <= v + eps + 1e-12]
        rows.append(
            {
                "epsilon": eps,
                "game_value_against_fixed_pi": v,
                "F": max(p.workload for p in feasible),
                "L": min(p.workload for p in feasible),
                "DeltaF": max(p.workload for p in feasible) - min(p.workload for p in feasible),
                "num_feasible_pairs": len(feasible),
            }
        )
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", default="tic_tac_toe")
    ap.add_argument("--out-dir", default="results/e24_open_spiel")
    ap.add_argument("--max-root-nodes", type=int, default=2_000_000)
    args = ap.parse_args()

    game = pyspiel.load_game(args.game)
    root = game.new_initial_state()
    require_supported(game, root)

    root_nodes = naive_subtree_nodes(root)
    if root_nodes > args.max_root_nodes:
        raise RuntimeError(
            f"naive tree has {root_nodes} nodes > --max-root-nodes={args.max_root_nodes}; "
            "choose a smaller game or extend with a clearly declared approximate protocol"
        )

    pairs = realized_pairs(root)
    curve = force_curve(pairs)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    with (out / "pairs.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["value", "workload"])
        w.writeheader()
        for p in pairs:
            w.writerow({"value": p.value, "workload": p.workload})

    with (out / "force_curve.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(curve[0].keys()))
        w.writeheader()
        w.writerows(curve)

    meta = {
        "game": args.game,
        "root_naive_subtree_nodes": root_nodes,
        "exact_minimax_value": exact_value(root),
        "num_distinct_realized_pairs": len(pairs),
        "architecture": "lexicographic exact minimax focal policy; naive full-tree node-count local cost",
        "warning": "solver-relative proxy, not intrinsic game complexity",
    }
    (out / "summary.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
