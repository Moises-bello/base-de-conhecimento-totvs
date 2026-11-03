#!/usr/bin/env bash
# Inicia o servidor local para receber chunks do console (TDN TEC)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"
exec .venv/bin/python tools/sync.py receive-tdn --source tdn-tec "$@"
