---
article_id: 28425036366103
category: ADVPL - Web Service
content_hash: a5fcac28994b3b7a137e774044cd8a291cc4430d3c480beb983953e43ba47fdd
fetched_at: '2026-06-28T22:40:10.569471+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - RESTFUL para
  REST tlppCore
type: support-article
updated_at: '2024-12-17T19:10:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28425036366103-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-RESTFUL-para-REST-tlppCore
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28425007306391)*Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**  
É possível fazer um REST TLPP como em ADVPL?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
Existe a possibilidade do desenvolvimento de REST customizado em TLPP utilizando o annotation do [**REST TlppCore**](https://tdn.totvs.com/pages/viewpage.action?pageId=553337101) no desenvolvimento, conforme o exemplo abaixo.

**Exemplo**:

```
#include "tlpp-core.th"  
#include "tlpp-rest.th"  
  
@Get("/sampleMigrateRestTlpp")  
user function GETsampleMigrateRestTlpp()  
  
local cId := ''  
local cData := ''  
local jPath  
  
jPath := oRest:getQueryRequest()  
if ( jPath <> Nil )  
cId := jPath[ 'id' ]  
if ( valtype(cId) == 'U' )  
cId := ''  
endif  
endif  
  
cData := '{ "METHOD" : "GET" ,"id" : "' + cId + '" }'  
  
oRest:setResponse( cData )  
return
```

**Saiba mais**

[**Migração WsRESTful para REST tlppCore**](https://tdn.totvs.com/pages/viewpage.action?pageId=553337101)  
[**GitHUB**](https://github.com/totvs/tlpp-sample-rest/tree/master/server/migrate-FWrest-2-tlpp)  
**[Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-b%C3%A1sica-REST-do-protheus?source=search)**
