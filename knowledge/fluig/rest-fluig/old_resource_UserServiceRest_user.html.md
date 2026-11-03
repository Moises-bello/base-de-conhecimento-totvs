---
content_hash: c0de8a805f99cb4cd8c4b5c651a57af5b52dfd507fc3f777a5f572c5a0cb14d2
fetched_at: '2026-11-03T14:34:40.439379+00:00'
page_id: resource_UserServiceRest_user
product: fluig
source: rest-fluig
title: Fluig REST — UserServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_UserServiceRest_user.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# UserServiceRest Resource

User

Available Since
:   1.5

### POST /wcm/user/create

Create an user  
  
If you have Identity enabled, you'll have to follow the password requirements below:  
Minimum 8, maximum 16 characters with at least 1 uppercase, 1 lowercase, 1 digit and 1 special character

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [UserVO](https://api.fluig.com/old/json_UserVO_vo.html) (JSON) | Request JSON (example):  ``` {                	"login" : "johndoe", // User's login                	"firstName" : "John", // User's first name                	"lastName" : "Doe", // User's last name                	"fullName" : "John Nash Doe", // User's full name                	"password" : "MyP@ssword81", // User's plain text password                	"email" : "johndoe@mycorp.com", // User's email                	"roles" : ["user", "financial"], // User's roles (optional)                	"groups" : ["directors", "managers"], // User's groups (optional)                	"customData": { // User's custom data (optional)                		"UserProjects" : "VP Fluig",                		"UserEmailHTML" : true                	}                } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return HTTP 200 status when the action is successful ``` |

Available Since
:   1.5

### POST /wcm/user/deleteByIdpId

Deactivate an user

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Request JSON (example):  ``` {                	"ipd_id" : "0srv639ypa9gs99v1435252241090", // IDP ID                } ``` |
| application/xml | string (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return HTTP 200 status when the action is successful ``` |

Available Since
:   1.5

### GET /wcm/user/findActiveUsersUsingFilter

Find only active users using filters

Available Since
:   1.5

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | Number of results to return | 20 | required |
| offset | query | Search offset | 0 | required |
| orderby | query | Field to order results by example: fullName\_ASC, email\_DESC | fullName\_ASC |  |
| pattern | query | Pattern to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ``` [{               	"id" : "1",               	"userId" : "1",               	"login" : "adm",               	"firstName" : "John",               	"lastName" : "Doe",               	"fullName" : "John Doe",               	"email" : "john@doe.com",               	"state" : "ACTIVE",               	"birthDay" : null,               	"tenantId" : "1",               	"tenantCode" : "1",               	"locationId" : "1",               	"locationCode" : null,               	"data" : {},               	"roles" : [],               	"groups" : [],               	"userCode" : "adm",               	"idpId" : null,               	"userType" : "NORMAL",               	"firstAccess" : null,               	"clouds" : null,               	"description" : "John Doe",               	"code" : "adm",               	"typeCode" : "User",           }] ``` |

Available Since
:   1.5

### GET /wcm/user/findUsingFilter

Find users using filters

Available Since
:   1.5

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | Number of results to return | 20 | required |
| offset | query | Search offset | 0 | required |
| orderby | query | Field to order results by example: fullName\_ASC, email\_DESC | fullName\_ASC |  |
| pattern | query | Pattern to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ``` [{               	"id" : "1",               	"userId" : "1",               	"login" : "adm",               	"firstName" : "John",               	"lastName" : "Doe",               	"fullName" : "John Doe",               	"email" : "john@doe.com",               	"state" : "ACTIVE",               	"birthDay" : null,               	"tenantId" : "1",               	"tenantCode" : "1",               	"locationId" : "1",               	"locationCode" : null,               	"data" : {},               	"roles" : [],               	"groups" : [],               	"userCode" : "adm",               	"idpId" : null,               	"userType" : "NORMAL",               	"firstAccess" : null,               	"clouds" : null,               	"description" : "John Doe",               	"code" : "adm",               	"typeCode" : "User",           }] ``` |
