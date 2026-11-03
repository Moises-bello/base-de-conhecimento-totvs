---
article_id: 360013675571
category: ADVPL - Classe e Função
content_hash: 110f5a5e6788db7907b20e61a5ee0dc12d64e823a37df33294705c6ebd907126
fetched_at: '2026-06-28T22:40:14.554076+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - cBody em Branco
  TMailMessage
type: support-article
updated_at: '2022-01-03T21:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013675571-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-cBody-em-Branco-TMailMessage
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao carregar a mensagem pela classe TmailMessage a propriedade cBody está vindo em branco.

Motivo de o cBody estar em branco nas Propriedades da Classe TmailMessage.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL -  A partir da versão 11.80  
  
**Causa**A propriedade do  cbody ( Corpo do E-mail) da Classe TMailMessage não aparece  quando não tem  a chave no Content-Type: text/plain no .eml  ou seja o e-mail é exclusivo html.  
  
**Solução**

Em caso do e-mail ser exclusivo Html, o corpo do E-mail virá  em branco e poderá ser salvo um anexo .html da página que está em anexo.  ( Neste caso, você poderia ler este arquivo para obter as informações que necessita).  
Caso o e-mail tenha texto no corpo do E-mail, será apresentado na propriedade do cbody.  
  
Exemplo de Fonte.

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
#INCLUDE "Ap5Mail.ch"  
#INCLUDE "XMLXFUN.CH"  
  
user function Rec_Mail()  
  Local oServer  
  Local oMessage  
  Local nAttach := 0, nI := 0  
  Local nMessages := 0, nM := 0  
  Local cAttach := "", cName := ""  
  Local aAttInfo := {}  
  Local xRet  
  Local nI, nY  
     
  oServer := tMailManager():New()  
  writePProString( "Mail", "Protocol", "POP3", getsrvininame() )  
     
  oServer:SetUseSSL( .T. )  
  xRet := oServer:Init( "pop.gmail.com", "", "email@gmail.com", "xxxxxx", 995, 0)  
  if xRet <> 0  
    conout( "Could not initialize mail server: " + oServer:GetErrorString( xRet ) )  
    return  
  endif  
     
  xRet := oServer:POPConnect()  
  if xRet <> 0  
    conout( "Could not connect on POP3 server: " + oServer:GetErrorString( xRet ) )  
    return  
  endif  
     
  oServer:GetNumMsgs( @nMessages )  
  conout( "Number of messages: " + cValToChar( nMessages ) )  
     
  oMessage := TMailMessage():New()  
  oMessage:Clear()
```

```
for ny := 1 to nMessages  
  
    conout( "Receiving newest message" )  
  
    xRet := oMessage:Receive( oServer, ny )  
  
    if xRet <> 0  
  
        conout( "Could not get message " + cValToChar( nMessages ) + ": " + oServer:GetErrorString( xRet ) )  
  
        return  
  
   endif
```

```
    cFile := "C:\EML\" + cValToChar( ny ) + ".eml"  
    conout( "Saving message " + cValToChar( ny ) + " to " + cFile )  
    oMessage:Save( cFile )  
          
    nAttach := oMessage:GetAttachCount()  
    for nI := 1 to nAttach  
        cAttach := oMessage:GetAttach( nI )  
        aAttInfo := oMessage:GetAttachInfo( nI )  
        varinfo( "", aAttInfo )  
       
        cName := "C:\emails\"      
        
            if aAttInfo[1] == ""  
                cName += "message"+cvaltochar(ny)+"."+ SubStr( aAttInfo[2], At( "/", aAttInfo[2] ) + 1, Len( aAttInfo[2] ) )  
            else  
                  cName += aAttInfo[1]  
            endif  
       
            conout( "Saving attachment " + cValToChar( nI ) + ": " + cName )          
              
            xRet := oMessage:SaveAttach( nI, cName )  
            if xRet == .F.  
                conout( "Could not save attachment " + cName  )  
                loop  
            endif  
  
            /*cfile := StrTran(AllTrim(aAttInfo[4]), '"', '',,)  
            cStrAtch := Memoread( cBaseName +'\'+ cfile)  
      
            CREATE oXML XMLSTRING cStrAtch*/  
          
    next nI    
next ny  
  
  xRet := oServer:POPDisconnect()  
  if xRet <> 0  
    conout( "Could not disconnect from POP3 server: " + oServer:GetErrorString( xRet ) )  
  endif  
return
```

**Saiba mais**

[ADV0123\_cBody\_em\_Branco\_TMailMessage](https://tdn.totvs.com/display/public/PROT/ADV0123_cBody_em_Branco_TMailMessage)
