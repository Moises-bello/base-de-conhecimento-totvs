---
article_id: 360044883213
category: ADVPL - Web Service
content_hash: 835e4325046147ec76978295abc70af526aae29a7692004785aaf76e11805e4e
fetched_at: '2026-06-28T22:40:10.500077+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Requisição para
  Token JWT Rest
type: support-article
updated_at: '2023-11-16T13:40:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044883213-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Requisi%C3%A7%C3%A3o-para-Token-JWT-Rest
---

**Dúvida**Como fazer a requisição do TOKEN JWT no Protheus?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL  – A partir da versão 12  
  
**Solução**Devido ao trafego de usuário e senha para esse **endpoint**, ele é um servido que recomendamos fortemente que seja acessado pelo protocolo seguro https. Caso seja utilizado sem o uso do **SSL**, uma mensagem é impressa no console do servidor a cada requisição que é respondida.  
  
Seus parâmetros são trafegados via **query string,** ou seja, fazem parte da URI conforme exemplo abaixo:

```
https://localhost:8080/rest/api/oauth2/v1/token?grant_type=password&password=senha&username=usuario  
POST /api/oauth2/v1/token  
Host exemplo: https://localhost:8080/rest  
Query Params: ?grant_type=password&password=senha&username=usuário
```

|  |  |
| --- | --- |
| **Parâmetro** | **Valor** |
| **grant\_type** | password |
| **password** | Senha do usuário |
| **username** | Usuário para autenticação |

**Reposta da requisição**

Caso as credenciais sejam válidas, a resposta será retornada no seguinte formato:

```
{  
 "access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJUT1RWUy1BRFZQTC1GV0pXVCIsInN1YiI6Im1hcmlvIiwiaWF0IjoxNTUzMDIyMjYwLCJleHAiOjE1NTMwMjU4NjAsInJlc3RyaWN0ZWR0byI6WyJhcGkvcHJvdGhldXMvIiwiYXBpL2ZyYW1ld29yay8iXX0.jgvejFxPYDchLtj04r7mizRZCerb7xFXhB8Ihk+kFqg=",  
 "refresh_token":"YEv3dtFbNCisITD3yDtKi5/x.T0jkPv12SWK/JjWS0xI01YbIXWM10KWw2ehCxG9yRVkXCiItBYN57Rizh4OH67m7H3-Jd-3ruC4/pBAWBkXVO251HPiS91KAh7FfbZqWaiDPmvYBvoiaP4KRR1gYcvCr9ES7wC3iRA2wQrQvODlH7b3FCTmvHzCVmRMi4eApgy4iOGVpBK7-ryI=.fD77MI4MBk1rW6eBjMq9EutN1ZIC1YKKuKqdEhbLf/k=",  
 "scope":"default",  
 "token_type":"Bearer",  
 "expires_in":3600  
}
```

Token validado no **Debugger** **JWT** **![Screenshot_81.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060413634)****Acesso às API’s REST**De posse então do **access\_token**, basta fazer a requisição à API desejada incluindo no cabeçalho a parâmetro **Authorization** com o valor **Bearer** mais o **token** de acesso.

O tempo padrão de expiração do token é 3600 segundos ou seja 60 minutos, não sendo possível sua alteração.

**Obs**: Existem duas principais formas de autenticação nas API´S REST, Basic via Token.

Quando a chave [security](https://tdn.totvs.com/pages/releaseview.action?pageId=185747842) estiver habilitada, será possível se autenticar das duas formas; não é possível desabilitar uma das opções de autenticação.

**Saiba Mais**  
**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - JSON Web Token (JWT)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044840733)**
