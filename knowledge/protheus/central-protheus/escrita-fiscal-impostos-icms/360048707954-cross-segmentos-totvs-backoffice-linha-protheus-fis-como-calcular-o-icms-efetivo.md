---
article_id: 360048707954
category: Escrita Fiscal - Impostos - ICMS
content_hash: 6d4d517542e8a89c26a81bb2bb30760071b756e1b9b1c605e7c2a6e2dd27fa02
fetched_at: '2026-06-28T22:39:24.388556+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como calcular o icms
  efetivo para atacadista ? '
type: support-article
updated_at: '2021-07-27T17:38:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048707954-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-icms-efetivo-para-atacadista
---

**Dúvida**Como calcular o ICMS efetivo para o atacadista regra 04 ?   
  
**Ambiente**Protheus - Fiscal - 11.80  
  
**Solução**  
Para calcular o icms efetivo nas notas fiscais de saídas, precisa criar um código de reflexo amarrado na TES

Notas fiscais Saídas

Tipo de cliente = Consumidor Final

CST = 60

TES

Atualiza estoque = sim

Calcula icms = não

L. fiscal icms = isento ou outras

CST = 60

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073681753/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073681813/mceclip1.png)

No momento do pedido de vendas será criado a CDA com o valor do icms efetivo

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073682013/mceclip2.png)
