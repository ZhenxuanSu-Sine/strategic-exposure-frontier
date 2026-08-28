#!/usr/bin/env python3
"""Measure Stockfish node budget required for move/eval stabilization on FENs.

This is an empirical solver-relative protocol, not a statement about intrinsic chess complexity.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
from pathlib import Path

import chess
import chess.engine


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cp_score(info, turn: chess.Color) -> int | None:
    score = info.get("score")
    if score is None:
        return None
    return score.pov(turn).score(mate_score=100000)


def analyse_trace(engine, board: chess.Board, node_grid: list[int]) -> list[dict]:
    rows = []
    for n in node_grid:
        info = engine.analyse(board, chess.engine.Limit(nodes=n), info=chess.engine.INFO_ALL)
        pv = info.get("pv") or []
        move = pv[0].uci() if pv else None
        rows.append(
            {
                "nodes_limit": n,
                "move": move,
                "score_cp": cp_score(info, board.turn),
                "depth": info.get("depth"),
                "seldepth": info.get("seldepth"),
                "reported_nodes": info.get("nodes"),
            }
        )
    return rows


def required_nodes(trace: list[dict], cp_tolerance: int) -> int | None:
    ref_move = trace[-1]["move"]
    ref_score = trace[-1]["score_cp"]
    for i, row in enumerate(trace):
        suffix = trace[i:]
        move_ok = all(x["move"] == ref_move for x in suffix)
        if ref_score is None:
            score_ok = True
        else:
            score_ok = all(
                x["score_cp"] is not None and abs(x["score_cp"] - ref_score) <= cp_tolerance
                for x in suffix
            )
        if move_ok and score_ok:
            return int(row["nodes_limit"])
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fens", required=True, help="text file: one FEN per non-comment line")
    ap.add_argument("--stockfish", default=os.environ.get("STOCKFISH_PATH") or shutil.which("stockfish"))
    ap.add_argument("--nodes", default="1000,2000,5000,10000,20000,50000,100000,200000")
    ap.add_argument("--cp-tolerance", type=int, default=20)
    ap.add_argument("--threads", type=int, default=1)
    ap.add_argument("--hash-mb", type=int, default=64)
    ap.add_argument("--out-dir", default="results/e26_chess_required_nodes")
    args = ap.parse_args()
    if not args.stockfish:
        raise SystemExit("Stockfish not found. Set STOCKFISH_PATH or pass --stockfish.")

    sf = Path(args.stockfish).resolve()
    node_grid = sorted({int(x) for x in args.nodes.split(",")})
    fens = [x.strip() for x in Path(args.fens).read_text(encoding="utf-8").splitlines() if x.strip() and not x.lstrip().startswith("#")]
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    engine = chess.engine.SimpleEngine.popen_uci(str(sf))
    engine.configure({"Threads": args.threads, "Hash": args.hash_mb})
    try:
        all_rows = []
        summary = []
        for idx, fen in enumerate(fens):
            board = chess.Board(fen)
            trace = analyse_trace(engine, board, node_grid)
            req = required_nodes(trace, args.cp_tolerance)
            for row in trace:
                all_rows.append({"fen_id": idx, "fen": fen, **row})
            summary.append(
                {
                    "fen_id": idx,
                    "fen": fen,
                    "required_nodes": req,
                    "reference_move": trace[-1]["move"],
                    "reference_score_cp": trace[-1]["score_cp"],
                }
            )
    finally:
        engine.quit()

    with (out / "trace.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader(); w.writerows(all_rows)
    with (out / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        w.writeheader(); w.writerows(summary)

    meta = {
        "stockfish_path": str(sf),
        "stockfish_sha256": sha256(sf),
        "engine_id": engine.id if hasattr(engine, "id") else None,
        "nodes": node_grid,
        "cp_tolerance": args.cp_tolerance,
        "threads": args.threads,
        "hash_mb": args.hash_mb,
        "criterion": "first tested node budget whose move remains equal to high-budget reference and score remains within cp tolerance for all larger tested budgets",
        "warning": "Stockfish/protocol-relative measurement, not intrinsic chess complexity",
    }
    (out / "metadata.json").write_text(json.dumps(meta, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"positions": len(fens), **meta}, indent=2, default=str))


if __name__ == "__main__":
    main()
