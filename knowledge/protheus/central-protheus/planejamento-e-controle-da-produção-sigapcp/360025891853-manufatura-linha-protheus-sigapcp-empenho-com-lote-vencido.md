---
article_id: 360025891853
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f6e200f4db2e39059b2e4388881c9b5298d6132ca530585349a2aef3cbc09c54
fetched_at: '2026-06-28T22:42:42.237722+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Empenho com lote vencido
type: support-article
updated_at: '2022-01-19T17:52:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025891853-Manufatura-Linha-Protheus-SIGAPCP-Empenho-com-lote-vencido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:34 min****Dúvida**Por que o Sistema empenha produtos com lote vencido?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Para que o Sistema não utilize lotes vencidos é necessário preencher o conteúdo do parâmetro **MV\_LOTVENC - Indica se devem ser utilizados Lotes/Sub-Lotes com a data de validade vencida.** com **N**.  
Desta forma o Sistema bloqueará a utilização dos lotes e sublotes vencidos.
