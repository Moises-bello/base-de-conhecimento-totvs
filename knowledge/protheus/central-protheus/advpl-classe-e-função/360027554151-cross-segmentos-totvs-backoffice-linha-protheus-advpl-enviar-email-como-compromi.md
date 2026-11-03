---
article_id: 360027554151
category: ADVPL - Classe e Função
content_hash: 24e59943e616a496337338f4dbf87372df6d9aed9ddd403ed425bd2f1e715d04
fetched_at: '2026-06-28T22:40:18.309886+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Enviar email
  como compromisso de agenda via TMailMessage
type: support-article
updated_at: '2022-01-06T18:59:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027554151-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Enviar-email-como-compromisso-de-agenda-via-TMailMessage
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Gostaria de saber se é possível enviar um email como um compromisso pelo Protheus usando o TMailMessage.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para atender essa necessidade é necessário enviar o arquivo do tipo \*.ICS em anexo, e  adicionar o cabeçalho via métodos [AddAttHTag](http://tdn.totvs.com/display/tec/TMailMessage%3AAddAttHTag) e [AddCustomHeader](http://tdn.totvs.com/display/tec/TMailMessage%3AAddCustomHeader).  
A seguir exemplo de utilização:

```
#Include 'Protheus.ch'  
  
User Function tEnv()  
  
 Local cUser := "", cPass := ""  
 Local nTimeout := 0  
 Local xRet  
 Local oServer, oMessage  
  
   
 cUser := "email@outlook.com" //define the e-mail account username  
 cPass := "" //define the e-mail account password  
 nTimeout := 60 // define the timout to 60 seconds  
   
 oServer := TMailManager():New()  
   
 oServer:SetUseSSL( .T. )  
 oServer:SetUseTLS( .T. )  
   
 oServer:Init( 'pop-mail.outlook.com', 'smtp-mail.outlook.com' , cUser, cPass, 995, 587 )  
   
 oServer:SetSmtpTimeOut( 120 )  
   
 //Verifica conexão SMTP  
 conout( 'Conectando do SMTP' )  
 nErro := oServer:SmtpConnect()  
 If nErro <> 0  
 conout( "ERROR:" + oServer:GetErrorString( nErro ) )  
 oServer:SMTPDisconnect()  
 return .F.  
 Endif   
   
 //Verifica autenticação  
 nErro := oServer:SmtpAuth( cUser ,cPass )  
 If nErro <> 0  
 conout( "ERROR:" + oServer:GetErrorString( nErro ) )  
 oServer:SMTPDisconnect()  
 return .F.  
 Endif  
   
 oMessage := TMailMessage():New()  
 oMessage:Clear()  
 oMessage:cFrom := "email@outlook.com"  
 oMessage:cTo := "email@outlook.com"  
 oMessage:cCc := ""  
 oMessage:cSubject := "teste"  
 oMessage:cBody := ""  
  
 oMessage:AddCustomHeader( "Content-Type", "text/calendar" )  
   
 If oMessage:AttachFile( "teste.ICS" ) < 0  
 Conout( "Erro ao atachar o arquivo" )  
 Return .F.  
 Else  
  
 //adiciona uma tag informando que é um attach e o nome do arq  
 oMessage:AddAtthTag('Content-Disposition: attachment; filename=teste.ICS')  
 EndIf  
   
 //Envia e-mail  
 nErro := oMessage:Send( oServer )  
   
 //Verifica se o e-mail foi enviado  
 if nErro <> 0  
 conout( "ERROR:" + oServer:GetErrorString( nErro ) )  
 oServer:SMTPDisconnect()  
 return .F.  
 Endif  
   
 conout( 'Desconectando do SMTP' )  
 oServer:SMTPDisconnect()  
   
return
```
