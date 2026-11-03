#!/usr/bin/env bash
# (Re)cria em ~/.claude/skills/ um symlink para cada skill (pasta com SKILL.md) em agents/.
# Rode depois de atualizar um pacote da TOTVS.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"

count=0
while IFS= read -r skill_md; do
  dir="$(dirname "$skill_md")"
  name="$(basename "$dir")"
  if [[ -e "$DEST/$name" && ! -L "$DEST/$name" ]]; then
    echo "⚠ $DEST/$name existe e não é symlink — ignorado"
    continue
  fi
  ln -sfn "$dir" "$DEST/$name"
  count=$((count + 1))
done < <(find "$ROOT/agents" -mindepth 3 -maxdepth 5 -name SKILL.md -not -path "*/references/*")

# Remove symlinks que apontavam para a base e quebraram
find "$DEST" -maxdepth 1 -type l ! -exec test -e {} \; -print | while read -r link; do
  [[ "$(readlink "$link")" == "$ROOT"/* ]] && rm "$link" && echo "removido link quebrado: $link"
done
echo "✓ $count skills ligadas em $DEST"
