---
article_id: 360017787171
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 81277e14452da4fdf69507b6363ba070af938fc12e676b934b92eb63a71bcc15
fetched_at: '2026-06-28T22:37:22.714339+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Envio de e-mail dos
  Eventos 038 (Aviso de Vencimento de Contrato) e 039 (Aviso de Término de Contrato)
  do EventViewer
type: support-article
updated_at: '2026-06-26T14:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017787171-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Envio-de-e-mail-dos-Eventos-038-Aviso-de-Vencimento-de-Contrato-e-039-Aviso-de-T%C3%A9rmino-de-Contrato-do-EventViewer
---

**Dúvida**

Envio de e-mail de alerta dos Eventos 038 (Aviso de Vencimento de Contrato) e 039 (Aviso de Término de Contrato) do EventViewer

**Ambiente**

Microsiga – Gestão de Contratos – A partir da versão P12.1.17

**Solução**

O envio de *e-mail's* de alerta para os eventos de Vencimento e Término de Contrato do GCT, são orientados pelo parâmetro MV\_ATUGCT  
  
1. Verifique se o parâmetro MV\_ATUGCT não se encontra com período superior a *database*;

2. Caso o parâmetro esteja superior a *database*, corrija a data do parâmetro para que seja 1 dia antes que a *database* do sistema. (Para que o sistema efetue a atualização automaticamente do parâmetro para validação do evento)

3. Segue exemplo de Configuração de e-mail de envio do "messenger/disparo de e-mail de eventos" para configuração em seu ambiente - [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - EventViewer / Disparo de e-mail de eventos – Central de Atendimento TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-EventViewer-Disparo-de-e-mail-de-eventos)

Após realizar a configuração de envio de e-mail conforme documentação acima configure o parâmetro **MV\_CNSCHED = 3.**

4. No cadastro do Tipo de contrato é necessário informar em quantos dias a notificação será enviada, esta informação é inserida no campo “Dias/Aviso” (CN1\_PRDALT):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41515845379607)

***Obs1:***

Se for inserido um conteúdo como 5 (CINCO) no campo o sistema avisará somente cinco dias antes do vencimento do contrato, caso necessite que o aviso seja enviado em mais dias é necessário separar com virgula os conteúdos (5,4,3,2,1).

***Obs2:***

Relação do parâmetro MV\_ATUGCT com evento 038 aviso de Vencimento.

Configure o parâmetro MV\_ATUGCT um dia antes da data do aviso do vencimento , acesse o sistema com a data base do dia do aviso do vencimento para realização de um novo teste.  
Obs: O e-mail será enviado apenas 1 vez por dia para o contrato, não havendo a possibilidade de se fazer um reenvio para o contrato no mesmo dia.

Saiba mais: <https://tdn.totvs.com/display/public/PROT/GCT0028_MV_ATUGCT_Eventos_038_e_039>

O sistema notificará o usuário cadastrado tendo como parâmetro a data informada no campo CN9\_DTFIM (Data final do contrato).

5. **CONFIGURAÇÃO DOS EVENTOS 038 e 039**  
  
Acesse a rotina CFGA040 (Insc. Event Viewer) e efetue a amarração dos eventos 038 e 039 ao usuário e respectivo e-mail, na aba Usuários SIGA é possível amarrar um grupo de usuários e na aba não usuários é possível informar qualquer e-mail que necessite receber a notificação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38778331646871)

**IMPORTANTE:**

A funcionalidade de envio de e-mails pelo M-Messenger será **descontinuada a partir da versão 12.1.2410**, e os eventos de disparo deverão ser cadastrados pelo EventViewer:

