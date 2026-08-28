from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
RESULTS = ROOT / "results"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    summaries = []
    for path in sorted((ROOT / "experiments").glob("e*.py")):
        module = load_module(path)
        summary = module.run(RESULTS)
        summaries.append(summary)
        print(json.dumps(summary, ensure_ascii=False))

    files = []
    for path in sorted(RESULTS.iterdir()):
        if path.name == "manifest.json" or not path.is_file():
            continue
        files.append({
            "path": str(path.relative_to(ROOT)),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        })
    manifest = {
        "project": "Strategic Exposure Frontier",
        "generated_by": "scripts_run_all.py",
        "summaries": summaries,
        "files": files,
    }
    (RESULTS / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
