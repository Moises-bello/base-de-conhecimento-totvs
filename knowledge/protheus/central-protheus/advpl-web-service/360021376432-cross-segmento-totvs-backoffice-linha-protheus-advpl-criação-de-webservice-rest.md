---
article_id: 360021376432
category: ADVPL - Web Service
content_hash: 0417a8ccee4b30b5b311a074fdeeb20d3260ff82fede278a15e0ea35f5f06622
fetched_at: '2026-06-28T22:40:10.419411+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criação de WebService
  Rest
type: support-article
updated_at: '2021-12-29T14:09:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021376432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-WebService-Rest
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Preciso criar um *WebService* no modelo *REST*, porém, só criei até hoje no modelo *SOAP*.

Vocês teriam algum exemplo e documentação sobre isso?! O que achei no TDN é muito pouco para que possamos fazer um primeiro teste.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Exemplo de Criação de um WS utilizando a Tecnologia Rest

```
#include "PROTHEUS.ch"
#include "RESTFUL.ch"

#xtranslate @{Header <(cName)>} => ::GetHeader( <(cName)> )
#xtranslate @{Param <n>} => ::aURLParms\[ <n> \]
#xtranslate @{EndRoute} => EndCase
#xtranslate @{Route} => Do Case
#xtranslate @{When <path>} => Case NGIsRoute( ::aURLParms, <path> )
#xtranslate @{Default} => Otherwise

Static aUsers := {{'1','Oscar','27'},{'2','Luana','40'},{'3','Kaua','25'}}

WsRestful tstwsrest Description "WebService REST para testes"

    WsMethod GET Description "Sincronização de dados via GET"       WsSyntax "/GET/{method}"
    WsMethod POST Description "Sincronização de dados via POST"     WsSyntax "/POST/{method}"
    WsMethod DELETE Description "Sincronização de dados via DELETE" WsSyntax "/DELETE/{method}"

End WsRestful

WsMethod GET WsService tstwsrest
	Local cUser  := ''
    Local nUser

    ::SetContentType( 'application/json' )

    @{Route}
        @{When '/users'}
            cUser := '['
            For nUser := 1 to Len(aUsers)
                cUser += '{"id":'+ aUsers[nUser][1]+;
			    ',"name":"'+aUsers[nUser][2]+;
			    '","age":'+aUsers[nUser][3]+'}'
                cUser += if(nUser < Len(aUsers),',','')
            Next nUser
            cUser += ']'
            ::SetResponse(cUser)
        @{When '/users/{id}'}
            nUser := aScan(aUsers,{|x| x[1] == @{Param 2} })
            If nUser > 0
                cUser := '{"id":'+ aUsers[nUser][1]+;
                            ',"name":"'+aUsers[nUser][2]+;
                            '","age":'+aUsers[nUser][3]+'}'
                ::SetResponse(cUser)
            Else
                SetRestFault(400,'Ops')
                Return .F.
            EndIf
        @{Default}
            SetRestFault(400,"Ops")
            Return .F.    
	@{EndRoute}

Return .T.

WsMethod POST WsService tstwsrest
    Local cJson := ::GetContent()
    Local oParser
    Local cUser, nUser

    ::SetContentType( 'application/json' )

    @{Route}
        @{When '/user'}
            If FwJsonDeserialize(cJson,@oParser)
                aAdd(aUsers,{cValToChar(oParser:id),oParser:name,cValToChar(oParser:age)})
                nUser := Len(aUsers)
                cUser := '{"id":'+ aTail(aUsers)[1]+;
                            ',"name":"'+aUsers[nUser][2]+;
                            '","age":'+aUsers[nUser][3]+'}'
                ::SetResponse(cUser)
            Else
                SetRestFault(400,'Ops')
                Return .F.
            EndIf
        @{Default}
            SetRestFault(400,"Ops")
            Return .F.
    @{EndRoute}
Return .T.

WsMethod DELETE WsService tstwsrest
    Local nUser
    ::SetContentType( 'application/json' )

    @{Route}
        @{When '/user/{id}'}
            nUser := aScan(aUsers,{|x| x[1] == @{Param 2} })
            If nUser > 0
                aDel(aUsers, nUser)
                aSize(aUsers, Len(aUsers) - 1)
            Else
                SetRestFault(400,"Ops")
                Return .F.
            EndIf
        @{Default}
            SetRestFault(400,"Ops")
            Return .F.
    @{EndRoute}
Return .T.
```
