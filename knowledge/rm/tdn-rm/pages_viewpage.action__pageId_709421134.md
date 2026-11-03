---
content_hash: 56058ec8862d55d30dca555c0bd78c961a0abce7f2f37429b2608a640ff6cc03
fetched_at: '2026-06-29T00:11:25.495622+00:00'
page_id: '709421134'
product: rm
source: tdn-rm
title: API de Medição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=709421134
version: 6
---

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API para inserção de Medição.

# 1 - API de Medição

---

Esta API permitirá a entrada de valores da medição da quantidade dos serviços que já foram executados no período selecionado. 

**Máscara de Url: <http://localhost:8051/api/construction-projects/v1/contract-measure-input>**

Irá retornar o mesmo JSON e uma lista de avisos que não provocaram erros:

**Método de entrada:** Post

falseExemplo de JSon de entradaVer JSON...

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | Exemplo de API: {   "companyId": 1,   "projectId": 2,   "contractId": 33,   "period": "0002",   "cities":[       {         "stateCode": "RO",          "cityCode": "00015",          "value": 20,         "products":[             {                 "value": 20,                  "measurements":[                     {                         "companyId": 1,                         "projectId": 2,                         "contractId": 33,                         "itemId": 182,                         "value": 20,                           "tasks":[    {                                 "companyId": 1,                                 "projectId": 2,                                 "taskId": 5,                                 "value": 20                             }                            ]                     }                 ]             }         ]         },       {         "value": 10,         "products":[             {                 "value": 10,                  "measurements":[                     {                         "companyId": 1,                         "projectId": 2,                         "contractId": 33,                         "itemId": 182,                         "value": 10,                           "tasks":[    {                                 "companyId": 1,                                 "projectId": 2,                                 "taskId": 5,                                 "value": 10                             }                            ]                     }                 ]             }         ]         }     ] } |
