---
article_id: 4412989812119
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 48e2b823b32f91884953e1ef9b376df4978237db674152da3519451547643945
fetched_at: '2026-06-28T22:38:43.885386+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Movimentação
  da tabela SD5 na nota de saída
type: support-article
updated_at: '2022-12-15T20:01:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412989812119-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Movimenta%C3%A7%C3%A3o-da-tabela-SD5-na-nota-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como movimentar a tabela SD5 através da nota de saída (mata460)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

O sistema efetua a movimentação da tabela **SD5 -** **Requisições por Lote**, quando o pedido de venda (mata410) faturado, está utilizando um produto com controle de rastreabilidade **(mv\_rastro=S)**, se ja **Lote** ou **Sub-lote**.

Uma vez  que o produto com lote é faturado , o sistema gera a movimentação na tabela **itens da nota** - **SD2** e irá gerar a movimentação na tabela **SD5 - Requisições por lote,** conforme a quantidade que foi vendida. Também gerará uma movimentação na **tabela de lotes - SB8**.

Para mais informações sobre movimentações de lote e sub-lote, acesse: [Como são gravados dados de Movimentos e Saldos de Lotes e Sublotes?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078488-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-s%C3%A3o-gravados-dados-de-Movimentos-e-Saldos-de-Lotes-e-Sublotes-)
