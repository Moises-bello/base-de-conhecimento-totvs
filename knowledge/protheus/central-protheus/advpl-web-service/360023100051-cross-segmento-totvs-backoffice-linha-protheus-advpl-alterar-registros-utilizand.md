---
article_id: 360023100051
category: ADVPL - Web Service
content_hash: 109301ea1e4e2e394da6491fa966a1651d70411aa9eb5a5a8c606819920d2b53
fetched_at: '2026-06-28T22:40:10.372437+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar registros
  utilizando as APIs '
type: support-article
updated_at: '2024-03-08T19:57:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023100051-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-registros-utilizando-as-APIs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como consumir as novas APIs da TOTVS de modo a alterar um registro já existente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.23  
  
**Solução**Para consumir as APIs TOTVS recomendamos a classe FwRest() e para este caso deverá ser utilizado o método PUT.  
  
**Exemplo**Utilizamos a API de Clientes/Fornecedores como exemplo para alteração de registro:FONTE

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PARA CONSUMO DO SERVIÇO REST  
User Function T165PUT()  
    Local cServer   := "10.172.22.122"                               // URL (IP) DO SERVIDOR  
    Local cPort     := "5085"                                        // PORTA DO SERVIÇO REST  
    Local cURI      := "http://" + cServer + ":" + (cPort + "/rest") // URI DO SERVIÇO REST  
    Local cId       := "/1/CLT02401"                                 // ID DO REGISTRO A SER ALTERADO  
    Local cResource := "/api/crm/v1/customerVendor"                  // RECURSO A SER CONSUMIDO  
    Local oRest     := FwRest():New(cURI)                            // CLIENTE PARA CONSUMO REST  
    Local aHeader   := {}                                            // CABEÇALHO DA REQUISIÇÃO  
  
    // PREENCHE CABEÇALHO DA REQUISIÇÃO  
    AAdd(aHeader, "Content-Type: application/json; charset=UTF-8")  
    AAdd(aHeader, "Accept: application/json")  
    AAdd(aHeader, "User-Agent: Chrome/65.0 (compatible; Protheus " + GetBuild() + ")")  
  
    // INFORMA O RECURSO  
    oRest:SetPath(cResource + cId)  
  
    // REALIZA O MÉTODO PUT, ENVIA O JSON NO CORPO (BODY) E VALIDA O RETORNO  
    If (oRest:Put(aHeader, GetJson()))  
        ConOut("PUT: " + oRest:GetResult())  
    Else  
        ConOut("PUT: " + oRest:GetLastError())  
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
    oJson["address"]["city"]["cityDescription"] := "ALTERADO"  
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
