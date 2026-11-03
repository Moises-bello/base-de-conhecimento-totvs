---
content_hash: 910b9f4bea32d3ca842bdc23d996a250f5144e5f364a5a2748d8299a0184b496
fetched_at: '2026-11-03T14:34:39.782236+00:00'
page_id: resource_FavoritesRest
product: fluig
source: rest-fluig
title: Fluig REST — FavoritesRest Resource
type: documentation
url: https://api.fluig.com/old/resource_FavoritesRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# FavoritesRest Resource

Favorites

Available Since
:   1.5.3

### GET /2.0/favorites/findFavoritesDocuments/{colleagueId}

Returns the user's favorite documents

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | :adm |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs favorite user documents.   {  	"content": {  		"tenantId": 1,  		"documentId": 170,  		"version": 1000,  		"documentTypeId": "",  		"languageId": null,  		"iconId": 0,  		"topicId": 0,  		"colleagueId": "login.user",  		"documentDescription": "teste-api-publica",  		"phisicalFile": "",  		"keyWord": "",  		"createDate": "2015-07-03",  		"approvedDate": null,  		"lastModifiedDate": "2015-07-03",  		"documentType": "1",  		"expirationDate": "2015-07-03",  		"accessCount": 0,  		"atualizationId": null,  		"parentDocumentId": 169,  		"visualization": null,  		"relatedFiles": null,  		"activeVersion": true,  		"versionDescription": "",  		"approvalAndOr": null,  		"externalDocumentId": "",  		"downloadEnabled": false,  		"approved": true,  		"validationStartDate": "2015-07-03",  		"publisherId": "login.user",  		"cardDescription": null,  		"allowMuiltiCardsPerUser": true,  		"documentPropertyNumber": null,  		"documentPropertyVersion": null,  		"privateDocument": false,  		"privateColleagueId": null,  		"indexed": false,  		"priority": null,  		"translated": false,  		"userNotify": false,  		"expires": false,  		"volumeId": "Default",  		"updateIsoProperties": false,  		"lastModifiedTime": null,  		"deleted": false,  		"imutable": null,  		"internalVisualizer": null,  		"crc": 0,  		"phisicalFileSize": 0,  		"permissionType": 0,  		"restrictionType": 0,  		"siteCode": "Fluig",  		"draft": false,  		"onCheckout": false,  		"uuid": "D472AB96-FBDF-445C-8895-717210129E27"  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.3

### GET /2.0/favorites/findFavoritesProcess/{colleagueId}

Returns the user's favorite processes

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | :adm |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs favorite user processes.   {  	"content": {  		"companyId": 1,  		"processId": 170,  		"version": 1000,  		"versionDescription": "teste-api-publica",  		"categoryStructure": null,  		"fullCategoryStructure": null,  		"processDescription": "teste-api-publica",  		"rowId": 0,  		"favorite": true,  		"mobileReady": false,  		"formId": 15,  		"formVersion": 1,  		"initialProcessState": {  		     "companyId": 1,  		     "sequence": 1,  		     "stateName": "state",  		     "stateDescription": "state",  	     }  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |
