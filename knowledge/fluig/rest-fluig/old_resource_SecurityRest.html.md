---
content_hash: 44d88d738ff8a755ea20fd7e99c0cdacb2c5683486623949d3210b1c48080df8
fetched_at: '2026-11-03T14:34:40.145847+00:00'
page_id: resource_SecurityRest
product: fluig
source: rest-fluig
title: Fluig REST — SecurityRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SecurityRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SecurityRest Resource

Security

Available Since
:   1.5.12

### POST /2.0/security/changeUserPassword

Change the user password

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UserPasswordVO](https://api.fluig.com/old/json_UserPasswordVO.html) (JSON) | Request JSON (example):`{ "login" : "fluig", "currentPassword" : "fluig", "newPassword" : "fluig2" }` |
| application/xml | [userPasswordVO](https://api.fluig.com/old/xml_ns0_userPasswordVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  "content": "OK" "message": { "message": "OK", "detail": "OK", "errorCode": null "type": "INFO" }` |

Available Since
:   1.5.12

### GET /2.0/security/getCurrentTenant

Get the current tenant

Available Since
:   1.5.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  content: { "id": 1, "code": "01", "federalId": null, "idpId": null, "description": "Fluig", "organizationUrl": "http://totvs.com", "volumeDir": null, "idpLogOff": null, "thumbnailEnabled": null, "removeVolume": null, "data": { }, "adminUser": null }, "message": { "message": "OK", "detail": "OK", "type": "INFO" }` |

Available Since
:   1.5.4

### POST /2.0/security/createPermissions/{resourceCode}

Create permissions for the resource  
  
Internal Resources can't be modified

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| resourceCode | path | The resource code |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [PermissionVO](https://api.fluig.com/old/json_PermissionVO.html) (JSON) | Request JSON (example):  ```          [{          	"permission": "NOTIFY_COMMUNITY", // Permission for the resource (REQUIRED)          	"categoryCode": "MODERATOR_RH", // Code of target resource (REQUIRED)          	"category": "GROUP"          // Category's Resource [ROLE,GROUP,USER] (REQUIRED)          },          {          	"permission": "NOTIFY_POST", // Permission for the resource (REQUIRED)          	"categoryCode": "MODERATOR_RH",// Code of target resource (REQUIRED)          	"category": "GROUP"          // Category's Resource [ROLE,GROUP,USER] (REQUIRED)          }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message            {           	"content": {           	"message": {           		"message": "OK",           		"detail": "OK",           		"type": "INFO"           	}           } ``` |

Available Since
:   1.5.4

### POST /2.0/security/deletePermissions/{resourceCode}

Delete permissions for the resource  
  
Internal Resources can't be modified

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| resourceCode | path | : The resource code |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [PermissionVO](https://api.fluig.com/old/json_PermissionVO.html) (JSON) | Request JSON (example):  ```          [{          	"permission": "NOTIFY_COMMUNITY", // Permission for the resource (REQUIRED)          	"categoryCode": "MODERATOR_RH", // Code of target resource (REQUIRED)          	"category": "GROUP"          // Category's Resource [ROLE,GROUP,USER] (REQUIRED)          },          {          	"permission": "NOTIFY_POST", // Permission for the resource (REQUIRED)          	"categoryCode": "MODERATOR_RH",// Code of target resource (REQUIRED)          	"category": "GROUP"          // Category's Resource [ROLE,GROUP,USER] (REQUIRED)          }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message            {           	"content": {           	"message": {           		"message": "OK",           		"detail": "OK",           		"type": "INFO"           	}           } ``` |

Available Since
:   1.5.4

### GET /2.0/security/getPermissionsByResourceCode/{resourceCode}

List the Resource's permissions

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| resourceCode | path | : The resource code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message            {               	"content": [                   {               		"permission": "pageUpdate",               		"permissionDescription": "Alterar página",               		"isSelected": false,               		"category": "ROLE",               		"categoryCode": "admin"                   },                   {               		"permission": "pageRemove",               		"permissionDescription": "Excluir página",               		"isSelected": false,               		"category": "ROLE",               		"categoryCode": "admin"                   },                   {               		"permission": "pageView",               		"permissionDescription": "Visualizar página",               		"isSelected": true,               		"category": "ROLE",               		"categoryCode": "admin"                   }                 ],               	"message": {               		"message": "OK",               		"detail": "OK",               		"type": "INFO"               }               } ``` |

Available Since
:   1.5.4

### GET /2.0/security/listResourcesByCategory/{category}

List resources by category  
  
List the resources by category[RESOURCE,ROLE,GROUP,USER]

Available Since
:   1.5.4

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| category | path | :category |  |  |
| filter | query | :filter to search |  |  |
| limit | query | :limit of records returned - Default:20 | 20 | required |
| offset | query | :the offset |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message            	"content": [{           		"id": 369,           		"code": "page.16",           		"description": "Preferências do usuário",           		"typeCode": "page"}],           	"message": {           		"message": "OK",           		"detail": "OK",           		"type": "INFO"}           } ``` |

Available Since
:   1.5

### GET /2.0/security/hasPermission/{resource}/{permiss}

Verify if has permisstion

Available Since
:   1.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| permiss | path | :permiss |
| resource | path | :resource |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, Object User   {  	content: true  	message: {  	message: "OK"  	detail: "OK"  	type: "INFO"  	}-  } ``` |
