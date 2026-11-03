---
content_hash: d4308cee3b315e11b66520db566359deff667bdc8b43e16b3eb40b75e83f3b2f
fetched_at: '2026-11-03T14:34:39.416539+00:00'
page_id: resource_CardIndexRest
product: fluig
source: rest-fluig
title: Fluig REST — CardIndexRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CardIndexRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CardIndexRest Resource

Card Index

Available Since
:   1.5.0

### POST /2.0/cardindexes/create

Create a index card

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CardIndexCreateVO](https://api.fluig.com/old/json_CardIndexCreateVO.html) (JSON) | REQUIRED Request JSON (example):  ``` {  	 "tenantId" : 100, // tenant's id  	 "publisherId" : 1, // publisherId  	 "documentDescription" : Document Description, // Document Description  	 "cardDescription" : Card Description, // Card Description  	 "datasetName" : Dataset Name, // Dataset Name  	 "persistenceType" : 123// Persistence Type  	 "attachments": [  		{  			"principal": false,  			"attach": true,  			"fileName": /FLUIGADHOC.html  		}  	]  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status, successful message   {  	"content": {  		"tenantId": 1,  		"documentId": 257,  		"parentDocumentId": null,  		"publisherId": "fluig.user",  		"documentDescription": "Document Description",  		"cardDescription": "Card Description",  		"datasetName": "Dataset Name",  		"persistenceType": 0,  		"attachments": [  			{  				"fileName": "test.xml",  				"principal": true,  				"attach": true  			}  		]  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5

### GET /2.0/cardindexes/getDefaultFormFolderId

Retrieve Default form folder id

Available Since
:   1.5

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method return an Integer and successful message   {  	"content": 0,  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.0

### POST /2.0/cardindexes/delete/{documentId}

Delete a index card

Available Since
:   1.5.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | :100 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status, successful message   {  	 content: null  	 message: {  		 message: "Anexo do formulário removido com sucesso!"  		 detail: "Anexo do formulário removido com sucesso!"  		 type: "INFO"  	 }-  } ``` |
