---
content_hash: 457c1cc3334bda4eefa5553ce41dc4332fbd031a382d8e3fb2db81cb80dc23f9
fetched_at: '2026-07-02T19:24:20.538989+00:00'
page_id: '257130839'
product: protheus
source: tdn-tec
title: ArrayAddItem
type: documentation
url: https://tdn.totvs.com/display/tec/ArrayAddItem
version: 1
---

ArrayAddItem

Adiciona novos elementos a um array que pode ser de tamanho pré-fixado ou não.

## Sintaxe

false, < nQtdade >, [ nInitPos ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| aName | vetor | Indica o Array que será manipulado. | X |  |
| nQtdade | numérico | Quantidade de elementos que serão incluídos. | X |  |
| nInitPos | numérico | Indica a posição inicial do Array onde os elementos serão inseridos. |  |  |

## Observações

* Na liguagem 4GL, o tipo ARRAY pode ser criado com um tamanho pré-fixado ou não, sempre respeitando o tamanho mínimo de 1 elemento. Assim, é possível manipular o tamanho de um ARRAY incluindo e removendo elementos.
* A partir do build 7.00.131227P versão 1.2.0, é possivel indicar a posição inicial do array onde serão inseridos novos elementos.

## Exemplos

falsefalsefalsefalse

## Abrangência

Disponível a partir do build 7.00.101202A

## Veja também
