# Environment — online Codex version

## Core baseline

Python >= 3.9. Core E18–E22 requires only the standard library. Optional plotting/tests use matplotlib/pytest.

```bash
python scripts_run_all.py
python selftest.py
```

## Online extras

Recommended Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-online.txt
```

The agent may install newer compatible versions if required, but must record resolved versions in the final manifest.

## Stockfish

Prefer the official Stockfish repository/releases. Set:

```bash
export STOCKFISH_PATH=/absolute/path/to/stockfish
```

The chess scaffold will also try `stockfish` on PATH.

For reproducibility record:

- engine version/commit;
- binary SHA256;
- Threads;
- Hash;
- NNUE network reported by engine;
- Syzygy configuration;
- CPU/hardware;
- node limits and MultiPV settings.

## OpenSpiel

Try PyPI first:

```bash
pip install open_spiel
```

If a needed game/algorithm is unavailable in the wheel, clone the official Google DeepMind OpenSpiel repo and build from source. Record commit hash.

## Ludii

Optional. Requires Java. Use only after exact finite-game methodology is stable.

## Internet research

The agent is expected to download papers/code when licenses permit. Do not commit large external corpora or third-party binaries into this repo. Instead save:

- source URL;
- DOI/repository commit;
- retrieval date;
- local hash if downloaded;
- license note where relevant.
