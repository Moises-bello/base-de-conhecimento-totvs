---
article_id: 360045545293
category: ADVPL - Web Service
content_hash: e88112243df165591313f637f2722573fe5fbd64df2713cdb2692bd1f2260d13
fetched_at: '2026-06-28T22:40:10.308075+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Quantidade de
  Registros API USER (TOTVS) '
type: support-article
updated_at: '2021-05-06T18:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045545293-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Quantidade-de-Registros-API-USER-TOTVS
---

**Dúvida**Ao consumir o serviço **RESTfull** de usuários, o mesmo respondeu com apenas 7 usuários.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**

Utilize o parâmetro **pageSize**, assim você pode definir o número de itens a serem exibidos em uma página. 

Por padrão, todos os resultados da consulta são exibidos em uma página. Para definir o parâmetro **pageSize** , você deve passar um valor maior que 0 como argumento de consulta.

```
Exemplo:  
http://localhost:1285/REST/01/api/framework/v1/users?PageSize=15
```

**Saiba Mais:**  
[API REFERENCE - USER](https://api.totvs.com.br/apidetails/User_v1_000.json)
