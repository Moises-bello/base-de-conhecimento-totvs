---
content_hash: 4e19b739fd4c0bfd07c0331bd554ade47b868d2b332ffed29e7ab9524b25f79b
fetched_at: '2026-11-03T14:34:40.333548+00:00'
page_id: resource_TagsCloudRest
product: fluig
source: rest-fluig
title: Fluig REST — TagsCloudRest Resource
type: documentation
url: https://api.fluig.com/old/resource_TagsCloudRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# TagsCloudRest Resource

Tags

Available Since
:   1.5.12

### POST /2.0/tags

Performs a search of the most popular tags

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SearchTagsCloudVO](https://api.fluig.com/old/json_SearchTagsCloudVO.html) (JSON) | REQUIRED Request JSON (example):`{ "communitiesAlias": ["alias1", "alias2"], //List of community's alias "maxDays": "60", //Periods in days "limit": "50" //Limit of results }` |
| application/xml | [searchTagsCloudVO](https://api.fluig.com/old/xml_ns0_searchTagsCloudVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ content: { "Lorem": 27, "porro": 30, "quisquam": 1, "est": 28, "qui": 45, "dolorem": 15, "ipsum": 31, "quia": 39, "dolor": 5, "sit": 60, "amet": 28, "consectetur": 27 }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |
