---
content_hash: e46c19488903d3f0c9f3188aa2a3f8421b72e5cc6bf621cc6e4c1fbfcf274419
fetched_at: '2026-06-29T00:10:44.954517+00:00'
page_id: '553338415'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Quando Usar a Issue type Apoio - Cliente (Issues
  sem Commit de Fonte)?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338415
version: 1
---

5%90%8%100%

* Status:*backlog, in progress,*concluído.
* Permite comunicar com o Cliente.
* Não permite *commit* de fonte no TFS.
* Não há expedição do pacote no *release*.
* Ao solucionar a *Issue*, solucionará o *Ticket* do Cliente.

A *Issue type***Apoio - Cliente** deve ser utilizada pela área de Desenvolvimento para demandas de Clientes onde não haverá *commit* de fonte e não serão executadas as demais etapas do processo padrão. Consulte abaixo algumas situações:

* **Problema corrigido em outra *Issue*, não identificado pelo Atendimento:** a área de Atendimento recebe um *ticket* do Cliente solicitando a correção de um problema, neste caso, é identificado que o problema já foi corrigido, mas não foi identificada a *Issue* para associar. A área de Atendimento deve criar uma nova *Issue* para o de Desenvolvimento analisar e enviar o link do pacote para o Cliente. 
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Corrigido em outra issue**".

* **Compilações de Fontes:**a área de Atendimento recebe um *ticket* do Cliente solicitando um pacote de determinada rotina que ainda não esteja disponível, neste caso, deve criar uma *Issue* para o Desenvolvimento compilar os fontes e publicar o pacote na Central de *Downloads*.
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Gerar/Enviar Pacote cliente(versão desatualizada)**".

* **Problema de parametrização na base do Cliente solucionado / Continuidade do Atendimento:**neste caso, a área de Atendimento já resolveu o problema de parametrização do Cliente e foi sugerida uma outra forma de trabalhar, sendo necessário uma análise técnica pelo Desenvolvimento.
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Correção / Atualização BD**".

* **Ajuste Banco de Dados do Cliente:** Nas situações em que o problema já foi corrigido e enviado a correção ao cliente, mas é necessário ter uma atuação do Desenvolvimento para ajustar o efeito no banco de dados, para rodar algum script ou acessar a base do cliente.
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Correção / Atualização BD**".

* **Piloto:** neste caso, a área de Desenvolvimento necessita explicar o processo piloto para o Cliente ou esclarecer alguma dúvida. Pode ser utilizado este *issue type* para registro e comunicação com o Cliente.
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Documentação Insuficiente**".

* **Documentação Insuficiente:**neste caso, a área de Desenvolvimento necessita criar ou melhorar a Documentação, e a área de Desenvolvimento deverá passar os procedimentos diretamente ao cliente realizando a comunicação com o Cliente.
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Documentação Insuficiente**".

* **Necessidade de Capacitação:**neste caso, a área de Atendimento necessita realizar a Capacitação para poder realizar o atendimento ao cliente, e a área de Desenvolvimento deverá passar os procedimentos diretamente ao cliente realizando a comunicação com o Cliente, e posteriormente prever a capacitação aos times pertinentes.
  + Essas demandas deverão ser solucionadas informando no campo "**Motivo Solução**" = "**Necessidade de Capacitação**".

* **Estudo de Performance**: neste caso, a área de Desenvolvimento necessita realizar um estudo da Performance do Cliente para analisar a causa da solicitação;

* **Ambiente do Cliente:** neste caso, há a necessidade de acesso ao Ambiente do Cliente, para que uma análise mais detalhada seja realizada antes do envio da solução;

Obs: O campo com o Motivo da Solução é solicitado ao Resolver as issues do tipo "Apoio - Cliente" e "Apoio" no momento de sua Resolução, é um campo opcional mas poderá ser utilizado conforme uma das justificativas citadas acima.

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
