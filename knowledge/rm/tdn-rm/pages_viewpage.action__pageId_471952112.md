---
content_hash: 185022a537df14d147d7118b16dfac44906a2f07ab91190248341048068a665f
fetched_at: '2026-06-29T00:10:16.587593+00:00'
page_id: '471952112'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1111 DT Erro no paginador quando número de registros é menor
  que 40
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471952112
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Paginador |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1111 |

## **02. SITUAÇÃO/REQUISITO**

Quando em uma tela, o número de registros exibidos era menor que 40, os labels do paginador ficavam inconsistentes.

## **03. SOLUÇÃO**

Foi realizado um ajuste no comportamento dos labels do paginador, para que, quando o número de registros fosse menor que 40, o texto fosse exibido no seguinte formato: 1 - X de X alunos, onde X é o total de alunos.

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
