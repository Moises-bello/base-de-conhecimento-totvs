---
content_hash: 51dd77a51dddce66fe1ec16e5901088b7db45086a5c695a159c5c87103431334
fetched_at: '2026-06-29T00:10:45.495418+00:00'
page_id: '553338750'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como Criar Issues Associadas ou Realizar Associação
  de Issues?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338750
version: 1
---

5%90%10%100%

A associação de *issue* deve ser realizada sempre que houver problemas iguais de clientes diferentes, associando as *issues*, no momento da expedição será enviada a solução para os dois clientes.

Ao identificar a necessidade de associação de *issue*, siga os passos abaixo:

A partir da ferramenta Zendesk (Suporte realiza a Associação)

1. Aplique a macro **Transferência Manutenção – Associação**.
   * *(Tipo do ticket será alterado para Incidente)*
2. Envie com o status **Em Espera**.
3. No aplicativo do JIRA, clique em **Criar Problema**.
4. Selecione o projeto que será transferido o problema e clique em **Criar Problema**.
5. Será exibida a tela para criação de novo problema no JIRA (imagem abaixo).
6. No campo *Tipo* selecione **Associado (sub-tarefa)**.
7. Será habilitado o campo ***Parent***.
8. No campo *Parent*informe a *issue* que receberá a associação.
9. Preencha os restantes dos campos solicitados.
10. Clique em **Criar Problema**.

*Será criada a issue de tipo associada no Jira como sub-tarefa da Issue que foi informada no campo Parent.*

A partir da ferramenta JIRA (Desenvolvimento realiza a Associação)

1. Clique em **More** / **Convert to Sub-task**.
2. Será exibida a tela para conversão da *issue*.
3. No campo *Select Parent Issue*, informe a *issue* Pai (que receberá a *sub-task*)
4. Confira que no campo *Select Sub-task Type*, já é apresentada a alteração da *issue type* de **Manutenção** para **Associado (sub-task)**.
5. Clique em **Next**.
6. Nas próximas 2 etapas clique em **Next**.
7. Para finalizar a associação clique em **Finish**.
8. Ao finalizar a issue será exibida com o tipo **Associado**.

**Perguntas e respostas rápidas sobre o assunto:**

**Posso associar uma issue a outra issue já expedida?**

Sim e será copiada a interação de expedição, após clicar no botão de **Expedir**.

**Como desassociar uma issue?**

É necessário converter a *subtask* em tarefa novamente, para isso siga os passos:

1. Acesse a opção *MORE*, clique em *Convert to Issue**;***

2. Selecione *Issue Type***:**Manutenção;

3. Informe o *Status* de Planejar/Especificar (para que o planejamento da *issue* seja realizado);

4. Não há necessidade de preencher o campo especificação.

**Quando não deve ser realizada uma associação?**

Quando a *issue* que será associada já possui *commit*;

Quando a *issue* que será associada já possui subtarefas (retrabalho, modelagem de dicionário de dados, compartilhamento, etc.).

Quando a *issue* principal está rejeitada/cancelada.

**Quando a área de Atendimento identificar um problema já existente, como deve proceder?**

A área de Atendimento deve criar uma nova *issue* associando esta a uma outra já existente. A *issue* criada fica como filha e será associada a *issue* pai.

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
