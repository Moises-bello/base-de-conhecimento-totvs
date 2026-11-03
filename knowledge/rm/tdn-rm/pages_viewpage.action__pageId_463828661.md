---
content_hash: 806428fcb5e2c0aae18376533528f84a0d9ff40254ce3dbe43b3ab33db43dfbe
fetched_at: '2026-06-29T00:10:15.300103+00:00'
page_id: '463828661'
product: rm
source: tdn-rm
title: 4944639 DEDUINTEGRACOES-4343 DT Anexo de parcelas do Contrato do Aluno - filtro
  cortado.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463828661
version: 6
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Anexo de Parcelas do Contrato |
| Ticket: | [4944639](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%224944639%22 "4944639") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-4343](http://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-4343) |

## **02. SITUAÇÃO/REQUISITO**

Ao abrir o contrato do aluno, ir em Anexo - Parcelas, aparentemente a tela está sendo apresentada e a parte superior da tela esta sendo apresentada cortada, fazendo com que o organizador de filtro fique escondido.

## **03. SOLUÇÃO**

Melhoria na visão de parcela para que o agrupador de filtros da visão seja apresentado corretamente sem cortar, possibilitando o usuário manipular os agrupadores facilmente.

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
