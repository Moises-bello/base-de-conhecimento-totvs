---
article_id: 9928395844247
category: Materiais - Compras (SIGACOM)
content_hash: c092d4ed2554811da2d9628a25158780641cd3fef661059c5c809e6b12d0b733
fetched_at: '2026-06-28T22:41:17.678544+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Evento 075 EventViewer
  para informar próximo aprovador que documento esta pendente de aprovação
type: support-article
updated_at: '2025-07-22T17:38:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9928395844247-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Evento-075-EventViewer-para-informar-pr%C3%B3ximo-aprovador-que-documento-esta-pendente-de-aprova%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21463121737623) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Evento 075 - EventViewer para informar próximo aprovador que documento está pendente de sua aprovação.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Para utilização deste evento o Protheus necessita estar configurado para envio de emails de Evento do Messenger/EventViewer.

1. Segue exemplo de Configuração de envio de e-mail do Messenger e EventViewer para que possa ser realizada a configuração no ambiente:

[- Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger-?source=search)

[- Como configurar o Event Viewer para disparar notificações](https://tdn.totvs.com/x/76s4E)

2.Cadastrar o e-mail de Recebimento para cada Aprovador do Grupo de Aprovação no Configurador do sistema conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32851096870551)

3. Seguir o passo a passo conforme Documentação abaixo:

[PCOM17003 - Evento para informar próximo aprovador que documento esta pendente de sua aprovação.](https://tdn.totvs.com/pages/releaseview.action?pageId=572490417)

4.Cadastrar todos usuários Aprovadores no EventViewer.Segue o exemplo de configuração abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21463121753879)

**-**Realizar o cadastro do evento 075, vinculando os usuários aprovadores conforme o menu indicado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33641164009367)

**Obs:**Caso o usuário Aprovador não tiver acesso habilitado para a rotina de Inscrição de eventviewer habilitar o acesso 174 conforme print abaixo, no cadastro de usuários no configurador do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33641164011287)

**Exemplo do email recebido:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32525406990359)**

**Obs1:**

Processo de envio de e-mail ao aprovador (evento 075) não é contemplado pela rotina MATA045 - **Messenger**. Ele tem sua funcionalidade disponível apenas em **Event Viewer** - [Configurar Event Viewer](https://tdn.totvs.com/display/framework/Configurar+Event+Viewer)

Necessário estar com o fonte **MATXALC - a partir de 06/11/2020**

**Obs2:**

Somente os usuários que fazem parte do processo de aprovação receberão o E-mail do evento.

**Obs3:**Esse processo pode ser configurado tanto para aprovações de Pedido , quanto as aprovação de solicitação de compras.

***Saiba Mais:***

* [PCOM17003 - Evento para informar próximo aprovador que documento esta pendente de sua aprovação.](https://tdn.totvs.com/pages/releaseview.action?pageId=572490417)
* [MP - SIGAEST - Falha autenticação do M-MESSENGER - AUTHENTICATION FAILED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004878272-MP-SIGAEST-Falha-autentica%C3%A7%C3%A3o-do-M-MESSENGER-AUTHENTICATION-FAILED)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger-?source=search)
* [Como configurar o Event Viewer para disparar notificações](https://tdn.totvs.com/x/76s4E)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
