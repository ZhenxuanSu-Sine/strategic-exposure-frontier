#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements-online.txt
python online/check_environment.py
