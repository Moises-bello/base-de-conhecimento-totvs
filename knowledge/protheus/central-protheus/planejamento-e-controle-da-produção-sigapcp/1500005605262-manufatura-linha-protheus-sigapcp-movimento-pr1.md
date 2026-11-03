---
article_id: 1500005605262
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 327b1f44746191759d817f2b86fd31eeb8fc15c7048c1c1af4d74967e8d40fce
fetched_at: '2026-06-28T22:42:44.563284+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Movimento PR1
type: support-article
updated_at: '2022-09-09T17:08:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005605262-Manufatura-Linha-Protheus-SIGAPCP-Movimento-PR1
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**Quando é gerado o movimento **PR1 - Produção Automática**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O registro **PR1** ocorre quando o Sistema identifica que um empenho vai ser atendido com a produção de outro item através da informação registrada no campo **D4\_OPORIG - OP Origem**.  
Através desse campo é identificada qual a **OP - Ordem de Produção** que produzindo atenderá a demanda do componente e é realizada o registro de produção desse item, com **PR1** .
