---
content_hash: 54ae858427229866a8aaa1f941771f023ad4e9bc51beff427906c1057fdcf126
fetched_at: '2026-11-03T14:34:39.820588+00:00'
page_id: resource_FilterService
product: fluig
source: rest-fluig
title: Fluig REST — FilterService Resource
type: documentation
url: https://api.fluig.com/old/resource_FilterService.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# FilterService Resource

Central Tasks Filter Services

### GET /ecm/filters

Returns the all the user filters.

Request Parameters

| name | type | description |
| --- | --- | --- |
| type | query | filter's type (PROCESS|DOCUMENT) for filtering, empty or null for all. |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"id" : "10",							// filter id  	"name" : "some-key",					// filter name  	"type" : "(DOCUMENT|PROCESS)" 		// filter type  } ``` |

### POST /ecm/filters/create

Creates a central task filter.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CentralTaskFilterVO](https://api.fluig.com/old/json_CentralTaskFilterVO.html) (JSON) | Request JSON (example):  ```  {  	"name" : "Sample Filter",    //filter's name (REQUIRED)  	"type" : "(DOCUMENT|PROCESS)",    //filter's type (REQUIRED)  	"processFields" : [{  		"key" : "processInstanceId",    //the process field's key (REQUIRED)  		"value" : "10",   //the process field's value  		"visible" : "true"   //if true the process field is visible on result table  	},{  		"key" : "processId",    //the process field's key (REQUIRED)  		"value" : "travel_request"   //the process field's value  	}],     // process type filter fields (ONLY available for PROCESS filter type)  	"formFields" : [{  		"key" : "userCode",    //the form field's key (REQUIRED)  		"value" : "joao.souza",   //the form field's value  		"visible" : "true"   //if true the form field is visible on result table  	},{  		"key" : "userName",    //the form field's key (REQUIRED)  		"value" : "travel_request"   //the form field's value  	}],     // form type filter fields (ONLY available for PROCESS filter type)  	"documentFields" : [{  		"key" : "some-key",    //the document field's key  		"value" : "some-value",   //the document field's value  	}],     // document type filter fields (ONLY available for DOCUMENT filter type)  	"orderKey" : "processInstanceId",    //filter's order field key (ONLY available for PROCESS filter type)  	"orderType" : "(ASC|DESC)",    //filter's order type (ONLY available for PROCESS filter type)  	"processId" : "travel_request"    //process id (REQUIRED for PROCESS filter type with FORM FIELDS)  }     @return  ```  This method just return HTTP 200 status with a success message ``` ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### POST /ecm/filters/remove

Removes a central task filter.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CentralTaskFilterVO](https://api.fluig.com/old/json_CentralTaskFilterVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "2",    //filter's id (REQUIRED)  }     @return  ```  This method just return HTTP 200 status with a success message ``` ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### POST /ecm/filters/update

Updates a central task filter.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CentralTaskFilterVO](https://api.fluig.com/old/json_CentralTaskFilterVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "2",    //filter's id (REQUIRED)  	"name" : "Sample Filter",    //filter's name (REQUIRED)  	"type" : "(DOCUMENT|PROCESS)",    //filter's type (REQUIRED)  	"processFields" : [{  		"key" : "processInstanceId",    //the process field's key (REQUIRED)  		"value" : "10",   //the process field's value  		"visible" : "true"   //if true the process field is visible on result table  	},{  		"key" : "processId",    //the process field's key (REQUIRED)  		"value" : "travel_request"   //the process field's value  	}],     // process type filter fields (ONLY available for PROCESS filter type)  	"formFields" : [{  		"key" : "userCode",    //the form field's key (REQUIRED)  		"value" : "joao.souza",   //the form field's value  		"visible" : "true"   //if true the form field is visible on result table  	},{  		"key" : "userName",    //the form field's key (REQUIRED)  		"value" : "travel_request"   //the form field's value  	}],     // form type filter fields (ONLY available for PROCESS filter type)  	"documentFields" : [{  		"key" : "some-key",    //the document field's key  		"value" : "some-value",   //the document field's value  	}],     // document type filter fields (ONLY available for DOCUMENT filter type)  	"orderKey" : "processInstanceId",    //filter's order field key (ONLY available for PROCESS filter type)  	"orderType" : "(ASC|DESC)",    //filter's order type (ONLY available for PROCESS filter type)  	"processId" : "travel_request"    //process id (REQUIRED for PROCESS filter type with FORM FIELDS)  }     @return  ```  This method just return HTTP 200 status with a success message ``` ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### GET /ecm/filters/{id}

Returns an specific filter

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED filter's id. | regex: \d+ |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"id" : "10",							// filter id  	"name" : "some-key",					// filter name  	"type" : "(DOCUMENT|PROCESS)" 		// filter type  } ``` |
