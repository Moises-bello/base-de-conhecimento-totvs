---
content_hash: 0061ea9f5cd4eddcea53c6c98a9f3b70b3d3a92ba187f5a96d7e7b2354eb3dba
fetched_at: '2026-11-03T14:34:39.829644+00:00'
page_id: resource_FolderDocumentRest
product: fluig
source: rest-fluig
title: Fluig REST — FolderDocumentRest Resource
type: documentation
url: https://api.fluig.com/old/resource_FolderDocumentRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# FolderDocumentRest Resource

Folder Document

Available Since
:   1.5

### POST /2.0/folderdocuments/create

Create a folder  
  
Create a new community: fill object CommunityCreateVO

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [FolderCreateVO](https://api.fluig.com/old/json_FolderCreateVO.html) (JSON) | Request JSON (example):  ``` {  	"parentFolderId": "0",  	"iconId": "1",  	"documentDescription": "Document Description",  	"additionalComments": "Additional Comments",  	"versionDescription": "VersionDescription",  	"expires": "false",  	"keyWord": "keyWord",  	"publisherId": "64654",  	"volumeId": "Default",  	"permissionType": "1",  	"restrictionType": "3",  	"inheritSecurity": "false",  	"approvalAndOr": "true",  	"permissions": [  		{  			"securityLevel": "1",  			"securityVersion": false,  			"inheritSecurity": true,  			"downloadEnabled": "true",  			"showContent": "true",  			"attributionDescription": "attributionDescription",  			"attributionType": "1",  			"attributionValue": "fluig.user"  		}  	],  	"restrictions": [  		{  			"securityLevel": "1",  			"securityVersion": "false",  			"inheritSecurity": "true",  			"downloadEnabled": "true",  			"showContent": "true",  			"attributionDescription": "attributionDescription",  			"attributionType": "1",  			"attributionValue": "fluig.user"  		}  	],  	"publisherApprovers": [  		{  			"approverType": "0",  			"colleagueId": "4645",  			"levelId": "544",  			"approvalMode": "0",  			"digitalSignature": "false",  			"levelDescription": "levelDescription"  		}  	],  	"downloadEnabled": "true",  	"updateIsoProperties": "false",  	"topicId": "133",  	"documentTypeId": "5",  	"notifyUser": "true",  	"internalVisualizer": "true"  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return successful message  {  	"content": {  		"tenantId": null,  		"documentId": 261,  		"version": 1000,  		"iconId": 1,  		"colleagueId": null,  		"documentDescription": "Document Description",  		"additionalComments": "Additional Comments",  		"versionDescription": "VersionDescription",  		"expires": false,  		"keyWord": "keyWord",  		"createDate": null,  		"parentFolderId": 0,  		"publisherId": "64654",  		"volumeId": "Default",  		"permissionType": 1,  		"restrictionType": 3,  		"inheritSecurity": false,  		"approvalAndOr": true,  		"permissions": [  			{  				"securityLevel": 1,  				"securityVersion": false,  				"inheritSecurity": true,  				"downloadEnabled": true,  				"showContent": true,  				"attributionDescription": "attributionDescription",  				"attributionType": 1,  				"attributionValue": "fluig.user"  			}  		],  		"restrictions": [  			{  				"securityLevel": 1,  				"securityVersion": false,  				"inheritSecurity": true,  				"downloadEnabled": true,  				"showContent": true,  				"attributionDescription": "attributionDescription",  				"attributionType": 1,  				"attributionValue": "fluig.user"  			}  		],  		"publisherApprovers": [  			{  				"approverType": 0,  				"colleagueId": "4645",  				"levelId": 544,  				"approvalMode": 0,  				"digitalSignature": false,  				"levelDescription": "levelDescription"  			}  		],  		"downloadEnabled": true,  		"updateIsoProperties": false,  		"topicId": 133,  		"documentTypeId": "5",  		"notifyUser": true,  		"imutable": false,  		"internalVisualizer": true  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.12

### POST /2.0/folderdocuments/listDocumentByFolder

List document by folder

Available Since
:   1.5.12

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | // Default value 20 | 20 | required |
| offset | query | // Default value 0 | 0 | required |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [FolderVO](https://api.fluig.com/old/json_FolderVO.html) (JSON) | Request JSON (example):`{ "documentId": "0", "documentTypes": ["1","2"] "filters": {"documentDescription":"Ata de reunião","securityVersion": "false"} }` |
| application/xml | [folderVO](https://api.fluig.com/old/xml_ns0_folderVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return document list  { "content": [{ "tenantId": 1, "documentId": 170, "version": 1000, "documentTypeId": "", "languageId": null, "iconId": 0, "topicId": 0, "colleagueId": "login.user", "documentDescription": "teste-api-publica", "phisicalFile": "", "keyWord": "", "createDate": "2015-07-03", "approvedDate": null, "lastModifiedDate": "2015-07-03", "documentType": "1", "expirationDate": "2015-07-03", "accessCount": 0, "atualizationId": null, "parentDocumentId": 169, "visualization": null, "relatedFiles": null, "activeVersion": true, "versionDescription": "", "approvalAndOr": null, "externalDocumentId": "", "downloadEnabled": false, "approved": true, "validationStartDate": "2015-07-03", "publisherId": "login.user", "cardDescription": null, "allowMuiltiCardsPerUser": true, "documentPropertyNumber": null, "documentPropertyVersion": null, "privateDocument": false, "privateColleagueId": null, "indexed": false, "priority": null, "translated": false, "userNotify": false, "expires": false, "volumeId": "Default", "updateIsoProperties": false, "lastModifiedTime": null, "deleted": false, "imutable": null, "internalVisualizer": null, "crc": 0, "phisicalFileSize": 0, "permissionType": 0, "restrictionType": 0, "siteCode": "Fluig", "draft": false, "onCheckout": false, "uuid": "D472AB96-FBDF-445C-8895-717210129E27" },...] "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5

### GET /2.0/folderdocuments/get/{folderId}

Retrieve folder id

Available Since
:   1.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| folderId | path | :15644 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ``` {  	"content": {  		"tenantId": 1,  		"documentId": 254,  		"version": 1000,  		"documentTypeId": "",  		"languageId": null,  		"iconId": 1,  		"topicId": 133,  		"colleagueId": "fluig.user",  		"documentDescription": "Document Description",  		"phisicalFile": "",  		"keyWord": "",  		"createDate": "2015-07-06",  		"approvedDate": null,  		"lastModifiedDate": "2015-07-06",  		"documentType": "1",  		"expirationDate": "2015-07-06",  		"accessCount": 0,  		"atualizationId": null,  		"parentDocumentId": 0,  		"visualization": null,  		"relatedFiles": null,  		"activeVersion": true,  		"versionDescription": "VersionDescription",  		"approvalAndOr": null,  		"externalDocumentId": null,  		"downloadEnabled": false,  		"approved": true,  		"validationStartDate": "2015-07-06",  		"publisherId": "fluig.user",  		"cardDescription": null,  		"allowMuiltiCardsPerUser": true,  		"documentPropertyNumber": 0,  		"documentPropertyVersion": 0,  		"privateDocument": false,  		"privateColleagueId": null,  		"indexed": false,  		"priority": null,  		"translated": false,  		"userNotify": false,  		"expires": false,  		"volumeId": "Default",  		"updateIsoProperties": false,  		"lastModifiedTime": null,  		"deleted": false,  		"imutable": null,  		"internalVisualizer": null,  		"crc": 0,  		"phisicalFileSize": 0,  		"permissionType": 1,  		"restrictionType": 3,  		"siteCode": null,  		"draft": false,  		"onCheckout": false,  		"uuid": "EE594947-FAA8-49F2-AC8D-EE6D8A1C4CCA"  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |
