---
content_hash: 414afc907b624cc75eef85a35e1bc2ffa4a7d4c06dfdc7ebdcb03e73246d897b
fetched_at: '2026-07-02T19:24:19.877156+00:00'
page_id: '244919947'
product: protheus
source: tdn-tec
title: TLinearLayout:addInLayout
type: documentation
url: https://tdn.totvs.com/display/tec/TLinearLayout%3AaddInLayout
version: 6
---

TLinearLayout:addInLayout

Insere um componente no layout.

## Sintaxe

false, [ nAlign ], [ nSpacerFactor ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oControl | objeto | Indica o componente que será inserido no layout. | X |  |
| nAlign | numérico | Especifica o alinhamento horizontal e/ou vertical do componente dentro de seu espaço no Layout. Um valor horizontal pode ser combinado a um vertical, por exemplo: LAYOUT\_ALIGN\_HCENTER + LAYOUT\_ALIGN\_TOP. Consulte a área de observações para conhecer as opções disponíveis. |  |  |
| nSpacerFactor | numérico | Especifica o fator de redimensionamento do componente (respeitando sua política) dentro do layout. Para maior legibilidade, pode ser usado um valor que represente a porcentagem. |  |  |

trueObservações

* Cada componente possui sua própria política de redimensionamento. Por exemplo, um TButton será redimensionado somente em sua largura, equanto um TMultiget, além da largura, também terá sua altura redimensionada.

### Valores disponíveis para o parâmetro nAlign:

| Valor | Descrição |
| --- | --- |
| 1 | Alinhamento horizontal à esquerda |
| 2 | Alinhamento horizontal à direita |
| 4 | Alinhamento horizontal ao centro |
| 32 | Alinhamento vertical ao topo |
| 64 | Alinhamento vertical à base |
| 128 | Alinhamento vertical ao centro |

## Exemplos

cppEclipsetruefalse

### Resultado do exemplo
