---
article_id: 360044356974
category: ADVPL - Web Service
content_hash: 6e27853a2a44772bfabc81b6434b2dfc78a4b1c531b3ea2ce634bad6c7516082
fetched_at: '2026-06-28T22:40:10.348100+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -  ADVPL - Requisição para
  refresh do Token JWT Rest
type: support-article
updated_at: '2021-12-20T14:44:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044356974-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Requisi%C3%A7%C3%A3o-para-refresh-do-Token-JWT-Rest
---

**Dúvida**Como Fazer o Refresh do Token JWT ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**

**A atualização do token**

Após a expiração do **token** de acesso, ao tentar requisitar alguma **API** protegida, será retornado o **status 401** de não autorizado, como se não houvesse sido enviado um **token** de acesso.

É o momento então de requisitar para a mesma **API** de **token** a atualização conforme o exemplo abaixo:

```
https://localhost:8081/rest/api/oauth2/v1/token?grant_type=refresh_token&refresh_token=YEv3dtFbNCisITD3yDtKi5/x.T0jkPv12SWK/JjWS0xI01YbIXWM10KWw2ehCxG9yRVkXCiItBYN57Rizh4OH67m7H3-Jd-3ruC4/pBAWBkXVO251HPiS91KAh7FfbZqWaiDPmvYBvoiaP4KRR1gYcvCr9ES7wC3iRA2wQrQvODlH7b3FCTmvHzCVmRMi4eApgy4iOGVpBK7-ryI=.fD77MI4MBk1rW6eBjMq9EutN1ZIC1YKKuKqdEhbLf/k=  
POST /api/oauth2/v1/token  
Host exemplo: https://localhost:8080/rest  
Query Params: ?grant_type=refresh_token&refresh_token=YEv3dtFbNCisITD3yDtKi5/x.T0jkPv12SWK/JjWS0xI01YbIXWM10KWw2ehCxG9yRVkXCiItBYN57Rizh4OH67m7H3-Jd-3ruC4/pBAWBkXVO251HPiS91KAh7FfbZqWaiDPmvYBvoiaP4KRR1gYcvCr9ES7wC3iRA2wQrQvODlH7b3FCTmvHzCVmRMi4eApgy4iOGVpBK7-ryI=.fD77MI4MBk1rW6eBjMq9EutN1ZIC1YKKuKqdEhbLf/k=
```

|  |  |
| --- | --- |
| **Parâmetro** | **Valor** |
| grant\_type | refresh\_token |
| refresh\_token | Token de refresh |

**Reposta da requisição**

Caso o refresh token seja válido, a resposta será retornada no mesmo formato anterior e esse ciclo pode se repetir inúmeras vezes, desde que o tempo de expiração não seja excedido:

```
{     
 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJUT1RWUy1BRFZQTC1GV0pXVCIsInN1YiI6Im1hcmlvIiwiaWF0IjoxNTUzMDIyOTQ0LCJleHAiOjE1NTMwMjY1NDQsInJlc3RyaWN0ZWR0byI6WyJhcGkvcHJvdGhldXMvIiwiYXBpL2ZyYW1ld29yay8iXX0.XsS38RdeJIetwh6Zq2DLQs0PhyLSRxCxOnCgp4SaoeY=",  
 "refresh_token": "YEv3dtFbNCisMST1yztKi5/x.T0jkPv12SWK/JjWS0xI01YbIXWM10KWw2ehCxG9yRVkXCiItBYN57Rizh4OH67m7H3-Jd-3ruC4/pBAWBkXVO251HPiS91KAh7FfbZqWaiDPmvYBvoiaP4KRR1hUct67vFah2VLUSymyfLQtOjltqqzVPkqZMBaVtyVl4c4pxTw4IQtpHw==.tIUbpKC8sWcB6oIMhXcbOhq/bveF216m9gmboBrxJ7U=",  
 "scope": "default",  
 "token_type": "Bearer",  
 "expires_in": 3600  
}
```

**Saiba Mais  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - JSON Web Token (JWT)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044840733)   
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Requisição para Token JWT Rest](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044883213)**
