---
article_id: 25363240997911
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 10e44282ddcdbf426c6dc2f569b4ed6d64bfbf9ede854160e43e62ca97232ab7
fetched_at: '2026-06-28T22:38:39.790068+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Faturamento de Pedidos de
  Venda com Carga
type: support-article
updated_at: '2025-01-24T20:40:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25363240997911-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Faturamento-de-Pedidos-de-Venda-com-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25363240944919) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Qual processo para realizar o faturamento de pedidos de vendas vinculados a uma Carga?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Foram realizados ajustes para que, caso exista um pedido de venda vinculado a uma carga, esse pedido ou item não possa ser faturado pela rotina de **Documento de Saída (MATA460A)**, devendo ser faturado exclusivamente através da rotina de **Faturamento de Documento de Saída - Carga (MATA460B)**.

Esta regra tem por finalidade manter a integridade entre as tabelas envolvidas no processo de cargas e faturamento de documentos de saída.

Se houver necessidade de agrupar os itens do pedido em uma carga que já foi faturada, deve-se utilizar o parâmetro **MV\_MANCARG = S**.

**Observação:**Dúvidas relacionadas à rotina de **Faturamento de Documento de Saída de Carga (MATA460B)**entre em contato com a equipe Protheus OMS.

**Saiba mais:**

**[26080 DT Faturamento de Pedidos de Venda com Carga](https://tdn.totvs.com/x/CQmRMg)**
