---
content_hash: f12ae6a5b33bde890f62b741ccc297680e7cd3ed63ac1d922d2632daad6617d2
fetched_at: '2026-07-02T19:24:22.405768+00:00'
page_id: '269549682'
product: protheus
source: tdn-tec
title: Construtor TMSPrinterSpool:New
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TMSPrinterSpool%3ANew
version: 1
---

Construtor TMSPrinterSpool:New

# Construtor TMSPrinterSpool:New

Método construtor da classe.

## Sintaxe

false, < cTextPage >, [ lPortrait ], < cRelSize > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nRow | numérico | Linha em que o componente visual deverá ser desenhado. |  |  |
| nCol | numérico | Coluna em que o componente visual deverá ser desenhado. |  |  |
| nWidth | numérico | Largura do componente visual. |  |  |
| nHeight | numérico | Altura do componente visual. |  |  |
| oWnd | objeto | Componente visual pai. | X |  |
| cTextPage | caractere | Texto a ser apresentado no preview. | X |  |
| lPortrait | lógico | Define se a orientação do documento será retrato (.T.) ou paisagem (.F.). |  |  |
| cRelSize | caractere | Tamanho do documento ("P" para pequeno, "M" para médio, "G" para grande). | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TMSPrinterSpool |

## Exemplos

cppEclipsetruefalse
