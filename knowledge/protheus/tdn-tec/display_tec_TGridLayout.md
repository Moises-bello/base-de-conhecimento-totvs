---
content_hash: 1ccd4cfcc7d71e5ec40658356c7a3d9bd8ffd6c959fc8fb65cad7b7bedcf7185
fetched_at: '2026-07-02T19:24:19.886051+00:00'
page_id: '244920990'
product: protheus
source: tdn-tec
title: TGridLayout
type: documentation
url: https://tdn.totvs.com/display/tec/TGridLayout
version: 4
---

Classe TGridLayout

Herda as características de um TPanel e acrescenta a funcionalidade de responsividade aos componentes nele inseridos, isto é, tais componentes se adaptam automaticamente ao tamanho do layout disponível, reajustando-se dinamicamente a largura e/ou altura de acordo com o espaço disponível. Os componentes são inseridos em um layout em formato de grid, dispostos em linhas e colunas.

## Hierarquia

* + TGridLayout

## Construtores

true

## Métodos

true

## Documentações de apoio

<https://medium.com/devtotvs/responsividade-em-formul%C3%A1rios-advpl-d61917e82912>

## Observações

* Com a classe TGridLayout é possível usar o conceito de layouts aninhados, isto é, quando um ou mais layouts são inseridos dentro de um outro layout. Para obter tal efeito, um objeto TGridLayout nunca deve ser adicionado diretamente em outro TGridLayout (tampouco um objeto TGridLayout ter como parent outro TGridLayout), o correto é criar um TPanel intermediário entre os dois layouts. O código fonte do segundo exemplo disponibilizado nesta página reproduz uma tela onde todo o layout foi comportado nas linhas e colunas de um TGridLayout e em cada uma de suas células foi aplicado um novo layout do componente  que se tornou responsável pelos componentes visuais. Consulte o segundo exemplo para maiores detalhes.

## Exemplos

cppEclipsetruefalse

### Resultado do Exemplo

cppEclipsetruefalseTítulo"},oHeaderLyt,,oTFont,,,,.T.,CLR\_WHITE,,0,0,,,,,,.T.)
oHeaderLyt:addInLayout(oSayHeader, LAYOUT\_ALIGN\_VCENTER)
oHeaderLyt:AddSpacer(2, 1)
// --------------------------------------------------------------------------------------------------------
// Cria o frame central
// Segmenta o frame central em três partes, usando TPanel para esse fim. Cada TPanel será o parent de um
// TAlignLayout diferente que por sua vez será o container dos compontentes visuais.
oMenuPnl := tPanel():New(0,0,,oMainLayout,,.T.,,,CLR\_LIGHTGRAY,0,0)
oCenterPnl := tPanel():New(0,0,,oMainLayout,,.T.,,,CLR\_CYAN,0,0)
oQuestPnl := tPanel():New(0,0,,oMainLayout,,.T.,,,CLR\_BROWN,0,0)
oMainLayout:addInLayout(oMenuPnl,2,1)
oMainLayout:addInLayout(oCenterPnl,2,2)
oMainLayout:addInLayout(oQuestPnl,2,3)
oMainLayout:AddSpacer(2,,70)
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
// Cria um TPanel intermediário para comportar um TAlignLayout com o conteúdo.
oBottomPnl := tPanel():New(0,0,,oMainLayout,,.T.,,,CLR\_LIGHTGRAY,0,40)
oBottomPnl:SetCSS("QFrame{ background-color: #0099cc; color: #ffffff; margin: 5px; }")
oMainLayout:addInLayout(oBottomPnl,3,1,,3)
oMainLayout:AddSpacer(3,,15)
oBottomLyt := tLinearLayout():New(oBottomPnl, LAYOUT\_LINEAR\_L2R, CONTROL\_ALIGN\_ALLCLIENT, 0, 0)
oSayBottom:= TSay():New(0,0,{||"Redimensione a janela para ver como o conteúdo responde ao redimensionamento."},oBottomLyt,,oTFont,,,,.T.,,,0,0,,,,,,.T.)
oSayBottom:SetCss("TSay{ qproperty-alignment: AlignCenter; }")
oBottomLyt:AddInLayout(oSayBottom)
oWnd:Activate("MAXIMIZED")
return
]]>

## Abrangência

Disponível para . Disponível para versão Desktop somente em builds superiores a 7.00.131227A.
