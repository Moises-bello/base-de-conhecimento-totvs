---
article_id: 360021048151
category: ADVPL - Classe e Função
content_hash: 44d1aed6d6b378af94e98f13af1875b933476f17c5a9747d176476bf2c127edf
fetched_at: '2026-06-28T22:40:17.152989+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Resposta json em
  objeto
type: support-article
updated_at: '2022-06-08T17:59:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021048151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Resposta-json-em-objeto
---

**Dúvida**Como transformar a resposta recebida em um serviço *web* REST em um objeto?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
   
**Solução**Utilize a função FwJSONDeserialize().  
  
**Fonte**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PARA TESTE  
User Function T110FWREST()  
    Local nStart  := Seconds() // HORA DE INÍCIO DA FUNÇÃO  
    Local oJSON   := NIL       // OBJETO JSON QUE RETORNADO PELA FUNÇÃO  
    Local oREST   := NIL       // OBJETO REST PARA GERAÇÃO DE REQUISIÇÃO  
    Local aHeader := {}        // CABEÇALHO DE INFORMAÇÕES DA REQUISIÇÃO  
  
    RPCSetEnv("99", "01") // PREPARAÇÃO DE AMBIENTE (REMOVER SE EXECUTADO VIA SMARTCLIENT)  
        oREST := FwRest():New("https://www.receitaws.com.br/v1/cnpj/53113791000122") // INSTANCIAÇÃO DE OBJETO REST  
  
        // CAMINHO DO RECURSO WEB  
        oREST:SetPath("")  
  
        // INÍCIO DE REQUISIÇÃO GET  
        If (oREST:Get(aHeader))  
            FwJSONDeserialize(oREST:cResult, @oJSON) // DESERIALIZAÇÃO DE STRING PARA OBJETO  
  
            // MENSAGEM DE SUCESSO  
            FwLogMsg("INFO", /*cTransactionId*/, "REST", FunName(), "", "01",;  
                        "JSON successfully parsed to Object", 0, (nStart -Seconds()), {})  
        Else  
            // MENSAGEM DE ERRO  
            FwLogMsg("ERROR", /*cTransactionId*/, "REST", FunName(), "", "01",;  
                        "Can't successfully parse JSON to Object", 0, (nStart - Seconds()), {})  
        EndIf  
    RPCClearEnv() // FECHAMENTO DE AMBIENTE (REMOVER SE EXECUTADO VIA SMARTCLIENT)  
Return (NIL)
```

**Saiba mais**  
[FWJsonDeserialize - Deserializa uma string no formato JSON](http://tdn.totvs.com/display/PROT/FWJsonDeserialize+-+Deserializa+uma+string+no+formato+JSON)
