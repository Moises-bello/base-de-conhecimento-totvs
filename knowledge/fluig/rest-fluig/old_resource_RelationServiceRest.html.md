---
content_hash: 14b61bca4e4fd7e1734e17bcca7ec4d099df0f3856715e5466f96bcaebeddb1f
fetched_at: '2026-11-03T14:34:40.109535+00:00'
page_id: resource_RelationServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — RelationServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_RelationServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# RelationServiceRest Resource

Relation

Available Since
:   1.4.4

### GET /relation/canAccessByLogin

Verify if a user can access a social(community, another user, etc). One
of the parameters must be a user, if not, then true will be returned.

If both parameters are users, then the validation is done with socialOne
can access socialTwo.

This method will always return true is access control is disabled.

Available Since
:   1.4.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| socialOne | query |  |
| socialTwo | query |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | True if access is allowed. |

Available Since
:   1.5.2

### POST /relation/canAccessByLogins

Verify if a user can access a social(community, another user, etc).

The method will validate the user's access right field socialAlias users of socialAliases list

This method will always return true is access control is disabled.

Available Since
:   1.5.2

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RelationVO](https://api.fluig.com/old/json_RelationVO.html) (JSON) | - RelationVO |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | True if access is allowed. |

Available Since
:   1.4.4

### GET /relation/canAccessBySocialId

Verify if a user can access a social(community, another user, etc). One
of the parameters must be a user, if not, then true will be returned.

If both parameters are users, then the validation is done with socialOne
can access socialTwo.

This method will always return true is access control is disabled.

Available Since
:   1.4.4

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialOne | query | - A social | long |
| socialTwo | query | - A social | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | True if access is allowed. |

### POST /relation/recountRelations

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.3.0

### GET /relation/followers/{genericId}

Return list followers

Available Since
:   1.3.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | int |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | int |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.3.0

### GET /relation/following/{genericId}

This method has been deprecated. Use /following/v2/ instead.

Return list following

Available Since
:   1.3.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | int |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | int |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.4.0

### GET /relation/isFollowing/{genericId}

Return te relation between the user and the logged user

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"content" : "1", //Status of relation  ACCEPTED, REJECTED, PENDING, BLOCKED, NOT_RELATED, ITSELF;  	"message" : "Succes or Error message"  }] ``` |

Available Since
:   1.4.0

### GET /relation/listFollowersWithRelevance/{genericId}

Return list followers with relevance and order type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 |  | required |
| offset | query | defines the first registry in the returned list. Default value 0 |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.4.0

### GET /relation/listFollowingWithRelevance/{genericId}

Return list following with relevance and order type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 |  | required |
| offset | query | defines the first registry in the returned list. Default value 0 |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.4.11

### GET /relation/followers/v2/{genericId}

Return list followers

Available Since
:   1.4.11

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | int |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | int |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`[{"content": { "id" : "1", //user's id "name" : "John Fluig", //user's name "description" : "Software Engineer", //user's description "alias" : "john.fluig", //user's alias "lastUpdate" : "100001582" //last time the user has been updated (in miliseconds) "foundationUserId" : 2, //user tenant's id }, //Response content "message": null} // Message if returns exception]` |

Available Since
:   1.4.11

### GET /relation/following/v2/{genericId}

Return list following

Available Since
:   1.4.11

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | int |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | int |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{"content": {  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }, //Response content  "message": null} // Message if returns exception] ``` |
