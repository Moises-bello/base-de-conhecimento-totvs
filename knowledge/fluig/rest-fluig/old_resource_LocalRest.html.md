---
content_hash: 64eba508763f989c1ef031424cbc29fb69abbacf091ac4cfafe0e1c9a68d4ff7
fetched_at: '2026-11-03T14:34:39.940036+00:00'
page_id: resource_LocalRest
product: fluig
source: rest-fluig
title: Fluig REST — LocalRest Resource
type: documentation
url: https://api.fluig.com/old/resource_LocalRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# LocalRest Resource

REST for locals

Available Since
:   1.6.2

### GET /2.0/locals

Query a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| expand | query |  | 0 |
| limit | query |  | 0 |
| name | query | Name of the location |  |
| offset | query |  | 0 |
| order | query |  |  |
| page | query | Page result | 1 |
| pageSize | query | Size of the page | 0 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResponseEnvelopeVO  { "content": { "hasNext": "false" "total": "1" "locals": [{ "id": 1, "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } ], "holidays": [ { "id": "ABC", "data" : "MM-dd", "recurrent" : true, "companyId" : 1, } ] }] }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### POST /2.0/locals

Create a new location.

Available Since
:   1.6.2

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [LocalVO](https://api.fluig.com/old/json_LocalVO.html) (JSON) | `This method return a LocalVO  { "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1 } ], "holidays": [ { "id": "ABC" } ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalVO  { "content": { { "id": 1, "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } ], "holidays": [ { "id": "ABC", "data" : "MM-dd", "recurrent" : true, "companyId" : 1, } ] } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### GET /2.0/locals/timezone

Get timezone from latitude and longitude.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| latitude | query | Latitude code |
| longitude | query | Longitude code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return the timezone  { "content": "America/Sao_Paulo", "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### DELETE /2.0/locals/{id}

Delete a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path | Local id |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a code 200` |

Available Since
:   1.6.2

### GET /2.0/locals/{id}

Query a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path | Location's id |
| expand | query |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalVO  { "content": { { "id": 1, "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } ], "holidays": [ { "id": "ABC", "data" : "MM-dd", "recurrent" : true, "companyId" : 1, } ] } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### PATCH /2.0/locals/{id}

Update specific parameters of a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path |  |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [LocalVO](https://api.fluig.com/old/json_LocalVO.html) (JSON) | `This method return a LocalVO  { "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1 } ], "holidays": [ { "id": "ABC" } ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalVO  { "content": { { "id": 1, "name": "NAME", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } ], "holidays": [ { "id": "ABC", "data" : "MM-dd", "recurrent" : true, "companyId" : 1, } ] } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### PUT /2.0/locals/{id}

Update a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path |  |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [LocalVO](https://api.fluig.com/old/json_LocalVO.html) (JSON) | `This method return a LocalVO  { "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1 } ], "holidays": [ { "id": "ABC" } ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalVO  { "content": { { "id": 1, "name": "NAME", "timezone": "America/Sao_Paulo", "latitude": "-26.265091", "longitude": "-48.851453", "radius": "6366.056", "localUsers": [ { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } ], "holidays": [ { "id": "ABC", "data" : "MM-dd", "recurrent" : true, "companyId" : 1, } ] } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### PUT /2.0/locals/{id}/default

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.2

### GET /2.0/locals/{id}/holidays

Find a holiday based on the local.

Available Since
:   1.6.2

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| id | path | Id to query the search. |  |
| exclusive | query | Only functional if there is a localId set, returns holidays only from that localId, excluding shared holidays. | false |
| expand | query | Can be locals and locals.localUsers, to expand the collections. |  |
| holidayId | query |  |  |
| limit | query |  | 0 |
| offset | query |  | 0 |
| order | query | Order request, can only be "id" by ASC (putting only id) or DESC (putting -id). |  |
| page | query | Actual page. | 1 |
| pageSize | query | Items by page. | 0 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a HolidayVO  { "content": { hasNext: false, total: 1, items[{ "id": "NAME", "date": "yyyy-MM-dd", "recurrent": false, "locals": {"id" : 1} }], "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### GET /2.0/locals/{id}/users

Query users from a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| id | path | Location's id |  |
| limit | query |  | 0 |
| offset | query |  | 0 |
| order | query | Order parameter, can be userName or userCode. |  |
| page | query | Result page. | 1 |
| pageSize | query | Size of the page. | 0 |
| userName | query | Pattern of the user name to be searched for. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalUserVO  { "content": { { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### POST /2.0/locals/{id}/users

Create a new relation between location and user.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path | Local id to be related |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [LocalUserVO](https://api.fluig.com/old/json_LocalUserVO.html) (JSON) | `This method return a LocalUserVO  { "userCode" : "adm", "userName" : "adm" }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalVO  { "content": { { "id" : 1, "localId" : 1, "userCode" : "adm", "userName" : "adm" } } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### POST /2.0/locals/{id}/usersgroup

Create a new relation between location and user.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path | Local id to be related |
| group | query | This method return a String whith code group or groups  { "group" : "a,b,c...", } |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalUserVO  { "content": { { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### DELETE /2.0/locals/{id}/holidays/{holidayId}

Delete a relation between local and holiday.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| holidayId | path | Holiday Id |
| id | path | Local id |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a code 200` |

Available Since
:   1.6.2

### GET /2.0/locals/{id}/users/unrelated

Query users without a location.

Available Since
:   1.6.2

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| id | path | Location's id |  |
| limit | query |  | 0 |
| offset | query |  | 0 |
| order | query | Order parameter, can be userName or userCode. |  |
| page | query | Result page. | 1 |
| pageSize | query | Size of the page. | 0 |
| userName | query | Pattern of the user name to be searched for. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a LocalUserVO  { "content": { { "id": 1, "userCode" : "adm", "localId" : 1, "userName" : "adm", } } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.2

### DELETE /2.0/locals/{id}/users/{userCode}

Delete a relation between user and location.

Available Since
:   1.6.2

Request Parameters

| name | type | description |
| --- | --- | --- |
| id | path | Local id |
| userCode | path | User code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a code 200` |
