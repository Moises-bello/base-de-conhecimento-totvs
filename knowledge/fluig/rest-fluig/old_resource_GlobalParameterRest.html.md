---
content_hash: 41bc034457f9f3af02e4cff9e52275429203d232b55a2c6423d7b2d571edc0c3
fetched_at: '2026-11-03T14:34:39.835383+00:00'
page_id: resource_GlobalParameterRest
product: fluig
source: rest-fluig
title: Fluig REST — GlobalParameterRest Resource
type: documentation
url: https://api.fluig.com/old/resource_GlobalParameterRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# GlobalParameterRest Resource

Global parameter

Available Since
:   1.5.3

### GET /2.0/globalparameter/getMaxUploadSizeForConnect

Retrieve the max size for upload in fluig Connect.

Available Since
:   1.5.3

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	{  		"content": 104857600, // bytes result  		"message": {  			"message": "OK",  			"detail": "OK",  			"type": "INFO"  		}  	} ``` |

Available Since
:   1.6.5

### GET /2.0/globalparameter/getViewJustProcessWithApproval

Returns whether the approval will show tasks not configured for it.

Available Since
:   1.6.5

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	{  		"content": true, // boolean result  		"message": {  			"message": "OK",  			"detail": "OK",  			"type": "INFO"  		}  	} ``` |

Available Since
:   1.5.3

### POST /2.0/globalparameter/setMaxUploadSizeForConnect

Sets a new value to connect upload size parameter

Available Since
:   1.5.3

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| size | query |  | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	{  		"content": true,  		"message": {  			"message": "OK",  			"detail": "OK",  			"type": "INFO"  		}  	} ``` |
