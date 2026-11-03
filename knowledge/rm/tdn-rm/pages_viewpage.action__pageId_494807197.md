---
content_hash: b4ca83f8db16a7558830506aee139ce05c3b77e5115bd4e3af5ed2432cde078a
fetched_at: '2026-06-29T00:10:21.901289+00:00'
page_id: '494807197'
product: rm
source: tdn-rm
title: '5918303 FISCAL01-9300 DT - NFC-e - RJ - Rejeição 391: Não informados os dados
  do cartão de crédito / débito nas Formas de Pagamento da Nota Fiscal'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494807197
version: 5
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Fiscal |
| Ticket: | 5918303 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9300 |

**02. SITUAÇÃO/REQUISITO**

Para NFC-e quando forem realizados paramentos com a forma de pagamento (Campo: pag / tPag - ID: YA02) igual à "03 - Cartão de Crédito" ou "04 - Cartão de Débito" deverá ser informado o tipo de integração do pagamento com cartão como 2= Pagamento não integrado com o sistema de automação da empresa.

**03. SOLUÇÃO**

Para a NFC-e será gerado o grupo card com os detalhes dos pagamentos realizados com cartão de crédito ou débito.

O grupo card é gerado dentro do grupo de detalhe do pagamento (detpag) e será gerado somente com a TAG tpIntegra com o valor fixo "2 - Pagamento não integrado com o sistema de automação da empresa".

xmlExemplo
0
03
300.00

2
]]>
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
