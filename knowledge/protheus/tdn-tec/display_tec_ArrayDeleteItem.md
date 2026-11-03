---
content_hash: c5657668eb7d4eaca07ec74721a660622508c607eba1c58caa1ab84eb9f34fcd
fetched_at: '2026-07-02T19:24:20.548207+00:00'
page_id: '257130930'
product: protheus
source: tdn-tec
title: ArrayDeleteItem
type: documentation
url: https://tdn.totvs.com/display/tec/ArrayDeleteItem
version: 1
---

ArrayDeleteItem

Remove elementos de um Array.

## Sintaxe

false, [ nQtdade ], [ nInitPos ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| aName | vetor | Indica o Array que será manipulado. | X |  |
| nQtdade | numérico | Quantidade de elementos que serão removidos. |  |  |
| nInitPos | numérico | Indica a posição inicial do Array onde os elementos serão removidos. |  |  |

## Observações

* Na liguagem 4GL, o tipo ARRAY pode ser criado com um tamanho pré-fixado ou não, sempre respeitando o tamanho mínimo de 1 elemento. Assim, é possível manipular o tamanho de um ARRAY incluindo e removendo elementos.
* A partir do build 7.00.131227P versão 1.2.0, é possivel indicar a partir de que posição do array serão removidos os elementos.
* Caso não seja informado o segundo parâmetro, serão deletados todos elementos do Array.

## Exemplos

falsefalse

## Abrangência

Disponível a partir do build 7.00.101202A

## Veja também
