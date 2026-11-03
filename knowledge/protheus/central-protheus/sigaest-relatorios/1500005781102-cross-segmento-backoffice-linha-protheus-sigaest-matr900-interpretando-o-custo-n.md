---
article_id: 1500005781102
category: SIGAEST - RELATORIOS
content_hash: 1226fe51c4618d9edb58c117506d5a9f4454f07c824e0aa9b921d53be1e2e6a3
fetched_at: '2026-06-28T22:39:06.194058+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Interpretando
  o Custo no Kardex antes e depois do Recálculo do Custo Médio
type: support-article
updated_at: '2026-04-13T16:08:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005781102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Interpretando-o-Custo-no-Kardex-antes-e-depois-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio
---

O artigo explica como interpretar o Kardex MATR900 antes e depois do Recálculo do Custo Médio no TOTVS Protheus. Antes do recálculo, a sequência de impressão segue a data de digitação; após, deve-se usar a sequência "Cálculo", pois o sistema reordena os movimentos conforme a ordem padrão (compras, movimentos internos e vendas). O recálculo ajusta os custos unitários e totais, influenciando os movimentos seguintes, e recomenda-se analisar o Kardex considerando essa ordenação para correta interpretação dos custos.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39711699975063)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como interpretar o Kardex - MATR900 e entender as mudanças que ocorrem nele depois do Recálculo do Custo Médio?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Antes de entrarmos no mérito da interpretação, é importante clarearmos alguns pontos:

* A pergunta "Sequencia de Impressão" **antes** **do Recálculo do Custo Médio**, tanto parametrizando como "Digitação" quanto "Cálculo", será impresso conforme a data da digitação (em ordem cronológica de datas).
* **Após** o Recálculo do Custo Médio, a interpretação do custo **deve ser sempre** **com "Sequência de impressão" =** **Cálculo** pois esse é o padrão que o sistema faz no Recálculo, então é desta forma que devemos analisar movimento por movimento e seus custos.

**Outro ponto importante:**

Este artigo mostrará movimentos e seus custos, mas não entraremos no mérito da explicação de como foram montados. Caso queira entender como ocorrem os cálculos dos custos e seus impactos na tabela SB2 com Entradas (**D1\_CUSTO**), Saídas (**D2\_CUSTO1**) e Movimentos Internos (**D3\_CUSTO1**), clique nos boletins abaixo:

|  |
| --- |
| [**MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202) |
| [**MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422) |
| [**MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161) |

**Cenário para interpretação do Kardex antes e depois do Recálculo do Custo Médio**

Temos abaixo uma tabela de Movimentações que fizemos para o nosso produto PA78, onde o mesmo inicialmente ele tinha:

Quantidade Inicial (B2\_QATU): 0

Custo Inicial Médio (B2\_CM1): R$ 0,00

Custo Total (B2\_VATU1): R$ 0,00

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Data** | **Movimento** | **Quantidade** | **Custo Unitário** | **Custo da Movimentação** | **CM Unitário** | **Valor Total em Estoque** | **Quantidade Total em Estoque** |
| 29/03/2021 | NF Entrada | +10  **(D1\_QUANT)** | R$ 1,00  **(D1\_VUNIT)** | R$ 10,00  **(D1\_CUSTO)** | R$ 1,00  **(B2\_CM1)** | R$ 10,00  **(B2\_VATU1)** | 10  **(B2\_QATU)** |
| 29/03/2021 | NF Entrada | +10  **(D1\_QUANT)** | R$ 4,00  **(D1\_VUNIT)** | R$ 40,00  **(D1\_CUSTO)** | R$ 2,50  **(B2\_CM1)** | R$ 50,00  **(B2\_VATU1)** | 20 **(B2\_QATU)** |
| 30/03/2021 | NF Saída | -8  **(D2\_QUANT)** | R$ 2,50  **(B2\_CM1)** | R$ 20,00  **(D2\_CUSTO1)** | R$2,50  **(B2\_CM1)** | R$ 30,00  **(B2\_VATU1)** | 12  **(B2\_QATU)** |
| 30/03/2021 | NF Saída | -7  **(D2\_QUANT)** | R$ 2,50  **(B2\_CM1)** | R$ 17,50  **(D2\_CUSTO1)** | R$2,50  **(B2\_CM1)** | R$ 12,50  **(B2\_VATU1)** | 5  **(B2\_QATU)** |
| 31/03/2021 | Requisição | -3  **(D3\_QUANT)** | R$ 2,50  **(B2\_CM1)** | R$ 7,50  **(D3\_CUSTO1)** | R$ 2,50  **(B2\_CM1)** | R$ 5,00  **(B2\_VATU1)** | 2  **(B2\_QATU)** |
| 01/04/2021 | NF Entrada | + 8  **(D1\_QUANT)** | R$ 5,00  **(D1\_VUNIT)** | R$ 40,00  **(D1\_CUSTO)** | R$ 4,50  **(B2\_CM1)** | R$ 45,00  **(B2\_VATU1)** | 10  **(B2\_QATU)** |

|  |  |
| --- | --- |
| **Legenda** | **Tabela SD1** |
| **Tabela SD2** |
| **Tabela SB2** |
| **Tabela SD3** |

