---
content_hash: f8f2de5b1076c9fd3c380332b9b691bd2a4d2a489ad76ab7f8c08d73ec9af64b
fetched_at: '2026-06-29T00:10:44.912996+00:00'
page_id: '553338315'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Procedimento Antes de Rejeitar ou Não Rejeitar
  uma Issue
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338315
version: 1
---

5%90%10%100%

Esse passo tem como finalidade definir qual o procedimento a ser seguido em cada uma das situações abaixo, se uma *issue* deve ou não ser rejeitada para o atendimento.

| Situação | Procedimento |
| --- | --- |
| Quando issue for aberta para uma equipe incorreta e há a necessidade de análise de outra equipe do atendimento Na situação em que o Desenvolvimento, após a análise da issue verificar que deveria ter sido direcionada para outra equipe e há a necessidade de análise de outra equipe do atendimento:   * Antes de se recusar a issue, é sugerido que haja **alinhamento** com o Analista de Suporte, não havendo o consenso, é sugerido **alinhamento** entre o Maestro e/ou Líder de Atendimento e *Product Owner*. Se o consenso for que a issue deverá ser recusada, **Recusar** a Issue em “**Rejeitar p/ Atendimento**” com o Motivo “**Transferência**” e descrever no campo “**Comment**” o motivo pelo qual a issue está sendo Recusada e para qual equipe o ticket deve ser transferido para ser novamente analisado. | ******Rejeitar \******* |
| Quando issue for aberta para uma equipe incorreta e não há a necessidade de análise de outra equipe do atendimento Na situação em que o Desenvolvimento, após a análise da issue verificar que deveria ter sido direcionada para outra equipe e não há a necessidade de análise de outra equipe do atendimento:   * Equipe deverá **transferir** a issue para a equipe correta e **notificar** via Zendesk, através do botão (), o Analista atribuído ao ticket e o Maestro e/ou Líder de Atendimento para o **ajuste** do Módulo.   + *Para as equipes **Protheus**, também mover a evidência para o Google Drive da equipe correta.* | **Não Rejeitar** |
| Quando sugestão de melhoria não é aprovada Na situação em que o Desenvolvimento, após a análise da issue verificar que a sugestão de melhoria não será aprovada, deve:   * Utilizar a opção **Recusar Melhoria** disponível na ferramenta JIRA. Neste caso, a *Issue* do Cliente ficará com o status recusado e o *Ticket* será resolvido. | **Não Rejeitar** |
| Quando issue for aberta como Manutenção, porém o correto seria ser Inovação Na situação em que o Desenvolvimento, após a análise da *issue* de Manutenção, concluir que deveria ter sido uma Inovação, deve:   * **Transferir** a *issue* para a equipe correta (atentar-se para **atualizar** a *issue-type* para **Melhoria** em “More” > “Move”) e; * **Notificar** via Zendesk, através do botão (), o Analista atribuído ao *ticket* e o Maestro e/ou  Líder de Atendimento para o ajuste do Módulo, e é sugerido que haja **alinhamento** do *Product Owner* e Líder de Atendimento para comunicar o cliente. | **Não Rejeitar** |
| Quando a issue aberta não se tratar de uma manutenção ou não necessita de nenhuma ação do Desenvolvimento Na situação em que o Desenvolvimento, após a análise da *issue* verificar que não se trata de uma manutenção ou não necessita de nenhuma ação do Desenvolvimento, deve:   * Antes de se recusar a *issue*, é sugerido que haja **alinhamento** com o Analista de Suporte, não havendo o consenso, é sugerido **alinhamento** entre o Maestro e/ou Líder de Atendimento e *Product Owner*. Se o consenso for que a *issue* deverá ser recusada, **Recusar** a *Issue* em “**Rejeitar p/ Atendimento**” com o Motivo “**Solicitação Indevida**” e descrever no campo “**Comment**” o motivo pelo qual a *issue* está sendo Recusada. | ****Rejeitar \***** |
| Quando não há retorno do cliente Na situação em que o Desenvolvimento não receber o retorno do cliente, deve:   * Não deverá recusar a *issue*, o Desenvolvimento deverá tentar **contato** com o cliente, não havendo resposta, deverá entrar em **contato** com o Analista de Atendimento para que este também tente contato (é sugerido **alinhar** ação em conjunto entre o Maestro e/ou Líder de Atendimento e *Product Owner* caso o cliente não retorne), a *issue* deve permanecer em aberto até que seja possível resolvê-la. | **Não Rejeitar** |
| Quando não há commit Na situação em que o Desenvolvimento, após análise da *issue* verificar que não há *commit*, deve:   * **Atualizar** a *issue-type* para **Apoio - Cliente** em “More” > “Move” e solucionar a *issue*.   A *Issue type* **Apoio - Cliente** deve ser utilizada pela área de Desenvolvimento para demandas de Clientes onde não haverá *commit* de fonte e não serão executadas as demais etapas do processo padrão. Consulte algumas das situações em **[Instrução de Trabalho - Quando Usar a Issue type Apoio - Cliente (Issues sem Commit de Fonte)?](http://tdn.totvs.com/x/KleIGw)**. | **Não Rejeitar** |
| Quando Dev Team define que ponto de entrada não será implementado (Protheus) Na situação em que o Desenvolvimento, após análise da *issue* verificar que o ponto de entrada não será implementado (cenário especifico para Protheus), deve:   * **Atualizar** a *issue-type* para **Apoio - Cliente** em “More” > “Move” e solucionar a issue. | **Não Rejeitar** |
| Quando issue associada não tem relação com o assunto original Na situação em que o Desenvolvimento, após análise da *issue* verificar que a issue associada não tem relação com a *issue* principal, deve:   * **Recusar** a *issue* em “Rejeitar p/ Atendimento” com o Motivo “**Solicitação Indevida**” e descrever no campo “**Comment**” o motivo pelo qual a issue está sendo Recusada.   *Antes de se realizar a associação o Analista de Atendimento deve se certificar que é a mesma situação (em caso de dúvida deverá confirmar com o ponto focal da equipe ou com o Analista de Atendimento da issue principal).*   * *Linha Datasul e Logix: Se já tiver liberação para a issue principal, efetuar a liberação para o cliente e associar posteriormente. Caso não tenha compatibilidade, acionar a manutenção para efetuar a liberação.* * *Linha Protheus: Poderá ser associado a qualquer momento e informar ao cliente onde está o pacote. Mas deverá ser verificada se o Release do cliente consta como release de expedição da issue.*   **\*** **Linha Protheus: O Desenvolvimento não analisa as *issues* filhas, dando foco apenas para a *issue* pai, sendo assim, neste caso não haverá necessidade de rejeição.** | ****Rejeitar \***** |
| Quando ao reproduzir o erro, este já não ocorre mais (nova versão do produto) Na situação em que o Desenvolvimento, após análise da *issue* verificar que o erro já não ocorre mais, deve:   * Analisar se é porque uma nova versão do produto já foi liberada e o erro já foi corrigido nessa versão:   + **Atualizar** a *issue-type* para **Apoio - Cliente** em “More” > “Move” e solucionar a issue.   A *Issue type* **Apoio - Cliente** deve ser utilizada pela área de Desenvolvimento para demandas de Clientes onde não haverá *commit* de fonte e não serão executadas as demais etapas do processo padrão. Consulte algumas das situações em **[Instrução de Trabalho - Quando Usar a Issue type Apoio - Cliente (Issues sem Commit de Fonte)?](http://tdn.totvs.com/x/KleIGw)**. | **Não Rejeitar** |
| Quando não se consegue reproduzir o erro ou falta informação técnica do suporte/cliente Na situação em que o Desenvolvimento, após análise da issue verificar que não está sendo possível reproduzir o erro ou falta informação técnica do suporte/cliente, deve:   * Antes de se recusar a *issue*, deve-se analisar a *issue* e o *ticket*, avaliando se o Analista de Suporte entendeu o problema do solicitante e seguiu todos os passos para reprodução do erro (caso tenha algum *check-list "**<http://tdn.totvs.com/x/EZNICw>**" ou critérios de DoR e DoD definidos "**[Suporte e Desenvolvimento - Backoffice Protheus](http://tdn.totvs.com/x/7hW6Gw)**"*) e realizar o **alinhamento** com o Analista de Suporte, não havendo o consenso, **alinhar** entre o Maestro e/ou Líder de Atendimento e *Product Owner*. Se o consenso for que a *issue* deverá ser recusada, **Recusar** a *Issue* em “**Rejeitar p/ Atendimento**” com o motivo: “**Falta check-list/evidência de transferência para Manutenção**” e descrever no campo “**Comment**” o motivo pelo qual a *issue* está sendo Recusada. | ****Rejeitar \***** |
| Quando não conseguem acessar o vídeo enviado na issue, por ele estar obsoleto Na situação em que o Desenvolvimento não conseguir acessar o vídeo enviado na *issue*, por ele estar obsoleto, deve verificar se o erro já não ocorre mais, e:   * Analisar se é porque uma nova versão do produto já foi liberada e o erro já foi corrigido nessa versão:   + **Atualizar** a *issue-type* para **Apoio - Cliente** em “More” > “Move” e solucionar a issue.   A *Issue type* **Apoio - Cliente** deve ser utilizada pela área de Desenvolvimento para demandas de Clientes onde não haverá *commit* de fonte e não serão executadas as demais etapas do processo padrão. Consulte algumas das situações em **[Instrução de Trabalho - Quando Usar a Issue type Apoio - Cliente (Issues sem Commit de Fonte)?](http://tdn.totvs.com/x/KleIGw)**. | ****Não Rejeitar**** |

Importante

É muito importante lembrar que ao rejeitar uma issue que tenha *issues* associadas, todas serão rejeitadas automaticamente.

Por isso, ao rejeitar uma *issue*, certifique-se de que a rejeição é pertinente e que o Analista e o Maestro e/ou Líder de Atendimento estejam alinhados com esta ação.

Dica

Para maiores detalhes sobre a integração Zendesk x JIRA acesse o **[Manual do Jira](http://tdn.totvs.com/x/n5IlE)**, onde podem ser encontradas informações como:

* Quais *issues types* utilizar ao criar ou associar uma *Issue*;
* Detalhes do aplicativo *.: JIRA - TOTVS :.* no *Zendesk*;
* Detalhes do *plugin* do *Zendesk* no *JIRA*;
* Fluxo *JIRA* x Ação esperada no *Zendesk*.
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
