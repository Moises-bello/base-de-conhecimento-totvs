---
content_hash: 75fcc87a8f8196ec21a931d0ecca9d5a4077a64aa596b4e177ef49fd1e304cd1
fetched_at: '2026-06-29T00:10:16.471720+00:00'
page_id: '469454849'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1163 DT Ajuste na Consulta de Extração da Fato de Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469454849
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Fast Analytics |
| Função: | Fato de Faturamento |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1163 |

## **02. SITUAÇÃO/REQUISITO**

Para fazer um subselect correto entre duas tabelas, presentes na consulta de extração da fato de faturamento, foi realizado uma juste na sentença.

## **03. SOLUÇÃO**

Foi realizado um ajuste na consulta da fato de faturamento, no subselect entre as tabelas SLAN e SBOLSALAN, onde foi adicionada a ligação entre as chaves SLAN.CODCOLIGADA e SBOLSALAN.CODCOLIGADA.

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
