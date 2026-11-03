---
content_hash: 3221f9fa471917b50744ab69b68409d3b34ba1267c93467a583f37a41d576a9f
fetched_at: '2026-11-03T14:34:40.125412+00:00'
page_id: resource_SearchRest
product: fluig
source: rest-fluig
title: Fluig REST — SearchRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SearchRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SearchRest Resource

Search

Available Since
:   1.5.13

### POST /2.0/search

Perform the new search, returning grouped documents

Available Since
:   1.5.13

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SearchVo](https://api.fluig.com/old/json_SearchVo.html) (JSON) | Request JSON (example):`{ "searchType" : "GLOBAL", // REQUIRED - Types: GLOBAL, USER, COMMUNITY, DOCUMENT, PROCESS, POST, FORM, TAG, WORD "pattern" : "cloud", // REQUIRED - Supports hash tags searches "startPeriod" : "2014-01-30", // Search start date (optional parameter) "endPeriod" : "2014-01-30", // Search end date (optional parameter) "period" : "LAST_HOUR", // Gaps: LAST_HOUR, LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR (optional parameter) // *the parameter period override the startPeriod and endPeriod parameters "ordering" : "RELEVANT", // Orderings: RELEVANT, NEWEST, OLDEST - Default value: RELEVANT "limit" : "2", // Limit of results - Default value: 10 "offset" : "0" // Result offset (optional parameter) - Default value: 0 }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "timeElapsed": 489, "totalHits": 5, "offset": 10, "items" : [{ "DOCUMENT" : [{ "id": "12", "name" : "relatorio cloud.pdf", "createDate" : "2016-11-17 08:12:32", "lastUpdateDate" : "2016-11-17 08:12:33" },{ "id": "28", "name" : "normas de cloud computing.doc", "createDate" : "2016-06-27 11:52:34", "lastUpdateDate" : "2016-08-17 09:32:13" }],{ "POST" : [{ "id": "22", "name" : "Reunião de planejamento da equipe de CLoud Computing ", "createDate" : "2016-11-17 08:12:32", "lastUpdateDate" : "2016-11-17 08:12:33" },{ "id": "38", "name" : "Bom dia. Meu ambiente no cloud está indisponível. Podem verificar?", "createDate" : "2016-06-27 11:52:34", "lastUpdateDate" : "2016-08-17 09:32:13" }],{ "COMMUNITY" : [{ "id": "02", "name" : "Cloud Computing", "createDate" : "2016-11-17 08:12:32", "lastUpdateDate" : "2016-11-17 08:12:33" }]} ] }` |

Available Since
:   1.5.13

### GET /2.0/search/findInfluencers

Find influencer users in a specific topic.

Available Since
:   1.5.13

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit | 10 | int |
| offset | query | offset | 0 | int |
| ordering | query | REQUIRED ordering must be RELEVANT |  |  |
| pattern | query | REQUIRED pattern |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content" : { "timeElapsed": 489, "totalHits": 28, "offset": 10, "items" : [{ "DOCUMENT" : 1, "COMMENT" : 2, "POST" : 13, "total" : 16, "alias" : "jose.silva", "fields" : { "DocumentType" : "INFLUENCERS" }, { "DOCUMENT" : 1, "COMMENT" : 2, "POST" : 9, "total" : 12, "alias" : "gabriela.schrader", "fields" : { "DocumentType" : "INFLUENCERS" } }}] } }` |

Available Since
:   1.5.13

### POST /2.0/search/groupedSearch

Perform a search by pattern and return grouped results

Available Since
:   1.5.13

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SearchVo](https://api.fluig.com/old/json_SearchVo.html) (JSON) | Request JSON (example):`{ "pattern" : "cloud", // REQUIRED - Supports hash tags searches "limit" : "2", // Limit of results - Default value: 10 "offset" : "2", // Result offset (optional parameter) - Default value: 0 "ordering" : "RELEVANT" // Orderings: RELEVANT, NEWEST, OLDEST - Default value:RELEVANT }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `[{ "DOCUMENT" : { "timeElapsed": 489, "totalHits": 23, "offset": 10, "hasMore": true, "infoList" : [{ "fields" : { "DocumentId" : "23", "DocumentName" : "Cloud computing.pdf", "DocumentCreateDate" : "20/02/2016", "DocumentDescription" : "Description" },{ "fields" : { "DocumentId" : "15", "DocumentName" : "Cloud normas.pdf", "DocumentCreateDate" : "30/01/2016", "DocumentDescription" : "Description of document" } }}] },{ "POST" : { "timeElapsed": 234, "totalHits": 8, "offset": 10, "hasMore": false, "infoList" : [{ "fields" : { "DocumentId" : "123", "DocumentName" : "Pesssoal, reunião de cloud foi remarcada.", "DocumentCreateDate" : "23/04/2016" },{ "fields" : { "DocumentId" : "15", "DocumentName" : "Dúvidas sobre Cloud?", "DocumentCreateDate" : "05/01/2016" } }}] } }]` |

Available Since
:   1.5.13

### POST /2.0/search/groupedSearchByType

Perform a search by type and pattern and return grouped results

Available Since
:   1.5.13

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SearchVo](https://api.fluig.com/old/json_SearchVo.html) (JSON) | Request JSON (example):`{ "pattern" : "cloud", // REQUIRED - Supports hash tags searches "searchType" : "DOCUMENT", // REQUIRED - Types: GLOBAL, USER, COMMUNITY, DOCUMENT, PROCESS, POST, FORM, TAG, WORD and INFLUENCERS "limit" : "2", // Limit of results - Default value: 10 "offset" : "2", // Result offset (optional parameter) - Default value: 0 "ordering" : "RELEVANT" // Orderings: RELEVANT, NEWEST, OLDEST - Default value:RELEVANT }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `[{ "DOCUMENT" : { "timeElapsed": 489, "totalHits": 23, "offset": 10, "hasMore": true, "infoList" : [{ "fields" : { "DocumentId" : "23", "DocumentName" : "Cloud computing.pdf", "DocumentCreateDate" : "20/02/2016", "DocumentDescription" : "Description" },{ "fields" : { "DocumentId" : "15", "DocumentName" : "Cloud normas.pdf", "DocumentCreateDate" : "30/01/2016", "DocumentDescription" : "Description of document" } }}] } }]` |
