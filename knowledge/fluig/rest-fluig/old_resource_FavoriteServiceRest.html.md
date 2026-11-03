---
content_hash: 58b2a529929743bf928e9545431dda8159b05a2e66db93750cbe8a4aa4062678
fetched_at: '2026-11-03T14:34:39.776210+00:00'
page_id: resource_FavoriteServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — FavoriteServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_FavoriteServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# FavoriteServiceRest Resource

Favorites

### GET /social/favorite

Returns all socials marked as favorites.
The socials can be users or communities.

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [FavoriteVO](https://api.fluig.com/old/json_FavoriteVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",					//social's id  	"alias" : "community01",	//social's alias  	"name" : "Community 01",	//social's name  	"socialType" : "COMMUNTY",	//type. It can be "USER" or "COMMUNITY"  	"lastUpdate" : "100001582"	//last time the social has been updated (in miliseconds)  }] ``` |

### POST /social/favorite

Adds a given social as favorite.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialFavoriteVO](https://api.fluig.com/old/json_SocialFavoriteVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community01"	//social's alias  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/favorite/remove

Removes a given social marked as favorite before.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialFavoriteVO](https://api.fluig.com/old/json_SocialFavoriteVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community01"	//social's alias  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /social/favorite/bytype/{type}

This method has been deprecated. Use /bytype/v2/ instead.

Returns all socials marked as favorites by a given type.
The socials can be users or communities.

Request Parameters

| name | type | description |
| --- | --- | --- |
| type | path | REQUIRED the favorite's type (USER | COMMUNITY) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [FavoriteVO](https://api.fluig.com/old/json_FavoriteVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",					//social's id  	"alias" : "community01",	//social's alias  	"name" : "Community 01",	//social's name  	"socialType" : "COMMUNTY",	//type. It can be "USER" or "COMMUNITY"  	"lastUpdate" : "100001582"	//last time the social has been updated (in miliseconds)  }] ``` |

### GET /social/favorite/flag/{genericId}

Checks if the given social has been added as a favorite.

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | boolean (JSON) | ```  A plain boolean value that indicates if the social has or not been marked as a favorite. ``` |

Available Since
:   1.4.11

### GET /social/favorite/bytype/v2/{type}

Returns all socials marked as favorites by a given type.
The socials can be users or communities.

Available Since
:   1.4.11

Request Parameters

| name | type | description |
| --- | --- | --- |
| type | path | REQUIRED the favorite's type (USER | COMMUNITY) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{"content": {  	"id" : "1",                 //social's id  	"alias" : "community01",    //social's alias  	"name" : "Community 01",    //social's name  	"socialType" : "COMMUNTY",  //type. It can be "USER" or "COMMUNITY"  	"lastUpdate" : "100001582"  //last time the social has been updated (in miliseconds)  }, //Response content  "message": null} // Message if returns exception] ``` |
