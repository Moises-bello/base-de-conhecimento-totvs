---
content_hash: 23d81a452cb24d27c4162f827e670b396e1c03dbb562abc687913e68680b5613
fetched_at: '2026-11-03T14:34:39.602752+00:00'
page_id: resource_ContentFilesRest
product: fluig
source: rest-fluig
title: Fluig REST — ContentFilesRest Resource
type: documentation
url: https://api.fluig.com/old/resource_ContentFilesRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# ContentFilesRest Resource

ContentFiles

Available Since
:   1.5

### POST /2.0/contentfiles/upload

Upload a File

Available Since
:   1.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| fileName | query | REQUIRED File Name |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | REQUIRED InputStream file |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status, successful message   {  	 content: "OK"  	 message: {  		 message: "OK"  		 detail: "OK"  		 type: "INFO"  	 }-  } ``` |
