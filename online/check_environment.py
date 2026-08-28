#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import os
import shutil
import socket

mods = ["pytest", "matplotlib", "numpy", "pandas", "scipy", "requests", "bs4", "chess", "pyspiel", "networkx"]
print("Python modules:")
for m in mods:
    print(f"  {m:12s} {'OK' if importlib.util.find_spec(m) else 'MISSING'}")

sf = os.environ.get("STOCKFISH_PATH") or shutil.which("stockfish")
print("Stockfish:", sf or "MISSING")

for host in ["arxiv.org", "github.com", "api.openalex.org"]:
    try:
        socket.gethostbyname(host)
        print(f"DNS {host}: OK")
    except Exception as e:
        print(f"DNS {host}: FAIL ({e})")
