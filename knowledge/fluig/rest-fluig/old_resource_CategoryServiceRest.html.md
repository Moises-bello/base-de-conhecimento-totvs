---
content_hash: 30628d032f0609230c8014500baf975e3007a6375731434761ee40ef2007589c
fetched_at: '2026-11-03T14:34:39.437694+00:00'
page_id: resource_CategoryServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — CategoryServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CategoryServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CategoryServiceRest Resource

Categories

Available Since
:   1.4.0

### POST /social/category/create

Create category

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CategoryVO](https://api.fluig.com/old/json_CategoryVO.html) (JSON) | ```  [{  	"parentId" : "4",  	"alias" : "Community 1",                             //Community alias  	"description" : "This is the first category",  	"type" : "FORM"                                      //FORM, ARTICLE  }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "2",  	"parentId" : "4",  	"name" : "Category 1",  	"alias" : "Community 1",                            //Community alias  	"description" : "This is the first category",  	"totalDocs" : "10",                                 //Number of docs inside this category  	"version" : "1000",  	"securityLevel" : "SECURITY_READ"                   //Secuirty Level: SECURITY_DENIED, SECURITY_READ, SECURITY_SAVE, SECURITY_MODIFY, SECURITY_FULL  }] ``` |

Available Since
:   1.4.0

### POST /social/category/update

Update category

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CategoryVO](https://api.fluig.com/old/json_CategoryVO.html) (JSON) | ```  [{  	"parentId" : "4",  	"alias" : "Community 1",                             //Community alias  	"description" : "This is the first category",  	"type" : "FORM"                                      //FORM, ARTICLE  }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | void value |

Available Since
:   1.4.0

### POST /social/category/remove/{id}

Remove category

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED category id | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | void value |

Available Since
:   1.4.0

### GET /social/category/list/{alias}/{parent}

List categories

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED Community alias |  |
| parent | path | REQUIRED Folder to list categories for | int |
| limit | query | REQUIRED Limit | required |
| offset | query | REQUIRED Offset | required |
| pattern | query | Word to search for |  |
| type | query | REQUIRED Type of category's list |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "2",  	"parentId" : "4",  	"name" : "Category 1",  	"alias" : "Community 1",                            //Community alias  	"description" : "This is the first category",  	"totalDocs" : "10",                                 //Number of docs inside this category  	"version" : "1000",  	"securityLevel" : "SECURITY_READ"                   //Secuirty Level: SECURITY_DENIED, SECURITY_READ, SECURITY_SAVE, SECURITY_MODIFY, SECURITY_FULL  }] ``` |

Available Since
:   1.4.0

### GET /social/category/root/{alias}/{type}

Get root folder of community by type

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED Community alias |
| type | path | REQUIRED Type of category's list |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | root folder id |

Available Since
:   1.4.0

### GET /social/category/find/{alias}/{id}/{type}

Find category by id

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED Community alias |  |
| id | path | REQUIRED category id | int |
| type | path | REQUIRED Category's type |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "2",  	"parentId" : "4",  	"name" : "Category 1",  	"alias" : "Community 1",                            //Community alias  	"description" : "This is the first category",  	"totalDocs" : "10",                                 //Number of docs inside this category  	"version" : "1000",  	"securityLevel" : "SECURITY_READ"                   //Secuirty Level: SECURITY_DENIED, SECURITY_READ, SECURITY_SAVE, SECURITY_MODIFY, SECURITY_FULL  }] ``` |

Available Since
:   1.4.0

### GET /social/category/findparent/{alias}/{id}/{parent}

Find category by name

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED Community alias |  |
| id | path | REQUIRED Category's id |  |
| parent | path | REQUIRED Category's parent id | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "2",  	"parentId" : "4",  	"name" : "Category 1",  	"alias" : "Community 1",  	"description" : "This is the first category",  	"totalDocs" : "10",                                 //Number of docs inside this category  	"version" : "1000",  	"securityLevel" : "SECURITY_READ"                   //Secuirty Level: SECURITY_DENIED, SECURITY_READ, SECURITY_SAVE, SECURITY_MODIFY, SECURITY_FULL  }] ``` |
