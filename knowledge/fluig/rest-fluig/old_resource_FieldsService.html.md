---
content_hash: 24e331fc60755a11187ebb8b8720287b09f6c391348c749e723e9bfd36c1044b
fetched_at: '2026-11-03T14:34:39.787798+00:00'
page_id: resource_FieldsService
product: fluig
source: rest-fluig
title: Fluig REST — FieldsService Resource
type: documentation
url: https://api.fluig.com/old/resource_FieldsService.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# FieldsService Resource

Central Tasks FilterFields Services

### GET /ecm/filters/{filterId}/fields

Returns the fields of a given a filter.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| filterId | path | REQUIRED filter's id. | regex: \d+ |
| type | query |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"id" : "10",					// field id  	"key" : "some-key",			// field key  	"value" : "some-value" 		// field value  } ``` |

### GET /ecm/filters/{filterId}/fields/{id}

Returns a specific field of a specific filter

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| filterId | path | REQUIRED filter's id. | regex: \d+ |
| id | path | REQUIRED filter field's id. | regex: \d+ |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"id" : "10",					// field id  	"key" : "some-key",			// field key  	"value" : "some-value" 		// field value  } ``` |
