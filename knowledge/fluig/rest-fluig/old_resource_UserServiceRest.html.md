---
content_hash: 708362167a217799f01d36d6eaeb84a5dd1a46a28e7465e046d4d6afa5c2e3ae
fetched_at: '2026-11-03T14:34:40.427339+00:00'
page_id: resource_UserServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — UserServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_UserServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# UserServiceRest Resource

Users

Available Since
:   1.4.0

### GET /social/listFavoriteUsersWithRelevance

List users with relevance and ordenation type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.4.0

### GET /social/listUsersWithRelevance

List users with relevance and ordenation type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| favoriteOnly | query |  |  | boolean |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

### GET /social/user

Returns a list of users.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit of records. Default value 250. | 250 | int |
| offset | query | the offset. Default value 0. | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",		//User's id  	"name" : "User 01",//User's name  	"description" : "User 01 description",	//User's description  	"alias" : "user01",	//user's alias  	"type" : "USER",	//fixed  	"tenantId" : "22",			//tenant's id  	"lastUpdate" : "10008520",	//date of last time the user has been modified (in miliseconds)  	"create" : "10008520",		//date the user has been created (in miliseconds)  	"numberModerations" : "1",	   //number of the communities the user is moderator  	"state" : "ACTIVE"			   //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}] ``` |

Available Since
:   1.3.0

### POST /social/change/image

This method has been deprecated. Use /change/image/v2 instead.

It changes user's picture
  
Accepted media types: PNG, JPG, JPEG.

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):(/h4>  ``` {                      	"base64media" : "4747545" //media's content in base64 format                   } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /social/follow/accept

It accepts the following of a previously requested social follow

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialId | query | REQUIRED the social identifier | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.12

### POST /social/follow/cleanAll

It removes all following of all social. Only tenant's administrators can execute.

Available Since
:   1.4.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /social/follow/reject

It rejects the following of a previously requested social follow

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialId | query | REQUIRED the social identifier | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /social/follow/remove

It removes the following of a social

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialId | query | REQUIRED the social identifier | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.12

### POST /social/follow/removeAll

It removes all following of a social. Only tenant's administrators can execute.

Available Since
:   1.4.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialId | query | REQUIRED the social identifier | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/follow/request

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialId | query |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.3.0

### GET /social/follower/{genericId}

Returns if logged user is being followed by alias

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GenericVO](https://api.fluig.com/old/json_GenericVO.html) (JSON) | Response List of JSON (example):  ``` [{  	"value" : "ACCEPTED" Values: ACCEPTED | REJECTED | PENDING | BLOCKED | NOT_RELATED | ITSELF  }] ``` |

Available Since
:   1.3.0

### GET /social/following/{genericId}

Returns if logged user is following the alias

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic indentify, can be (alias, idpId and userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GenericVO](https://api.fluig.com/old/json_GenericVO.html) (JSON) | Response List of JSON (example):  ``` [{               	"value" : "ACCEPTED" Values: ACCEPTED | REJECTED | PENDING | BLOCKED | NOT_RELATED | ITSELF           }] ``` |

### GET /social/image/{genericId}

Returns the user's profile image based on its alias

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | A application/octet-stream with the image file |

### GET /social/user/logged

This method has been deprecated. Use /user/logged/v2 instead.

Return the logged user details.

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",     //User's id  	"name" : "User 01",//User's name  	"description" : "User 01 description",  //User's description  	"alias" : "user01", //user's alias  	"type" : "USER",    //fixed  	"tenantId" : "22",          //tenant's id  	"uuid" : "asd1as5d4a5sd4",          //tenant's uuid  	"lastUpdate" : "10008520",  //date of last time the user has been modified (in miliseconds)  	"createDate" : "10008520",      //date the user has been created (in miliseconds)  	"customPage" : "/social/page",      //the user's custom page if exists  	"numberParticipations" : "1",     //number of the communities the user is participant  	"numberFollowing" : "1",     //number of the users the user is following  	"numberFollowers" : "1",     //number of the users that follow this user  	"numberModerations" : "1",     //number of the communities the user is moderator  	"tenantAdmin" : "false",           //indicates if this user is one of the tenant's administrators  	"page" : "/social/alias",          //social's default page  	"state" : "ACTIVE" ,            //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	"userData":{  		"UserRamal":"11 1111111",  		"UserProjects":"VP Fluig",  		"UserSpecialization":"Programadora Java",  		"UserEmailHTML":null} // User data  } ``` |

### GET /social/user/{genericId}

Return the user details based on its alias.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) | regex: (?!(logged$)).\* |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response JSON (example):  ``` { 		"id" : "1",		//User's id 		"name" : "User 01",//User's name 		"description" : "User 01 description",	//User's description  		"alias" : "user01",	//user's alias  		"type" : "USER",	//fixed   	"email" : "maria@teste.com.br", // User's email  		"tenantId" : "22",			//tenant's id  		"lastUpdate" : "10008520",	//date of last time the user has been modified (in miliseconds)  		"create" : "10008520",		//date the user has been created (in miliseconds)  		"numberModerations" : "1",	   //number of the communities the user is moderator  		"state" : "ACTIVE",			   //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")   	"userData":{   		"UserRamal":"11 1111111",   		"UserProjects":"VP Fluig",   		"UserSpecialization":"Programadora Java",   		"UserEmailHTML":null} // User data  	} ``` |

Available Since
:   1.4.11

### POST /social/change/image/v2

It changes user's picture
  
Accepted media types: PNG, JPG, JPEG.

Available Since
:   1.4.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):(/h4>  ``` {  	"base64media" : "4747545" //media's content in base64 format  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### GET /social/imageBySize/{genericId}/{size}

Returns the user's profile image based on its alias and size

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |
| size | path | REQUIRED image size. Possible values: 80|160|320|432|640|864|1060. | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | A application/octet-stream with the image file |

Available Since
:   1.4.8

### POST /social/user/disable/{genericId}

Disable user

Available Since
:   1.4.8

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic indentify, can be (alias, idpId and userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.8

### POST /social/user/enable/{genericId}

Enable user

Available Since
:   1.4.8

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.11

### GET /social/user/logged/v2

Return the logged user details.

Available Since
:   1.4.11

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{"content":{ "id" : "1", //User's id "name" : "User 01",//User's name "description" : "User 01 description", //User's description "alias" : "user01", //user's alias "type" : "USER", //fixed "tenantId" : "22", //tenant's id "uuid" : "asd1as5d4a5sd4", //tenant's uuid "lastUpdate" : "10008520", //date of last time the user has been modified (in miliseconds) "createDate" : "10008520", //date the user has been created (in miliseconds) "customPage" : "/social/page", //the user's custom page if exists "numberParticipations" : "1", //number of the communities the user is participant "numberFollowing" : "1", //number of the users the user is following "numberFollowers" : "1", //number of the users that follow this user "numberModerations" : "1", //number of the communities the user is moderator "tenantAdmin" : "false", //indicates if this user is one of the tenant's administrators "page" : "/social/alias", //social's default page "state" : "ACTIVE" , //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED") "foundationUserId" : 2, //Foundation User Id "userData":{ "UserRamal":"11 1111111", "UserProjects":"VP Fluig", "UserSpecialization":"Programadora Java", "UserEmailHTML":null} // User data }, //Response content "message": null} // Message if returns exception` |
