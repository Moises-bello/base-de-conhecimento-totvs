---
article_id: 360022852272
category: ADVPL - Web Service
content_hash: f60b7e426f92f99e7e6da288134c70952260ec630b5178a02f0be1bfcc92809e
fetched_at: '2026-06-28T22:40:10.238179+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Deleção de registro
  utilizando as APIs totvs
type: support-article
updated_at: '2021-05-06T18:04:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022852272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Dele%C3%A7%C3%A3o-de-registro-utilizando-as-APIs-totvs
---

**Dúvida**Como consumir as novas APIs TOTVS de modo a deletar um registro já existente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**Para consumir as APIs TOTVS recomendamos a classe FwRest() e para este caso deverá ser utilizado o método *DELETE*.  
  
**Exemplo**Utilizamos a API de Clientes/Fornecedores como exemplo para deleção de um registro:FONTE

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// FUNÇÃO PARA CONSUMO DO SERVIÇO REST  
User Function T168DELETE()  
    Local cServer   := "10.172.22.122"                               // URL (IP) DO SERVIDOR  
    Local cPort     := "5085"                                        // PORTA DO SERVIÇO REST  
    Local cURI      := "http://" + cServer + ":" + (cPort + "/rest") // URI DO SERVIÇO REST  
    Local cId       := "/1/CLT02401"                                 // ID DO REGISTRO A SER DELETADO  
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
    If (oRest:Delete(aHeader))  
        ConOut("DELETE: " + oRest:GetResult())  
    Else  
        ConOut("DELETE: " + oRest:GetLastError())  
    EndIf  
Return (NIL)
```

  
**Observação**  
As APIs efetuam o mesmo controle de relacionamento dos dados que as rotinas padrões, assim sendo, qualquer inclusão, alteração ou deleção que possa ferir a integridade dos dados, irá retornar erro.  
  
**Saiba mais**  
[API REFERENCE - TOTVS DEVELOPERS](https://api.totvs.com.br/)  
[FWREST - CLIENT PARA CONSUMO REST](http://tdn.totvs.com/display/framework/FWRest)
