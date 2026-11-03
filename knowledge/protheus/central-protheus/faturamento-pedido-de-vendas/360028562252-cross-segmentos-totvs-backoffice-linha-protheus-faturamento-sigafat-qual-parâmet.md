---
article_id: 360028562252
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 02ff2caa8f69192ae521406efb30d56eea3b07d2fbb94c6c1953c557d06e5b42
fetched_at: '2026-06-28T22:38:41.196921+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT )- Qual
  parâmetro habilitar para mostrar o motivo do bloqueio de regra
type: support-article
updated_at: '2023-03-24T18:55:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028562252-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Qual-par%C3%A2metro-habilitar-para-mostrar-o-motivo-do-bloqueio-de-regra
---

**Ocorrência**

Qual parâmetro habilitar para mostrar o motivo do bloqueio de regra?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Para que o sistema apresente o motivo do bloqueio de regra é necessário ativar o parâmetro **MV\_VEBLQRG** **= .T.** ele ira habilitar a opção **Blq. Regra** na rotina de Liberação de Pedido de Venda **MATA440**.

![BLOQ_REGRA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360029594611/BLOQ_REGRA.gif)
