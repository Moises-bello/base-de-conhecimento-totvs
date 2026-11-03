---
article_id: 360016648671
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 7b848fa4686328ff1154e10654a89f2266dd8555ecb33290a793ad82366a4528
fetched_at: '2026-06-28T22:38:45.048772+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Faturamento
  pela Segunda Unidade de Medida
type: support-article
updated_at: '2026-04-10T11:48:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016648671-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-pela-Segunda-Unidade-de-Medida
---

**Dúvida**

Como realizar o Faturamento pela Segunda Unidade de Medida?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A segunda Unidade de Medida do Produto (UM Secundária) é utilizada como facilitadora, de forma que:

Estando o cadastro de Produto devidamente configurado para Fator de Conversão, é possível digitar nos registros de Movimentos (tanto em movimento de entrada como o Pedido de Compra; como em movimento de saída como o Pedido de Venda) a quantidade direto no campo da Segunda Unidade de Medida, e então, o sistema automaticamente converte a quantidade no campo da Primeira Unidade (para evitar seu cálculo de conversão manual).

**Resultado do faturamento em segunda unidade de medida por etapas:**

Abaixo um exemplo, faturando um item com o valor de R$10 inserido no pedido de venda:

**1) No cadastro do Produto (MATA010):**

| B1\_UM | B1\_SEGUM | B1\_CONV | B1\_TIPCONV |
| --- | --- | --- | --- |
| UN | T | 10,00 | M - Multiplicador |

**2) Ao colocar o produto no Pedido de Vendas (MATA410):**

| C6\_QTDVEN | C6\_UM | C6\_UNSVEN | C6\_SEGUM | C6\_QTDLIB | C6\_QTDLIB2 |
| --- | --- | --- | --- | --- | --- |
| **10,00**(por exemplo) | UN | **100,00** (C6\_QTDVEN \* B1\_CONV) | T | 0,00 | 0,00 |

**3) Ao liberar completamente todo o item do pedido de venda:**

| C9\_QTDLIB | C9\_QTDLIB2 |
| --- | --- |
| 10,00 | 100,00 |

**4) Ao faturar o pedido de vendas:**

| D2\_QUANT | D2\_UM | D2\_QTSEGUM | D2\_SEGUM |
| --- | --- | --- | --- |
| **10,00** | UN | **100,00** | T |

Saiba mais:

<https://tdn.totvs.com/x/AIvXDw>
