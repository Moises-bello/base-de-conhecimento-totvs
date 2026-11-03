---
article_id: 4410465626647
category: Controle de Documentos (SIGAQDO)
content_hash: 4a1fb8748c6e4435efce447d16259fa7cf5379dc0b5a54ed786f0438ca3f8898
fetched_at: '2026-06-28T22:42:29.051664+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Envio de e-mail de pendências
type: support-article
updated_at: '2021-10-11T14:15:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410465626647-Manufatura-Linha-Protheus-SIGAQDO-Envio-de-e-mail-de-pend%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:55 min** **Dúvida**Como configurar o módulo **SIGAQDO - Controle de Documentos** para enviar *e-mails*?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**O módulo **SIGAQDO** envia uma notificação por *e-mail* para os usuários que estiverem com o campo **QAA\_RECMAI - Receb E-mail** da rotina **QAXA010 - Usuários** como **1-Sim** sempre que uma pendência é gerada.  
Para que este envio de *e-mail* ocorra com sucesso, o módulo **SIGAQDO** utiliza as mesmas configurações para envio de *e-mail* que os demais módulos do **Protheus**, onde são validadas as seguintes parametrizações:

* Servidor **SMTP - Simple Mail Transfer Protocol**, conforme a documentação [Configurar o SMTP para envio de relatórios por e-mail](http://tdn.totvs.com/pages/releaseview.action?pageId=271166884)
* **MV\_RELSERV - Nome do Servidor de Envio de E-mail utilizado nos relatório**: Servidor **SMTP**a ser utilizado no envio do *e-mail*. Pode ser um nome **WINS - Windows Internet Name Service**, **DNS - Domain Name System** ou um **IP - Internet Protocol**;
* **MV\_RELAUTH - Servidor de e-mail necessita de Autenticação**: Se este parâmetro for **.T.**, será possível enviar *e-mail* para outros domínios diferentes do servidor de envio;
* **MV\_EMCONTA - Indica qual conta utilizada para envio de e-mails automáticos pelo Sistema**;
* **MV\_EMSENHA - Indica qual a senha da conta utilizada para envio de e-mails automáticos pelo Sistema**: A senha da conta no servidor de **SMTP**;
* **MV\_RELAPSW - Senha para autenticação no servidor de e-mail**;
* **MV\_RELACNT - Conta a ser utilizada no envio de E-Mail para os relatórios;**
* **MV\_RELFROM - E-mail utilizado no campo FROM no envio de relatórios por e-mail**

Além dos parâmetros gerais citados acima, também são validados os parâmetros abaixo, para o envio de *e-mails* periodicamente:

* **MV\_QDOAVEM - Define se há envio de e-mail aos usuários com lançamentos pendentes**;
* **MV\_QUDQDON - Define o período em dias, de envio de e-mail de pendências**.
