---
article_id: 360025018113
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ec4c12a29b6352f061a19a83ca63aa87c6a37ec9c3302daafdd5819b77deb9e8
fetched_at: '2026-06-28T22:38:42.377444+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Parâmetro  MV_ALTPED
type: support-article
updated_at: '2025-11-17T13:59:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025018113-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metro-MV-ALTPED
---

**Dúvida**

Como faço para que os pedidos faturados não sejam alterados?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Para não permitir a alteração  do pedido após o faturamento, configure o parâmetro **MV\_ALTPED** igual a **Não (N)**.

Este parâmetro é justamente para bloquear a alteração de um pedido de venda (**MATA410**) *totalmente* faturado, se o pedido foi faturado parcialmente, o parâmetro não irá tratar.
