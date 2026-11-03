---
article_id: 19059175828759
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 06dcdf264fa6410971d8c1d592b072c9ccf9fda6fddf5ad31d224cd188a79b1c
fetched_at: '2026-06-28T22:42:44.448171+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem Data inicial de apontamento
  menor que a data de validade inicial da operação
type: support-article
updated_at: '2023-11-16T11:54:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19059175828759-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Data-inicial-de-apontamento-menor-que-a-data-de-validade-inicial-da-opera%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19059183365399)***Tempo aproximado para leitura: **00:00:50 min  
  
Ocorrência**Ao incluir o apontamento de produção através da rotina **MATA681 - Apontamento Produção Mod2**, é apresentada a mensagem **Data inicial de apontamento menor que a data de validade inicial da operação**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A operação informada não esta válida para a data inicial do apontamento.  
  
**Solução**  
Acesse o roteiro de operações através da rotina **PCPA124 - Processo Produtivo**, e ajuste a data inicial da operação através do campo **G2\_DTINI - Data de validade inicial**, para uma data anterior a data que está informando no campo **H6\_DATAINI - Data Inicial**.
