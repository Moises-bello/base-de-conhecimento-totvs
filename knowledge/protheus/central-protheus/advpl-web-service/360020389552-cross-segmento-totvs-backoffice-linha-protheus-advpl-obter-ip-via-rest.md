---
article_id: 360020389552
category: ADVPL - Web Service
content_hash: a58ad3a4346d8bc4dc5f987dfa7f913ea2ef55b3f7afa5ed1a68f765784739ec
fetched_at: '2026-06-28T22:40:10.296376+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Obter IP via Rest
type: support-article
updated_at: '2024-05-17T14:21:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020389552-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Obter-IP-via-Rest
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23555651057687)*** Tempo aproximado para leitura: **00:03:00 min****Dúvida**E possível identificar um acesso proveniente de um "IP Externo" à rede Local / Sistema Protheus12.1.17, quando utilizado os Métodos: "GET" e/ou "POST" por terceiros?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Até o release 12.1.27  
  
**Solução**A função() retorna um array com as informações, enviadas no cabeçalho da requisição, as quais o servidor REST Protheus utiliza. Dentre estas informações, está o endereço IP da requisição, acessível diretamente por **HTTPHEADER('\_\_IPCONN\_\_')**.

Esta somente funciona até **12.1.27** utilizando **Rest AdvPL.**

A seguir, o exemplo de uma API simples:

```
#INCLUDE "TOTVS.CH"  
#INCLUDE "RESTFUL.CH"  
  
WSRESTFUL TGETSEC DESCRIPTION "Exemplo de serviço REST"  
   
WSMETHOD GET DESCRIPTION "Teste GET" WSSYNTAX "/_TGETSEC || /_TGETSEC/{id}"   
   
END WSRESTFUL  
  
WSMETHOD GET WSSERVICE TGETSEC  
Local cIpConn  
  
cIpConn := HTTPHEADER('__IPCONN__')  
  
::SetResponse(EncodeUtf8('Requisição recebida do endereço: ' + cIpConn))  
  
Return .T.
```

Para conseguir o IP da requisição para o **Rest 2.0** deve utilizar o método getClientIp() no objeto oRest.

A seguir exemplo:

```
#include 'PROTHEUS.CH'  
#include 'TOTVS.CH'  
#include 'RESTFUL.CH'  
#include 'RWMAKE.CH'  
#include 'TOPCONN.CH'  
#Include "FWMVCDEF.CH"  
  
WSRESTFUL EXECTST DESCRIPTION "TESTE"  
WSMETHOD GET DESCRIPTION "TESTE" WSSYNTAX "/EXECTST"  
END WSRESTFUL  
  
WSMETHOD GET WSSERVICE EXECTST  
local cClientIP as character  
  
cClientIP := oRest:getClientIP()  
cResponse := "{'Client IP':" + cClientIP + "}"  
  
oRest:SetResponse(cResponse)  
Return
```

**Observação:**   
[oRest:getClientIP](https://tdn.totvs.com/display/tec/oRest%3AgetClientIP)  
[Entendendo as novidades do REST 2.0](https://tdn.totvs.com/display/framework/Entendendo+as+novidades+do+REST)
