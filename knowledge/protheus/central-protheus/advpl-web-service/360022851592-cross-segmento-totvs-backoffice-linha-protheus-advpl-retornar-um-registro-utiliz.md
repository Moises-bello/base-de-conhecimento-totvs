---
article_id: 360022851592
category: ADVPL - Web Service
content_hash: 9b72691b531ed2ac5fdcb39a2d0f14886762ef3aff4b359957bb4cf4981ba678
fetched_at: '2026-06-28T22:40:10.314572+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Retornar um registro
  utilizando as APIs totvs
type: support-article
updated_at: '2021-05-06T19:06:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022851592-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retornar-um-registro-utilizando-as-APIs-totvs
---

**Dúvida**Como consumir as novas APIs da TOTVS de modo a retornar os dados de apenas um registro já existente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**Para consumir as APIs TOTVS recomendamos a classe FwRest() e para este caso deverá ser utilizado o método GET.  
  
**Exemplo**Utilizamos a API de Clientes/Fornecedores como exemplo para retorno de um registro:FONTE

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PARA CONSUMO DO SERVIÇO REST  
User Function T166GETONE()  
    Local cServer   := "10.172.22.122"                               // URL (IP) DO SERVIDOR  
    Local cPort     := "5085"                                        // PORTA DO SERVIÇO REST  
    Local cURI      := "http://" + cServer + ":" + (cPort + "/rest") // URI DO SERVIÇO REST  
    Local cId       := "/1/CLT02401"                                 // ID DO REGISTRO A SER RETORNADO  
    Local cResource := "/api/crm/v1/customerVendor"                  // RECURSO A SER CONSUMIDO  
    Local oRest     := FwRest():New(cURI)                            // CLIENTE PARA CONSUMO REST  
    Local aHeader   := {}                                            // CABEÇALHO DA REQUISIÇÃO  
  
    // PREENCHE CABEÇALHO DA REQUISIÇÃO  
    AAdd(aHeader, "Content-Type: application/json; charset=UTF-8")  
    AAdd(aHeader, "Accept: application/json")  
    AAdd(aHeader, "User-Agent: Chrome/65.0 (compatible; Protheus " + GetBuild() + ")")  
  
    // INFORMA O RECURSO  
    oRest:SetPath(cResource + cId)  
  
    // REALIZA O MÉTODO GET E VALIDA O RETORNO  
    If (oRest:Get(aHeader))  
        ConOut("GET: " + oRest:GetResult())  
    Else  
        ConOut("GET: " + oRest:GetLastError())  
    EndIf  
Return (NIL)
```

  
**Saiba mais**  
[API REFERENCE - TOTVS DEVELOPERS](https://api.totvs.com.br/)  
[FWREST - CLIENT PARA CONSUMO REST](http://tdn.totvs.com/display/framework/FWRest)
