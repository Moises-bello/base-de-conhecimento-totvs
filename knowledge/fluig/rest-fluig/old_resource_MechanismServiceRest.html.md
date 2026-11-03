---
content_hash: 626dc26099040e7c060bee401756c94a6e18e08769252db052e45f4c0ab7689f
fetched_at: '2026-11-03T14:34:39.948420+00:00'
page_id: resource_MechanismServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — MechanismServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_MechanismServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# MechanismServiceRest Resource

Mechanisms

### POST /bpm/mechanism/create

Creates a custom attribution mechanism.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AttributionMechanismVO](https://api.fluig.com/old/json_AttributionMechanismVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "custom_mechanism",      //mechanism's id  	"name" : "Custom Mechanism",    //mechanism's name  	"description" : "This is a custom mechanism"    //mechanism's description  	"content" : "function resolve(process,colleague){ var userList = new Array(); userList.push('adm'); userList.push('john');  return userList; }",     //mechanism's function  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /bpm/mechanism/remove

Removes a custom attribution mechanism.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AttributionMechanismVO](https://api.fluig.com/old/json_AttributionMechanismVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "custom_mechanism"      //REQUIRED mechanism's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /bpm/mechanism/update

Update a custom attribution mechanism.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AttributionMechanismVO](https://api.fluig.com/old/json_AttributionMechanismVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "custom_mechanism",      //mechanism's id  	"name" : "New Custom Mechanism",    //mechanism's name  	"description" : "This is a new custom mechanism",    //mechanism's description  	"content" : "function resolve(process,colleague){ var userList = new Array(); userList.push('adm'); userList.push('robert');  return userList; }"     //mechanism's function  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /bpm/mechanism/{id}/{process}

Returns a resolved attribution mechanism.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED mechanism's id |  |
| process | path | process instance number | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of string (JSON) | ```  The user's code list from resolved mechanism ``` |
