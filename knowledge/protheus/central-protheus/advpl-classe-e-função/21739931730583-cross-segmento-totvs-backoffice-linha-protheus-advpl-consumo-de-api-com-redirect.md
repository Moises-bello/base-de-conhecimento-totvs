---
article_id: 21739931730583
category: ADVPL - Classe e Função
content_hash: 7b5f533af9c23691056203b42af0098466215fc1a6a8ad6c91e882f2be967a7f
fetched_at: '2026-06-28T22:40:18.264208+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Consumo de API com
  redirect
type: support-article
updated_at: '2024-03-01T17:55:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21739931730583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-API-com-redirect
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21739931715095) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Existe alguma função para consumo de API com redirect?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Soluções**

Atualmente não existe função ou método específico para fazer o redirect no consumo ou deixá-lo automático, todavia é possível capturar o retorno do header da requisição e refazê-la assim efetuando o redirect de forma manual.

**Exemplo**

```
#include 'PROTHEUS.CH'  
#include "tlpp-core.th"  
#include "tlpp-rest.th"  
  
user function cgettst1()  
  
Local cUrl := 'https://suaapi.com.br'  
Local oRestClient := FWRest():New(cUrl)  
Local aHeader := {}  
Local aHead := {}  
Local cLink  
Local nTam  
Local cPath  
Local cRet :=""  
Local cRet1 :=""  
Private oJson  
  
aAdd(aHeader, "Content-Type: application/xml; charset=UTF-8" )  
aAdd(aHeader, "Accept: application/xml" )  
aAdd(aHeader, "Authorization:")  
aAdd(aHeader, "x-Authorization-Encrypted-Data: ")  
aAdd(aHeader, "x-Authorization-Raw-Data: ")  
  
oRestClient:setPath("/seu path")  
  
//Primeira requisição  
If oRestClient:Get(aHeader)  
cRet:=("GET",oRestClient:GetResult())  
Else  
ConOut("GET", oRestClient:GetLastError())  
EndIf  
  
cLink:= oRestClient:getHeader("Location") //Pega o link para realizar a seguda requisição  
  
//Monta o header para a segunda requisição  
aAdd(aHead, "content-length:" +FwCutOff(oRestClient:getHeader("content-length")))  
aAdd(aHead, "cache-control:" +FwCutOff(oRestClient:getHeader("cache-control")))  
aAdd(aHead, "pragma:" +FwCutOff(oRestClient:getHeader("pragma")))  
aAdd(aHead, "expires:" +FwCutOff(oRestClient:getHeader("expires")))  
aAdd(aHead, "x-request-id:" +FwCutOff(oRestClient:getHeader("x-request-id")))  
aAdd(aHead, "x-newrelic-app-data:"+FwCutOff(oRestClient:getHeader("x-newrelic-app-data")))  
aAdd(aHead, "x-aspnet-version:" +FwCutOff(oRestClient:getHeader("x-aspnet-version")))  
aAdd(aHead, "x-powered-by:" +FwCutOff(oRestClient:getHeader("x-powered-by")))  
aAdd(aHead, "strict-transport-security:"+FwCutOff(oRestClient:getHeader("strict-transport-security")))  
  
//tratamento do link para efetuar requisição  
nTam := Len(cLink)  
cPath := Right( cLink , ntam-36)  
cPath := FwCutOff(cPath)  
cLink := left(cLink,36)  
  
//Limpa o objeto e instancia novamente a classe  
Freeobj(oRestClient)  
oRestClient := FWRest():New(cLink)  
oRestClient:setpath(cPath)  
  
If oRestClient:Get(aHead)  
cRet:=("GET",oRestClient:GetResult())  
lRet:= GzStrDecomp( cRet, Len(cRet), @cRet1 ) //descompacta o gzip retornado para apresentar o XML  
Else  
ConOut("GET", oRestClient:GetLastError())  
EndIf  
  
RETURN
```

**Saiba Mais**

[FWRest](https://tdn.totvs.com/display/public/framework/FWRest)

[FwCutOff](https://tdn.totvs.com/display/public/framework/FwCutOff)
