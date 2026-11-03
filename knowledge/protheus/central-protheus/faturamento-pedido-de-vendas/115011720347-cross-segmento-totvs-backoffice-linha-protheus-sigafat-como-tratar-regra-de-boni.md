---
article_id: 115011720347
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b1be2e3defea391e845b3128088ee7fe4130f074c11689361e9281ad286c0b01
fetched_at: '2026-06-28T22:38:38.494838+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como tratar
  regra de bonificação financeira sobre os pedidos
type: support-article
updated_at: '2026-05-22T18:52:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011720347-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-tratar-regra-de-bonifica%C3%A7%C3%A3o-financeira-sobre-os-pedidos
---

**Dúvida**

Como tratar regra de bonificação financeira sobre os pedidos?  
  

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Preciso bonificar meus clientes em 5% ao atingirem o valor de vendas de R$ 20.000,00, porém, surgiu as seguinte dúvida:  
  
O Microsiga Protheus considera esse valor de R$ 20.000,00 que foi especificado na regra , somando todos os pedidos do cliente ou ele leva em consideração apenas um pedido de cada vez?  Exemplo: se o cliente tiver dois pedidos, onde o primeiro tenha valor de 15.000,00 e o segundo pedido tenha valor de 10.000,00, esse cliente terá bonificação?

O sistema levará em consideração a soma dos dois pedidos para realizar a Bonificação Financeira.

No exemplo em questão, ao processar a bonificação financeira, o sistema soma estes pedidos faturados para verificar se atingiram o valor de R$20.000,00, feita esta verificação e validado que atingiu o valor, é concedido a bonificação.

Outra situação possível , quando é efetuado uma terceira venda, no valor total de R$ 20.000,00, após faturar este pedido e processar a bonificação financeira, o sistema concede a bonificação desta venda também, porém, estornando o primeiro título gerado e acumulando a primeira bonificação com a segunda em  um único título para o cliente.   
Desta forma, o sistema somente levará em consideração o valor cheio, se há vários pedidos parciais e no final chegar ao valor estipulado, a bonificação será gerada.
