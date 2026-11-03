---
article_id: 360025649392
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1b35ccb0f1e654b70ee8903db2e72e465f11b431ae45f10827d9d51a6e913f3c
fetched_at: '2026-06-28T22:42:43.579251+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A240DTVALI
type: support-article
updated_at: '2021-06-07T10:38:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025649392-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A240DTVALI
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura:**00:00:45 min****Ocorrência**Ao alterar a data de validade do lote nas rotinas de apontamento de produção o usuário recebe a mensagem **A240DTVALI - A data de validade do lote será corrigida de acordo com a data de validade original**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**O Sistema valida se já existe um apontamento com esse número de lote e encontrando corrige a data de validade do apontamento para a data de validade do lote localizada.  
  
**Solução**Se a data de validade estiver errada:  
1. Acesse a rotina **MATA390 -  Manutenção de lotes**e corrija a data de validade do lote;  
2. Volte para a rotina de apontamento de produção e refaça o apontamento.
