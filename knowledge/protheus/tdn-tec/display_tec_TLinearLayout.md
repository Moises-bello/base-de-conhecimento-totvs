---
content_hash: 9a3138388f211b80272cb6ba0dd28186562804013b634a3ea65fa88cca0872fa
fetched_at: '2026-07-02T19:24:19.852247+00:00'
page_id: '244919329'
product: protheus
source: tdn-tec
title: TLinearLayout
type: documentation
url: https://tdn.totvs.com/display/tec/TLinearLayout
version: 6
---

Classe TLinearLayout

Herda as características de um TPanel e acrescenta a funcionalidade de responsividade aos componentes nele inseridos, isto é, tais componentes se adaptam automaticamente ao tamanho do layout disponível, reajustando-se dinamicamente a largura e/ou altura de acordo com o espaço disponível. Os componentes são inseridos linearmente na horizontal ou na vertical dependendo da configuração.

## Hierarquia

* + TLinearLayout

## Construtores

true

## Propriedades

true

## Métodos

true

## Documentações de apoio

<https://medium.com/devtotvs/responsividade-em-formul%C3%A1rios-advpl-d61917e82912>

## Observações

* Com a classe TLinearLayout é possível usar o conceito de layouts aninhados, isto é, quando um ou mais layouts são inseridos dentro de um outro layout. Para obter tal efeito, um objeto TAlignLayout nunca deve ser adicionado diretamente em outro TAlignLayout (tampouco um objeto TAlignLayout ter como parent outro TAlignLayout), o correto é criar um TPanel intermediário entre os dois layouts. O código fonte do segundo exemplo disponibilizado nesta página reproduz uma tela onde um layout central foi segmentado em outros três layouts. Consulte tal exemplo para maiores detalhes.

## Exemplos

cppEclipsetruefalse

### Resultado do Primeiro Exemplo

cppEclipsetruefalseTítulo"},oHeaderLyt,,oTFont,,,,.T.,CLR\_WHITE,,0,0,,,,,,.T.)
oHeaderLyt:addInLayout(oSayHeader, LAYOUT\_ALIGN\_HCENTER + LAYOUT\_ALIGN\_VCENTER)
oHeaderLyt:AddSpacer(2, 1)
// --------------------------------------------------------------------------------------------------------
// Cria o frame central
oBodyLyt := tLinearLayout():New(oWnd, LAYOUT\_LINEAR\_L2R, CONTROL\_ALIGN\_ALLCLIENT, 0, 0)
oBodyLyt:SetColor(,CLR\_BLACK)
// Segmenta o frame central em três partes, usando TPanel para esse fim.
oMenuPnl := tPanel():New(0,0,,oBodyLyt,,.T.,,,CLR\_LIGHTGRAY,0,0)
oCenterPnl := tPanel():New(0,0,,oBodyLyt,,.T.,,,CLR\_CYAN,0,0)
oQuestPnl := tPanel():New(0,0,,oBodyLyt,,.T.,,,CLR\_BROWN,0,0)
oBodyLyt:addInLayout(oMenuPnl,,25)
oBodyLyt:addInLayout(oCenterPnl,,50)
oBodyLyt:addInLayout(oQuestPnl,,25)
// No primeiro TPanel, cria o layout que comportará o menu lateral
oMenuLyt := tLinearLayout():New(oMenuPnl, LAYOUT\_LINEAR\_T2B, CONTROL\_ALIGN\_ALLCLIENT, 0, 0)
oMenuLyt:SetCSS("QFrame{ margin: 15px; } TButton{ background-color: #33b5e5; color: #ffffff; text-align: left; margin-bottom: 7px; font-size: 18px; }" )
oTButton1 := TButton():New( 0, 0, "Botão Um", oMenuLyt,{||conout("Botão Um")}, 40,20,,,.F.,.T.,.F.,,.F.,,,.F. )
oTButton2 := TButton():New( 0, 0, "Botão Dois", oMenuLyt,{||conout("Botão Dois")}, 40,20,,,.F.,.T.,.F.,,.F.,,,.F. )
oTButton3 := TButton():New( 0, 0, "Botão Três", oMenuLyt,{||conout("Botão Três")}, 40,20,,,.F.,.T.,.F.,,.F.,,,.F. )
oTButton4 := TButton():New( 0, 0, "Botão Quatro", oMenuLyt,{||conout("Botão Quatro")}, 40,20,,,.F.,.T.,.F.,,.F.,,,.F. )
oMenuLyt:addInLayout(oTButton1)
oMenuLyt:addInLayout(oTButton2)
oMenuLyt:addInLayout(oTButton3)
oMenuLyt:addInLayout(oTButton4)
oMenuLyt:AddSpacer(5)
// No segundo TPanel, cria o layout que comportará o texto central
oCenterLyt := tLinearLayout():New(oCenterPnl, LAYOUT\_LINEAR\_T2B, CONTROL\_ALIGN\_ALLCLIENT, 0, 0)
oCenterLyt:SetCSS("QFrame{ margin: 15px; }")
cCity := "

