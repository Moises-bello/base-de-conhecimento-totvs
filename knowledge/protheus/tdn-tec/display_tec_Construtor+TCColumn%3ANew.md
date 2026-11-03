---
content_hash: 3b5df292b10e004647ed87fbd73ed3c43613f300efa506950ebecc40e07ccb7f
fetched_at: '2026-07-02T19:24:18.847147+00:00'
page_id: '221551624'
product: protheus
source: tdn-tec
title: Construtor TCColumn:New
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TCColumn%3ANew
version: 1
---

Construtor TCColumn:New

# Construtor TCColumn:New

Método construtor da classe.

## Sintaxe

false, < bData >, [ cPicture ], [ uParam4 ], [ uParam5 ], [ cAlinhamento ], [ nLargura ], [ lBitmap ], [ lEdit ], [ uParam10 ], [ bValid ], [ uParam12 ], [ uParam13 ], [ uParam14 ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cTitulo | caractere | Indica o título da coluna. | X |  |
| bData | bloco de código | Indica o bloco de código que contém o campo da tabela que será apresentado no browse. | X |  |
| cPicture | caractere | Indica a picture necessária para edição da coluna. |  |  |
| uParam4 | qualquer | Compatibilidade. |  |  |
| uParam5 | qualquer | Compatibilidade. |  |  |
| cAlinhamento | caractere | Indica o tipo de alinhamento da coluna. Sendo: Left (à esquerda), Center (centralizada) ou Right (à direita). |  |  |
| nLargura | numérico | Indica a largura da coluna. |  |  |
| lBitmap | lógico | Indica se, verdadeiro (.T.), a coluna é uma imagem; caso contrário, falso (.F.) (conteúdo padrão). |  |  |
| lEdit | lógico | Compatibilidade. |  |  |
| uParam10 | qualquer | Compatibilidade. |  |  |
| bValid | bloco de código | Indica o bloco de código de validação que será executado quando o conteúdo do objeto for modificado. Retorna verdadeiro (.T.), se o conteúdo é válido; caso contrário, falso (.F.). |  |  |
| uParam12 | qualquer | Compatibilidade. |  |  |
| uParam13 | qualquer | Compatibilidade. |  |  |
| uParam14 | qualquer | Compatibilidade. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TCColumn |

## Exemplos

cppEclipseExemplo 1truefalseA1\_COD },"@!",,,"LEFT",,.F.,.F.,,,,,))
]]>
