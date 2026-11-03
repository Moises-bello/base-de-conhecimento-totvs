---
article_id: 1500005383202
category: SIGAEST - CUSTOS
content_hash: 9f011113974cac186ff23951d3c864fde7d4da48e93ee9c4c1dc89dbe4e49ee3
fetched_at: '2026-06-28T22:39:00.708476+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o
  campo D1_CUSTO ao efetuar um Documento de Entrada?
type: support-article
updated_at: '2026-03-17T17:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-calculado-o-campo-D1-CUSTO-ao-efetuar-um-Documento-de-Entrada
---

**Dúvida**  
Como é composto o custo em movimentos de Entrada (Documento de Entrada)? Como é montado o campo D1\_CUSTO? Qual a equação que relaciona o Documento de Entrada com os saldos físico e financeiro na SB2?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Para entendermos melhor como é composto o campo D1\_CUSTO, vamos utilizar o cenário e a tabela abaixo:

**Produto: PA78**

**Saldo Físico Inicial: 0**

**Custo inicial: R$ 0,00**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Movimento** | **Quantidade** | **Custo Unitário** | **Custo da Movimentação** | **CM Unitário** | **Valor Total em Estoque** | **Quantidade Total em Estoque** |
| NF Entrada | +10  **(D1\_QUANT)** | R$ 1,00  **(D1\_VUNIT)** | R$ 10,00  **(D1\_CUSTO)** | R$ 1,00  **(B2\_CM1)** | R$ 10,00  **(B2\_VATU1)** | 10  **(B2\_QATU)** |
| NF Entrada | +10  **(D1\_QUANT)** | R$ 4,00  **(D1\_VUNIT)** | R$ 40,00  **(D1\_CUSTO)** | R$ 2,50  **(B2\_CM1)** | R$ 50,00  **(B2\_VATU1)** | 20 **(B2\_QATU)** |

|  |  |
| --- | --- |
| **Legenda** | **Tabela SD1** |
| **Tabela SB2** |

Perceba que a regra para o custo da nota (**células verdes**) é:

**Quantidade (****D1\_QUANT****) x Custo Unitário (****D1\_VUNIT****) = Custo da Movimentação (****D1\_CUSTO****)**.

Essas informações são refletidas na tabela SB2 (**células em azul**) por meio das seguintes equações:

**D1\_QUANT** **+** **B2\_QATU** **=** **B2\_QATU atualizada**

**D1\_CUSTO** **+** **B2\_VATU1 = B2\_VATU1 atualizada**

Já o CM Unitário (B2\_CM1) **não** **é puxado** de D1\_VUNIT, mas sim de **B2\_VATU1 / B2\_QATU = B2\_CM1**

**Por qual motivo ficou com estes valores na tabela SB2 após a segunda entrada?**

Basicamente ocorre da seguinte forma:

Somatória de **D1\_CUSTO** das 2 NFs: **R$ 10,00** (**D1\_CUSTO**) **+ 40,00** (**D1\_CUSTO**)**= R$ 50,00** (**B2\_VATU1**)

Somatória de **D1\_QUANT** das 2 NFs: **10** (**D1\_QUANT**) **+ 10** (**D1\_QUANT**) **= 20** (**B2\_QATU**)

Equação final: **B2\_VATU1** / **B2\_QATU** = **B2\_CM1**

Então: **R$ 50,00 / 20 = R$ 2,50**

**B2\_CM1** **= R$ 2,50**

**CENÁRIO PRÁTICO**

Utilizaremos estes dados abaixo para simulação da teoria explicada acima:

Produto: PA78

Saldo Físico Inicial: 0

Custo inicial: R$ 0,00

**Vamos para o primeiro registro de entrada:**

1° - Dar entrada na primeira nota com TES que não tem nenhum imposto deduzindo do Custo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007127942)

Agora vamos ver se os dados na base batem com o primeiro registro da tabela:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007140282)

**Vamos para o segundo registro de entrada:**

2° - Agora vamos dar entrada na segunda nota:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007304321)

Agora vamos ver se os dados na base batem com o primeiro registro da tabela:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007151722)

Vamos analisar no Kardex:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007305281)

Então, confirma-se os dados da tabela no início do artigo.

**Observação sobre a relação de D1\_CUSTO com D1\_TOTAL e Impostos**

O campo SD1->D1\_CUSTO (Custo de entrada do produto) é em suma alimentado por Valor \* Quantidade. Porém, ele também pode ser alimentado após a apuração, outras variáveis de custo que a movimentação contabilize (Impostos creditados e debitados, despesas, frete, etc). Além disso, estas variáveis diferem conforme cadastro do TES utilizado e/ou tipo do documento digitado, integrações com módulos (SIGAEIC, SIGAEEC) ou ainda amarrações (notas complementares, GNRE).

Para analise deve-se filtrar o registro da tabela SD1 referente ao documento de entrada e verificar os campos e valores, para os tributos que farão parte do custo ou não, verifique com seu departamento fiscal se o TES utilizado possui as configurações corretas (esta analise deve ser realizado com a área fiscal ou analista em campo para avaliação dos campos da SF4, por se tratar de uma tabela fiscal que possui aproximadamente 220 campos que poderão interferir tanto no custo como também na escrituração fiscal).

**Importante:**

* Veja nesse link os impostos que podem afetar o custo do produto na nota fiscal de entrada:   
  [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Refaz Custo de Entrada (MATA190) - Conceito e Exemplos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)
* Para que o TES em questão agregue o custo do produto é necessário que o campo F4\_ESTOQUE esteja como "Sim". Caso o o campo F4\_ESTOQUE esteja como "Não" o custo não será atribuído ao produto porque a movimentação não atualiza estoque

**Saiba mais:**

[*MP - SIGAEST - MATR900 - Interpretando o Custo no Kardex antes e depois do Recálculo do Custo Médio*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102)

[*MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161)

[*MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
