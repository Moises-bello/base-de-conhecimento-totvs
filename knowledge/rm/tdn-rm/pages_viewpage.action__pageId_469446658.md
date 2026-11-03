---
content_hash: 5314851ff9fe748b4b5fb85a4611ca8d8169f4d220f34a4b8012046f5229c5bb
fetched_at: '2026-06-29T00:10:16.433575+00:00'
page_id: '469446658'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1150 DT O app está deixando excluir uma situação de aluno que
  foi relacionada a uma ação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469446658
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Situação de Alunos |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1150 |

## **02. SITUAÇÃO/REQUISITO**

Estava sendo possível excluir uma situação de aluno, mesmo ela estando vinculada à uma ação.

## **03. SOLUÇÃO**

Foi realizado uma ajuste na tela de situação de aluno, para que não seja mais possível excluir um registro dessa tela quando houver uma ação relacionada à eles.

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
