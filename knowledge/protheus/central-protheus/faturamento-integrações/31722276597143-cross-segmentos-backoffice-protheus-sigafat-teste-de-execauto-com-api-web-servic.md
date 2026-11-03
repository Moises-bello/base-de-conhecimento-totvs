---
article_id: 31722276597143
category: Faturamento - Integrações
content_hash: d2017237222c85ca6b0b1d9cfd22f896e8d47e8fb87d1365b290bb8240ef4845
fetched_at: '2026-06-28T22:38:26.530929+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Teste de ExecAuto com API
  (Web Services)
type: support-article
updated_at: '2025-04-29T19:00:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31722276597143-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Teste-de-ExecAuto-com-API-Web-Services
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31722228415639) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como realizar um teste de ExecAuto com API (WS)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

No suporte, testamos o WebServices puro sem customizações:

```
#include "protheus.ch"
#include "totvs.ch"
#include "apwebsrv.ch"


// API para chamar execauto via WS

WSSERVICE wsteste01
WSDATA cumped AS string
WSDATA cRet AS string
WSDATA UserCode AS String

WSMETHOD wsteste
ENDWSSERVICE

WSMETHOD wsteste WSRECEIVE UserCode, cumped WSSEND cRet WSSERVICE wsteste01
U_MyMata410() //função a ser chamada

Return.T.
```

**OBS:** Note que a API chama a função do ExecAuto. No exemplo acima, é a rotina automática do pedido de vendas "U\_MyMata410", ou seja, é necessário que a sua rotina automática esteja compilada.

No lugar do código onde está "U\_MyMata410() //função a ser chamada" deve ser trocado para sua rotina automática desejada
