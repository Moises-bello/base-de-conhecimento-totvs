---
article_id: 360057780753
category: ADVPL - Classe e Função
content_hash: c58f1a71f76fa94eb9c14d6e705d3bfc6bb3e385fd59a6ba3a2dc8abb53eb38d
fetched_at: '2026-06-28T22:40:15.471521+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe WSCLIENT
  para SOAP: Passar autenticação '
type: support-article
updated_at: '2022-01-04T20:34:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057780753-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-WSCLIENT-para-SOAP-Passar-autentica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Na classe  WSCLIENT(), é possível ativar a chave **authorization** no http header?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para informar a **autenticação** ou qualquer outro conteúdo do **header** da requisição **SOAP**, é possível utilizar da **propriedade *\_HEADOUT*.**  
Abaixo um exemplo de como enviar uma requisição com a autenticação do tipo *BASIC*:

```
#include "protheus.ch"  
  
// ----------------------------------------------------------------------  
/*/{Protheus.doc} soapBasic  
Exemplo de requisição SOAP com autenticação BASIC  
  
@author Daniel Mendes  
@since 14/10/2020  
@version 1.0  
/*/  
// ----------------------------------------------------------------------  
user function soapBasic()  
local oDictionary as object  
local nLoop as numeric  
  
oDictionary := WSFWDICTIONARY():New()  
  
if oDictionary:_HEADOUT == nil  
oDictionary:_HEADOUT := {}  
endif  
  
aAdd(oDictionary:_HEADOUT, "Authorization: Basic " + Encode64("admin:1"))  
  
oDictionary:cTABLEFILTER := "SED"  
oDictionary:GETTABLELIST()  
  
for nLoop := 1 to Len(oDictionary:oWSGETTABLELISTRESULT:cString)  
ConOut(oDictionary:oWSGETTABLELISTRESULT:cString[nLoop])  
next  
  
FreeObj(oDictionary)  
oDictionary := nil  
  
return
```

**Saiba mais**[WSCLIENT](https://tdn.totvs.com/display/tec/WSCLIENT)
