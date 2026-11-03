# Base de conhecimento TOTVS — guia para IA

Base de conhecimento **local** para consulta por agentes de IA (Claude Code, Codex, Cursor, Copilot). Não é código de aplicação.

**Somente documentação oficial TOTVS.** Não adicione dados, schemas ou documentos de clientes.

Regras de consulta (o que buscar, prioridade de fontes, como responder): [`tools/config/global-ai-instructions.md`](tools/config/global-ai-instructions.md) — é a fonte única; `tools/scripts/manutencao/install-global-instructions.sh` copia esse texto para `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md` e `~/AGENTS.md`.

## Estrutura

```
<raiz da base>/
├── AGENTS.md, README.md
├── knowledge/           ← ⭐ SOMENTE documentação oficial TOTVS (Markdown com frontmatter: title, source, url, type)
│   ├── fluig/    tdn-fluig, api-fluig, rest-fluig, sdk-fluig, style-guide
│   ├── rm/       central-rm, tdn-rm
│   ├── protheus/ central-protheus, tdn-tec
│   └── totvs/    central-ciclo-vida
├── agents/              ← skills de IA oficiais TOTVS (SKILL.md) — não é conteúdo RAG
│   ├── totvs/fluig/             pacote oficial TOTVS (skills + context + examples)
│   └── totvs/advpl-tlpp/        pacote oficial TOTVS (skills Protheus)
├── tools/
│   ├── sync.py          CLI (search, show, sync, import-tdn, build-index…)
│   ├── catalog/         _INDEX.md (roteador de fontes, 1 KB), index.json (metadados — nunca carregue),
│   │                    blocklist-discontinued.json (páginas descontinuadas que o sync não deve rebaixar)
│   ├── mirror/          código Python (paths.py = todos os caminhos)
│   ├── config/          sources.yaml + instruções globais + snippets VS Code
│   ├── bin/totvs-search
│   └── scripts/         console/ (F12, TDN), tdn/, fluig-api/, manutencao/
└── .cache/              ← regenerável: search.db (busca full-text), mirror HTML, chunks, manifest.db, sync.log
    └── secrets/         cookies/sessões TDN (não compartilhar)
```

## Conteúdo por fonte

| Pasta em `knowledge/` | Conteúdo | Docs |
|-------|----------|------|
| `fluig/tdn-fluig/` | Documentação oficial TDN (Confluence) | ~1.700 |
| `fluig/api-fluig/` | Referência REST (OpenAPI → Markdown) | 11 módulos |
| `fluig/rest-fluig/` | API REST pública (`/api/public`): 65 recursos + 760 VOs JSON | 826 |
| `fluig/sdk-fluig/` | Javadoc Fluig SDK (`com.fluig.sdk.*`: WorkflowAPIService, VOs…) | 216 |
| `fluig/style-guide/` | Fluig Style Guide (CSS, componentes, JS) | 6 |
| `rm/central-rm/` | Central de Atendimento — RM | ~2.700 |
| `rm/tdn-rm/` | TDN — espaço LRM (técnico) | ~30.000 |
| `protheus/central-protheus/` | Central de Atendimento — Protheus | ~22.000 |
| `protheus/tdn-tec/` | TDN — TOTVS Tec (AdvPL/TLPP, AppServer) | ~1.250 |
| `totvs/central-ciclo-vida/` | Ciclo de Vida TOTVS (comunicados, políticas) | ~200 |

## Busca (fluxo de menor custo em tokens)

```bash
# 1. Buscar: full-text (título > seções > corpo), sem acento, 5 resultados com caminho, URL, seção e trecho
.venv/bin/python tools/sync.py search "cancelar solicitação" --product fluig
.venv/bin/python tools/sync.py search "CancelInstancesVO" --product fluig --source sdk-fluig
# 2. Ler: doc pequeno inteiro; doc grande → sumário de seções
.venv/bin/python tools/sync.py show knowledge/fluig/sdk-fluig/old_sdk_com_fluig_sdk_service_WorkflowAPIService.html.md
# 3. Só a seção necessária
.venv/bin/python tools/sync.py show knowledge/fluig/sdk-fluig/old_sdk_com_fluig_sdk_service_WorkflowAPIService.html.md --secao cancelInstances
```

A busca reindexa sozinha (`.cache/search.db`, ~20 s) quando o catálogo muda (import/export/prune) ou quando o commit do git muda (`git pull`). `knowledge/` é versionado no git — só documentação oficial TOTVS.

De qualquer pasta: `totvs-search "termo" --product rm` — requer no `~/.zshrc`:

```bash
export PATH="<CAMINHO_DA_BASE>/tools/bin:$PATH"
```

## Manutenção

Sempre `.venv/bin/python` nesta raiz:

```bash
.venv/bin/python tools/sync.py status          # estatísticas do espelho
.venv/bin/python tools/sync.py sync            # sync incremental de todas as fontes habilitadas
.venv/bin/python tools/sync.py export          # regenera knowledge/ a partir de .cache/mirror
.venv/bin/python tools/sync.py build-index     # regenera tools/catalog/_INDEX.md + índice de busca
.venv/bin/python tools/sync.py prune           # dry-run: obsoletos + duplicatas (--apply executa)
```

- Importar export do console (TDN): `sync.py import-tdn <arquivo.json> --source <fonte>` — scripts em `tools/scripts/console/`, detalhes no `README.md`.
- Atualizar docs de API Fluig: `sync.py export-api` (OpenAPI) e `tools/scripts/fluig-api/export-fluig-old-docs.py rest|sdk` + `import-tdn` (REST pública e SDK; sem browser).
- Atualizou um pacote em `agents/`? Rode `tools/scripts/manutencao/link-skills.sh` (ver `agents/README.md`).
- Mudou as regras de consulta? Edite `tools/config/global-ai-instructions.md` e rode `tools/scripts/manutencao/install-global-instructions.sh`.
- Caminhos são definidos só em `tools/mirror/paths.py` — não monte `data_dir / "knowledge"` à mão.
