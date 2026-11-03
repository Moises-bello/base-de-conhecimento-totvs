---
content_hash: bc2a3fca392cb180da8c8146c838bb7ce27e8344f5c28d302e43a98e20be2aa1
fetched_at: '2026-11-03T14:34:39.268202+00:00'
page_id: resource_AdHocServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — AdHocServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_AdHocServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# AdHocServiceRest Resource

AdHoc Processes (Task List)

### POST /bpm/adhoc/create

Creates adhoc process tasks.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AdHocProcessVO](https://api.fluig.com/old/json_AdHocProcessVO.html) (JSON) | Request JSON (example):  ```  {  	"processInstanceId" : 1,      // (REQUIRED) process instance number  	"stateSequence" : 10,    // (REQUIRED) adhoc subprocess sequence  	"name" : "Pendências Reunião",    //adhoc process name  	"description" : "Tarefas pendentes da reunião"    //adhoc process description  	"adHocTasks" : [{ // (REQUIRED)  		"name" : "Desenvolver Relatório"    // (REQUIRED)  adhoc task name  		"dueDate" : "10/05/2014"   // (REQUIRED) adhoc task due date  		"responsible" : "pedro.teixeira"   // (REQUIRED) adhoc task responsible  	},{  		"name" : "Contactar Clientes"    // (REQUIRED) adhoc task name  		"dueDate" : "15/05/2014"   // (REQUIRED) adhoc task due date  		"responsible" : "joao.souza"   // (REQUIRED) adhoc task responsible  	}]  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### GET /bpm/adhoc/{process}/{sequence}

Returns an adhoc process.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| process | path | REQUIRED process process instance number | int |
| sequence | path | REQUIRED sequence adhoc subprocess sequence | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"processInstanceId" : 1,      //process instance number  	"stateSequence" : 10,    //adhoc subprocess sequence  	"name" : "Pendências Reunião",    //adhoc process name  	"description" : "Tarefas pendentes da reunião"    //adhoc process description  	"adHocTasks" : [{  		"name" : "Desenvolver Relatório"    //adhoc task name  		"dueDate" : "10/05/2014"   //adhoc task due date  		"responsible" : "pedro.teixeira"   //adhoc task responsible  	},{  		"name" : "Contactar Clientes"    //adhoc task name  		"dueDate" : "15/05/2014"   //adhoc task due date  		"responsible" : "joao.souza"   //adhoc task responsible  	}]  } ``` |
