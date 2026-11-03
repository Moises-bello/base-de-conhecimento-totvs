#!/usr/bin/env bash
# Pipeline completo após receber chunks do browser (TDN TEC / TOTVSTEC)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"

echo "==> Importando chunks TEC..."
.venv/bin/python tools/sync.py import-tdn-dir .cache/chunks/tdn-tec --source tdn-tec "$@"

echo "==> Gerando índice Protheus..."
.venv/bin/python tools/sync.py build-index --product protheus

echo "==> Exportando handoff para a Área de Trabalho..."
.venv/bin/python tools/sync.py export-tdn-handoff --source tdn-tec

echo "✓ Concluído. Markdown em knowledge/protheus/tdn-tec/"
echo "✓ Pacote para outro dev em ~/Desktop/tdn-tec-export/"
