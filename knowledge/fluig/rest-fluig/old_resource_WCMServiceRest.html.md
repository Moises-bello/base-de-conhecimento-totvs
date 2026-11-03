---
content_hash: 942dad4c90106d70c316936a06a2d43a5cb8f04e0e3df22fccba963266bb3de7
fetched_at: '2026-11-03T14:34:40.486765+00:00'
page_id: resource_WCMServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — WCMServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_WCMServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# WCMServiceRest Resource

WCM core services

Available Since
:   1.5.0

### GET /wcm/assembleMenu

Assemble Fluig Menu

Available Since
:   1.5.0

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| pageCode | query | Optional |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content":[  		{  			"pageId": 23,  			"title": "Home",  			"description": "Home",  			"displayOrder": 1,  			"authType": 1,  			"hidden": false,  			"domain": "emp",  			"page": "home",  			"children": [],  			"disableChildLevel": false,  			"menuGroup": false,  			"uri": "/p/emp/home",  			"friendlyURL": null 		} 	], 	"message": null } ``` |

Available Since
:   1.5.0

### GET /wcm/configuration

Return system configuration information.
Used by mobile application

Available Since
:   1.5.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Object VO containing ID\_CONFIGURATION, SERVER\_URL, DEFAULT\_LAYOUT\_ID and DEFAULT\_THEME\_ID:  ```  {  	"content": {  		"id": long,  		"serverUrl": "http://host:port/portal",  		"defaultLayoutId": "long",  		"defaultThemeId": "long",  	},  	"message": null  } ``` |

Available Since
:   1.3.0

### GET /wcm/display

Display the current set locale.

Available Since
:   1.3.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List (example):  ```  [  	"value", "pt_BR"  ] ``` |

### GET /wcm/findPages

Return de search result of editable pages into Fluig

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| filter | query | Optional. Default value = '' |  |  |
| pageIndex | query | Optional. Default value = 0 | 0 | required |
| pageSize | query | Optional Default value = 30 | 30 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```   {   	"content": {   		"totalpages": 0,   		"totalrecords": "8",   		"currpage": 0,   		"invdata": [   			{   				"title": "Fluig",   				"description": "Fluig",   				"layout": 204,   				"layoutDescription": "Layout Simple",   				"pageIcon": "fluigpage.fluig_logo.png",   				"pageKey": {   					"id": 129,   					"code": "fluigpage"   				},   				"parent": 0,   				"authorization": 1,   				"permissions": null,   				"displayOrder": 118,   				"childrens": null,   				"enabledChildren": true,   				"enabledPathParam": false,   				"editable": true,   				"disableChildLevel": false,   				"menuGroup": false,   				"iconUploaded": false,   				"parentVO": null,   				"hidden": false,   				"opened": false,   				"clazz": null,   				"friendlyURL": null,   				"preferences": {},   				"resourceDescription": "Fluig",   				"resourceType": "page",   				"securityCode": "page.129"   			}   		],   		"genericObject": null   	},   	"message": null   } ``` |

Available Since
:   1.6.0

### GET /wcm/isHighAvailability

Confirm if the application server is running on High Availability

Available Since
:   1.6.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON:true if it's running on high availability, false if it's not.  ```   {   	"content":true,   	"message":null   } ``` |

Available Since
:   1.4.3

### POST /wcm/logout

User logout

Available Since
:   1.4.3

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": true,  	"message": null  } ``` |

Available Since
:   1.4.8

### GET /wcm/theme

Display the current tenant theme.

Available Since
:   1.4.8

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content":{  		"colorMenu":"rgb(252, 70, 252)",  		"colorBackground":"rgba(0, 0, 0, 0)",  		"colorHeader":"rgb(250, 205, 3)",  		"tenant":{  			"id":56987,  			"code":"company",  			"federalId":"company",  			"UUID":"xxxx-xxxxx-xxxx-xxxx",  			"idpId":null,  			"description":"company",  			"organizationUrl":"http://totvs.com",  			"data":{  			"key":"value" // Teant Data  			},  			"adminUser":null,  			"products":[  				"ECM",  				"social_application"  			],  			"idpLogOff":false,  			"thumbnailEnabled":false,  			"removeVolume":false  		}  	},  	"message":null  } ``` |

Available Since
:   1.3.0

### GET /wcm/version

This method has been deprecated. Use /version/v2 instead.

Get version of the system

Available Since
:   1.3.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List (example):  ```  [  value : "1.3.0"  ] ``` |

Available Since
:   1.5.2

### GET /wcm/chronos/meanTimes

Return fluig metrics mean times.

Available Since
:   1.5.2

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Collection with metric name and mean time in miliseconds |

Available Since
:   1.4.8

### POST /wcm/oauth/generateKeys

Generate the tokenAccess and tokenSecret for the current user.  
This method is used to generate oauth keys for a user who is already logged and
would like to start an external app already authenticated.

Available Since
:   1.4.8

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [OAuthAppKeyVO](https://api.fluig.com/old/json_OAuthAppKeyVO.html) (JSON) | Request JSON with application key:  ```  { 		"appKey" : "myApplicationKey"  	} ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Object containing tokenAccess and tokenSecret:  ```  {  	"content": {  		"id": null,  		"signatureMethod": "HMAC-SHA1",  		"consumerKey": "myappkey",  		"tokenSecret": "0bc1a6f0-672c-4789-9412-e1c071e36d238c4e9b1c-d841-4ab2-bb0d-42c4fa7591c2",  		"tokenAccess": "ee81e3e6-9309-4cf4-9e6e-e37feef07672",  	},  	"message": null 	} ``` |

Available Since
:   1.5

### POST /wcm/oauth/generateKeysToUser

Generate the tokenAccess and tokenSecret for an user login.  
This method is used to generate oauth keys to a desired user login by an admin user
that's would like to start an external app using user login keys.

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [OAuthAppKeyVO](https://api.fluig.com/old/json_OAuthAppKeyVO.html) (JSON) | Request JSON with application key and user login:  ```  {  	"appKey" : "myApplicationKey",  	"login" : "johndoe"  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Object containing tokenAccess and tokenSecret:  ``` {  	"content": {  		"id": null,  		"signatureMethod": "HMAC-SHA1",  		"consumerKey": "myappkey",  		"tokenSecret": "0bc1a6f0-672c-4789-9412-e1c071e36d238c4e9b1c-d841-4ab2-bb0d-42c4fa7591c2",  		"tokenAccess": "ee81e3e6-9309-4cf4-9e6e-e37feef07672",  	},  	"message": null 	} ``` |

Available Since
:   1.4.11

### GET /wcm/version/v2

Get version of the system

Available Since
:   1.4.11

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List (example):  ```  {  	"content":"1.4.11" //Response content  	"message": null // Message if returns exception  } ``` |

Available Since
:   1.5.0

### GET /wcm/findPageFriendlyURL/{tenantId}/{pageCode}

Find the page's friendly url

Available Since
:   1.5.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| pageCode | path |  |  |
| tenantId | path |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```   {   	"content":"/PagUrl",   	"message":null   } ``` |
