#!/usr/bin/env bash
# Copia tools/config/global-ai-instructions.md (fonte única) para as instruções globais
# de cada ferramenta de IA, entre marcadores — o resto de cada arquivo é preservado.
# {{KB_ROOT}} no texto é trocado pelo caminho desta base na máquina de quem instala.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
SRC="$ROOT/tools/config/global-ai-instructions.md"
BEGIN="<!-- BEGIN base-totvs (gerado por tools/scripts/manutencao/install-global-instructions.sh) -->"
END="<!-- END base-totvs -->"

TARGETS=(
  "$HOME/.claude/CLAUDE.md"   # Claude Code
  "$HOME/.codex/AGENTS.md"    # Codex
  "$HOME/AGENTS.md"           # ferramentas que leem AGENTS.md da home
)

for target in "${TARGETS[@]}"; do
  mkdir -p "$(dirname "$target")"
  touch "$target"
  "$ROOT/.venv/bin/python" - "$target" "$SRC" "$BEGIN" "$END" "$ROOT" <<'PY'
import sys
from pathlib import Path
target, src, begin, end, root = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
content = src.read_text(encoding='utf-8').rstrip().replace('{{KB_ROOT}}', root)
block = f"{begin}\n{content}\n{end}\n"
text = target.read_text(encoding="utf-8")
if begin.split(" (")[0] in text and end in text:
    head = text[: text.index(begin.split(" (")[0])]
    tail = text[text.index(end) + len(end):].lstrip("\n")
    text = head + block + ("\n" + tail if tail else "")
else:
    text = (text.rstrip() + "\n\n" if text.strip() else "") + block
target.write_text(text, encoding="utf-8")
PY
  echo "✓ $target"
done
