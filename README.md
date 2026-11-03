# Base de conhecimento TOTVS

Espelhador incremental de documentação TOTVS (Fluig, RM, Protheus) para uso offline e como base de conhecimento (RAG, busca local, etc.).

## Fontes suportadas

| Fonte | Tipo | Status |
|-------|------|--------|
| [api.fluig.com](https://api.fluig.com/latest/) | Site estático (Angular SPA) | Pronto |
| [style.fluig.com](https://style.fluig.com/) | Site estático (HTML) | Pronto |
| [tdn.totvs.com](https://tdn.totvs.com/display/public/fluig/) | Confluence + Cloudflare | Requer Playwright |
| [Central Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001794451-TOTVS-Linha-Protheus) | Zendesk Help Center | Pronto |
| [Central RM](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011673474-TOTVS-RH-Linha-RM) | Zendesk Help Center | Pronto |
| [Fluig REST pública](https://api.fluig.com/old/) | Enunciate (recursos + VOs JSON) | `tools/scripts/fluig-api/export-fluig-old-docs.py rest` |
| [Fluig SDK Javadoc](https://api.fluig.com/old/sdk/allclasses.html) | Javadoc | `tools/scripts/fluig-api/export-fluig-old-docs.py sdk` |

## Como funciona o sync incremental

1. Cada URL baixada é registrada em `.cache/manifest.db` (SQLite)
2. No sync seguinte, envia `HEAD` e compara `ETag` / `Last-Modified`
3. Se os headers não mudaram, pula o download
4. Se mudaram (ou não há headers), baixa e compara hash SHA-256 do conteúdo
5. Só grava arquivo quando o conteúdo é novo ou alterado

## Instalação

```bash
# Windows: antes do clone, habilite caminhos longos (alguns arquivos de knowledge/ passam de 200 caracteres)
#   git config --global core.longpaths true
git clone <url-do-repositório> base-totvs && cd base-totvs
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/requirements.txt

# A documentação (knowledge/) já vem no clone; gere o catálogo e o índice de busca (~1 min)
.venv/bin/python tools/sync.py build-index

# Skills oficiais TOTVS no Claude Code (~/.claude/skills) e instruções globais das IAs
# (~/.claude/CLAUDE.md, ~/.codex/AGENTS.md, ~/AGENTS.md) com o caminho desta pasta
./tools/scripts/manutencao/link-skills.sh
./tools/scripts/manutencao/install-global-instructions.sh

# Opcional: comando totvs-search em qualquer pasta (adicione ao ~/.zshrc)
export PATH="$PWD/tools/bin:$PATH"

# Para espelhar tdn.totvs.com (Confluence + Cloudflare):
./tools/scripts/tdn/setup-tdn.sh
# ou: python tools/sync.py setup-tdn
```

## Atualizar a documentação compartilhada

`knowledge/` é versionado. Quem atualiza (sync, import do TDN, export das APIs) faz commit do resultado:

```bash
.venv/bin/python tools/sync.py sync        # e/ou import-tdn / export-api / export-fluig-old-docs.py
.venv/bin/python tools/sync.py build-index
git add knowledge tools/catalog && git commit -m "docs: atualização da base TOTVS"
```

Os demais só fazem `git pull` — a busca se reindexa sozinha na próxima consulta.
Regra: **somente documentação oficial TOTVS** em `knowledge/` (nada de cliente).

## Uso

```bash
# Primeiro download completo
python tools/sync.py sync

# Sync incremental (só o que mudou)
python tools/sync.py sync

# Uma fonte específica
python tools/sync.py sync --source style-guide

# Forçar re-download
python tools/sync.py sync --force

# Ver estatísticas
python tools/sync.py status
```

## Sync semanal (cron)

```bash
chmod +x tools/scripts/manutencao/weekly-sync.sh

# Editar crontab: todo domingo às 3h
crontab -e
# 0 3 * * 0 "<CAMINHO_DA_BASE>/tools/scripts/manutencao/weekly-sync.sh"
```

## Estrutura de dados

Três camadas (caminhos definidos em `tools/mirror/paths.py`; visão completa em `AGENTS.md`):

```
.cache/                  # regenerável — pode apagar (o próximo sync baixa de novo)
├── search.db            # busca full-text (gerada por build-index / auto)
├── manifest.db          # controle incremental (URLs, hashes, datas)
├── mirror/<fonte>/      # espelho raw (HTML, JSON, assets)
├── chunks/<fonte>/      # JSON exportado pelos scripts de console (TDN)
└── secrets/             # cookies, sessões e perfis de browser do TDN
tools/catalog/           # gerado: _INDEX.md (roteador), index.json (metadados), blocklist de descontinuados
knowledge/               # ⭐ somente documentação oficial TOTVS — Markdown com metadados
├── fluig/    tdn-fluig, api-fluig, rest-fluig, sdk-fluig, style-guide
├── protheus/ central-protheus, tdn-tec
├── rm/       central-rm, tdn-rm
└── totvs/    central-ciclo-vida
```

### Formato Markdown (otimizado para RAG)

Cada arquivo `.md` tem **frontmatter YAML** com metadados e corpo em Markdown limpo:

```markdown
---
title: CSS
source: style-guide
product: fluig
type: documentation
url: https://style.fluig.com/css.html
fetched_at: 2026-06-28T16:00:00+00:00
content_hash: abc123...
---

## Grids
...
```

Isso é o formato ideal para:
- **Cursor / Claude** com `@` em pastas
- **RAG** (embeddings + busca vetorial)
- **LlamaIndex, LangChain**, etc.

### O que cada fonte gera

| Fonte | Raw (`mirror/`) | IA (`knowledge/`) |
|-------|-----------------|-------------------|
| style-guide | HTML + CSS + imagens | `.md` por página |
| tdn-fluig | HTML renderizado | `.md` por página |
| central-protheus | JSON Zendesk | `.md` por artigo de suporte |
| central-rm | JSON Zendesk | `.md` por artigo de suporte |
| api-fluig | JS bundles (SPA) + swagger.json | `.md` por módulo API (11 módulos, ~215 endpoints) |

### Regenerar knowledge a partir do espelho existente

```bash
.venv/bin/python tools/sync.py export        # HTML + fórum + API Fluig
.venv/bin/python tools/sync.py export-api    # só specs OpenAPI da API Fluig
```

## TDN — contornar Cloudflare (recomendado)

O Cloudflare **detecta automação** (Playwright) e entra em loop. Use uma destas alternativas:

### Opção A — Script no Console do Chrome (mais simples)

1. Abra o **Chrome normal** (não pelo script)
2. Acesse https://tdn.totvs.com/display/public/fluig/Central+de+ajuda
3. Passe o Cloudflare **no seu browser habitual** (costuma funcionar melhor)
4. **F12 → Console** → abra `tools/scripts/console/tdn-export-console.js`, copie tudo e cole no console
5. Aguarde o download de `tdn-fluig-export.json`
6. Importe:

```bash
.venv/bin/python tools/sync.py import-tdn ~/Downloads/tdn-fluig-export.json
```

Gera Markdown em `knowledge/` automaticamente. Para atualizar depois, rode o script no console de novo e importe de novo (só páginas novas/alteradas são ignoradas).

### Opção B — Chrome com depuração remota (sync automático depois)

Terminal 1:

```bash
chmod +x tools/scripts/tdn/open-chrome-tdn.sh
./tools/scripts/tdn/open-chrome-tdn.sh
```

Passe o Cloudflare na janela que abrir. Terminal 2:

```bash
.venv/bin/python tools/sync.py sync-tdn-cdp
```

Usa **seu** Chrome real — sem abrir browser automatizado.

### Opção C — auth-tdn (pode falhar)

`sync.py auth-tdn` só se as opções acima não servirem — Cloudflare costuma bloquear.

## APIs Fluig (REST e SDK)

São três conjuntos em api.fluig.com, todos atuais (o `/old/` da URL não significa obsoleto):

| Fonte | O que é | Atualizar |
|-------|---------|-----------|
| `api-fluig` | OpenAPI dos módulos novos (`/latest/<módulo>/swagger-ui`) | `.venv/bin/python tools/sync.py export-api` |
| `rest-fluig` | API REST pública `/api/public/...` + tipos de dados (VOs JSON) | `export-fluig-old-docs.py rest` + import |
| `sdk-fluig` | Javadoc do `fluig-sdk-api.jar` (`fluigAPI`, VOs Java) | `export-fluig-old-docs.py sdk` + import |

```bash
.venv/bin/python tools/scripts/fluig-api/export-fluig-old-docs.py rest
.venv/bin/python tools/sync.py import-tdn .cache/chunks/rest-fluig/rest-fluig-export.json --source rest-fluig
.venv/bin/python tools/scripts/fluig-api/export-fluig-old-docs.py sdk
.venv/bin/python tools/sync.py import-tdn .cache/chunks/sdk-fluig/sdk-fluig-export.json --source sdk-fluig
.venv/bin/python tools/sync.py build-index --product fluig
```

Não precisa de browser (não há Cloudflare).

## Expandir para RM e Protheus

Fontes configuradas em `tools/config/sources.yaml`:

```bash
.venv/bin/python tools/sync.py sync --source central-protheus
.venv/bin/python tools/sync.py sync --source central-rm
```

A seção Protheus inclui módulos adicionais (Backoffice, Framework, Manufatura, etc.) via `extra_root_section_ids`.

## Visualizar localmente

```bash
# API docs (SPA)
cd .cache/mirror/api-fluig/api.fluig.com/latest
python3 -m http.server 8080
# Abra http://localhost:8080

# Style guide
cd .cache/mirror/style-guide/style.fluig.com
python3 -m http.server 8081
```

## Próximos passos sugeridos

- Embeddings para RAG com o conteúdo em `knowledge/`
