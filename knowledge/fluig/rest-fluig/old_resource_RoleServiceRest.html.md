---
content_hash: 920908cd3e7c0eb573d19a730c0a3754b0c096787ac323fbd9f6838b3053a859
fetched_at: '2026-11-03T14:34:40.113908+00:00'
page_id: resource_RoleServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — RoleServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_RoleServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# RoleServiceRest Resource

Roles

### GET /wcm/role/findUsingFilter

Find roles using filters

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | Number of results to return | 20 | required |
| offset | query | Search offset | 0 | required |
| orderby | query | Field to order results by example: fullName\_ASC, email\_DESC | fullName\_ASC |  |
| pattern | query | Pattern to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"tenantId" : 1,  	"code" : "Administrador",  	"description" : "Administrador"  }] ``` |
