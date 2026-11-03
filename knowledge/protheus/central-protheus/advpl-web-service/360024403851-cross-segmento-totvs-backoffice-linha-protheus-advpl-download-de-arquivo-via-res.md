---
article_id: 360024403851
category: ADVPL - Web Service
content_hash: f8a2ca1c9099aa551cd5c073c11e2d825ec0d9447b4749c895ae9ff1929042dd
fetched_at: '2026-06-28T22:40:10.352832+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL  - Download de arquivo
  via Rest
type: support-article
updated_at: '2025-01-24T19:04:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024403851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Download-de-arquivo-via-Rest
---

**Dúvida**Como baixar um arquivo da URL (*Uniform Resource Locator*)?   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Utilize a classe FwRest()  
  
Fonte

```
// BIBLIOTECAS NECESSÃRIAS  
#Include "TOTVS.ch"  
  
// BAIXA UM ARQUIVO .PDF DE UMA URL  
User Function T170FILEGET()  
    Local cURL    := "http://www.imt.usp.br"                      // URL DO SERVIÇO  
    Local cPath   := "/wp-content/uploads/comissoes/cipa/NR5.pdf" // RECURSO DA URI  
    Local aHeader := {}                                           // CABEÇALHO DE INFORMAÇÕES DA REQUISIÇÃO  
    Local oRest   := NIL                                          // CLIENTE PARA CONSUMO  
    Local nHandle := 00                                           // CÓDIGO DE SUPORTE AO ARQUIVO  
  
        // INSTANCIA O CLIENTE REST  
        oRest := FwRest():New(cURL)  
  
        // INFORMA O RECURSO E O BODY  
        oRest:SetPath(cPath)  
  
        // ENVIA A REQUISIÇÃO E VALIDA O RESULTADO  
        If (oRest:Get(aHeader))  
            // CRIA O NOME DO ARQUIVO (FUNÇÕES UTILIZADAS PARA EVITAR CONFLITO DE NOME)  
            nHandle := FCreate("\dirdoc\" + StrTran(DToS(Date()) + "_" + Time() + "_DOCUMENT.pdf", ":", ""))  
            FWrite(nHandle, oRest:GetResult())  
            FClose(nHandle)  
  
            // VERIFICA SE O ARQUIVO FOI CRIADO CORRETAMENTE  
            If (!File("\dirdoc\" + cFileName))  
                ConOut("@ADVPL: Couldn't generate *.PDF file")  
            EndIf  
        Else  
            ConOut("@ADVPL: Couldn't consume API")  
        EndIf  
    
Return (NIL)
```

**Saiba mais**  
[FWRest - Cliente para consumo REST](http://tdn.totvs.com/display/framework/FWRest)  
[Upload de arquivos via rest](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020278071)
