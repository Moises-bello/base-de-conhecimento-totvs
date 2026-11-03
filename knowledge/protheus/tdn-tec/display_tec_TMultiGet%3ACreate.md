---
content_hash: bf4cd8e7f9b6a3752bd7609c69898ca64314ee604ad27646d86661425bd8d013
fetched_at: '2026-07-02T19:24:19.619512+00:00'
page_id: '235337270'
product: protheus
source: tdn-tec
title: TMultiGet:Create
type: documentation
url: https://tdn.totvs.com/display/tec/TMultiGet%3ACreate
version: 2
---

Construtor TMultiGet:Create

# Construtor TMultiGet:Create

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oWnd | object | Indica a janela ou controle visual onde o objeto será criado. |  |  |
| bSetGet | codeblock | Indica o bloco de código, no formato {|u| if( Pcount( )>0, := u, ) }, que será executado para atualizar a variável (essa variável deve ser do tipo caracter). Desta forma, se a lista for sequencial, o controle atualizará com o conteúdo do item selecionado, se for indexada, será atualizada com o valor do índice do item selecionado. |  |  |
| nRow | numeric | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nCol | numeric | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| nWidth | numeric | Indica a largura em pixels do objeto. |  |  |
| nHeight | numeric | Indica a altura em pixels do objeto. |  |  |
| oFont | object | Indica o objeto do tipo TFont utilizado para definir as características da fonte aplicada na exibição do conteúdo do controle visual. |  |  |
| uParam8 | logical | Parâmetro de compatibilidade. Passar Nil. |  |  |
| uParam9 | numeric | Parâmetro de compatibilidade. Passar Nil. |  |  |
| uParam10 | numeric | Parâmetro de compatibilidade. Passar Nil. |  |  |
| uParam11 | character | Parâmetro de compatibilidade. Passar Nil. |  |  |
| lPixel | logical | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| uParam13 | character | Parâmetro de compatibilidade. Passar Nil. |  |  |
| uParam14 | logical | Parâmetro de compatibilidade. Passar Nil. |  |  |
| bWhen | codeblock | Indica o bloco de código que será executado quando a mudança de foco da entrada de dados, na janela em que o controle foi criado, estiver sendo efetuada. Observação: O bloco de código retornará verdadeiro (.T.) se o controle permanecer habilitado; caso contrário, retornará falso (.F.). |  |  |
| uParam16 | logical | Parâmetro de compatibilidade. Passar Nil. |  |  |
| uParam17 | logical | Parâmetro de compatibilidade. Passar Nil. |  |  |
| lReadOnly | logical | Indica se o conteúdo da variável associada ao objeto permanecerá apenas para leitura. |  |  |
| bValid | codeblock | Indica o bloco de código de validação que será executado quando o conteúdo do objeto for modificado. Retorna verdadeiro (.T.), se o conteúdo é válido; caso contrário, falso (.F.). |  |  |
| uParam20 | codeblock | Parâmetro de compatibilidade. Passar Nil. |  |  |
| uParam21 | logical | Parâmetro de compatibilidade. Passar Nil. |  |  |
| lNoBorder | logical | Indica se habilita(.T.)/desabilita(.F.) a apresentação da borda no objeto. |  |  |
| lVScroll | logical | Indica se habilita(.T.)/desabilita(.F.) a barra de rolagem vertical. O valor default é Desabilitado. |  |  |
| cLabelText | character | indica o texto que será apresentado na Label. |  |  |
| nLabelPos | numeric | Indica a posição da label, sendo 1=Topo e 2=Esquerda |  |  |
| oLabelFont | object | Indica o objeto, do tipo TFont, que será utilizado para definir as características da fonte aplicada na exibição da label. |  |  |
| nLabelColor | numeric | Indica a cor do texto da Label. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | object | Nova instância da classe TMultiGet |

## Observações

* Em versões superiores à 120420A foi implementada a opção para definição de uma label(descrição) do componente visual. Preenchendo os parâmetros cLabelText, nLabelPos, oLabelFont e nLabelColor será disponibilizada, ao topo ou à esquerda, a descrição definida para o componente. Esta característica visa diminuir a quantidade de interações entre o SmartClient e o AppServer na construção de telas, otimizando assim este processo.
* A criação automática do label através dos parâmetros desse método não funciona se o componente estiver posicionado em algum layout (como o [TGridLayout](https://tdn.totvs.com/display/tec/TGridLayout)), neste caso é necessário criar o label utilizando o componente [TSay](https://tdn.totvs.com/display/tec/TSay).

**Importante:** Quando utilizada esta opção não será possível alinhar o componente, sendo a Label um objeto independente ela não será alinhada juntamente com o Controle principal, nesta situação é necessário fazer o posicionamento manualmente.

## Exemplos

cppEclipsetruefalse0,cTexto2:=u,cTexto2)},92,01,260,92,,,,,,.T.)
]]>
