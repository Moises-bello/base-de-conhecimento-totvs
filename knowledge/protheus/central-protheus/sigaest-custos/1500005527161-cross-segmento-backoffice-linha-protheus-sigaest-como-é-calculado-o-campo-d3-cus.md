---
article_id: 1500005527161
category: SIGAEST - CUSTOS
content_hash: cce52575f0a89b349e97ab146a27c388b265fcdc57a60a068ff46905f18e6be6
fetched_at: '2026-06-28T22:39:00.513244+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus)  - SIGAEST - Como é calculado
  o campo D3_CUSTO1 ao efetuar Movimentos Internos?
type: support-article
updated_at: '2025-03-12T12:25:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-calculado-o-campo-D3-CUSTO1-ao-efetuar-Movimentos-Internos
---

**Dúvida**Como é composto o custo em Movimentos Internos? Como é montado o campo D3\_CUSTO1? Qual a equação que relaciona Movimento Interno com os saldos físico e financeiro na SB2/Kardex?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Antes de entrarmos no assunto do campo D3\_CUSTO1, é importante que saibamos como é montado o custo em entradas/compras e também de vendas/pedido de vendas. Caso tenha dúvidas de como é montado D1\_CUSTO e D2\_CUSTO1, veja a 1° parte  e 2° parte deste artigo contida nos boletins abaixo:

|  |
| --- |
| **[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)** |
| **[MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)** |

**Observação:** Este artigo abordará a montagem do campo D3\_CUSTO1 sem entrar no viés do tipo de movimento.

**Montagem do Custo em Movimentações Internas (D3\_CUSTO1)**

Para entendermos melhor como é composto o campo D3\_CUSTO1, vamos utilizar o cenário e a tabela abaixo:

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
| Requisição | -3  **(D3\_QUANT)** | R$ 2,50  **(B2\_CM1)** | R$ 7,50  **(D3\_CUSTO1)** | R$ 2,50  **(B2\_CM1)** | R$ 5,00  **(B2\_VATU1)** | 2  **(B2\_QATU)** |

|  |  |
| --- | --- |
| **Leg****enda** | **Tabela SD1** |
| **Tabela SD2** |
| **Tabela SB2** |
| **Tabela SD3** |

Com isso, perceba que, **com as movimentações de venda (em vermelho)**, o produto permanece com Custo Unitário de R$ 2,50, que nada mais é do que o resultado de Valor Total / Quantidade.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007619221)

Caso queira entender melhor como é composto o Custo com Compras (Doc. de Entrada) e Vendas (Pedido de Venda), bem como gerou estes valores acima, **clique nos boletins do início do artigo pois este seguirá a sequência deles.**

**O que o sistema fez na requisição?**

Considerando que nosso produto tem:

Custo Total = R$ 12,50

Quantidade = 5

Custo Unitário Médio = R$ 2,50

O Protheus cria o campo D3\_CUSTO1 com base na seguinte equação:

**D3\_QUAN****T** **\*** **B2\_CM1=** **D3\_CUSTO1**

**3 \*  2,50 = R$ 7,50**

Com isso, é calculada a nova quantidade e custo total do produto, com base na seguinte equação:

**B2\_VATU1** **- D3\_CUSTO1** **=** **B2\_VATU1** **atualizado**

**12,50** - **7,50**= **R$ 5,00**

**B2\_QATU** **-** **D3\_QUANT** **=** **B2\_QATU atualizado**

**5 - 3 = 2**

**B2\_VATU1 atualizado** **/** **B2\_QATU atualizado** **=** **B2\_CM1** (**que nunca muda em vendas/movimentações internas**)

**5 / 2 = 2,50**

**Observações importantes:**

* Por padrão, uma Compra (Doc de Entrada) **pode mudar** o Custo Médio Unitário (B2\_CM1). Já a Venda (Pedido de Venda) e Movimentos Internos, **apenas consomem** o Custo Médio Unitário (B2\_CM1) já existente, pois o conceito é de que a saída leva o mesmo custo atual do produto quando ele sai do Armazém.
* Movimentos Internos, independentemente da rotina, sempre vai efetuar a equação D3\_QUANT \* B2\_CM1 = D3\_CUSTO1.

**CENÁRIO PRÁTICO**

Utilizaremos estes dados abaixo para simulação da teoria explicada acima:

Produto: PA78

Custo Total = R$ 12,50

Quantidade = 5

Custo Unitário Médio = R$ 2,50

**Vamos para o uma requisição manual (MATA241):**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007619521)**

Perceba que o campo "Custo" está zerado. Mesmo que colocássemos qualquer valor diferente o sistema mesmo assim fará a equação D3\_QUANT \* B2\_CM1 = D3\_CUSTO1

Agora vamos ver se os dados na base batem com o primeiro registro de requisição da tabela:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007568782)

Vamos analisar no Kardex

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007733361)

Com isso, confirma-se as informações apresentadas na teoria do início do artigo.

**Saiba mais:**

*[MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)*

*[MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)*

*[MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR860 - Interpretando Custos em Ordem de Produção (OP)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012330641)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)*
