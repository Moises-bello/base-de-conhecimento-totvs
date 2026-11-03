---
content_hash: ef4b22b44dfe8544af5ed73948e2a264a84a6b731141a735cea99a5dd981eec2
fetched_at: '2026-06-29T00:10:44.896382+00:00'
page_id: '553338267'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como Realizar Links entre Issues no JIRA (Depende
  de, Relates to)?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338267
version: 1
---

5%90%10%100%

**Depende de**

O link **dependente de** pode ser utilizado em situações que a *Issue* precise estar relacionada a outra *Issue* e uma não pode ser concluída sem que a outra também esteja concluída. **Este tipo de link é indicado para produtos com integração e que as alterações precisam ser liberadas em conjunto.**

Na tarefa principal, onde está o link **dependente de** possui uma validação que não permite finalizar a etapa de **Teste Integrado** para **Expedição/Teste Integrado Concluído**, sem que a *Issue* a qual possui dependência esteja concluída. 

Após conclusão da *Issue* com dependência a transição de **Liberar para Expedição** ou **Finalizar Teste Integrado** fica novamente disponível.

**Como Criar Link Depende de:**

1. 1. Clique em **More** > **Link**.
   2. Na issue original, do Cliente por exemplo, deve ser informado o tipo de link “**Depende de**” e informado a issue que será vinculada, ou seja, qual issue precisará ser finalizada antes da issue atual.
   3. Clique no botão **Link** para confirmar.

**Relates to**

O link **Relates to** pode ser utilizado em situações que a Issue precise estar relacionada a outra Issue para manter a rastreabilidade, mas que uma não dependa da outra para liberação ao Cliente.   Esse tipo de link é apenas informativo para auxiliar na visualização e acompanhamento em Dashboards. **Este tipo de link é indicado para produtos com integração.**

**Criar Link Relates to:**

1. 1. Clique em **More** > **Link**.
   2. Deve ser informado o **tipo de link** e a **Issue original** que será vinculada.
   3. Clique no botão **Link** para confirmar.
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
