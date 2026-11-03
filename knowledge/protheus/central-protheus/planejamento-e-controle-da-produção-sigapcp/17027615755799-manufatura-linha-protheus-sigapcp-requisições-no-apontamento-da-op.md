---
article_id: 17027615755799
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1c40de76c2015d65c002e34ce34c7c66a8e0d4d43e06a83c473e10e371c93f9a
fetched_at: '2026-06-28T22:42:45.884550+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Requisições no apontamento da OP '
type: support-article
updated_at: '2023-08-25T14:56:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17027615755799-Manufatura-Linha-Protheus-SIGAPCP-Requisi%C3%A7%C3%B5es-no-apontamento-da-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17027606727447) Tempo aproximado para leitura: **00:00:44 min** **Dúvida**As requisições registradas automaticamente na entrada da nota fiscal ou manualmente são descontadas da quantidade a ser requisitada no apontamento da **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**As requisições registras na entrada da nota fiscal, que preenchem o campo **D3\_CF - Tipo RE/DE** com **RE5 - Requisição informando OP na nota fiscal de entrada** ou preenchem o campo **D3\_CF** com **RE0 - Requisição manual** não são descontadas da quantidade a ser requisitada no apontamento da **OP**, se o saldo empenhado desse produto, isto é, se o campo **D4\_QUANT - Saldo do Empenho** estiver com o conteúdo diferente de 0.
