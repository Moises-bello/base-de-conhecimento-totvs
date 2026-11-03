---
content_hash: 0fd42fb4ae08fe34f2482f104a38e4257e4e56551405c68e859a84a59403208a
fetched_at: '2026-06-29T00:10:36.398288+00:00'
page_id: '532041580'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6440 DT Gravação do desconto por antecipação utilizado na baixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532041580
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Baixa de lançamentos |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-6440](https://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-6440) |

## **02. SITUAÇÃO/REQUISITO**

Com a necessidade de registrar o desconto por antecipação utilizado na baixa de lançamentos, foi se criado campos para o lançamento referencie diretamente o item de desconto utilizado para efeito de histórico.

## **03. SOLUÇÃO**

Foram criados 02 campos na tabela **SLAN** ( **IDDESCONTO** e **IDAGRUPADESCPONTUAL** ) para que fosse possível a inserção de uma chave estrangeira que ligasse o registro do lançamento que foi baixado com o item de desconto por antecipação utilizado da tabela **SLANDESCPONTUAL**.

Dessa forma é possível manter um registro histórico de qual desconto foi utilizado para o cálculo do valor de baixa do lançamento.

Caso tenhamos um cancelamento dessa baixa, esses campos terão seus valores removidos, uma vez que o dia da baixa poderá ser alterado com a realização de uma nova baixa.

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
