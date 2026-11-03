---
content_hash: 1a54a4db8989b5bdaa0e12613956500a46c291efd0017cd80d7c409a9e9cc05b
fetched_at: '2026-06-29T00:10:08.690197+00:00'
page_id: '452719559'
product: rm
source: tdn-rm
title: Exemplo de cálculo da avaliação de desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719559
version: 2
---

**Exemplo de cálculo da avaliação de desempenho**

**COMPETÊNCIA X ITENS DE PERFORMANCE**

Cálculo da Nota a ser Obtida na Competência:

1º) PesoItemPerfomance x Nota Obtida na Avaliação para o item(Conforme valor definido na escala)

2º) Soma dos pesos dos itens de performance (pesos definidos na função)

3º) Soma das notas obtidas

|  |
| --- |
| Fórmula: **NC = (pIP1 \* VN1) + (pIP2 \* VN2) + ...(pIPn \* VNn)+** |
| **(pIP1 + pIP2 + ...+pIPn)** |

  Onde

NC = Nota da Competência

pIP = peso do Item de Perfomance

VN = Valor da Nota Obtida na Avaliação

**Exemplo**

Vamos avaliar a função Atendente, competência Inglês, funcionário João da Silva. Competência: Inglês

|  |  |
| --- | --- |
| Itens de Perfomance | Peso |
| Compreensão | 1 |
| Escrita | 2 |
| Fala | 2 |

Função: Atendente Competência: Inglês

|  |  |
| --- | --- |
| Itens de Perfomance | Peso |
| Compreensão | 3 |
| Escrita | 3 |
| Fala | 3 |

**Observação**

O peso dos itens de performance pode ser alterado para uma determinada função, ou seja, não precisa ser o mesmo definido na competência.

Montagem da avaliação:

|  |  |
| --- | --- |
| Escala da Avaliação | Peso |
| Não Atende | 1 |
| Atende Parcialmente | 2 |
| Atende | 3 |
| Supera | 4 |
| Supera com excelência | 5 |

RM Portal - Avaliação do funcionário João da Silva

1) Inglês = ? (ainda não possui nota definida) Competência avaliada da seguinte forma:

Compreensão = Atende

Fala = Supera

Escrita = Atende Parcialmente

Conforme escala definida na avaliação tem-se:

|  |  |
| --- | --- |
| Item Performance | Nota |
| Compreensão | 3 (Atende) |
| Fala | 4 (Supera) |
| Escrita | 2 (Atende Parcialmente) |

Aplicando a fórmula, tem-se:

|  |
| --- |
| **NC = (pIP1 \* VN1) + (pIP2 \* VN2) + ...(pIPn \* VNn)+** |
| **(pIP1 + pIP2 + ...+pIPn)** |

|  |
| --- |
| (3 \* 3) + (3 \* 4) + (3 \* 2) = 9 + 12 + 6 = 27 = 3 |
| (3 + 3 + 3) 9 |

NC = 3 (Atende) 3 é igual a "Atende" na escala definida na avaliação.

**Atenção**

Ao responder os itens de performance é feita a média preponderante apresentada na fórmula acima e calculada a escala correspondente à competência. Na apuração da NC é considerado o menor intervalo em que essa se encontra.

**Exemplo**

Caso no cálculo citado fosse encontrado o valor 2,5, a NC seria 2,0 ao invés de 3,0, pois 2,5 está entre 2,0 e 3,0.

**GRÁFICOS** **Como Achar A Nota Obtida Expressa No Resultado Dos Gráficos**

A cada competência, ação e fator avaliados dentro de uma avaliação de desempenho por competência, deve-se aplicar as fórmulas abaixo. Após aplicação das fórmulas, deve-se somar os valores obtidos em cada um desses, onde  essa soma será o resultado apontado no gráfico.

**Nota da Avaliação:**

Nota Obtida: Fórmula: NOA = NA\* PA onde:

NOA = Nota Obtida na Avaliação

NA = Nota Avaliada.

PA = Peso definido na Avaliação Nota Máxima Obtida:

Fórmula: NMA = MN \* PA onde:

NMA = Nota Máxima na Avaliação

MN = Maior nota possível da escala

PA = Peso definido na Avaliação

**- Gráfico Comparativo de Notas**

Nota Obtida: Fórmula: NO = NOA onde:

NO = Nota Obtida

NOA = Nota Obtida na Avaliação Nota Máxima Obtida:

Fórmula: NM = NMA o onde:

NM = Nota Máxima

NMA = Nota Máxima na Avaliação

**- Gráfico Comparativo por percentual**

Nota Obtida: Fórmula: NO = NOA \* PIF onde:

NO = Nota Obtida

NOA = Nota obtida na Avaliação

PIF = Peso do Item na Função Nota Máxima Obtida:

Fórmula: NM = NMA \* PIF onde:

NM = Nota Máxima

NMA = Nota Máxima na Avaliação

PIF = Peso do Item na Função

**Atenção**

Esse cálculo deve ser aplicado a cada competência, ação e fator avaliados.
