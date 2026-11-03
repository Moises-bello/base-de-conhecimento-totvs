---
article_id: 360011724292
category: Materiais - Compras (SIGACOM)
content_hash: 39fb632cb99b5b997e7ce5b3f03e3cecb0c04629762b979466c1d5c57d90bf1b
fetched_at: '2026-06-28T22:41:08.864836+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - EventViewer  / Disparo
  de e-mail de eventos
type: support-article
updated_at: '2026-03-03T18:25:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-EventViewer-Disparo-de-e-mail-de-eventos
---

**Dúvida**

Exemplo de configuração para disparo de e-mails de Eventos EventViewer.  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.8  
  
**Solução**

Antes de iniciar a configuração há um ponto Importante:

Para cada servidor de e-mail existe uma particularidade quanto as permissões para uso de envio de e-mail a sistemas. O processo de configuração do Gmail para realizar essas permissões foi alterado, onde antes de iniciar a configuração no Protheus, orientamos por favor seguir as recomendações do Link abaixo para configurar a senha de App.

[WF0023\_WorkFlow - GMAIL nova config. para utilização com o Workflow Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=689063841)

**Obs:** Preencher a nova senha de App configurada em todos os parâmetros referente a senha dos passos abaixo:

Exemplo da configuração de envio de e-mail:

**Configurador > Cadastros > E-mail/proxy**  
**​**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573355321751)![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573357757591)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573397664535)![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008553632)

- Configurar os parâmetros:

* **MV\_RELSERV**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573539052567)

* **MV\_RELACNT**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573614807447)**

* **MV\_RELPSW**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573666147607)

* **MV\_RELAUTH**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573742621079)

* **MV\_RELAPSW**

**Obs:** Para configurar a senha de App no gmail seguir o passo a passo da documentação do link [WF0023\_WorkFlow - GMAIL nova config. para utilização com o Workflow Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=689063841)

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573814867991)**

* **MV\_RELSSL**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7573857476631)**

* **MV\_RELTLS**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7574070308375)**

* **MV\_RELAUSR**

**![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7577118415767)**

* **MV\_RELFROM**

**![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7577156104471)**

* **MV\_EMSENHA**

**![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7577215407639)**

* **MV\_EMCONTA**

**![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7577250952215)**

Segue exemplo de configuração do gmail de todos os parâmetros no configurador.

MV\_RELSERV //smtp.gmail.com:587   
MV\_RELACNT //teste11915@gmail.com   
MV\_RELPSW // xxxxxxxxxxxxx  
MV\_RELAUTH // .T.   
MV\_RELAPSW // xxxxxxxxxxxxxxxxx  
MV\_RELSSL // .F.   
MV\_RELTLS // .T.   
MV\_RELAUSR // teste11915@gmail.com   
MV\_RELFROM = teste11915@gmail.com   
MV\_EMSENHA = xxxxxxxxxxxxxxxxxxx  
MV\_EMCONTA = [teste11915@gmail.com](mailto:teste11915@gmail.com)

**Obs:** O exemplo do e-mail de configuração e-mail de envio e de senha de app dessa documentação é de uso do gmail, caso utilize outros servidores de e-mail realizar a consulta das configurações com o servidor de seu e-mail.

Para adicionar o evento via Eventviewer é necessário acessar a rotina **Inscrição de Event Viewer (**[**CFGA040**](https://tdn.totvs.com/x/76s4E)**)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38776682319383)

***Obs:***

A rotina M-messenger (MATA045) será descontinuada em 31/10/2024.

**Rotina Substituta:**  
[CFGA040 - Event Viewer](https://tdn.totvs.com/x/76s4E) (Tabela SXI)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Substituição da Rotina Messenger(MATA045)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23139788947607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Substitui%C3%A7%C3%A3o-da-Rotina-Messenger-MATA045?source=search)

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Substituição da Rotina Messenger(MATA045)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23139788947607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Substitui%C3%A7%C3%A3o-da-Rotina-Messenger-MATA045?source=search)
* [Substituição de rotinas TOTVS Backoffice - Linha Protheus 2024](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22998379177495-Substitui%C3%A7%C3%A3o-de-rotinas-TOTVS-Backoffice-Linha-Protheus-2024?source=search)
* [Como configurar o Event Viewer para disparar notificações](https://tdn.totvs.com/x/76s4E)
* [Configurar o SMTP para envio de relatórios por e-mail e Configurando com a utilização do Office 365 (Office Online) como provedor SMTP](https://tdn.totvs.com/pages/releaseview.action?pageId=271166884)
* [MP - SIGAEST - Falha autenticação do M-MESSENGER - AUTHENTICATION FAILED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004878272-MP-SIGAEST-Falha-autentica%C3%A7%C3%A3o-do-M-MESSENGER-AUTHENTICATION-FAILED)
* [GCT0127\_Eventos\_038\_e\_039\_Configuração\_via\_Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=402071753)
* [GCT0028\_MV\_ATUGCT\_Eventos\_038\_e\_039](https://tdn.totvs.com/display/public/PROT/GCT0028_MV_ATUGCT_Eventos_038_e_039)
* [GCT0125 - Ativando e-mails de avisos automáticos do módulo GCT](https://tdn.totvs.com/pages/releaseview.action?pageId=393363398)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
