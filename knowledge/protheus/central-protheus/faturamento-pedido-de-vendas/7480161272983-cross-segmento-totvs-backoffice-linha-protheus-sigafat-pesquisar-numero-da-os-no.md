---
article_id: 7480161272983
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: dbc8ea95ee3d1f1e4e31eaadb4ceaa78a27c1a6c8c0fd6aebb8c5d211eab5774
fetched_at: '2026-06-28T22:38:38.604777+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pesquisar numero
  da OS no pedido de vendas
type: support-article
updated_at: '2022-08-09T11:26:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7480161272983-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pesquisar-numero-da-OS-no-pedido-de-vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como pesquisar numero da OS no pedido de vendas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

Quando uma **Ordem de Serviço(OS)** é efetivada em pedido de venda, o sistema marca dois campos:

**c6\_pedcli** ---> conterá o número do atendimento da ordem de serviço

**c6\_numos** - conterá o código da OS efetivada em pedido

Desta forma, para pesquisar o número da Os, basta buscar em consultas , cadastros, genéricos, da tabela SC6:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7480101725207/mceclip0.png)
