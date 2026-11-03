---
content_hash: 0a0d21a9e0cfe43ed989d5ba179e52d545da773acde205ccb513b374ac7c2643
fetched_at: '2026-11-03T14:34:39.872992+00:00'
page_id: resource_HolidayRest
product: fluig
source: rest-fluig
title: Fluig REST — HolidayRest Resource
type: documentation
url: https://api.fluig.com/old/resource_HolidayRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# HolidayRest Resource

Available Since
:   1.6.2

### GET /2.0/holidays

Find a holiday.

Available Since
:   1.6.2

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| description | query |  |  |
| exclusive | query | Only functional if there is a localId set, returns holidays only from that localId, excluding shared holidays. | false |
| expand | query | Can be locals and locals.localUsers, to expand the collections. | 0 |
| limit | query |  | 0 |
| localId | query | Local id to be queried. |  |
| offset | query |  | 0 |
| order | query | Order request, can only be "id" by ASC (putting only id) or DESC (putting -id). | description |
| page | query | Actual page. | 1 |
| pageSize | query | Items by page. | 0 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a HolidayVO  { "content": { hasNext: false, total: 1, items[{ "id": 1, "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }], "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### POST /2.0/holidays

Create a new holiday.

Available Since
:   1.6.2

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [HolidayVO](https://api.fluig.com/old/json_HolidayVO.html) (JSON) | `This method return a HolidayVO  { "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a HolidayVO  { "content": { "id": 1, "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### DELETE /2.0/holidays/{id}

Delete a holiday.

Available Since
:   1.6.2

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | Actual holiday id. | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a code 200` |

Available Since
:   1.6.2

### GET /2.0/holidays/{id}

Find a holiday.

Available Since
:   1.6.2

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | Actual holiday id. | long |
| expand | query |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a HolidayVO  { "content": { "id": 1, "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### PATCH /2.0/holidays/{id}

Update a holiday by each field.

Available Since
:   1.6.2

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | Actual holiday id. | long |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [HolidayVO](https://api.fluig.com/old/json_HolidayVO.html) (JSON) | `This method return a HolidayVO  { "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a HolidayVO  { "content": { "id": 1, "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### PUT /2.0/holidays/{id}

Update a holiday.

Available Since
:   1.6.2

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | Actual holiday id. | long |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [HolidayVO](https://api.fluig.com/old/json_HolidayVO.html) (JSON) | `This method return a HolidayVO  { "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a HolidayVO  { "content": { "id": 1, "description": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |
