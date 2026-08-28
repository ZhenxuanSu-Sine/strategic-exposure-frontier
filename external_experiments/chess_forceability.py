#!/usr/bin/env python3
"""One-ply empirical epsilon-forceability with Stockfish.

For each input position where the opponent is to move:
1. evaluate every legal opponent move at a high node budget;
2. define centipawn regret relative to the opponent's best move;
3. after each candidate move, measure focal Stockfish required nodes for stabilization;
4. compute maximum induced required nodes under regret threshold epsilon.

Centipawn score is a proxy for payoff. Required nodes is engine/protocol-relative.
"""
from __future__ import annotations

import argparse
import csv
import os
import shutil
from pathlib import Path

import chess
import chess.engine

from chess_required_nodes import analyse_trace, required_nodes, cp_score


def eval_root_move(engine, board: chess.Board, move: chess.Move, nodes: int) -> int:
    info = engine.analyse(
        board,
        chess.engine.Limit(nodes=nodes),
        root_moves=[move],
        info=chess.engine.INFO_ALL,
    )
    score = cp_score(info, board.turn)
    if score is None:
        raise RuntimeError("engine returned no score")
    return int(score)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fen", required=True)
    ap.add_argument("--stockfish", default=os.environ.get("STOCKFISH_PATH") or shutil.which("stockfish"))
    ap.add_argument("--opponent-eval-nodes", type=int, default=300000)
    ap.add_argument("--focal-nodes", default="1000,2000,5000,10000,20000,50000,100000,200000")
    ap.add_argument("--cp-tolerance", type=int, default=20)
    ap.add_argument("--eps-cp", default="0,10,20,50,100")
    ap.add_argument("--threads", type=int, default=1)
    ap.add_argument("--hash-mb", type=int, default=64)
    ap.add_argument("--out", default="results/e27_chess_forceability.csv")
    args = ap.parse_args()
    if not args.stockfish:
        raise SystemExit("Stockfish not found. Set STOCKFISH_PATH or pass --stockfish.")

    board = chess.Board(args.fen)
    node_grid = sorted({int(x) for x in args.focal_nodes.split(",")})
    eps_grid = sorted({int(x) for x in args.eps_cp.split(",")})

    engine = chess.engine.SimpleEngine.popen_uci(args.stockfish)
    engine.configure({"Threads": args.threads, "Hash": args.hash_mb})
    try:
        move_rows = []
        for move in list(board.legal_moves):
            opp_score = eval_root_move(engine, board, move, args.opponent_eval_nodes)
            child = board.copy(stack=False)
            child.push(move)
            trace = analyse_trace(engine, child, node_grid)
            req = required_nodes(trace, args.cp_tolerance)
            move_rows.append({
                "move": move.uci(),
                "opponent_score_cp": opp_score,
                "focal_required_nodes": req,
                "focal_reference_move": trace[-1]["move"],
                "focal_reference_score_cp": trace[-1]["score_cp"],
            })
    finally:
        engine.quit()

    best = max(r["opponent_score_cp"] for r in move_rows)
    for r in move_rows:
        r["opponent_regret_cp"] = best - r["opponent_score_cp"]

    curve_rows = []
    for eps in eps_grid:
        feasible = [r for r in move_rows if r["opponent_regret_cp"] <= eps and r["focal_required_nodes"] is not None]
        curve_rows.append({
            "row_type": "curve",
            "epsilon_cp": eps,
            "F_required_nodes": max((r["focal_required_nodes"] for r in feasible), default=None),
            "L_required_nodes": min((r["focal_required_nodes"] for r in feasible), default=None),
            "num_feasible_moves": len(feasible),
        })

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "row_type", "move", "opponent_score_cp", "opponent_regret_cp", "focal_required_nodes",
        "focal_reference_move", "focal_reference_score_cp", "epsilon_cp", "F_required_nodes",
        "L_required_nodes", "num_feasible_moves"
    ]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in move_rows:
            w.writerow({"row_type": "move", **r})
        for r in curve_rows:
            w.writerow(r)
    print(f"wrote {out} ({len(move_rows)} legal moves, {len(curve_rows)} epsilon points)")


if __name__ == "__main__":
    main()
