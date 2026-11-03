---
content_hash: 75e044880fa391ad8fec298ae95ac7b2a03840d80c7875318006ae2d15fb3fe4
fetched_at: '2026-07-02T19:24:27.783137+00:00'
page_id: '680967019'
product: protheus
source: tdn-tec
title: Application Server - Uso de e-mail com GMail
type: documentation
url: https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail
version: 3
---

Atualmente, para poder utilizar no true uma conta GMail para envio e recebimento de e-mails, é necessário configurar o protocolo de recebimento que será utilizado e configurar a utilização de aplicativos menos seguros.

Uma vez feita essa configuração, para poder utilizar a conta do GMail com o true, é necessário configurar a chave  na seção Mail no arquivo INI e utilizar o endereço de e-mail e senha da conta ao configurar um objeto da classe  ou . A TMailMng não tem dependência da chave Protocol, devendo configurar o protocolo usando o construtor da classe ().

Contudo, a partir de  o **Google**, por motivo de segurança, irá descontinuar a configuração de aplicativos menos seguros. Para continuar usando a conta GMail com o true após essa data, o é necessário configurar as **Senhas de App**. A documentação do Google para a utilização está em  <https://support.google.com/accounts/answer/185833> .

Para habilitar o uso de **Senhas de App** é necessário habilitar a **Verificação em duas etapas**. A documentação para habilitar essa configuração está disponível em <https://support.google.com/accounts/answer/185839?hl=pt-BR> .

Após habilitar a **Verificação em duas etapas**, aparecerá a opção de **Senhas de App**.

Clicando em **Senhas de app**, clique em **Selecionar app**, escolha **Outro (nome personalizado)**, coloque um nome (Protheus, por exemplo) e clique em **Gerar**.

A senha será gerada e deve ser anotada, pois não ficará disponível após clicar em **Concluído**.

Essa configuração é **independente** da ativação dos protocolos **POP** e/ou **IMAP** nas configurações do e-mail Google. A definição de uso dos protocolos continua sendo **necessária** para o uso com o true.

Uma vez que a senha tenha sido gerada e está definido qual protocolo será utilizado, para poder enviar e/ou receber e-mails é só configurar no true o endereço de e-mail e essa senha gerada, não mais a senha da conta. A senha pode ser utilizada sem espaço entre os blocos que são mostrados.

 0
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
return]]>
