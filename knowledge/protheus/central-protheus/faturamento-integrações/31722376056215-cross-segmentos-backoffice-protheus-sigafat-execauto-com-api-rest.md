---
article_id: 31722376056215
category: Faturamento - Integrações
content_hash: b58076e7b84f99ec286fe271ce288bb5844c25a6b9374a0041381ff5868b2598
fetched_at: '2026-06-28T22:38:26.479448+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - ExecAuto com API (REST)
type: support-article
updated_at: '2025-04-29T19:02:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31722376056215-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-ExecAuto-com-API-REST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31722430730903) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como realizar um teste de ExecAuto com API (RESTful)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

No suporte, testamos a API REST pura sem customizações:

```
#INCLUDE 'PROTHEUS.CH'
#INCLUDE 'TOTVS.CH'
#INCLUDE 'RESTFUL.CH'
#INCLUDE 'RWMAKE.CH'
#INCLUDE 'TOPCONN.CH'
#INCLUDE "FWMVCDEF.CH"



// API para chamar execauto via REST

WSRESTFUL EXECTST2 DESCRIPTION "TESTE"
    WSMETHOD GET DESCRIPTION "TESTE" WSSYNTAX "/EXECTST"
END WSRESTFUL

WSMETHOD GET WSSERVICE EXECTST2
    U_MyMata410() //Função a ser chamada
Return
```

**OBS:** Note que a API chama a função do ExecAuto. No exemplo acima, é a rotina automática do pedido de vendas "U\_MyMata410", ou seja, é necessário que a sua rotina automática esteja compilada.

No lugar do código onde está "U\_MyMata410() //função a ser chamada" deve ser trocado para sua rotina automática desejada
