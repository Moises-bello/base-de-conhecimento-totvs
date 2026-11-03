---
content_hash: 6e2b709d1c9403a78b931c73162157d937f28df2ccffb31cf25b6a794d5c61c2
fetched_at: '2026-11-03T14:34:40.360774+00:00'
page_id: resource_TenantRest
product: fluig
source: rest-fluig
title: Fluig REST — TenantRest Resource
type: documentation
url: https://api.fluig.com/old/resource_TenantRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# TenantRest Resource

Tenants - V2

Available Since
:   1.5

### POST /2.0/tenants/create

Create a new Tenant  
  
Create a new community: fill object CommunityCreateVO

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [TenantCreateVO](https://api.fluig.com/old/json_TenantCreateVO.html) (JSON) | Request JSON (example):  ``` {                	"id": 2,                	"code": "2",                	"federalId": "federalId",                	"idpId": "1545fdfs54",                	"description": "2",                	"organizationUrl": "2",                	"volumeDir": "D:\\FLUIG-SYSTEM\\fluig\\repository\\2",                	"idpLogOff": "false",                	"thumbnailEnabled": "true",                	"removeVolume": "false",                	"adminLogin": "admin",                	"adminCode": "admin",                	"adminEmail": "mail@mail.com",                	"adminPassword": "password",                	"adminFirstName": "adminFirstName",                	"adminLastName": "adminLastName",                	"data" : {}                	} ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return CommunityVO object                {                	"content": null,                	"message": {                		"message": "Tenante criado com sucesso!",                		"detail": "Tenante criado com sucesso!",                		"type": "INFO"                	}                } ``` |

Available Since
:   1.5.13

### GET /2.0/tenants/getTenantData/{keys}

Retrieve specific tenant data

Available Since
:   1.5.13

Request Parameters

| name | type | description |
| --- | --- | --- |
| keys | path | Tenant data keys separated by commas |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "key" : String "value" }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |
