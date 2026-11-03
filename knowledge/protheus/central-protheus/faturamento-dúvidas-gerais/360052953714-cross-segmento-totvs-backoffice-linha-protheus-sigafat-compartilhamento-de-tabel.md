---
article_id: 360052953714
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: f4e585080e411f396870ca0f6412e639a66f2a7e009919792111bd389fa449a8
fetched_at: '2026-06-28T22:38:28.523484+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Compartilhamento
  de tabelas do Modulo de Faturamento
type: support-article
updated_at: '2023-09-21T14:30:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052953714-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Compartilhamento-de-tabelas-do-Modulo-de-Faturamento
---

**Dúvida**

Como deve ser e qual o modo de compartilhamento usar no Modulo Faturamento ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Solução**

A operação de Faturamento (geração de Nota Fiscal de Saída de material) tem como premissa um Pedido de Vendas (SC5) com itens (SC6), a Liberação do Pedido de Vendas (SC9) e a geração da Nota Fiscal (SF2) com seus ítens (SD2).

Portanto, as tabelas SC5, SC6, SC9, SD2 e SF2 devem estar todas no mesmo modo de compartilhamento. (x2\_modo), ou todas compartilhadas ou todas exclusivas por filial.
