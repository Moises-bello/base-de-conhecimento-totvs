---
content_hash: 323ad46782ee0e5914ed13a5bdb11cc82e3204d52580635347963af479aaa39d
fetched_at: '2026-06-29T00:10:45.471377+00:00'
page_id: '553338620'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Classes de Serviço e Como Utilizar nas Issues
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338620
version: 1
---

5%90%10%100%

**Como utilizar a Classe de Serviço nas Issues?**

O campo "**Classe de Serviço**" poderá ser utilizado para classificar a *issue* conforme sua característica, para que possam ser tratados, organizados e planejados o *Backlog* e Plano de Entregas.

Para que os times possam utilizar a Classe de Serviço conforme suas necessidades, o campo que será utilizado será do tipo "***Label***" onde poderão ser inseridos os dados desejados.

O campo irá aparecer na tela de criação, visualização e edição das *issues* :

Como trata-se de um campo do tipo *Label*, é importante que os times criem um padrão para inserir os dados :

* + Usar palavras com o mesmo padrão de maiúscula e minúscula. Ex: PRAZO ≠ Prazo
  + Usar padrão com relação a utilização de acentos. Ex. Padrão ≠ Padrao
  + Quando usar mais de uma palavra, unir com "*underline*", caso contrário serão consideradas duas tags . Ex: Prazo\_Fixo, Melhoria\_Processo
  + Podem ser informadas mais de uma informação no campo Classe de Serviço.

---

**Dica!**

Por padrão o JIRA não mostra os campos vazios na tela de visualização da *issue*.

Então para facilitar a edição do campo aconselhamos incluí-lo na configuração do *board* como um campo na opção "Issue Detail View":

* + Acesse o board do seu time;
  + Na opção "Board" > "Configure";
  + Na última opção do menu, clique em "Issue Detail View";
  + Selecione o campo "Classe de Serviço" e clique em "ADD";
  + Agora ao selecionar a issue no seu board, no canto lateral direito, irá aparecer o campo para editar:

---

**Importante!**

Para quem já utilizava o campo "Classe de Serviço" ele foi renomeado para "OLD - Classe de Serviço" e foi desabilitado das telas de visualização e edição.

Porém você poderá realizar filtros com esse campo e realizar alteração em lote para atualizar o novo campo "Classe de Serviço" com o *label* que você irá utilizar.

Como alterar em lote:

* + Realize o filtro desejado;
  + No canto superior direito acesse "Tools" e selecione as *issues*;
  + Na tela seguinte selecione todas as *issues*;
  + Selecione a opção "Edit Issues";
  + Localize o campo "Classe de Serviço" e digite o *label* desejado (atente-se a regra citada acima);
  + Confirme a alteração, e as *issues* serão atualizadas.
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
hr {
border-bottom: 1px solid #FF8000;
}
]]>
