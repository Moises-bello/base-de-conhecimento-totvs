---
content_hash: ffcc2848b97d68e91f106feba748be5537423271be5033d9d3c0a8a1920447ae
fetched_at: '2026-11-03T14:34:39.409747+00:00'
page_id: resource_AuthorizeClientRest
product: fluig
source: rest-fluig
title: Fluig REST — AuthorizeClientRest Resource
type: documentation
url: https://api.fluig.com/old/resource_AuthorizeClientRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# AuthorizeClientRest Resource

Authorize

Available Since
:   1.5.10

### POST /2.0/authorize/client/invoke

Invoke a service with oauth authentication  
  
Invoke a service with oauth authentication: fill object OAuthServiceInvokeVO

Available Since
:   1.5.10

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AuthorizeClientVO](https://api.fluig.com/old/json_AuthorizeClientVO.html) (JSON) | Request JSON (example):`{ serviceCode: 'serviceCode', tenantCode: 'totvs', endpoint: '/api/public/2.0/oauth/invoke', method: 'get', params:{ param1: { key: 'code', type: 'formParam', value: '123456' }, param2: { key: 'description', type: 'queryParam', value: 'description' } } }` |
| application/xml | [authorizeClientVO](https://api.fluig.com/old/xml_ns0_authorizeClientVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "code": null, "method": "Zendesk", "endpoint": "Serviço Zendesk", "params": "param" "result": "json result" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.10

### GET /2.0/authorize/client/test

Invoke a service with oauth authentication  
  
Invoke a service with oauth authentication: fill object OAuthServiceInvokeVO

Available Since
:   1.5.10

Request Parameters

| name | type | description |
| --- | --- | --- |
| serviceCode | query |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "id": null, "serviceCode": "Zendesk", "tenantCode": "totvs", "description": "Serviço Zendesk", "result": "param" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |
