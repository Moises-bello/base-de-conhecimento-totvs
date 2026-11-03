---
content_hash: e7bf4d57ba04159feda64c9de7d827f2d67476bc1ebc9d263aa6236d4c9edd60
fetched_at: '2026-07-02T19:24:19.913028+00:00'
page_id: '244921265'
product: protheus
source: tdn-tec
title: TFlowLayout
type: documentation
url: https://tdn.totvs.com/display/tec/TFlowLayout
version: 4
---

Classe TFlowLayout

Herda as características de um TPanel e acrescenta a funcionalidade de responsividade aos componentes nele inseridos, mantendo a altura e largura de cada um, porém reposicionando-os dinamicamente de acordo com o espaço disponível no layout.

## Hierarquia

* + TFlowLayout

## Construtores

true

## Métodos

true

## Documentações de apoio

<https://medium.com/devtotvs/responsividade-em-formul%C3%A1rios-advpl-d61917e82912>

## Exemplos

cppEclipsetruefalse 0, cTexto1 := u, cTexto1 ) }, oLayout1, 50, 50,,,,,,.T. )
oLayout1:AddInLayout(oTMultiget1)
cTexto2 := "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra turpis a tempor tempus. Vivamus sit amet eleifend ante, quis suscipit nulla. Morbi sollicitudin eleifend dapibus. Integer congue sapien quis augue dignissim sodales. Sed a sapien justo. Ut sodales nulla sed lacus sollicitudin, a dignissim magna convallis. Maecenas facilisis purus id aliquam tempus. Quisque tempus magna quis nunc ultrices, sit amet luctus ante facilisis."
oTMultiget2 := tMultiget():new( 0, 0, {| u | if( pCount() > 0, cTexto2 := u, cTexto2 ) }, oLayout1, 50, 50,,,,,,.T. )
oLayout1:AddInLayout(oTMultiget2)
cTexto3 := "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pharetra turpis a tempor tempus. Vivamus sit amet eleifend ante, quis suscipit nulla. Morbi sollicitudin eleifend dapibus. Integer congue sapien quis augue dignissim sodales. Sed a sapien justo. Ut sodales nulla sed lacus sollicitudin, a dignissim magna convallis. Maecenas facilisis purus id aliquam tempus. Quisque tempus magna quis nunc ultrices, sit amet luctus ante facilisis."
oTMultiget3 := tMultiget():new( 0, 0, {| u | if( pCount() > 0, cTexto3 := u, cTexto3 ) }, oLayout1, 100, 80,,,,,,.T. )
oLayout1:AddInLayout(oTMultiget3)
oWnd:Activate("MAXIMIZED")
return
]]>

### Resultado do exemplo conforme a janela é redimensionada

## Abrangência

Disponível para . Disponível para versão Desktop somente em builds superiores a 7.00.131227A.
