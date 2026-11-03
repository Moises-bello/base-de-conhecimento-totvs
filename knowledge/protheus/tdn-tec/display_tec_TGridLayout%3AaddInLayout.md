---
content_hash: 6e8d00ea4f915d8fa95de2b620b3ed46495ce0af223a8c03db47d459a7f0f9d0
fetched_at: '2026-07-02T19:24:19.903053+00:00'
page_id: '244921033'
product: protheus
source: tdn-tec
title: TGridLayout:addInLayout
type: documentation
url: https://tdn.totvs.com/display/tec/TGridLayout%3AaddInLayout
version: 2
---

TGridLayout:addInLayout

Insere um componente no layout.

## Sintaxe

false, [ nRow ], [ nColumn ], [ nRowSpan ], [ nColumnSpan ], [ nAlign ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oControl | objeto | Indica o componente que será inserido no layout. | X |  |
| nRow | numérico | Especifica em qual linha do grid o componente será inserido. |  |  |
| nColumn | numérico | Especifica em qual coluna do grid o componente será inserido. |  |  |
| nRowSpan | numérico | Especifica quantas linhas serão mescladas. |  |  |
| nColumnSpan | numérico | Especifica quantas colunas serão mescladas. |  |  |
| nAlign | numérico | Especifica o alinhamento horizontal e/ou vertical do componente dentro de seu espaço no Layout. Um valor horizontal pode ser combinado a um vertical, por exemplo: LAYOUT\_ALIGN\_HCENTER + LAYOUT\_ALIGN\_TOP. Consulte a área de observações para conhecer as opções disponíveis. |  |  |

## Observações

* Cada componente possui sua própria política de redimensionamento. Por exemplo, um TButton será redimensionado somente em sua largura, equanto um TMultiget, além da largura, também terá sua altura redimensionada.

### Valores disponíveis para o parâmetro nAlign:

| Valor | Descrição |
| --- | --- |
| 1 | Alinhamento horizontal à esquerda |
| 2 | Alinhamento horizontal à direita |
| 4 | Alinhamento horizontal ao centro |
| 32 | Alinhamento vertical ao topo |
| 64 | Alinhamento vertical ao centro |
| 128 | Alinhamento vertical à base |

## Exemplos

cppEclipsetruefalse

### Resultado do exemplo
