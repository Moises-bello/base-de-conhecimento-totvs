---
article_id: 4409197960983
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 91a2d24ad7fd3b683b144e23e763d7fc30cde77167d9909c464b87cdb673cbb0
fetched_at: '2026-06-28T22:38:29.957810+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Divergência
  no valor da parcela utilizando condição de pagamento 9 da Planilha Financeira quando
  há IPI
type: support-article
updated_at: '2021-09-22T16:55:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409197960983-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Diverg%C3%AAncia-no-valor-da-parcela-utilizando-condi%C3%A7%C3%A3o-de-pagamento-9-da-Planilha-Financeira-quando-h%C3%A1-IPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Valor diferente entre parcela do Pedido de Venda e da planilha financeira do pedido de vendas utilizando condição de pagamento tipo 9 quando há IPI na nota.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Somente para o tipo de condição de pagamento 9, o parâmetro **MV\_IPITP9** define se o valor do IPI será incluso nas parcelas, desta forma, será necessário certificar-se que o seu Pedido esteja calculando IPI:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409197687575/mceclip2.png)

Por exemplo: Pedido de Venda no valor de R$ 1.371,60 + R$ 120,42 de frete + R$ 74,60 IPI

Total: R$ 1.566,62

As parcelas digitadas para gerar as duplicatas foram:

1º Parcela: R$ 1.000,00 - Vencimento 22/09/2021

2º Parcela: R$ 566,62 - Vencimento 23/09/2021.

Ao acessar a planilha financeira as duplicatas foram dividas da seguinte forma:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409197485463/mceclip1.png)

Isso ocorre por conta do IPI não estar incluso na parcela, ou seja, **MV\_IPITP9 = N,** dessa forma, o sistema inclui o valor de IPI nas parcelas, ficando diferente do valor que foi definido nas parcelas do cabeçalho do pedido.

Abaixo, utilizando o parâmetro **MV\_IPITP9 = S**, o valor de IPI já vem incluso no valor das parcelas:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409197727895/mceclip3.png)

**Obs**. Esse processo é válido também para o Televendas do módulo Call Center, ao efetuar a venda, definir as parcelas e gerar o Pedido de Venda com a condição tipo 9, o sistema valida a configuração do parâmetro **MV\_IPITP9.**

**Saiba Mais: [Condição de Pagamento Tipo 9](https://tdn.totvs.com/x/LiAwDg)**
