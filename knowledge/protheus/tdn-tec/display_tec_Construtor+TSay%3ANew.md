---
content_hash: 8d585ba86899dbebc114a681145dab713d5fe9e86fefdd5597d95ada7497f953
fetched_at: '2026-07-02T19:24:18.678839+00:00'
page_id: '219684754'
product: protheus
source: tdn-tec
title: Construtor TSay:New
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TSay%3ANew
version: 5
---

Construtor TSay:New

# Construtor TSay:New

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nRow | numérico | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nCol | numérico | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| bText | bloco de código | Indica o bloco de código que será executado para retornar e apresentar uma string. |  |  |
| oWnd | objeto | Indica a janela ou controle visual onde o objeto será criado. |  |  |
| cPicture | caractere | Indica a máscara de formatação, do conteúdo, que será apresentada. Verificar . |  |  |
| oFont | objeto | Indica o objeto do tipo TFont utilizado para definir as características da fonte aplicada na exibição do conteúdo do controle visual. |  |  |
| uParam7 | lógico | Compatibilidade. |  |  |
| uParam8 | lógico | Compatibilidade. |  |  |
| uParam9 | lógico | Compatibilidade. |  |  |
| lPixels | lógico | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| nClrText | numérico | Indica a cor do texto do objeto. |  |  |
| nClrBack | numérico | Indica a cor de fundo do objeto. |  |  |
| nWidth | numérico | Indica a largura em pixels do objeto. |  |  |
| nHeight | numérico | Indica a altura em pixels do objeto. |  |  |
| uParam15 | lógico | Compatibilidade. |  |  |
| uParam16 | lógico | Compatibilidade. |  |  |
| uParam17 | lógico | Compatibilidade. |  |  |
| uParam18 | lógico | Compatibilidade. |  |  |
| uParam19 | lógico | Compatibilidade. |  |  |
| lHTML | lógico | Indica se, verdadeiro (.T.), habilita a visualização do texto no formato HTML; caso contrário, falso (.F.). |  |  |
| nTxtAlgHor | numérico | Alinhamento horizontal do texto (Consulte tabela na página do método SetTextAlign). Disponível a partir da versão 17.3.0.0. |  |  |
| nTxtAlgVer | numérico | Alinhamento vertical do texto (Consulte tabela na página do método SetTextAlign). Disponível a partir da versão 17.3.0.0. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TSay |

## Exemplos

cppEclipsetruefalsecppEclipsetruefalse'+;
'Linha 01 Red  
'+;
'Linha 02 Green  
'+;
'Linha 03 Pink  
'+;
'Linha 04 Blue  
'+;
'Linha 05 black  
'+;
'Html label1 '+;
'Html Label2 '+;
'

Html parágrafo1

'+;
'

##### Html header H5

  
'+;
'

'+;
'|  |  |  |
| --- | --- | --- |
|'+;
' Coluna 01a |'+;
' Coluna 02a |'+;
' Coluna 03a |'+;
'
'+;
'|'+;
' Coluna 01b |'+;
' Coluna 02b |'+;
' Coluna 03b |'+;
'
'+;
'|'+;
' Coluna 01c |'+;
' Coluna 02c |'+;
' Coluna 03c |'+;
'
'+;
'

'
// Cria o TSay permitindo texto no formato HMTL
lHtml := .T.
oSay := TSay():New(01,01,{||cTextHtml},oDlg,,oFont,,,,.T.,,,400,300,,,,,,lHtml)
ACTIVATE DIALOG oDlg CENTERED
Return
]]>

### Resultado do Exemplo

## Referências

A construção de um componente da classe TSAY() pelo construtor NEW() também pode ser feita através do comando AdvPL
