#!/usr/bin/env bash
# Executa sync semanal de todas as fontes habilitadas.
# Agende com cron, ex: 0 3 * * 0 /caminho/weekly-sync.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"
cd "$PROJECT_DIR"

if [[ -d .venv ]]; then
  source .venv/bin/activate
fi

python tools/sync.py sync 2>&1 | tee -a .cache/sync.log
