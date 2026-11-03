# agents/ — Skills de IA

Pacotes **oficiais TOTVS** de **skills** (`SKILL.md`) prontos para Claude Code e outras ferramentas. Diferente de `knowledge/`, isto não é documentação espelhada: são instruções de trabalho para o agente. Somente fontes TOTVS ficam aqui.

| Pasta | Origem | Skills |
|-------|--------|--------|
| `totvs/fluig/` | Oficial TOTVS — Fluig (`skills/`, `context/`, `examples/`, `AGENTS.md`, `CLAUDE.md`) | 16 (`fluig-*`) |
| `totvs/advpl-tlpp/` | Oficial TOTVS — ADVPL/TLPP Protheus (`skills/`, `AGENTS.md`, `CLAUDE.md`) | 19 |

Cada skill é ligada por symlink em `~/.claude/skills/<nome>` — por isso aparecem em qualquer projeto.

## Atualizar um pacote

Quando a TOTVS liberar nova versão (`AGENTS.md` / `CLAUDE.md` / `skills.zip`):

1. **Fluig:** substitua o conteúdo de `totvs/fluig/` pelo novo pacote.
2. **ADVPL/TLPP:** o zip oficial traz `skills/advpl-tlpp/` e `skills/superpowers/`:
   - conteúdo de `skills/advpl-tlpp/*` → `totvs/advpl-tlpp/skills/`
   - `AGENTS.md` / `CLAUDE.md` → `totvs/advpl-tlpp/`
   - **descarte** `skills/superpowers/` — são skills genéricas da comunidade (github.com/obra/superpowers), não TOTVS
3. Rode `../tools/scripts/manutencao/link-skills.sh` para ligar skills novas e remover links quebrados.
