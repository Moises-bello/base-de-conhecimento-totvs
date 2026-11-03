---
content_hash: b93a6559a0bcc25e4d4e948960936b186a7e61ad1728dc170c28349c7202289e
fetched_at: '2026-06-29T00:10:38.653073+00:00'
page_id: '544709204'
product: rm
source: tdn-rm
title: DT Exibir final de semana no quadro de horário da Matrícula ES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544709204
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | Portal do Aluno |
| Função: | Matrícula Ensino Superior |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | PORTALMOBILE01-9638 |

## **02. SITUAÇÃO/REQUISITO**

Ao acessar a matrícula do ensino superior, quadro de horário, não era possível visualizar os horários de sábado e domingo.

## **03. SOLUÇÃO**

Foi incluído a opção de "Visualizar final de semana" no canto direito superior do quadro de horário, que quando marcado passa a exibir no quadro de horário o sábado e domingo mesmo não havendo disciplinas selecionadas para a matrícula com horários nestes dias. Caso contrário, somente será exibido o Sábado e/ou Domingo caso o aluno selecione alguma disciplina que possua horário nesses dias.

Obs: A funcionalidade "Ocultar final de semana" não retira do quadro de horário nenhum dia da semana que já possua horário de uma disciplina selecionada para a matrícula. Caso o aluno possua alguma aula no Sábado, ou no Domingo, esta funcionalidade irá ocultar apenas o dia do final de semana que não possui horário. E, em caso do aluno selecionar disciplinas contendo aula tanto no Sábado quanto no Domingo, não será possível visualizar a opção para "Ocultar final de semana".

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
