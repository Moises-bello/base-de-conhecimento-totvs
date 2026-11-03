---
content_hash: dc917f5a324cecfe17574a5d6193db07932ef0dd43438a43fbe52e8d49c402b8
fetched_at: '2026-06-29T00:10:45.520402+00:00'
page_id: '553338784'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Comprometimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338784
version: 1
---

5%90%10%90%

O *status* de **Comprometimento** foi criado com o objetivo de registrar a data em que uma atividade, que está sob a responsabilidade do *Dev Team*, entra no Plano de Entregas para ser desenvolvida. Dessa forma, os indicadores de *Lead Time* e *Cycle Time* tornam-se mais precisos.

No JIRA  o *status* de **Comprometimento** será registrado da seguinte forma:

 Para equipes que utilizam *Sprints* para planejamento de entregas:

* Para as *issues* que estiverem com o *Status* "**Grooming Concluído**", será passado de forma automática para o *status* "**Comprometido**" e o campo "**Data Comprometimento**" será atualizado.
* Para as *issues* que não estiverem com o "**Grooming Concluído**" não passará para o *status* "**Comprometido**" mas a "**Data de Comprometimento**" será preenchida para que o *Lead Time* possa ser calculado.

 Para equipes que utilizam Fluxo Puxado para planejamento de entregas:

* Poderá ser criada uma coluna no quadro Kanban para registrar o comprometimento, seguindo a mesma regra acima, onde os itens com "**Grooming Concluído**" poderão ser colocados no **status** **Comprometido**, e o campo "**Data de Comprometimento**" será registrado.

O *Status* de Comprometimento será inserido nas *issues* do tipo: Story, Manutenção, Legislação, Participativo, Apoio, Apoio-Cliente, Lição Aprendida, Réplica.

**Importante:** Devem ser atualizados todos os *boards* dos times para considerar esse novo *status* "**Comprometido**" na configuração das Colunas.

5%
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
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
