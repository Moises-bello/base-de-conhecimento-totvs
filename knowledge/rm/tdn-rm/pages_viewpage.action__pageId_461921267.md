---
content_hash: 1c4f41c426d70617b4f2b7e030e86cc28288b73a18de49d8c6e7694c5bedde93
fetched_at: '2026-06-29T00:10:14.671160+00:00'
page_id: '461921267'
product: rm
source: tdn-rm
title: 3136218 EDUCACIONAL01-5432 DT USO DE FÓRMULA VISUAL NA MONTAGEM DE QUADRO DE
  HORÁRIO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461921267
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Transferência interna |
| Ticket: | 3136218 |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-5432 |

## **02. SITUAÇÃO/REQUISITO**

Não está sendo possível a utilização de fórmulas visuais no processo de montagem de quadro de horário.

## **03. SOLUÇÃO**

Foi realizada uma reformulação no processo de salvamento das informações da montagem de quadro de horários para que seja possível a utilização de fórmulas visuais nos gatilhos dos devidos DataServers.

A tela de montagem de quado de horário de turmas disciplinas utiliza 03 DataServers para o salvamento das informações dos horários, dos professores e os horários dos professores das turmas disciplinas:

* + EduProfessorTurmaData (Professor da turma/disciplina)
  + EduHorarioTurmaData (Horário da turma/disciplina)
  + EduHorarioProfessorData (Horário do professor da turma/disciplina)

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
