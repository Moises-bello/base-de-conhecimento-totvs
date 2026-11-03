#!/usr/bin/env bash
# Instala dependências Python e o browser Chromium para o crawler do TDN.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"
cd "$PROJECT_DIR"

if [[ -d .venv ]]; then
  source .venv/bin/activate
else
  echo "Criando ambiente virtual..."
  python3 -m venv .venv
  source .venv/bin/activate
fi

echo "Instalando dependências do TDN..."
pip install -r tools/requirements-tdn.txt

echo "Instalando Chromium para Playwright..."
playwright install chromium

echo ""
echo "Pronto. Para sincronizar o TDN:"
echo "  1. Em config/sources.yaml, defina tdn-fluig.enabled: true"
echo "  2. python tools/sync.py sync --source tdn-fluig"