# Conteúdo

  
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra turpis a tempor tempus. Vivamus sit amet eleifend ante, quis suscipit nulla. Morbi sollicitudin eleifend dapibus. Integer congue sapien quis augue dignissim sodales. Sed a sapien justo. Ut sodales nulla sed lacus sollicitudin, a dignissim magna convallis. Maecenas facilisis purus id aliquam tempus. Quisque tempus magna quis nunc ultrices, sit amet luctus ante facilisis."
oSayCenter := TSay():New(0,0,{|| cCity},oCenterLyt,,oTFont,,,,.T.,,,0,0,,,,,,.T.)
oCenterLyt:addInLayout(oSayCenter)
// No terceiro TPanel, cria o layout que comportará o texto à direita
oQuestLyt := tLinearLayout():New(oQuestPnl, LAYOUT\_LINEAR\_T2B, CONTROL\_ALIGN\_ALLCLIENT, 0, 0)
oQuestLyt:SetColor(,CLR\_WHITE)
oQuestLyt:SetCss("QFrame{ margin: 5px; }")
cPerguntas := "

# Item 1

  
Lorem ipsum dolor sit amet, consectetur adipiscing elit.  

# Item 2

  
Vivamus pharetra turpis a tempor tempus.  

# Item 3

  
Quisque tempus magna quis nunc ultrices, sit amet luctus ante facilisis."
oSayQuest := TSay():New(0,0,{|| cPerguntas},oQuestLyt,,oTFont,,,,.T.,CLR\_WHITE,CLR\_HBLUE,0,0,,,,,,.T.)
oSayQuest:SetCss("TSay{ qproperty-alignment: AlignCenter; background-color: #33b5e5; color: #ffffff; }")
oQuestLyt:addInLayout(oSayQuest)
// --------------------------------------------------------------------------------------------------------
// Cria o frame do rodapé
oBottomLyt := tLinearLayout():New(oWnd, LAYOUT\_LINEAR\_L2R, CONTROL\_ALIGN\_BOTTOM, 0, 40)
oBottomLyt:SetCSS("QFrame{ background-color: #0099cc; color: #ffffff; margin: 5px; }")
oSayBottom:= TSay():New(0,0,{||"Redimensione a janela para ver como o conteúdo responde ao redimensionamento."},oBottomLyt,,oTFont,,,,.T.,,,0,0,,,,,,.T.)
oSayBottom:SetCss("TSay{ qproperty-alignment: AlignCenter; }")
oBottomLyt:addInLayout(oSayBottom)
oWnd:Activate("MAXIMIZED")
return
]]>

### Resultado do Segundo Exemplo

## Abrangência

Disponível para . Disponível para versão Desktop somente em builds superiores a 7.00.131227A.
