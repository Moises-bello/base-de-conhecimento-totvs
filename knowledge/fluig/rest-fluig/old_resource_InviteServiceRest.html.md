---
content_hash: 7cd088517ea534b7f51ed09f38a26109e30fb2e6179af9b05f4ee27ef45b68a7
fetched_at: '2026-11-03T14:34:39.888489+00:00'
page_id: resource_InviteServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — InviteServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_InviteServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# InviteServiceRest Resource

Invites

### GET /social/invite

List the created invites.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit of records. Default value 50. | 20 | int |
| offset | query | the offset. Default value 0. | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialInviteVO](https://api.fluig.com/old/json_SocialInviteVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",			//invite's id  	"tenantId" : "22",	//tenant's id  	"alias" : "user",	//alias of user that has created the invited  	"token" : "1122000",//token created to the invite  	"email" : "invited@fluig.com",	//e-mail invited  	"expiration" : "10001555",		//date the invite expires (in miliseconds)  	"lastSubmission" : "10001555",	//timestamp last time the invite has been sent  	"qttSubmission" : "1",			//number of times the invite has been sent  	"userCreated" : "true",			//indicates if the invited user has joined the application  	"fileName" : "invitesFile.txt",         //file name if invite was created through a file  	"status" : "USER_CREATED" 	//it can be: INVALID_EMAIL, PENDING, USER_CREATED, EXPIRED, DUPLICATED_INVITE, FAIL_TO_SEND_EMAIL  }] ``` |

### POST /social/invite

Sends an invite to a given e-mail.
It allows to give groups to include the created user automatically. The groups need to be informed comma separated.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [InviteVO](https://api.fluig.com/old/json_InviteVO.html) (JSON) | Request JSON (example):  ```  {  	"email" : "invited@fluig.com",	//user's e-mail to be invited  	"groups" : "group1,group2",	//OPTIONAL: groups the invited user will become participant  	"dialect" : "pt_BR"		//it can be "pt_BR", "es" or "en_US"  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /social/invite/filter/{email}/{status}

List the created invites based on a pattern filter.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| email | path | e-mail invited |  |  |
| status | path | (INVALID\_EMAIL | PENDING | USER\_CREATED | EXPIRED | DUPLICATED\_INVITE | FAIL\_TO\_SEND\_EMAIL) |  |  |
| limit | query | the limit of records | 30 | int |
| offset | query | the offset | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialInviteVO](https://api.fluig.com/old/json_SocialInviteVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",			//invite's id  	"tenantId" : "22",	//tenant's id  	"alias" : "user",	//alias of user that has created the invited  	"token" : "1122000",//token created to the invite  	"email" : "invited@fluig.com",	//e-mail invited  	"expiration" : "10001555",		//date the invite expires (in miliseconds)  	"lastSubmission" : "10001555",	//timestamp last time the invite has been sent  	"qttSubmission" : "1",			//number of times the invite has been sent  	"userCreated" : "true",			//indicates if the invited user has joined the application  	"fileName" : "invitesFile.txt",         //file name if invite was created through a file  	"status" : "USER_CREATED" 	//it can be: INVALID_EMAIL, PENDING, USER_CREATED, EXPIRED, DUPLICATED_INVITE, FAIL_TO_SEND_EMAIL  }] ``` |
