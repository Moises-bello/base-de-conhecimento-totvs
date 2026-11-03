---
content_hash: 10f33f4d239a0cc670fcbb72821a5a1fc6f45bddf84bf9d67168264e5b335f31
fetched_at: '2026-06-29T00:10:56.762524+00:00'
page_id: '592768521'
product: rm
source: tdn-rm
title: DT- Integração da Natureza Financeira com outros backoffices (EAI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592768521
version: 17
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | Integração da Natureza Financeira com outros backoffices |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-12943](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12943) |

## **02. SITUAÇÃO/REQUISITO**

Na integração do Totvs Folha de Pagamento com o BackOffice Protheus, atualmente o cliente precisa fixar uma Natureza Financeira através do parâmetro de integração chamado 'RH\_NATUREZAFINANCEIRADEFAULT'. O cliente solicita que seja levado para o Protheus de forma "automática" a Natureza Financeira existente no lançamento financeiro (AccountPayableDocument.FinancialNatureInternalId).

## **03. SOLUÇÃO**

Permitir que o processo de integração financeira entre RM x Protheus, busque essa informação por lançamento, ou seja, essa informação seja cadastrada nos parâmetros financeiros do RM Folha de pagamento como ocorre na integração com o RM Fluxus.

## **04. DEMAIS INFORMAÇÕES**

[EAI 2.0](https://tdn.totvs.com/display/INT/EAI+2.0+-+Linha+RM)

[TOTVS Folha de Pagamento RM X BackOffice Protheus](https://tdn.totvs.com/display/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus#Manual_Doc_Integracao_RMLabore_BackOfficeProtheus-_Toc462828095)

## **05. ASSUNTOS RELACIONADOS**

* [Exemplo de configuração da Natureza Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=602627935)

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
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
