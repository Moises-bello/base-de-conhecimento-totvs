---
content_hash: 6d4eaaa4a0133ef5493536a9383c076c051f62de9da3f44253336c423b970aa3
fetched_at: '2026-06-29T00:10:45.530684+00:00'
page_id: '553338793'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Prazo de Entrega Desenvolvimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338793
version: 1
---

5%90%10%90%Processo: Quando eu devo preencher a Data Acordo de Entrega?

**A data acordo de entrega deve ser preenchida nos projetos de Desenvolvimento e Manutenção, conforme regras abaixo:**

**Issuetypes obrigatórias:**

* Manutenção
* Legislação;
* Rejeição - Manutenção;
* Ponto de Entrada;
* Participativo.

**Issuetype opcional:**

* Story.

**Em que momento a Data Acordo de Entrega deve ser preenchida na ferramenta?**

* Nas issues do Projeto de Desenvolvimento, a data acordo de entrega deve ser preenchida ao iniciar o Desenvolvimento (Tradicional ou Simplificado);
* Nas issues do Projeto de Manutenção, a data acordo de entrega deve ser preenchida ao finalizar a Especificação (Planejar/Especificar).

Ferramenta: Como informar a Data Acordo de Entrega?

No JIRA há uma opção de workflow **Alterar Data Entrega** que poderá ser acessada em qualquer status da *issue*.

Habilitará a tela para selecionar a data em que será entregue a *issue;*

Não é necessário inserir comentário nessa tela, visto que essa informação não será enviada ao cliente, qualquer comentário inserido ficará registrado internamente na *issue*.

A mensagem a seguir será registrada no *ticket* e enviado uma notificação ao cliente;

**Importante**

* + Se a issue tiver subtarefas do tipo Associadas, essa data será replicada para todas as associações, e a notificação será enviada a todos os clientes.
  + O campo **Data Acordo de Entrega** foi retirado da tela padrão de edição e colocado apenas para ser alterado no workflow do Jira, para que possa ser enviado a notificação ao cliente.

Para mais detalhes, assista ao **[vídeo How To](http://fluig.totvs.com:80/portal/p/10097/videos/qualidadedesoft3300/5235839/5989739)**.

Ferramenta: Como priorizar o Ticket? 

O Cliente pode solicitar a priorização via telefone ou iteração do ticket. Esta solicitação preencherá o campo **prioriza = SIM** na ferramenta Zendesk.

Quando ocorrer via telefone, o Analista do Atendimento é responsável pelo preenchimento do campo, além também de poder informar o campo "Motivo Priorizado". Quando a solicitação de priorização vier por meio de interação do cliente, automaticamente o campo será preenchido para Sim, através de um gatilho.

Para facilitar a identificação dos itens que foram priorizados pelo cliente, no JIRA está habilitado para consulta o campo "Priorizado" que é preenchido pelo Atendimento no Zendesk ao existir algum tipo de priorização.

O campo **Data da Priorização** é alimentado através do processo de priorização no *ticket* do cliente, ou seja, assim que o atendimento prioriza um *ticket*, os campos "**Priorizado = Sim**" e "**Motivo da Priorização**" são atualizados na *issue* do Jira e o campo "**Data da Priorização**" é preenchido automaticamente com a informação da data corrente (data do evento da priorização).

Se o ticket já estiver priorizado na abertura da *issue*, o campo **Data da Priorização** é preenchido com a data da criação da *issue*, ou seja, com a data corrente.

Ferramenta: Onde fica registrada as alterações realizadas no campo Data Acordo de Entrega?

Para consultar todas as alterações do campo "Data Acordo Entrega" acesse a aba Statistics da *issue*, onde poderá ser visualizado todo o histórico desse campo:

Ferramenta: Como acompanhar a violação do prazo informado?

O*Product Owner* pode acompanhar a violação deste prazo através de filtros como no exemplo abaixo:

* project = "DSEGQZA - DESENVOLVIMENTO" AND "Data Acordo Entrega" <= endOfDay() AND status not in (Recusada, Concluído, "Teste Integrado Concluído", Cancelado)

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
