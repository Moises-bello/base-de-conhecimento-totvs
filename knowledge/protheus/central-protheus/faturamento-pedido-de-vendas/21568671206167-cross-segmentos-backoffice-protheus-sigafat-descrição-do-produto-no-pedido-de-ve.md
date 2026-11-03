---
article_id: 21568671206167
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d09a6525cfc55cd7fdb4e9f7ef903e06be1896e506d0a13203a14c7904368cbf
fetched_at: '2026-06-28T22:38:39.766426+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Descrição do produto no pedido
  de venda diferente por cliente
type: support-article
updated_at: '2024-02-23T17:09:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21568671206167-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Descri%C3%A7%C3%A3o-do-produto-no-pedido-de-venda-diferente-por-cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21568671178135) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

Como utilizar a descrição do produto no pedido de venda diferente por cliente, de modo que quando eu utilizar certo cliente com um certo produto no pedido de venda, seja informado uma descrição particular?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Para utilizar uma descrição que não é a que está informada no produto por padrão, de modo que só usará a descrição quando certo cliente estiver inserido no pedido de venda, é possível utilizar a rotina "MATA370 - Produto x Cliente".

**Passos:**

1 - Entrar na rotina "MATA370 - Produto x Cliente" e incluir um registro.

2 - Informar o cliente, loja e o produto.

3 - Informar o novo nome do produto no campo "Descr. Client (A7\_DESCCLI)":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21568671178775)

Assim está simbolizando ao Protheus, quando estiver o cliente "A" e loja "01" no pedido de venda, com o item "ZZ3", utilizar esse nome "PRODUTO A+ZZ3" e não a descrição do produto "Descrição (B1\_DESC)".

4 - Resultado ao informar no pedido de venda:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21568705020439)

"Descr. Client (A7\_DESCCLI)" levou valor ao campo "Descricao (C6\_DESCRI)"

**OBSERVAÇÃO:** O campo "Cod.Prod.Cli (A7\_CODCLI)" pode ser usado pela DANFE/XML, para substituir o código do item.
