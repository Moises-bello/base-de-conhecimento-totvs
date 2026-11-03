---
content_hash: 2d90c85ed9dcfe8900f86ff6197ef485b5322ea9d01dd4e44c4ef8b838304bd5
fetched_at: '2026-06-29T00:10:44.944502+00:00'
page_id: '553338403'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como Realizar Liberação Emergencial?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338403
version: 1
---

5%90%10%100%

A **Liberação Emergencial** (*Issues* de Manutenção, Legislação e Ponto de Entrada) deve ser feita ao Cliente em casos **Críticos**, onde não há possibilidade de aguardar a liberação oficial. Pode ser realizada a partir da conclusão da subtarefa de **Codificação.**

1. Acesse o botão **Liberação Emergencial** na *Issue* principal. Para *issues* do **Produto Protheus**, acesse o botão **Solicitar Robô SP - Liberação Emergencial**. Essa liberação enviará uma mensagem padrão ao cliente com o link da Central de *Download*.
2. *Scripts*, Pacotes e Instaladores devem ser disponibilizados na Central de *Downloads* e deve ser informado o endereço no campo Comentário, do JIRA.
3. É possível**reforçar** a Liberação Emergencial por meio do botão **Comunicação com o Cliente** e **informar ao cliente que liberações feitas após as subtarefas de Codificação e Teste de Unidade não contemplam a realização de todos os níveis de testes do produto.**
4. Quando é feita uma liberação Emergencial para o Cliente, o SLA da *Issue* é pausado, o *status* do ticket atualiza para Pendente e é realizado um comentário público no ticket. O Desenvolvimento deve prosseguir executando as demais etapas do Processo de Desenvolvimento Ágil.
5. **Antes de solucionar a *Issue*****deve ser avaliado se o Cliente deu algum retorno no ticket.** Esse retorno pode ser consultado por meio do campo **último comentário do Zendesk**, na aba Zendesk.

#FF8000#FFF8DCsolid

**IMPORTANTE:**

 **Envio de pacotes/*patchs* em anexo em *tickets* ou *issues***

Por questões de segurança para o Cliente e para a TOTVS, **NÃO** é correto o envio de pacotes/patchs em anexo nos *tickets* ou *issues* para o Cliente/Solicitante.

* Toda e qualquer expedição deve ser realizada via **Central de *Download***, que é o canal oficial de liberação de pacotes/*patchs*.

* + Quando a Central de Downloads estiver inacessível, informar à TI o ocorrido e aguardar o seu restabelecimento e/ou utilizar o publicador para prosseguir com o atendimento.

Abaixo o workflow de Liberação Emergencial:

Consulte todos os workflow no **[Manual do JIRA](http://tdn.totvs.com/x/n5IlE)**.

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
