---
content_hash: 0c4b74a389e7265b400a2abd99316ff0a8792bf2f01dada86b503275ef230ab5
fetched_at: '2026-07-02T19:24:19.907637+00:00'
page_id: '244921080'
product: protheus
source: tdn-tec
title: TGridLayout:addSpacer
type: documentation
url: https://tdn.totvs.com/display/tec/TGridLayout%3AaddSpacer
version: 2
---

TGridLayout:addSpacer

Insere um espaçador no layout.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nRow | numérico | Representa a linha do grid onde será inserido um espaçador. |  |  |
| nColumn | numérico | Representa a coluna do grid onde será inserido um espaçador. |  |  |
| nSpaceFactor | numérico | Especifica um fator que representa sua proporcionalidade em relação a outros espaçadores inseridos no mesmo layout. Um fator maior que zero é suficiente, caso seja o único espaçador no Layout. |  |  |

## Observações

* É possível especificar os valores de linha e/ou coluna que apontem para uma célula que contenha um componente, assim o componente será redimensionado para ocupar o espaço disponível (sempre respeitando sua política de redimensionamento). É possível, no entando, apontar para uma linha e/ou coluna que não contenha componente(s), espaçando somente a linha/coluna, gerando assim um efeito de alinhamento.
* Cada componente possui sua própria política de redimensionamento. Por exemplo, um TButton será redimensionado somente em sua largura, equanto um TMultiget, além da largura, também terá sua altura redimensionada.

## Exemplos

cppEclipsetruefalse

### Resultado do exemplo
