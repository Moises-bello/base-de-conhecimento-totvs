---
content_hash: d3a8fa982f5303257f02ee4104747dff2ef65a16498e4a89e97911c38d4546d2
fetched_at: '2026-06-29T00:10:22.541050+00:00'
page_id: '497200731'
product: rm
source: tdn-rm
title: PORTALMOBILE01-7602 DT Loading no questionário do novo portal de inscrições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497200731
version: 1
---

Loading na inscrição utilizando questionário

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Processo Seletivo |
| Função: |  |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | PORTALMOBILE01-7602 |

## **02. SITUAÇÃO/REQUISITO**

Ao carregar pela primeira vez o questionário no novo portal de inscrições, estava ocorrendo uma demora, pelo fato do questionário ser do portal Corpore.Net e a tela ficava em branco, com impressão que não tinha acontecido nada.

## **03. SOLUÇÃO**

Foi implementado um loading no questionário, que enquanto não carregar completamente o questionário será exibido o loading.

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
