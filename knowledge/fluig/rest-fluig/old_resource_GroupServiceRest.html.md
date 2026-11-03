---
content_hash: c30f29e3c787c7220baf4fbab50a2bbbdd9cefd237e4a4470ca7ea72e376c1b4
fetched_at: '2026-11-03T14:34:39.856598+00:00'
page_id: resource_GroupServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — GroupServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_GroupServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# GroupServiceRest Resource

Groups

### GET /wcm/group

Get the groups of the current tenant.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of string (JSON) | Response List (example):  ```  [  	"group1", "group2"  ] ``` |

### GET /wcm/group/findUsingFilter

Find groups using filters

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | Number of results to return | 20 | required |
| offset | query | Search offset | 0 | required |
| orderby | query | Field to order results by example: fullName\_ASC, email\_DESC | description\_ASC |  |
| pattern | query | Pattern to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"groupDescription" : "Group description,  	"login" : null,  	"roleCode" : null,  	"tenantId" : 1,  	"childGroupCode" : null,  	"isCloudDefault" : false,  	"groupType" : "user",  	"description" : "Group description",  	"code" : "Finances",  	"id" : "1",  	"typeCode" : "group",  }] ``` |

### GET /wcm/group/byuser/{genericId}

Get the groups of a given user.

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of string (JSON) | Response List (example):  ```  [  	"group1", "group2"  ] ``` |
