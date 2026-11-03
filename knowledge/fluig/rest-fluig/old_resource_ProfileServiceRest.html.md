---
content_hash: 2a1cb061b1916a6fb1618efddb59614809a354e46e85fd6a2acba503814981e0
fetched_at: '2026-11-03T14:34:40.074835+00:00'
page_id: resource_ProfileServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — ProfileServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_ProfileServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# ProfileServiceRest Resource

Profile

Available Since
:   1.4.0

### POST /profile/change/picture

It changes the profile picture. Can be community, user or application user
  
Accepted media types: PNG, JPG, JPEG.

Available Since
:   1.4.0

Request Body

| media type | data type |
| --- | --- |
| application/json | [FDNUserPictureVO](https://api.fluig.com/old/json_FDNUserPictureVO.html) (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /profile/edit/profile

Edit user profile

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UpdateUserVo](https://api.fluig.com/old/json_UpdateUserVo.html) (JSON) | Response List of JSON (example):  ```  [{  	"name" : "Maria",  	"lastName" : "Silva",  	"fullName" : "Maria Silva",  	"description" : "User description",  	"email" : teste@teste.com",  	"userData" : {  		"UserRamal":"11 1111111",  		"UserProjects":"VP Fluig",  		"UserSpecialization":"Programadora Java",  		"UserEmailHTML":null} // User data  }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {	"content": { 		"name" : "User 01",//User's name 		"description" : "User 01 description",	//User's description   	"userData":{   		"UserRamal":"11 1111111",   		"UserProjects":"VP Fluig",   		"UserSpecialization":"Programadora Java",   		"UserEmailHTML":null} // User data  	},   message: "" } ``` |

Available Since
:   1.4.0

### GET /profile/image/{genericId}/{type}

Returns the profile's image based on alias

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |
| type | path | REQUIRED the type of images are X\_SMALL\_PICTURE, SMALL\_PICTURE, MEDIUM\_PICTURE and LARGE\_PICTURE | "DEFAULT\_PICTURE" or "LARGE\_PICTURE" or "MEDIUM\_PICTURE" or "ORIGINAL\_PICTURE" or "SMALL\_PICTURE" or "TEMPORARY\_PICTURE" or "X\_SMALL\_PICTURE" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | A application/octet-stream with the image file |
