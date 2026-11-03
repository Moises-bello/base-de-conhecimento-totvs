---
content_hash: 7912d3b11c66cc1040917c67c740e17a0553acd8c04a43e102a335bc9c2db282
fetched_at: '2026-11-03T14:34:40.329114+00:00'
page_id: resource_SubstituteUserServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — SubstituteUserServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SubstituteUserServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SubstituteUserServiceRest Resource

Substitute User

### POST /bpm/substituteUser/create

Creates a substitute user.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SubstituteUserVO](https://api.fluig.com/old/json_SubstituteUserVO.html) (JSON) | Request JSON (example):  ``` {  	"companyId" : 1,    // (REQUIRED) company ID  	"userId" : 123,    // (OPTIONAL) user ID  	"substituteId" : 456,  // (REQUIRED) substitute ID  	"validationStartDate" : "06/09/2014", // (REQUIRED) start of replacement  	"validationFinalDate" : "18/09/2014",  // (REQUIRED) end of replacement  	"processes" : [{ // (OPTIONAL) list of process  		"process" : 10  // (REQUIRED) process ID  	},{  		"process" : 15  // (REQUIRED) process ID  	}]  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |
| application/xml | anyType (XML) |

### POST /bpm/substituteUser/remove

Removes a substitute user.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SubstituteUserVO](https://api.fluig.com/old/json_SubstituteUserVO.html) (JSON) | Request JSON (example):  ```  {  	"companyId" : 1,    // (REQUIRED) company's Id  	"userId" : 123,    // (REQUIRED) user's Id  	"substituteId" : 456  // (REQUIRED) substitute's Id  } ```  Request JSON (example):  ```  {  	"id" : 1    // (REQUIRED) Substitute record id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |
| application/xml | anyType (XML) |

### POST /bpm/substituteUser/update

Updates a substitute user.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SubstituteUserVO](https://api.fluig.com/old/json_SubstituteUserVO.html) (JSON) | Request JSON (example):  ```  {  	"companyId" : 1,    // (REQUIRED) company ID  	"id" : 1,    // (REQUIRED) Substitute record id  	"userId" : 123,    // (REQUIRED) user ID  	"substituteId" : 456,  // (REQUIRED) substitute ID  	"validationStartDate" : "06/09/2014", // (REQUIRED) start of replacement  	"validationFinalDate" : "18/09/2014",  // (REQUIRED) end of replacement  	"processes" : [{ // (OPTIONAL) list of process  		"process" : 10  // (REQUIRED) process ID  	},{  		"process" : 15  // (REQUIRED) process ID  	}]  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |
| application/xml | anyType (XML) |

### GET /bpm/substituteUser/getSubstitutesOfUser/{companyId}/{userId}

Returns a list of all users who can replace the selected user, whether they are active or not.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| userId | path | REQUIRED user's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Returns a substitutes list of user ``` |

### GET /bpm/substituteUser/getValidSubstituteOfUser/{companyId}/{userId}

Returns a list of all valid users who can replace the selected user.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| userId | path | REQUIRED user's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Returns the list of substitutes of the replaced user. ``` |

### GET /bpm/substituteUser/getValidSubstitutedUsers/{companyId}/{substituteId}

Returns a list of all the users that can be replaced by user selected

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| substituteId | path | REQUIRED substitute's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Returns the list of replaced user by substitute. ``` |

### GET /bpm/substituteUser/getAllSubstitute/{companyId}/{userId}/{substituteId}

Returns the list of substitute, whether they are active or not.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| substituteId | path | REQUIRED substitute's Id |  |
| userId | path | REQUIRED substituted's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` List of substitute ``` |

### GET /bpm/substituteUser/getAllValidSubstitute/{companyId}/{userId}/{substituteId}

Returns user information replaced if still valid.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| substituteId | path | REQUIRED substitute's Id |  |
| userId | path | REQUIRED user's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Returns the valid substitute of the substituted user. ``` |

### GET /bpm/substituteUser/getSubstitute/{companyId}/{userId}/{substituteId}

This method has been deprecated. Since 1.6, use getAllSubstitute

Returns the data of substitute, whether they are active or not.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| substituteId | path | REQUIRED substitute's Id |  |
| userId | path | REQUIRED substituted's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` The data of substitute ``` |

### GET /bpm/substituteUser/getValidSubstitute/{companyId}/{userId}/{substituteId}

This method has been deprecated. Since 1.6, use getAllValidSubstitute

Returns user information replaced if still valid.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| companyId | path | REQUIRED company's Id | required |
| substituteId | path | REQUIRED substitute's Id |  |
| userId | path | REQUIRED user's Id |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Returns the valid substitute of the substituted user. ``` |
