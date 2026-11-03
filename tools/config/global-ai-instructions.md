# Base de conhecimento local — TOTVS (Fluig / Protheus / RM)

Para Fluig, Protheus, RM ou integração TOTVS (ou se o usuário citar "base/conhecimento local"), consulte esta base **antes** da web ou da memória. Só contém documentação oficial TOTVS.

Raiz: `{{KB_ROOT}}` — rode os comandos nela.

## Fluxo de menor custo (siga nesta ordem)

1. `.venv/bin/python tools/sync.py search "termos" --product fluig|rm|protheus [--source <fonte>]` → 5 resultados com caminho, URL, seção e trecho. Muitas vezes o trecho já responde.
2. `.venv/bin/python tools/sync.py show <caminho>` → doc pequeno vem inteiro; doc grande vem só o sumário de seções.
3. `.venv/bin/python tools/sync.py show <caminho> --secao "nome"` → só a seção necessária.

Não liste pastas, não abra `tools/catalog/index.json` nem `.md` grandes inteiros, não use `.cache/`. Qual fonte usar para cada assunto: `tools/catalog/_INDEX.md` (1 KB).

## Fluig — qual API

- REST nova (OpenAPI): `api-fluig` · REST pública `/api/public/...` + VOs JSON com campos: `rest-fluig` · Java `fluigAPI`/`WorkflowAPIService`: `sdk-fluig`.
- `api.fluig.com/old/...` **não** é obsoleto: é a doc oficial atual. Versão exata do cliente: `http://[servidor_fluig]/api`.

## Ao responder

- Cite a URL que o search/show mostra.
- Diferencie Fluig (ECM/BPM), Protheus (ERP) e RM (RH). RM: pergunta vaga → `central-rm`; técnica → `tdn-rm`.
- Não há schema de banco de cliente: não invente tabela/coluna; busque no TDN e confirme com o usuário.
- Busca inconclusiva → pergunte tela/rotina/versão antes de adivinhar.

## Skills oficiais TOTVS

`agents/totvs/fluig/` (skills `fluig-*`, convenções em `context/`) e `agents/totvs/advpl-tlpp/` (Protheus: `mvc-generator`, `query-builder`, `tlpp-rest-endpoint-generator`…). No Claude Code já estão em `~/.claude/skills/`; em outras ferramentas leia o `SKILL.md`. Prefira a skill oficial a gerar código do zero.
