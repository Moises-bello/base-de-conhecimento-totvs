---
article_id: 360053356334
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6305085d1cce7892a79bada4599af1ba5614aba56dab713bb02cc98db18794bd
fetched_at: '2026-06-28T22:38:38.690626+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Help
  A415QTDCTR
type: support-article
updated_at: '2023-04-20T13:48:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053356334-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Help-A415QTDCTR
---

**Ocorrência**

Ao incluir um pedido de vendas quando coloco o código do produto vou confirmar o pedido ele apresenta o help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090985253/mceclip0.png)

Como faço para corrigir e fazer um novo pedido de venda sem vincular ao contrato de parceria já existente?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT – todas as versões.

**Causa**

O problema ocorre por que o parâmetro **MV\_PRCCTR** está ativo, ele defini que se caso exista contrato de parceria,o sistema irá utiliza-lo durante a captação do Pedido de Venda ou Orçamento.  
  
**Solução**

Para solucionar essa ocorrência, deixe o parâmetro **MV\_PRCCTR**igual a**F.**
