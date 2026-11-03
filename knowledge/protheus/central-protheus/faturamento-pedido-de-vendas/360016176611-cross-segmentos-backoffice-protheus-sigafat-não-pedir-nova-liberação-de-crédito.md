---
article_id: 360016176611
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0e7887d04d64ad82dfa2125b307e02e18314e2a0188b3ad5c0a33f511a9c6b13
fetched_at: '2026-06-28T22:38:39.893935+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Não pedir nova liberação
  de crédito em liberações seguintes (MV_AVALCRD)
type: support-article
updated_at: '2026-04-06T12:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016176611-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-N%C3%A3o-pedir-nova-libera%C3%A7%C3%A3o-de-cr%C3%A9dito-em-libera%C3%A7%C3%B5es-seguintes-MV-AVALCRD
---

**Dúvida**

Qual o comportamento do uso do parâmetro **MV\_AVALCRD** na alteração de um Pedido de Vendas com liberação?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões.

**Solução**

Segue o comportamento do parâmetro , conforme a informação indicada:

* Configurando o parâmetro **MV\_AVALCRD** como **.F.**:  Toda alteração do Pedido de Venda com liberação exigirá uma nova análise de crédito.
* Configurando o parâmetro **MV\_AVALCRD** como **.T.**:  Indica que durante a alteração de um Pedido de Venda com liberação, a análise de crédito será avaliada com base no valor total da última liberação do respectivo pedido. Ou seja, se o novo valor para o Pedido de Venda não ultrapassar ao valor da sua última liberação, o mesmo terá seu crédito liberado, automaticamente. Caso contrário, será exigida uma nova análise de crédito.

**OBSERVAÇÃO:**

**1.** Para que o pedido não perca a liberação de crédito, na alteração do pedido de venda tem que ser informada quantidade no campo "Qtd.Liberada" (**C6\_QTDLIB**).

**2.** O parâmetro **MV\_AVALCRD** servirá para controlar se deve ou não gerar um novo bloqueio em relação ao limite de crédito, mas não sobre o **risco de inadimplência** do ciente, isto significa que os **Pedidos de Venda** cujo **Cliente** possua título vencido a mais tempo que a tolerância designada para este em seu risco (**RISCO-B**,**RISCO-C**ou**RISCO-D**) sofrerão o bloqueio, assim como os clientes **RISCO-E**.

Para visualização de exemplos da aplicação do parâmetro, acesse: [Comportamento do parâmetro MV\_AVALCRD no Pedido de Venda](https://tdn.totvs.com/x/woFPFg)
