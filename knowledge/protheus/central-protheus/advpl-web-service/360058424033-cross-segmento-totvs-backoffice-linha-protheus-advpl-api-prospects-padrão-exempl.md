---
article_id: 360058424033
category: ADVPL - Web Service
content_hash: ed0a0e6b4570d99c3e64ab43b35f507c91950d7ea3bf077734a4a3dc6ec8b1b2
fetched_at: '2026-06-28T22:40:10.155340+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - API Prospects
  padrão: Exemplo do método Post'
type: support-article
updated_at: '2021-05-06T15:05:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058424033-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-API-Prospects-padr%C3%A3o-Exemplo-do-m%C3%A9todo-Post
---

**Dúvida**Você teriam um exemplo da API padrão Prospects no método Post?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão P12

**Solução**Abaixo segue um exemplo.  
API - **/api/crm/v1/Prospects/{Order, Page, PageSize, Fields}**

```
{
    "address": {
        "address": "AV. BRAS LEME, 1020",
        "zipCode": "00000000",
        "state": {
            "stateId": "SP",
            "stateInternalId": "SP"
        },
        "district": "CASA VERDE ",
        "city": {
            "cityCode": "50308",
            "cityDescription": "SAO PAULO"
        },
        "country": {
            "countryCode": "105"
        }
    },
    "ShortName": "TESTE POST",
    "StrategicType": "1",
    "EntityType": "2",
    "marketsegment": {
        "marketSegmentCode": ""
    },
    "RegisterSituation": "2",
    "GovernmentalInformation": [
        {
            "scope": "CNPJ|CPF",
            "id": "78193663000167",
            "name": "CNPJ|CPF",
            "issueOn": "2020-10-15",
            "expiresOn": "2020-10-15"
        }
    ],
    "Code": "POST02",
    "StoreId": "01",
    "InternalInformation": {
        "LastVisit": "    -  -  T00:00:00"
    },
    "CompanyInfo": {
        "Employees": "1",
        "CreditLimitDate": "    -  -  T00:00:00",
        "Annualbilling": 0,
        "CreditLimit": 0,
        "CreditLimitCurrency": 1
    },
    "Name": "TESTE POST API",
    "ProspectSituation": "1"
}
```

**Saiba Mais**[API reference TOTVS](https://api.totvs.com.br/)
