---
content_hash: 910bc1cc0a18fb3bac0528aabd0805a8debe1223752c87b8d628de659258967f
fetched_at: '2026-11-03T14:34:39.976779+00:00'
page_id: resource_MentionServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — MentionServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_MentionServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# MentionServiceRest Resource

Mention

Available Since
:   1.5.0

### GET /mention/findMentions

Return a JSON with a MAP containing the id as key and the fullname as value of the mentioned Social(user or community).

Available Since
:   1.5.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| mentioningClass | query | Class of mentioned REQUIRED |  |
| mentioningId | query | Id of mentioned REQUIRED | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{  	    "content": {  	    "mary": "Mary Jane Olsen"  	} ``` |
