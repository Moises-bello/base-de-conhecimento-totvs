---
content_hash: dfef949f5b8b265d24122f0bac7b7eb993e813fbbf069b4c01f8fcaa42915471
fetched_at: '2026-06-29T00:10:25.324072+00:00'
page_id: '502464017'
product: rm
source: tdn-rm
title: EDUCACIONAL01-9796 DT Alocação de salas por meio do cadastro de turma/disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502464017
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Acadêmico |
| Função: | Alocação de salas |
| Ticket: | #6124305 |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-9796 |

## **02. SITUAÇÃO/REQUISITO**

Quando se realizava a alocação de uma sala, através do cadastro da turma/disciplina, o sistema não validava se a sala comportava a quantidade máxima de alunos que a turma disciplina poderia ter.  
Além disso, foi percebido que o parâmetro "Permitir alocar salas com turmas/disciplinas acima da capacidade", não funcionava corretamente.

## **03. SOLUÇÃO**

Foi realizado um ajuste na tela de turma/disciplina, para que houvesse uma validação da capacidade máxima da sala, no momento de se salvar o registro da turma/disciplina. Também foi realizado um ajuste na tela de alocação manual de salas, para que o parâmetro "Permitir alocar salas com turmas/disciplinas acima da capacidade" funcionasse corretamente.

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
