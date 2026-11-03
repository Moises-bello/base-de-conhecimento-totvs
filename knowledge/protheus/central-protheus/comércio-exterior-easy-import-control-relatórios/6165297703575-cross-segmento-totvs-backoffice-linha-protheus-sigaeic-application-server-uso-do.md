---
article_id: 6165297703575
category: Comércio Exterior - Easy Import Control - Relatórios
content_hash: 84dcc17b85be60f9351e59d871f1d65039e30ec9efe45cc92be45cb1b7854f4d
fetched_at: '2026-06-28T22:39:43.394208+00:00'
product: protheus
section_id: 1500001549662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Application Server
  - Uso do GMAIL para questões de envio de e-mails de relatórios, integração despachante
  e Workflow
type: support-article
updated_at: '2023-02-06T19:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6165297703575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Application-Server-Uso-do-GMAIL-para-quest%C3%B5es-de-envio-de-e-mails-de-relat%C3%B3rios-integra%C3%A7%C3%A3o-despachante-e-Workflow
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Por motivo de segurança, o Google, irá descontinuar a configuração de Aplicativos menos seguros de sua ferramenta. Tal mudança impactará nas configurações da conta para utilização dentro do COMEX para o envio de e-mails de relatórios, integração despachante e Workflow.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**A partir de **30/05/2022,** o **Google**, por motivo de segurança, irá descontinuar a configuração de aplicativos menos seguros. Para continuar usando a conta **GMail** com o **TOTVS | Application Server** após essa data, será necessário configurar as **Senhas de App**. A documentação do Google para a utilização está em  <https://support.google.com/accounts/answer/185833> .

Para habilitar o uso de **Senhas de App** é necessário habilitar a **Verificação em duas etapas**. A documentação para habilitar essa configuração está disponível em <https://support.google.com/accounts/answer/185839?hl=pt-BR> .

Após habilitar a **Verificação em duas etapas**, aparecerá a opção de **Senhas de App**.

![](https://tdn.totvs.com/download/attachments/680967019/senhadeapp.png?version=1&modificationDate=1649876108933&api=v2)

Clicando em **Senhas de app**, clique em **Selecionar app**, escolha **Outro (nome personalizado)**, coloque um nome (Protheus, por exemplo) e clique em **Gerar**.

![](https://tdn.totvs.com/download/attachments/680967019/addsenhaapp.png?version=1&modificationDate=1649876108883&api=v2)

![](https://tdn.totvs.com/download/attachments/680967019/nomesenhaapp.png?version=1&modificationDate=1649876108833&api=v2)

A senha será gerada e deve ser anotada, pois não ficará disponível após clicar em **Concluído**.

![](https://tdn.totvs.com/download/attachments/680967019/senhaappgerada.png?version=1&modificationDate=1649876108783&api=v2)

![](https://tdn.totvs.com/download/attachments/680967019/listasenhaapp.png?version=1&modificationDate=1649876108730&api=v2)

Essa configuração é **independente** da ativação dos protocolos **POP** e/ou **IMAP** nas configurações do e-mail Google. A definição de uso dos protocolos continua sendo **necessária** para o uso com o **TOTVS | Application Server**.

Uma vez que a senha tenha sido gerada e está definido qual protocolo será utilizado, para poder enviar e/ou receber e-mails é só configurar no **TOTVS | Application Server** o endereço de e-mail e essa senha gerada, não mais a senha da conta. A senha pode ser utilizada sem espaço entre os blocos que são mostrados.

```
user function gmail()  
Local oServer := TMailManager():New()  
Local oMsg := TMailMessage():New()  
Local cSnd := "smtp.gmail.com"  
Local cRcv := "imap.gmail.com"  
Local nSndPort := 0  
Local nRcvPort := 0  
Local cUser := "account@gmail.com"  
Local cPass := "gikzztcmxdcrnwhi"  
Local cTo := "otheraccount@gmail.com"  
Local nMessages := 0  
  
oServer:SetUseTLS( .T. )  
  
if oServer:Init( cRcv, cSnd, cUser, cPass, nRcvPort, nSndPort ) <> 0  
conout( "Erro init" )  
return  
endif  
  
//connect on SMTP server, to send e-mails  
conout( "Connecting" )  
if oServer:SMTPConnect() <> 0  
conout( "SMTPConnect error" )  
return  
endif  
  
conout( "Authenticating" )  
if oServer:SMTPAuth( cUser, cPass ) <> 0  
conout( "Error authenticating account " + cUser )  
return  
endif  
  
oMsg:cDate := cValToChar( Date() )  
oMsg:cFrom := cUser  
oMsg:cTo := cTo  
oMsg:cCc := Nil  
oMsg:cBcc := Nil  
oMsg:cSubject := "Subject: test"  
oMsg:MsgBodyType( "text/plain" )  
oMsg:MsgBodyEncode( 1 )  
oMsg:cBody := "Test"  
  
conout( "Sending message" )  
nError := oMsg:Send( oServer )  
If nError <> 0  
conout( "Error: " + oServer:getErrorString( nError ) )  
else  
conout( "Message sent" )  
endif  
  
//disconnect from SMTP server  
oServer:SMTPDisconnect()  
  
//connect on IMAP server, to receive e-mails  
xRet := oServer:IMAPConnect()  
if xRet <> 0  
conout( "IMAPConnect error" )  
return  
endif  
  
oMsg:Clear()  
  
oServer:GetNumMsgs( @nMessages )  
  
//if there is messages in the account  
if nMessages > 0  
//receiving just 1 e-mail  
xRet := oMsg:Receive( oServer, 1 )  
if xRet <> 0  
conout( "Error on receive" )  
else  
conout( " Date: " + oMsg:cDate )  
conout( " From: " + oMsg:cFrom )  
conout( " To: " + oMsg:cTo )  
conout( "Subject: " + oMsg:cSubject )  
conout( " Body: " + oMsg:cBody )  
endif  
endif  
  
//disconnect from IMAP server  
xRet := oServer:IMAPDisconnect()  
if xRet <> 0  
conout( "IMAPDisconnect error" )  
return  
endif  
  
conout( "Success!!!" )  
return
```

**Saiba mais: [Application Server - Uso de e-mail com GMAIL.](https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail?spaceEditingRestriction=true)**

#
