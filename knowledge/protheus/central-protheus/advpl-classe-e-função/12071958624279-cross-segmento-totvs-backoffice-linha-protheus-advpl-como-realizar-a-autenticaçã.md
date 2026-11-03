---
article_id: 12071958624279
category: ADVPL - Classe e Função
content_hash: 322758c8abd4781cb94572a82695bd9138e5024557d71a1a80b894c0fa7a34d0
fetched_at: '2026-06-28T22:40:20.623219+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Como realizar a
  autenticação no modelo OAuth2 para o Office 365 no Protheus
type: support-article
updated_at: '2024-06-14T19:07:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12071958624279-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-realizar-a-autentica%C3%A7%C3%A3o-no-modelo-OAuth2-para-o-Office-365-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Como realizar a autenticação no modelo OAuth2 para o Office 365 no Protheus?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - a partir da versão 12.1.33

**Solução**

1° Deve-se possuir o *token* de acesso gerado pela **Microsoft**:

<https://learn.microsoft.com/pt-br/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#register-your-application>

As permissões devem ser habilitadas no **Azure Active Directory** para que o *token* funcione corretamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12073422903319)

O token tem um tempo de validade no qual sempre deve ser renovado. 

2° Com o Token será possível passar para o método da classe [TMailManager:SetOAuthToken](https://tdn.totvs.com/display/tec/TMailManager%3ASetOAuthToken) no qual será permitido a autenticação.

**Observações:**

* O método deve ser chamado após chamar o método *Init* e antes de chamar os métodos de *connect* (**SMTPConnect**, **POPConnect**, ou **IMAPConnect**).
* Esse método impacta o recebimento e o envio de e-mails.
* Se a conexão utilizada for usando o protocolo **MAPI**, o método não tem efeito

**Saiba mais**

[Application Server - E-mail - Office 365](https://tdn.totvs.com/display/tec/Application+Server+-+E-mail+-+Office+365)

[SetOAuthToken](https://tdn.totvs.com/display/tec/TMailManager%3ASetOAuthToken)  
[TMailManager](https://tdn.totvs.com/display/tec/Classe+TMailManager)