Movimentações feitas e emissão de Kardex:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007626922)

Recálculo do Custo Médio com Apropriação Mensal apenas para exemplo pois é a Apropriação mais comum. ([**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291) para ter mais informações sobre as perguntas do Recálculo do Custo Médio):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007642282)

**O que o Recálculo faz com o Custo dos Movimentos?**

Com base nas perguntas do Recálculo do Custo Médio, ele vai reordenar de forma que atenda a ordenação padrão dos custos do Produto. [**Clique aqui para entender como é a ordenação padrão no Recálculo**)](https://tdn.totvs.com/x/A9pc)

**Após o Recálculo do Custo Médio...**

Veja como fica a nossa tabela que fizemos no início do artigo após o Recálculo:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Data** | **Movimento** | **Quantidade** | **Custo Unitário** | **Custo da Movimentação** | **CM Unitário** | **Valor Total em Estoque** | **Quantidade Total em Estoque** |
| 29/03/2021 | NF Entrada | +10  **(D1\_QUANT)** | R$ 1,00  **(D1\_VUNIT)** | R$ 10,00  **(D1\_CUSTO)** | R$ 1,00  **(B2\_CM1)** | R$ 10,00  **(B2\_VATU1)** | 10  **(B2\_QATU)** |
| 29/03/2021 | NF Entrada | +10  **(D1\_QUANT)** | R$ 4,00  **(D1\_VUNIT)** | R$ 40,00  **(D1\_CUSTO)** | R$ 2,50  **(B2\_CM1)** | R$ 50,00  **(B2\_VATU1)** | 20 **(B2\_QATU)** |
| 01/04/2021 | NF Entrada | + 8  **(D1\_QUANT)** | R$ 5,00  **(D1\_VUNIT)** | R$ 40,00  **(D1\_CUSTO)** | R$ 3,21  **(B2\_CM1)** | R$ 90,00  **(B2\_VATU1)** | 28  **(B2\_QATU)** |
| 31/03/2021 | Requisição | -3  **(D3\_QUANT)** | R$ 3,21  **(B2\_CM1)** | R$ 9,64  **(D3\_CUSTO1)** | R$ 3,21  **(B2\_CM1)** | R$ 80,36  **(B2\_VATU1)** | 25  **(B2\_QATU)** |
| 30/03/2021 | NF Saída | -8  **(D2\_QUANT)** | R$ 3,21  **(B2\_CM1)** | R$ 25,72  **(D2\_CUSTO1)** | R$ 3,21  **(B2\_CM1)** | R$ 54,64  **(B2\_VATU1)** | 17  **(B2\_QATU)** |
| 30/03/2021 | NF Saída | -7  **(D2\_QUANT)** | R$ 3,21  **(B2\_CM1)** | R$ 22,50  **(D2\_CUSTO1)** | R$ 3,21  **(B2\_CM1)** | R$ 32,14  **(B2\_VATU1)** | 10  **(B2\_QATU)** |

Perceba que o Recálculo ordenou:

**1°** - Compras (Ordem de Cálculo 100)

**2°** - Movimentos Internos (Ordem de Cálculo 300)

**3°** - Vendas (Ordem de Cálculo 500)

A montagem de **D1\_CUSTO**, **D2\_CUSTO1** e **D3\_CUSTO1** permanece a mesma, só mudando o fato de que, como as compras ficaram acima, obviamente os custos "embutidos" influenciam os movimentos seguintes, então continua-se:

**D1\_CUSTO** **=** **D1\_QUANT** **\*** **V1\_VUNIT**

**D2\_CUSTO1** **=** **D2\_QUANT** **\*** **B2\_CM1**

**D3\_CUSTO1** **=** **D3\_QUANT** **\*** **B2\_CM1**

Além disso, dentro da SB2, a equação também é a mesma:

**B2\_VATU1 / B2\_QATU1 = B2\_CM1**

Veja o Kardex após o recálculo com Sequencia Impressão = Cálculo (que é o adequado para analisar):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007628102)

Com isso, podemos concluir que a análise de Kardex deve ser feita com critérios de entendimento com viés da ordenação do cálculo. Então recomendamos que sempre em caso de dúvidas sobre a ordem de um movimento no Kardex, comparar com a tabela do artigo de [**Ordenação de Movimentos**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17221653862551-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-feita-a-ordena%C3%A7%C3%A3o-dos-movimentos-ap%C3%B3s-rec%C3%A1lculo-do-custo-m%C3%A9dio) para entender se faz sentido mesmo aquele movimento estar ali ou não

**Observações:**

- Caso queria manipular a ordenação de forma que atenda ao seu negócio, avalie a utilização do Ponto de Entrada [**MA330TRB**](https://tdn.totvs.com/x/2uNc), onde podes escolher a regra desejada.

- Caso queira manipular a Ordenação de Movimentos internos, avalie a possibilidade de uso do parâmetro [**MV\_SEQ300.**](https://tdn.totvs.com/x/WrHPN)

**Saiba mais:**

[*MP - SIGAEST - Como é calculado o campo D1\_CUSTO ao efetuar um Documento de Entrada?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005383202)

[*MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422)

[*MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012224673-SIGAEST-RELATORIOS)
