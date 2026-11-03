---
content_hash: 0a0e8e63e20a64466830bb2de7a0b126eeb18a106da1ac86ab407a14d1ed8cd1
fetched_at: '2026-06-29T00:08:30.276311+00:00'
page_id: '272417877'
product: rm
source: tdn-rm
title: 597531 MEDU-2985 DT Contabilização por competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272417877
version: 108
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Contabilização por competência |
| **Situação/Requisito:** | O problema de geração de aumentos ou cancelamentos indevidos teve a sua origem no arredondamento da última parcela calculada por número de créditos feito pela simulação de valores financeiros das parcelas (mesma rotina utilizada pela geração de lançamentos).    Quando o contrato possuía lançamentos baixados e essas parcelas eram calculadas por número de créditos, essa rotina de arredondamento não conseguia identificar que precisava arredondar os valores da última parcela desconsiderando esse arredondamento.    Exemplo:    - Valor total calculado para o contrato:  R$ 12.469,00 (Número de créditos a serem cobrados x Valor dos créditos a serem considerados)  - Número total de parcelas do contrato: 6 (seis)  - Valor calculado para cada parcela: R$ 12.469,00 / 6 =  2078,17 (2078,166666666667 após o arredondamento para duas casas decimais)  - Valores calculados para as parcelas:                  1ª parcela: 2078,17                  2ª parcela: 2078,17                  3ª parcela: 2078,17                  4ª parcela: 2078,17                  5ª parcela: 2078,17                  6ª parcela: 2078,17    Ao somarmos os valores calculados acima, teremos uma diferença de dois centavos gerando um resultado de R$ 12.469,**02** |
| **Solução/Implementação:** | Foi feito o ajuste na rotina de arredondamento de valores para identificar corretamente a última parcela do contrato e efetuar o devido ajuste em seu valor.  Ao identificar corretamente a última parcela no exemplo acima, o valor da última parcela passará a ser 2078,**15** e a contabilização passará a não gerar contabilizações de aumento pois não serão identificadas divergências nos valores do contrato. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
