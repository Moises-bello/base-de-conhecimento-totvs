---
article_id: 360023098671
category: ADVPL - Web Service
content_hash: 983e98c6f7a40261b688ba5c350e356a0a986d63a5a245b9958866d6a95fb6a4
fetched_at: '2026-06-28T22:40:10.277850+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Incluir registros
  utilizando as APIs
type: support-article
updated_at: '2026-06-24T14:20:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023098671-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Incluir-registros-utilizando-as-APIs
---

**Dúvida**Como consumir as novas *APIs* do Protheus de modo a incluir um novo registro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para consumir as *APIs* do Protheus, recomendamos a classe FwRest(). e para este caso deverá ser utilizado o método *POST*.  
  
**Exemplo**Utilizamos a API de Clientes/Fornecedores como exemplo para inclusão de registro:FONTE

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PARA CONSUMO DO SERVIÇO REST  
User Function T164POST()  
    Local cServer   := "10.172.22.122"                               // URL (IP) DO SERVIDOR  
    Local cPort     := "5085"                                        // PORTA DO SERVIÇO REST  
    Local cURI      := "http://" + cServer + ":" + (cPort + "/rest") // URI DO SERVIÇO REST  
    Local cResource := "/api/crm/v1/customerVendor"                  // RECURSO A SER CONSUMIDO  
    Local oRest     := FwRest():New(cURI)                            // CLIENTE PARA CONSUMO REST  
    Local aHeader   := {}                                            // CABEÇALHO DA REQUISIÇÃO  
  
    // PREENCHE CABEÇALHO DA REQUISIÇÃO  
    AAdd(aHeader, "Content-Type: application/json; charset=UTF-8")  
    AAdd(aHeader, "Accept: application/json")  
    AAdd(aHeader, "User-Agent: Chrome/65.0 (compatible; Protheus " + GetBuild() + ")")  
  
    // INFORMA O RECURSO E INSERE O JSON NO CORPO (BODY) DA REQUISIÇÃO  
    oRest:SetPath(cResource)  
    oRest:SetPostParams(GetJson())  
  
    // REALIZA O MÉTODO POST E VALIDA O RETORNO  
    If (oRest:Post(aHeader))  
        ConOut("POST: " + oRest:GetResult())  
    Else  
        ConOut("POST: " + oRest:GetLastError())  
    EndIf  
Return (NIL)  
  
// CRIA O JSON QUE SERÁ ENVIADO NO CORPO (BODY) DA REQUISIÇÃO  
Static Function GetJson()  
    Local bObject := {|| JsonObject():New()}  
    Local oJson   := Eval(bObject)  
  
    oJson["code"]                               := "CLT024"  
    oJson["branchId"]                           := "01"  
    oJson["name"]                               := "MENIACX IMPORTAÇÕES CORP"  
    oJson["shortName"]                          := "MENIACX CORP"  
    oJson["type"]                               := 1  
    oJson["strategicCustomerType"]              := "F"  
    oJson["address"]                            := Eval(bObject)  
    oJson["address"]["state"]                   := Eval(bObject)  
    oJson["address"]["state"]["stateId"]        := "SP"  
    oJson["address"]["address"]                 := "AVENIDA SOUZA CRUZ"  
    oJson["address"]["city"]                    := Eval(bObject)  
    oJson["address"]["city"]["cityDescription"] := "JARDIM ALVES CARMO"  
Return (oJson:ToJson())
```

JSON

```
{  
    "branchId": "01",  
    "code": "NAIR18",  
    "name": "NAIR02",  
    "shortName": "NAIR02",  
    "type": 1,  
    "strategicCustomerType": "F",  
    "address": {  
        "state": {  
            "stateId": "SP"  
        },  
        "address": "AVENIDA SOUZA CRUZ",  
        "city": {  
            "cityDescription": "JARDIM ALVES CARMO"  
        }  
    }  
}
```

  
**Observação**  
As APIs efetuam o mesmo controle de relacionamento dos dados que as rotinas padrões, assim sendo, qualquer inclusão, alteração ou deleção que possa ferir a integridade dos dados, irá retornar erro.  
  
**Saiba mais**  
[API REFERENCE - TOTVS DEVELOPERS](https://api.totvs.com.br/)  
[FWREST - CLIENT PARA CONSUMO REST](http://tdn.totvs.com/display/framework/FWRest)
