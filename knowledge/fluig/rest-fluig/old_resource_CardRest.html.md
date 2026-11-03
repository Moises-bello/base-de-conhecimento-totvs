---
content_hash: 291f754760b873142a271bcda99e842b6c271c9b9e7b77c769b6dbb6f3c81e29
fetched_at: '2026-11-03T14:34:39.420281+00:00'
page_id: resource_CardRest
product: fluig
source: rest-fluig
title: Fluig REST — CardRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CardRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CardRest Resource

Cards

Available Since
:   1.5

### POST /2.0/cards/create

Create card instances

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CardCreateVO](https://api.fluig.com/old/json_CardCreateVO.html) (JSON) | Request JSON (example):`{ "documentDescription": "newcard", "parentDocumentId": 6, "version": 1000, "inheritSecurity": false, "attachments": [ { "absoluteFileName": "fig.png", "principal": false, "attach": true, "fileName": "fig.png" } ], "formData": [ { "name": "nome", "value": "john doe" }, { "name": "fone", "value": "5555555" }, { "name": "idade", "value": 11 } ], * "permissions": [ * { * "securityLevel": 3, * "securityVersion": true, * "inheritSecurity": false, * "downloadEnabled": false, * "showContent": true, * "attributionDescription": "user user", * "attributionType": 1, * "attributionValue": "user" * } * ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": null, "message": { "message": "Card criado com sucesso!", "detail": "Card criado com sucesso!", "type": "INFO" } }` |
