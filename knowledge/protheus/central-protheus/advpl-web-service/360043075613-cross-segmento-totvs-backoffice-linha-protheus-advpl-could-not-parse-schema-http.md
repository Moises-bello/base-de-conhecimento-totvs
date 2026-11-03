---
article_id: 360043075613
category: ADVPL - Web Service
content_hash: 7d2b67625c195b5f1da4a45c0962a284ca31ba611d39287a57678b8062baaf20
fetched_at: '2026-06-28T22:40:10.211261+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Could not parse
  schema http://schemas.xmlsoap.org/wsdl/
type: support-article
updated_at: '2022-04-29T21:43:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043075613-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Could-not-parse-schema-http-schemas-xmlsoap-org-wsdl
---

**Ocorrência**Ao realizar uma requisição **SOAP** com a classe**TWsdlManager**  e utilizando o método **ParseURL,**em ambiente local funciona corretamente, porémem ambiente **cloud(Totvs),** sempre retorna o erro abaixo:

```
An exception occurred ar 1:0 WsdlParser Exception: Could not parse schema http://schemas.xmlsoap.org/wsdl/ 
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
 **Causa**Esse incidente ocorre, pois a parametrização do ambiente está incorreta e na maioria das vezes os protocolos necessários para a requisição não estão liberados.  
  
**Solução**  
Para solucionar essa ocorrência, libere os protocolos **TCP****\ HTTP \ SOAP** no ambiente cloud em questão.