[GCT0158\_Cadastrando eventos no EventViewer do GCT](https://tdn.totvs.com/x/Nyz2MQ) 

**Opção de utilização via Schedule.**

Abaixo, segue a configuração dos parâmetros para que a notificação dos eventos 038 e 039 sejam enviados via schedule.

Parâmetros:

1. **MV\_COMPEVE** = Define se o evento 038 ou 039 é 1- Empresa ou 2-Respeita o compartilhamento da tabela do contrato (CN9);  
2. **MV\_CNSCHED** = Informa se a verificação de alerta de vencimento de Contrato deverá ser por 1=Início do Modulo, 2=Schedule (CFG) ou 3=Ambos; → Parâmetro descontinuado a partir da release 12.1.2610  
3. **MV\_CNSCHAT =** Data de atualização do envio de email de aviso de vencimento/término do contrato por agendamento (schedule).

**IMPORTANTE:** O parâmetro **MV\_CNGRMSG**, não possui mais funcionalidade a **partir da release 12.1.2410**

Para o cadastro do agendamento no schedule, informar a rotina SCHEDCTAAL.

![](https://tdn.totvs.com/download/attachments/402071753/image2018-9-5_18-10-25.png?version=1&modificationDate=1536181827000&api=v2)

Para maiores informações sobre configurações via schedule acesse a documentação - [GCT0127\_Eventos\_038\_e\_039\_Configuração\_via\_Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=402071753) 

Veja mais detalhes na Documentação: [GCT0125 - Ativando e-mails de avisos automáticos do módulo GCT](https://tdn.totvs.com/pages/releaseview.action?pageId=393363398)

**IMPORTANTE:** houve uma mudança na geração de senha do gmail segue o novo processo na documentação abaixo para que possa configurar a senha conforme abaixo para preenchimento dos parãmetros de senha corretamente..  
   
Geração de senha de app gmail  
<https://tdn.totvs.com/pages/releaseview.action?pageId=689063841>

Exemplo de e-mail de "Aviso de Vencimento" (Evento 038):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7699531502615)

Exemplo de e-mail de "Término do Contrato" (Evento 039):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7699549077015)

***Obs3:***

O usuário que fizer a inscrição para receber aviso de vencimento de contrato vai receber aviso sobre TODOS os contratos ou somente aqueles que ele tem acesso?

**Resposta:** No cadastro dos Evento do Eventviewer de Vencimento de Contrato do Gestão de Contratos assim como os demais eventos do módulo, caso o usuário seja cadastrado, ele receberá os avisos de todos os contratos, sendo que hoje não há uma funcionalidade ou parametrização para que receba os avisos apenas dos contratos em que ele possui acesso.

***Obs4:***

O SIGAGCT possui configuração para se filtrar as notificações do Eventviewer 038 (Aviso de Vencimento de Contrato) e 039 (Aviso de Término de Contrato) por usuário responsável ou por tipo de Contrato (Compra ou Venda) ou para não se receber aviso de uma filial que não é mais utilizada ?

***Resposta:*** No padrão do módulo de Gestão de Contrato ele não possui uma funcionalidade ou parametrização para realização deste processo de filtro no disparo de envios dos e-mails do evento 038 e 039, onde no padrão ele dispara para todos usuários que estiverem com o evento cadastrado.

***Obs5:***

Atualmente o SIGAGCT não possui uma funcionalidade ou evento do Messenger para o disparo de e-mail quando a medição foi aprovada em sua alçada ou também quando o contrato teve a alçada aprovada.

***Saiba Mais:***

[GCT0028\_MV\_ATUGCT\_Eventos\_038\_e\_039](http://tdn.totvs.com/display/PROT/GCT0028_MV_ATUGCT_Eventos_038_e_039)

[GCT0127\_Eventos\_038\_e\_039\_Configuração\_via\_Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=402071753)

[GCT0125 - Ativando e-mails de avisos automáticos do módulo GCT](https://tdn.totvs.com/pages/releaseview.action?pageId=393363398)

[GCT0032\_Aviso\_de\_Vencimento](https://tdn.totvs.com/display/public/PROT/GCT0032_Aviso_de_Vencimento)

[GCT0158\_Cadastrando eventos no EventViewer do GCT](https://tdn.totvs.com/x/Nyz2MQ)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração Messenger / EventViewer / Disparo de e-mail de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger-EventViewer-Disparo-de-e-mail-de-eventos)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
