---
content_hash: bcbf3333b923ae865df5c96e90b16fb845247139cdddfabe304761650d656a9a
fetched_at: '2026-11-03T14:34:39.598448+00:00'
page_id: resource_ConfigurationServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — ConfigurationServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_ConfigurationServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# ConfigurationServiceRest Resource

System Configuration

Available Since
:   1.5.6

### GET /2.0/wcm/config/availableConfigurations

Return a list of supported configurations.

Available Since
:   1.5.6

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` 	["LS_HOST","LS_PORT", ...] ``` |

Available Since
:   1.5.6

### GET /2.0/wcm/config/downloadConfig

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object |  |

Available Since
:   1.5.6

### POST /2.0/wcm/config/updateConfigurations

Allow update system configurations.

Available Since
:   1.5.6

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [ConfigurationDataVO](https://api.fluig.com/old/json_ConfigurationDataVO.html) (JSON) | REQUIRED Request JSON (example):  ```  	[{"name":"LS_HOST","value":"ls.example.com"},  	{"name":"LS_PORT","value":"9999"}] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.5.6

### POST /2.0/wcm/config/uploadCertificate

Request Body

| media type | data type |
| --- | --- |
| multipart/form-data | object |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.6

### POST /2.0/wcm/config/uploadCertificateKey

Request Body

| media type | data type |
| --- | --- |
| multipart/form-data | object |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.6

### POST /2.0/wcm/config/validateCertificate

Request Body

| media type | data type |
| --- | --- |
| application/json | array of [ConfigurationDataVO](https://api.fluig.com/old/json_ConfigurationDataVO.html) (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.6

### POST /2.0/wcm/config/validateCertificatePassword

Request Body

| media type | data type |
| --- | --- |
| application/json | array of [ConfigurationDataVO](https://api.fluig.com/old/json_ConfigurationDataVO.html) (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.1

### GET /2.0/wcm/config/getConfiguration/{property}

Retrieve a specific system configuration

Available Since
:   1.6.1

Request Parameters

| name | type | description |
| --- | --- | --- |
| property | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { content: "true" message: null}` |
