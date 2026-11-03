#!/usr/bin/env bash
# Abre Chrome com depuração remota — use SEU perfil, passe Cloudflare uma vez.
set -euo pipefail

PROFILE="${HOME}/.chrome-tdn"
mkdir -p "$PROFILE"

echo "Abrindo Chrome para TDN..."
echo "1. Acesse: https://tdn.totvs.com/display/public/fluig/Central+de+ajuda"
echo "2. Passe o Cloudflare (no SEU Chrome, não automação)"
echo "3. Em outro terminal: .venv/bin/python tools/sync.py sync-tdn-cdp"
echo ""

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$PROFILE" \
  "https://tdn.totvs.com/display/public/fluig/Central+de+ajuda"
