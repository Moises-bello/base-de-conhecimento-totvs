---
article_id: 1500005465422
category: SIGAEST - CUSTOS
content_hash: 74372216e5af5ecba679e13b9f8d3f4706ac506f3559bc874e26b98f07d3b12e
fetched_at: '2026-06-28T22:39:00.729207+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o
  campo D2_CUSTO1 ao efetuar Pedido de Venda?
type: support-article
updated_at: '2025-08-27T18:03:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-calculado-o-campo-D2-CUSTO1-ao-efetuar-Pedido-de-Venda
---

**Dúvida**Como é composto o custo em movimentos de Saída (Pedido de Venda - MATA410)? Como é montado o campo D2\_CUSTO1? Qual a equação que relaciona o Pedido de Venda com os saldos físico e financeiro na SB2/Kardex?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Antes de entrarmos no assunto do campo D2\_CUSTO1, é importante que saibamos como é montado o custo em entradas/compras também. Caso tenha dúvidas, veja a 1° parte deste artigo contida no boletim abaixo:

|  |
| --- |
| **[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)** |

**Montagem do Custo em Vendas (D2\_CUSTO1)**

Para entendermos melhor como é composto o campo D2\_CUSTO1, vamos utilizar o cenário e a tabela abaixo:

**Produto: PA78**

**Saldo Físico Inicial: 0**

**Custo inicial: R$ 0,00**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Movimento** | **Quantidade** | **Custo Unitário** | **Custo da Movimentação** | **CM Unitário** | **Valor Total em Estoque** | **Quantidade Total em Estoque** |
| NF Entrada | +10  **(D1\_QUANT)** | R$ 1,00  **(D1\_VUNIT)** | R$ 10,00  **(D1\_CUSTO)** | R$ 1,00  **(B2\_CM1)** | R$ 10,00  **(B2\_VATU1)** | 10  **(B2\_QATU)** |
| NF Entrada | +10  **(D1\_QUANT)** | R$ 4,00  **(D1\_VUNIT)** | R$ 40,00  **(D1\_CUSTO)** | R$ 2,50  **(B2\_CM1)** | R$ 50,00  **(B2\_VATU1)** | 20 **(B2\_QATU)** |
| NF Saída | -8  **(D2\_QUANT)** | R$ 2,50  **(B2\_CM1)** | R$ 20,00  **(D2\_CUSTO1)** | R$2,50  **(B2\_CM1)** | R$ 30,00  **(B2\_VATU1)** | 12  **(B2\_QATU)** |
| NF Saída | -7  **(D2\_QUANT)** | R$ 2,50  **(B2\_CM1)** | R$ 17,50  **(D2\_CUSTO1)** | R$2,50  **(B2\_CM1)** | R$ 12,50  **(B2\_VATU1)** | 5  **(B2\_QATU)** |

|  |  |
| --- | --- |
| **Legenda** | **Tabela SD1** |
| **Tabela SD2** |
| **Tabela SB2** |

Com isso, perceba que, **com as movimentações de compra (em verde)**, o produto ficou com Custo Unitário de R$ 2,50, que nada mais é do que o resultado de Valor / Quantidade.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007455502)

Caso queira entender melhor como é composto o Custo com Compras (Doc. de Entrada) e como gerou estes valores acima, **[clique aqui e veja o artigo detalhado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)**

**O que o sistema fez na primeira venda?**

Considerando que nosso produto tem:

Custo Total = R$ 50,00

Quantidade = 20

Custo Unitário Médio = R$ 2,50

O Protheus cria o campo D2\_CUSTO1 com base na seguinte equação:

**D2\_QUAN****T** **\*** **B2\_CM1=** **D2\_CUSTO1**

**8 \*  2,50 = R$ 20,00**

Com isso, é calculada a nova quantidade e custo total do produto, com base na seguinte equação:

**B2\_VATU1** **- D2\_CUSTO1** **=** **B2\_VATU1** **atualizado**

**50** - **20** = **R$ 30,00**

**B2\_QATU** **-** **D2\_QUANT** **=** **B2\_QATU atualizado**

**20 - 8 = 12**

**B2\_VATU1 atualizado** **/** **B2\_QATU atualizado** **=** **B2\_CM1** (**que nunca muda em vendas/saídas**)

**30 / 12 = 2,50**

**O que o sistema fez na segunda venda?**

Para a segunda venda, o Protheus segue o mesmo efeito "cascata" da primeira, onde temos agora:

Custo Total = R$ 30,00

Quantidade = 12

Custo Unitário Médio = R$ 2,50

Onde é calculado o D1\_CUSTO1 com base em **D2\_QUAN****T** **\*** **B2\_CM1=** **D2\_CUSTO1**

**7 \*  2,50 = R$ 17,50**

E o novo Custo Total e Quantitativo é:

**B2\_VATU1 atualizado** **/** **B2\_QATU atualizado** **=** **B2\_CM1** (**que nunca muda em vendas/saídas**)

**12,50 / 5 = 2,50**

**Observações importantes:**

* Por padrão, uma Compra (Doc de Entrada) **pode mudar** o Custo Médio Unitário (B2\_CM1). Já a Venda (Pedido de Venda), **apenas consome** o Custo Médio Unitário (B2\_CM1) pois o conceito é de que a saída leva o mesmo custo atual do produto quando ele sai do Armazém.
* Não confunda D1\_TOTAL com D1\_CUSTO1, pois D1\_TOTAL é **sempre** o resultado de Quantidade \* Valor Unitário, enquanto o D1\_CUSTO1 que em suma é o mesmo resultado, pode ter mudanças a depender de variáveis como crédito/débito de impostos, frete, despesas, etc.

**CENÁRIO PRÁTICO**

Utilizaremos estes dados abaixo para simulação da teoria explicada acima:

Produto: PA78

Custo Total = R$ 50,00

Quantidade = 20

Custo Unitário Médio = R$ 2,50

**Vamos para o primeiro registro de saída (MATA410):**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007488741)**

Agora vamos ver se os dados na base batem com o primeiro registro de venda da tabela:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007339542)**

**Vamos para o segundo registro de saída (MATA410):**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007489281)**

Agora vamos ver se os dados na base batem com o primeiro registro de venda da tabela:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007489741)

Vamos analisar o Kardex:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007341102)

Então, confirma-se os dados da tabela no início do artigo.

**Para que o TES em questão CALCULE o custo do produto é necessário que o com F4\_ESTOQUE no cadastro do TES esteja = "SIM".**

**Ou seja, caso esteja como F4\_ESTOQUE = "NÃO", O CUSTO NÃO vai ser preenchido no campo D2\_CUSTO1 para notas fiscais do tipo normal.**

Caso deseje atualizar o Custo da nota fiscal do pedido de venda terá que avaliar na documentação do faturamento como fazer o tratamento:

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Atualização do campo D2\_CUSTO1 ao utilizar TES que atualiza estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429372-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Atualiza%C3%A7%C3%A3o-do-campo-D2-CUSTO1-ao-utilizar-TES-que-atualiza-estoque?source=search)

**Saiba mais:**

*[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)*

*[MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161)*

*[MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)*

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
