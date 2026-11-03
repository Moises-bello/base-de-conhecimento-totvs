---
article_id: 360034668313
category: ADVPL - Web Service
content_hash: f15f1a1518b9ee180b85ead45bc9fb0015d89150737326fa1275bb123d13654e
fetched_at: '2026-06-28T22:40:10.413684+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Consumo de web services
  com totvs http broker
type: support-article
updated_at: '2022-03-28T13:21:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034668313-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consumo-de-web-services-com-totvs-http-broker
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Após a migração para o T-*Cloud*, nossas customizações de integração com os *web services* Protheus (tanto os fontes em ADVPL, quanto nas demais linguagens de mercado) pararam de funcionar.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Causa**Esta inconsistência ocorre porque na primeira requisição, mesmo que retornado um código 200, o conteúdo da requisição não é enviado, mas sim, uma orientação falando que o sistema está utilizando o TOTVS *Broker* HTTP + *cookie* para requisição.  
  
**Solução**Dado o fato do TOTVS *Broker* HTTP trabalhar com diversas instancias como *slave*, na primeira requisição é enviado um *cookie* para "amarrar" a sessão do requisitante à um *slave* específico (TOTVS\_PROXY\_SH\_001).  
Desta forma, torna-se necessário o envio do *cookie* na segunda requisição para o correto retorno dos dados.  
  
**Exemplo**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
//------------------------------------------------------  
// REALIZA CONSUMO EM SERVIÇOS QUE UTILIZAM BROKER HTTP  
//------------------------------------------------------  
User Function T225BROKER()  
    Local aHeader   := {}        // CABEÇALHO  
    Local oRest     := RestDef() // CLIENTE DE REQUISIÇÃO  
    Local cResponse := Space(0)  // RESPOSTA  
    Local cCookie   := Space(0)  // COOKIE PARA ENVIO  
  
    // DEFINE O RETORNO OBRIGATÓRIO DO SERVIÇO  
    AAdd(aHeader, "Content-Type: application/json")  
  
    // REALIZA O PRIMEIRO POST  
    If (oRest:Post(aHeader))  
        // VERIFICA SE FOI ENVIADO ALGO NA RESPOSTA DA REQUISIÇÃO  
        If (Len(oRest:oResponseH:aHeaderFields) > 0)  
            // CASO TENHA SIDO ENVIADO, ENCONTRA O CONTEÚDO DE SET-COOKIE  
            cCookie := oRest:oResponseH:aHeaderFields[AScan(oRest:oResponseH:aHeaderFields, {|x| Upper(AllTrim(x[1])) == "SET-COOKIE"})][2]  
  
            // EXTRAI APENAS O COOKIE DO CABEÇALHO DE RETORNO  
            cCookie := StrTokArr2(cCookie, ";", .F.)[1]  
  
            // ADICIONA O COOKIE NO CABEÇALHO DA NOVA REQUISIÇÃO  
            AAdd(aHeader, "Cookie: " + EncodeUTF8(cCookie))  
            oRest := RestDef()  
   
            // REALIZA O SEGUNDO POST  
            If (oRest:Post(aHeader))  
                cResponse := oRest:GetResult()  
            Else  
                cResponse := oRest:GetLastError()  
            EndIf  
        EndIf  
    Else  
        cResponse := oRest:GetLastError()  
    EndIf  
Return (NIL)  
  
//------------------------------------------------------  
// GERA UM CLIENTE DE REQUISIÇÃO PRONTO DA EXECUÇÃO  
//------------------------------------------------------  
Static Function RestDef()  
    Local cURI  := "http://minhaempresaqui.protheus.cloudtotvs.com.br:4050/rest" // URL DO SERVIÇO  
    Local cPath := "/fornecedor"                                                 // RECURSO SOLICITADO  
    Local oRest := FwRest():New(cURI)                                            // CLIENTE DE REQUISIÇÃO  
  
    // DEFINE O RECURSO E O CORPO DA REQUISIÇÃO (BODY)  
    oRest:SetPath(cPath)  
    oRest:SetPostParams(JsonDef())  
Return (oRest)  
  
//------------------------------------------------------  
// REALIZA A MONTAGEM DO JSON DO CORPO DA REQUISIÇÃO  
//------------------------------------------------------  
Static Function JsonDef()  
    Local bJson := {|| JsonObject():New()} // OBJETO DE MACROEXECUÇÃO  
    Local oJson := Eval(bJson)             // JSON DO CORPO DA REQUISIÇÃO (BODY)  
  
    // VETOR DE CAMPOS  
    oJson["fornecedor"] := {}  
  
    // CAMPOS DO VETOR  
    AAdd(oJson["fornecedor"], Eval(bJson))  
    oJson["fornecedor"][Len(oJson["fornecedor"])]["field"] := "A2_COD"  
    oJson["fornecedor"][Len(oJson["fornecedor"])]["value"] := "000001"  
  
    AAdd(oJson["fornecedor"], Eval(bJson))  
    oJson["fornecedor"][Len(oJson["fornecedor"])]["field"] := "A2_LOJA"  
    oJson["fornecedor"][Len(oJson["fornecedor"])]["value"] := "01"  
  
    /* DEMAIS INFORMAÇÕES DO JSON AQUI */  
Return (oJson:ToJson())
```

  
**Saiba mais**  
[Broker HTTP - Detalhes do balanceamento](http://tdn.totvs.com/display/tec/Detalhes+do+balanceamento)

[MP - ADVPL - Erro: Host not found em consumo REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022591872)
