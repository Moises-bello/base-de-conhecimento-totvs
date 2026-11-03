---
content_hash: 4e7ff8a34e7f266ee68fedbf8aaac2005e5ba7f0d53f9f9b62051c992ba62a2f
fetched_at: '2026-06-29T00:10:25.934512+00:00'
page_id: '506990177'
product: rm
source: tdn-rm
title: DT Realizar o calculo dos tributos Pis, Cofins e Csll considerando o valor
  original da baixa para calculo na baixa parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Realizar+o+calculo+dos+tributos+Pis%2C+Cofins+e+Csll+considerando+o+valor+original+da+baixa+para+calculo+na+baixa+parcial
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BACKOFFICE |
| Módulo: | Totvs Gestão Financeira |
| Função: | cálculo de tributos na Baixa Parcial |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FINANCEIRO01-12713](https://jiraproducao.totvs.com.br/browse/FINANCEIRO01-12713) |

## **02. SITUAÇÃO/REQUISITO**

Implementação do parâmetro "Informar base de cálculo dos tributos de lançamentos a pagar" e campo "Base Cálculo dos Tributos" na tela de baixa.

## **03. SOLUÇÃO**

Possibilitar ao usuário informar no momento da baixa o valor base que será usado  para cálculo de tributos PIS, COFINS e CSLL na baixa parcial.

Implementado parâmetro no menu Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar **|**Baixa | Baixas a Pagar | Informar base de cálculo dos tributos de lançamentos a pagar.

Quando marcado o parâmetro o campo "Base Cálculo dos Tributos", será apresentado na tela de baixa:

Ao definir valor base o sistema irá usar esse valor como base para cálculo dos tributos PIS, COFINS e CSLL, na baixa parcial

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
