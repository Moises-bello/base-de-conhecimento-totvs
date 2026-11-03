---
content_hash: 16e9ede554ad58a4085a8a28fd258d322d098a12ee3223a849e7798d7721491e
fetched_at: '2026-07-02T19:24:18.589486+00:00'
page_id: '200905937'
product: protheus
source: tdn-tec
title: TComboBox:New
type: documentation
url: https://tdn.totvs.com/display/tec/TComboBox%3ANew
version: 4
---

Construtor TComboBox:New

# Construtor TComboBox:New

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nRow | numérico | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nCol | numérico | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| bSetGet | bloco de código | Indica o bloco de código, no formato {|u| if( Pcount( )>0, := u, ) }, que será executado para atualizar a variável (essa variável deve ser do tipo caracter). Desta forma, se a lista for seqüencial, o controle atualizará com o conteúdo do item selecionado, se for indexada, será atualizada com o valor do índice do item selecionado. |  |  |
| nItens | vetor | Indica uma lista de itens e caracteres que serão apresentados. Essa lista pode ter os seguintes formatos: Seqüencial (Exemplo: {"item1","item2",...,"itemN"}) ou Indexada (Exemplo: {"a=item1","b=item2",...,"n=itemN"}). |  |  |
| nWidth | numérico | Indica a largura em pixels do objeto. |  |  |
| nHeight | numérico | Indica a altura em pixels do objeto. |  |  |
| oWnd | objeto | Indica a janela ou controle visual onde o objeto será criado. |  |  |
| uParam8 | numérico | Compatibilidade. |  |  |
| bChange | bloco de código | Indica o bloco de código que será executado quando o item selecionado é alterado. |  |  |
| bValid | bloco de código | Indica o bloco de código de validação que será executado quando o conteúdo do objeto for modificado. Retorna verdadeiro (.T.), se o conteúdo é válido; caso contrário, falso (.F.). |  |  |
| nClrText | numérico | Indica a cor de texto do objeto. |  |  |
| nClrBack | numérico | Indica a cor de fundo do objeto. |  |  |
| lPixel | lógico | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| oFont | objeto | Indica o objeto do tipo TFont utilizado para definir as características da fonte aplicada na exibição do conteúdo do controle visual. |  |  |
| uParam15 | caractere | Compatibilidade. |  |  |
| uParam16 | lógico | Compatibilidade. |  |  |
| bWhen | bloco de código | Indica o bloco de código que será executado quando a mudança de foco da entrada de dados, na janela em que o controle foi criado, estiver sendo efetuada. Observação: O bloco de código retornará verdadeiro (.T.), se o controle permanecer habilitado; caso contrário, retornará falso (.F.). |  |  |
| uParam18 | lógico | Compatibilidade. |  |  |
| uParam19 | vetor | Compatibilidade. |  |  |
| uParam20 | bloco de código | Compatibilidade. |  |  |
| uParam21 | caractere | Compatibilidade. |  |  |
| cReadVar | caractere | Indica o nome da variável, configurada no parâmetro bSetGet, que será manipulada pelo objeto. Além disso, esse parâmetro será o retorno da função ReadVar(). |  |  |
| cLabelText | caractere | indica o texto que será apresentado na Label. |  |  |
| nLabelPos | numérico | Indica a posição da label, sendo 1=Topo e 2=Esquerda |  |  |
| oLabelFont | objeto | Indica o objeto, do tipo TFont, que será utilizado para definir as características da fonte aplicada na exibição da label. |  |  |
| nLabelColor | numérico | Indica a cor do texto da Label. |  |  |

## Retorno

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| oObj | Objeto | Nova instância da classe TComboBox |

## Observações

Em versões superiores à 120420A foi implementada a opção para definição de uma label(descrição) do componente visual. Preenchendo os parâmetros cLabelText, nLabelPos, oLabelFont e nLabelColor será disponibilizada, ao topo ou à esquerda, a descrição definida para o componente. Esta característica visa diminuir a quantidade de interações entre o SmartClient e o AppServer na construção de telas, otimizando assim este processo.

A criação automática do label através dos parâmetros desse método não funciona se o componente estiver posicionado em algum layout (como o [TGridLayout](https://tdn.totvs.com/display/tec/TGridLayout)), neste caso é necessário criar o label utilizando o componente [TSay](https://tdn.totvs.com/display/tec/TSay).

## Exemplos

cppEclipseExemplo 1truefalse0,cCombo:=u,cCombo)},; aItems,100,20,oDlg,,{||Alert('Mudou item da combo')};,,,,.T.,,,,,,,,,'cCombo')
]]>
