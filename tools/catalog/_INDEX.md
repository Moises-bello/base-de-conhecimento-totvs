# Base TOTVS — roteador

Não liste pastas: **busque** e abra só o necessário.

```bash
.venv/bin/python tools/sync.py search "termos" --product <produto> [--source <fonte>]
.venv/bin/python tools/sync.py show knowledge/<arquivo>.md                # pequeno: inteiro; grande: sumário
.venv/bin/python tools/sync.py show knowledge/<arquivo>.md --secao "nome" # só uma seção
```

| Produto | Fonte (`--source`) | Docs | Quando usar |
|---|---|---|---|
| fluig | `tdn-fluig` — TDN Fluig | 1706 | processos/BPM, datasets, formulários, widgets, servidor, instalação, FAQ |
| fluig | `api-fluig` — API REST (OpenAPI) | 11 | endpoints novos: admin, process-management, dataset, ecm-forms… |
| fluig | `rest-fluig` — API REST pública /api/public | 826 | endpoints /2.0, /ecm, /bpm, /alert e VOs JSON (campos, obrigatórios) |
| fluig | `sdk-fluig` — Fluig SDK Java | 216 | fluigAPI, WorkflowAPIService e VOs Java do fluig-sdk-api.jar |
| fluig | `style-guide` — Style Guide | 6 | componentes visuais, CSS, FLUIGC |
| rm | `central-rm` — Central de Atendimento RM | 2607 | como fazer, erro, rotina, configuração (perguntas vagas: comece aqui) |
| rm | `tdn-rm` — TDN RM (LRM) | 29850 | parâmetros, eSocial/CLT, WebServices, releases (técnico) |
| protheus | `central-protheus` — Central de Atendimento Protheus | 21848 | como fazer, erro, rotina, configuração |
| protheus | `tdn-tec` — TDN TEC | 1224 | AdvPL/TLPP, AppServer, SmartClient, TOTVS Platform |
| totvs | `central-ciclo-vida` — Ciclo de Vida TOTVS | 202 | comunicados, políticas, fim de suporte de versões |
