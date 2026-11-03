---
content_hash: 0cc9773bbcd33a6993f77d76b31c4c9c655d383ea18a23e1e9857cfb217d70f2
fetched_at: '2026-06-29T00:10:16.513668+00:00'
page_id: '471935608'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1087 DT Sinalização de probabilidade de evasão, através de cores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471935608
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Score de provável evasão |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1087 |

## **02. SITUAÇÃO/REQUISITO**

Necessita-se sinalizar a probabilidade de evasão de um aluno, através de cores.

## **03. SOLUÇÃO**

Com o objetivo de sinalizar a probabilidade de evasão de um aluno através de cores, a coluna Score, das listas de alunos e gerenciamento de ações, e o Widget de Score, no detalhe do aluno,  possuem a cor do texto alterado, conforme o valor do Score diminui.

A lógica inicial para essa sinalização será:

* Valores abaixo de 60, são coloridos de verde.
* Valores entre 60 e 80, são coloridos de amarelo.
* Valores acima de 80, são coloridos de vermelho.

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
