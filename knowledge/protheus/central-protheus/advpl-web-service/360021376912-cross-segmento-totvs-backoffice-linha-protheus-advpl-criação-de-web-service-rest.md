---
article_id: 360021376912
category: ADVPL - Web Service
content_hash: 38c95073aba62e598ccac20c31aa3a84002eb7d8837ea21d7519cae25ddc236b
fetched_at: '2026-06-28T22:40:10.219896+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Criação de Web
  Service REST
type: support-article
updated_at: '2021-05-06T17:37:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021376912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-Web-Service-REST
---

**Dúvida**

Preciso criar um *WebService* no modelo *REST*, porém, só criei até hoje no modelo *SOAP*.

Vocês teriam algum exemplo e documentação sobre isso?! O que achei no TDN é muito pouco para que possamos fazer um primeiro teste.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
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
  
WsMethod GET Description "Sincronização de dados via GET" WsSyntax "/GET/{method}"  
 WsMethod POST Description "Sincronização de dados via POST" WsSyntax "/POST/{method}"  
 WsMethod DELETE Description "Sincronização de dados via DELETE" WsSyntax "/DELETE/{method}"  
  
End WsRestful  
  
WsMethod GET WsService tstwsrest  
 Local cUser := ''  
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

**Segue alguns Link para auxilio no desenvolvimento Rest**

##### [REST ADVPL](http://tdn.totvs.com/display/framework/REST+ADVPL "REST ADVPL")

[01. Web Services REST/Server](http://tdn.totvs.com/pages/viewpage.action?pageId=75268866)

* [01. Configuração](http://tdn.totvs.com/pages/viewpage.action?pageId=185747842 "01. Configuração")
* [02. Criando uma classe REST](http://tdn.totvs.com/display/framework/02.+Criando+uma+classe+REST "02. Criando uma classe REST")
* [03. Comandos REST](http://tdn.totvs.com/display/framework/03.+Comandos+REST "03. Comandos REST")
* [05. Propriedades REST](http://tdn.totvs.com/display/framework/05.+Propriedades+REST "05. Propriedades REST")
* [06. Funções REST](http://tdn.totvs.com/pages/viewpage.action?pageId=75269476 "06. Funções REST")
* [07. Autenticação HTTP Basic](http://tdn.totvs.com/pages/viewpage.action?pageId=185748452 "07. Autenticação HTTP Basic")
* [08. Autenticação baseada em token](http://tdn.totvs.com/pages/viewpage.action?pageId=465386127 "08. Autenticação baseada em token")
