---
content_hash: c823c89f230e7c6c451b5cbe0bef866ae851664622d63edcf73456c336dd8138
fetched_at: '2026-11-03T14:34:40.573740+00:00'
page_id: resource_WorkflowRest
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowRest Resource
type: documentation
url: https://api.fluig.com/old/resource_WorkflowRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# WorkflowRest Resource

Workflow

Available Since
:   1.5.11

### POST /2.0/workflows/assumeProcessTask

Assign selected instance in pool to the colleague

Available Since
:   1.5.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AssumeProcessTaskVO](https://api.fluig.com/old/json_AssumeProcessTaskVO.html) (JSON) | Request JSON (example):`{ "colleagueId" : "adm", // Colleague id "processInstanceId" : 1, // Process instance id "movementSequence" : 1, // Sequence from the task to take "replacementId" : "usr" // User id from the replacement taking the task for the user }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a AssumeProcessTaskResult  { "content": { "colleagueId" : "adm", // Colleague Id "processInstanceId" : 1, // Process Instance Id "movementSequence" : 1, // Movement Sequence from the task "status" : "SUCCESS", // REST call status "message" : "SUCCESS", // Error message or SUCCESS if without problems "errorCode" : null, // Code of the error, null if without problems "complement" : null, // Success message, null if with problems }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.11

### POST /2.0/workflows/assumeProcessTasks

Assign selected instances in pool to the specified colleagues

Available Since
:   1.5.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AssumeProcessTasksVO](https://api.fluig.com/old/json_AssumeProcessTasksVO.html) (JSON) | Request JSON (example):`{"assumeProcessTaskList" : [ { "colleagueId" : "adm", // Colleague id "processInstanceId" : 1, // Process instance id "movementSequence" : 1, // Sequence from the task to take "replacementId" : "usr" // User id from the replacement taking the task for the user }, { "colleagueId" : "usr", // Colleague id "processInstanceId" : 2, // Process instance id "movementSequence" : 1 // Sequence from the task to take } ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a AssumeProcessTasksResult  { { "content": "successCount" : 1, "failCount" : 0, "takeProcessTaskResults": [{ "colleagueId" : "adm", // Colleague Id "processInstanceId" : 1, // Process Instance Id "movementSequence" : 1, // Movement Sequence from the task "status" : "SUCCESS", // REST call status "message" : "SUCCESS", // Error message or SUCCESS if without problems "errorCode" : null, // Code of the error, null if without problems "complement" : null, // Success message, null if with problems }] }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.6.0

### POST /2.0/workflows/cancelInstance

Cancel instance process

Available Since
:   1.6.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CancelInstanceVO](https://api.fluig.com/old/json_CancelInstanceVO.html) (JSON) | Request JSON (example):`{ "processInstanceId" : 1, //Process instance id "cancelText" : "Canceled", //Cancel text "replacedId" : "usr" //User id from the replaced cancel process instance }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a CancelInstanceResult  { "content": { "processInstanceId" : 1, // Process Instance Id "status" : "SUCCESS", // REST call status "message" : "SUCCESS", // Error message or SUCCESS if without problems "errorCode" : null, // Code of the error, null if without problems }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.6.0

### POST /2.0/workflows/cancelInstances

Cancel instances process

Available Since
:   1.6.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CancelInstancesVO](https://api.fluig.com/old/json_CancelInstancesVO.html) (JSON) | Request JSON (example):  ``` {    "cancelText" : "Canceled", //Cancel text    "cancelInstanceList" : [       {          "processInstanceId" : 1, //Process instance id          "cancelText" : "Canceled as a replacement", //Cancel text          "replacedId" : "usr" //User id from the replaced cancel process instance       },       {          "processInstanceId" : 2, //Process instance id       }    ] } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a CancelInstancesResult             {            	{            	"content":            	 "successCount" : 1,            	 "failCount" : 0,            	 "cancelInstanceResults": [{            		"processInstanceId" : 1, // Process Instance Id            		"status" : "SUCCESS", // REST call status            		"message" : "SUCCESS", // Error message or SUCCESS if without problems            		"errorCode" : null, // Code of the error, null if without problems            	}]            },            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.5.8

### POST /2.0/workflows/createProcessObservation

Create observation of an existing process.  
  
Return the observation.

Available Since
:   1.5.8

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ProcessObservationVO](https://api.fluig.com/old/json_ProcessObservationVO.html) (JSON) | Request JSON (example):`{ "processInstanceId" : 15 // Id do artigo que será atualizado (REQUIRED) "stateSequence" : 4 // Alias da comunidade onde o artigo foi publicado (REQUIRED) "threadSequence" : 2 // Titulo do Artigo (REQUIRED) "observation" : "recurso liberado" // Versão do artigo que será atualizado (REQUIRED) " }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method returns VO of process observation and a message with the result status  { "content": { "id": 15, "colleagueId": "RT0542", "processInstanceId": 2441, "observationDate": "2016-02-04 12:22:11", "stateSequence": 4, "threadSequence": 2, "observation": "recurso liberado" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.6

### GET /2.0/workflows/listProcess

Retrieve all processes  
  
Return all processes.

Available Since
:   1.6

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query |  | 10 | required |
| offset | query |  | 0 | required |
| pattern | query |  |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of ProcessDefinitionVO   {  	"content": [  		     {  		         "processId": "FLUIGADHOC",  		         "processDescription": "Listar Tarefas"  		     },  		     {  		         "processId": "FLUIGADHOCPROCESS",  		         "processDescription": "Executar Tarefa Ad Hoc"  		     }  	],  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.13

### GET /2.0/workflows/findActiveTasks/{processInstanceId}

Retrieve active tasks  
  
Return a list of active tasks.

Available Since
:   1.5.13

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| processInstanceId | path | Process instance Id | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ProcessInstanceInfoVO  { "content": { "companyId": 1, // company id "processId": "consenso", // process id "processVersion": 3, // process version "processInstanceId": 1000209, // process instance number "startDateProcess": "2016-11-11 08:46:50", // process start date "formId": 26102, // process form id "formVersion": 1000, // process form version "formValues": { // form values "id": "value" "companyid": "1", "nome": "Fluig", "tableid": "principal", "documentid": "26102", "url": "http://fluig.com", "cardid": "26101", "version": "1000" }, "taskObservations": [ // list of process observation { "id": 5, //comment's id "colleagueId": "adm", // commenting user "processInstanceId": 1000209, // process instance number "observationDate": "2016-11-11 08:47:01", // comment's date "stateSequence": 2, // state sequence "threadSequence": 0, // thread sequence of comment "movementSequence": 2, // movement sequence of comment "observation": "<p>second comment</p>\n" // comment }, { "id": 4, "colleagueId": "adm", // commenting user "processInstanceId": 1000209, // process instance number "observationDate": "2016-11-11 08:46:50", // comment's date "stateSequence": 1, // state sequence "threadSequence": 0,// thread sequence of comment "movementSequence": 1, // movement sequence of comment "observation": "<p>first comment</p>\n" // comment } ], "attachments": [ // list of process attachments { "documentId": 26103, // attachment id "version": 1000, // attachment version "originalMovementSequence": 2, // movement that the attachment was added "colleagueId": "adm", // user who added the attachment "attachedDate": "2016-11-11 14:01:42", // date that the attachment was added "description": "arquivo.png" // attachment name }, { "documentId": 26104, // attachment id "version": 1000, // attachment version "originalMovementSequence": 2, // movement that the attachment was added "colleagueId": "adm", // user who added the attachment "attachedDate": "2016-11-11 14:01:42", // date that the attachment was added "description": "outro_arquivo.pdf" // attachment name } ], "tasksInfo": [ // list of task information { "movementSequence": 2, // movement sequence "transferredSequence": 1, // thread sequence "stateSequence": 2, // state sequence "startDateTask": "2016-11-11 08:46:50", // task's start date "colleagueName": "adm adm", // responsible "status": 0, // task status (NOT_COMPLETED(0), PENDING_CONSENSUS(1), COMPLETED(2), TRANSFERRED(3), CANCELED(4)) "state": { // state data "tenantId": 1, // company id "sequence": 2, // state sequence "stateName": "a", // state name "stateDescription": "a" // state description }, "taskDeadline": "2016-12-11 14:01:42", // task deadline "expired": false, // task is expired "active": true // task is active } ] }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5

### GET /2.0/workflows/getProcessVersion/{processId}

Retrieve process version  
  
Return process version.

Available Since
:   1.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| processId | path | Request JSON (example):  ```  {  	"processId" : "1", // Process id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return an Integer and successful message   {  	"content": 0,  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/listSlaProcess

Retrieve all processes  
  
Return all processes whith Sla. Configured

Available Since
:   1.6.1

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of ProcessDefinitionVO   {  	"content": [  		     {  		         "processId": "FLUIGADHOC",  		         "processDescription": "Listar Tarefas"  		     },  		     {  		         "processId": "FLUIGADHOCPROCESS",  		         "processDescription": "Executar Tarefa Ad Hoc"  		     }  	],  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla

Make a resume of the found requests with configurated SLA.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Tasks' assignees user code. |  |
| assigneeLocals | query | Comma-separated list that contains the activity's responsible local code that will be considered in the search. |  |
| calculate | query | If the rest will bring the calculated variables related to time e percentage. | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "actualTasks" and/or "cardFields" and/or "requesterLocal" and/or "assigneeLocal" field to return it. |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| manager | query | A manager to be used as parameter to define the processes. |  |
| order | query | Order by fields. It's possible to order by: processInstanceId, deadlineDate, processId, requesterCode, requesterName, startDate and endDate. If you want a "DESC" ordenation, put a minus (-) simbol before the order parameter. | -processInstanceId |
| page | query | Page number. | 1 |
| pageSize | query | Size of the page. | 0 |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| requester | query | Request's requester user code. |  |
| requesterLocals | query | Comma-separated list that contains the requester's local code that will be considered in the search. |  |
| statusRequired | query | List separated by comma containing all the status that are being requested, all other counters of the object will not be part of the search. If no values are specified, all status will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResponseEnvelopeVO  { "content": { "hasNext": "false", "total": "1", "items": [{ "percentageConcluded" : 100, // Reached percentage of the time passed on the requests sla. "deadlineDate" : "2017-03-24 00:00:00", // Deadline date of the request. "processInstanceId" : 1, // Process instance (Request) Id. "processId" : "PROCESS_ID", // Process id. "processDescription" : "Generic Process", // Process description. "requesterCode" : "user", // Requester's user code. "requesterName" : "User User", // Requester's full name. "remainingTime" : 0, // Remaining sla time of the request. "fullTime" : 10000, // Request's sla full time. "statusSla" : "EXPIRED", // Status of the SLA. 0 - OPEN, 1 - ON_TIME, 2 - WARNING, 3 - EXPIRED. "statusRequest" : "FINALIZED", // Status of the request. 0 - OPEN, 1 - CANCELED, 2 - FINALIZED. "startDate" : "2017-03-24 00:00:00", // Request's start date. "processVersion" : 1000, // Process version. "endDate" : "2017-03-24 00:00:00", // Request's finalized date. "warningDate" : "2017-03-24 00:00:00", // Request's warning date. "actualTasks" : { // Only returns if "expand" field is declared with "actualTasks". It's a list of RequestTaskSLAVO. "activityDescription" : "Activity", // Current task's activity description. "activityCode" : "Activity", // Current task's activity code. "assigneeName" : "User User", // Current task's assignee name (if the request is finalized this field is not present). "assigneeCode" : "user", // Current task's assignee code (if the request is finalized this field is not present). "assigneeLocal" : { // Only returns if "expand" field is declared with "assigneeLocals" and "actualTasks". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }, "cardFields": {}, "requesterLocal" : { // Only returns if "expand" field is declared with "requesterLocals". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }] }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Assignee |  |
| calculate | query | To calculate SLA | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "cardFields" |  |
| finalStartDate | query | Final Start Date |  |
| initialStartDate | query | Initial Start Date |  |
| manager | query | Manager |  |
| page | query | Page | 1 |
| pageSize | query | Page Size | 0 |
| processId | query | Process Id |  |
| requester | query | Requester |  |
| statusTypeTaskRequest | query | 1 onTime; 2 warning, 3 Expired Status Required | 1 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.6

### GET /2.0/workflows/getAvailableProcess/{tenantId}/{userId}

Retrieve available process  
  
Return a list of available process. The first level is the category of process, the second level is the process.

Available Since
:   1.5.6

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| tenantId | path | Request JSON (example):  ```  {  	"tenantId" : "1", // Tenant id  } ``` | required |
| userId | path | Request JSON (example):  ```  {  	"userId" : "adm", // User id  } ``` |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of ProcessVersionVO   {  	"content": {  		"companyId": 1,  		"processId": "Folder",  		"formId": 0,  		"versionDescription": "Recursos Humanos",  		"children": [  		     {  		         "companyId": 1,  		         "processId": "processo_contratacao",  		         "formId": 0,  		         "versionDescription": "Contratação",  		         "children": null,  		         "favorite": true,  		         "selected": true  		     },  		     {  		         "companyId": 1,  		         "processId": "processo_indicacao",  		         "formId": 0,  		         "versionDescription": "Indicação de talento",  		         "children": null,  		         "favorite": false,  		         "selected": false  		     },  		     {  		         "companyId": 1,  		         "processId": "processo_demissao",  		         "formId": 0,  		         "versionDescription": "Demissão de colaborador",  		         "children": null,  		         "favorite": false,  		         "selected": false  		     }  		 ],  		"favorite": false,  		"selected": false  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/resume

Make a resume of the found requests with configurated SLA.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Tasks' assignees user code. |  |
| assigneeLocals | query | Comma-separated list that contains the activity's responsible local code that will be considered in the search. |  |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| countersRequired | query | Comma-separated list that contains all the counters that are being requested, all other counters of the object not return. If no values are specified, all counters will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| manager | query | A manager to be used as parameter to define the processes. |  |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| requester | query | Request's requester user code. |  |
| requesterLocals | query | Comma-separated list that contains the requester's local code that will be considered in the search. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResumeRequestsSLAVO  { "content": { "finishedRequests" : 1, // General finished requests counter. A number if the counter is requested, null if it's not. "finishedExpiredRequests" : 1, // Expired finished requests counter. A number if the counter is requested, null if it's not. "finishedOnTimeRequests" : 1, // Finished requests on time counter. A number if the counter is requested, null if it's not. "finishedWarningRequests" : 1, // Warned finished requests counter. A number if the counter is requested, null if it's not. "canceledRequests" : 1, // General canceled requests counter. A number if the counter is requested, null if it's not. "canceledExpiredRequests" : 1, // Expired canceled requests counter. A number if the counter is requested, null if it's not. "canceledOnTimeRequests" : 1, // Canceled requests on time counter. A number if the counter is requested, null if it's not. "canceledWarningRequests" : 1, // Warned canceled requests counter. A number if the counter is requested, null if it's not. "openRequests" : 1, // General open requests counter. A number if the counter is requested, null if it's not. "openExpiredRequests" : 1, // Expired open requests counter. A number if the counter is requested, null if it's not. "openOnTimeRequests" : 1, // Open requests on time counter. A number if the counter is requested, null if it's not. "openWarningRequests" : 1 // Warned open requests counter. A number if the counter is requested, null if it's not. }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/resume

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query |  |  |
| finalStartDate | query |  |  |
| initialStartDate | query |  |  |
| manager | query |  |  |
| processId | query |  |  |
| requester | query |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/{processInstanceId}/sla

Make a resume of the found a specific request with configurated SLA.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| processInstanceId | path | Process Instance Id to be found. |  |
| calculate | query | If the rest will bring the calculated variables related to time e percentage. | false |
| expand | query | Declare the expandable "actualTasks" and/or "cardFields" and/or "requesterLocal" and/or "assigneeLocal" field to return it. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a RequestSLAVO  { "content": { "percentageConcluded" : 100, // Reached percentage of the time passed on the requests sla. "deadlineDate" : "2017-03-24 00:00:00", // Deadline date of the request. "processInstanceId" : 1, // Process instance (Request) Id. "processId" : "PROCESS_ID", // Process id. "processDescription" : "Generic Process", // Process description. "requesterCode" : "user", // Requester's user code. "requesterName" : "User User", // Requester's full name. "remainingTime" : 0, // Remaining sla time of the request. "fullTime" : 10000, // Request's sla full time. "statusSla" : "EXPIRED", // Status of the SLA. 0 - OPEN, 1 - ON_TIME, 2 - WARNING, 3 - EXPIRED. "statusRequest" : "FINALIZED", // Status of the request. 0 - OPEN, 1 - CANCELED, 2 - FINALIZED. "startDate" : "2017-03-24 00:00:00", // Request's start date. "processVersion" : 1000, // Process version. "endDate" : "2017-03-24 00:00:00", // Request's finalized date. "warningDate" : "2017-03-24 00:00:00", // Request's warning date. "actualTasks" : { // Only returns if "expand" field is declared with "actualTasks". It's a list of RequestTaskSLAVO. "activityDescription" : "Activity", // Current task's activity description. "activityCode" : "Activity", // Current task's activity code. "assigneeName" : "User User", // Current task's assignee name (if the request is finalized this field is not present). "assigneeCode" : "user", // Current task's assignee code (if the request is finalized this field is not present). "assigneeLocal" : { // Only returns if "expand" field is declared with "assigneeLocals" and "actualTasks". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }, "cardFields" : {}, "requesterLocal" : { // Only returns if "expand" field is declared with "requesterLocals". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5.8

### GET /2.0/workflows/findObservations/{processInstanceId}/{stateSequence}/{threadSequence}

Retrieve available process observations  
  
Return a list of process observations.

Available Since
:   1.5.8

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| processInstanceId | path | Process instance Id | int |
| stateSequence | path | State sequence | int |
| threadSequence | path | Thread Sequence | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a list of ProcessObservationVO  { "content": [{ "id": 15, "colleagueId": "RT0542", "processInstanceId": 2441, "observationDate": "2016-04-04 15:21:26", "stateSequence": 4, "threadSequence": 2, "observation": "recurso liberado" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" },{ "id": 16, "colleagueId": "RT0542", "processInstanceId": 2441, "observationDate": "2016-04-04 11:32:26", "stateSequence": 4, "threadSequence": 2, "observation": "E-mail criado!" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/assignee/me

Make a resume of the found requests with configurated SLA assuming that the logged user is the assignee.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assigneeLocals | query | Comma-separated list that contains the activity's responsible local code that will be considered in the search. |  |
| calculate | query | If the rest will bring the calculated variables related to time e percentage. | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "actualTasks" and/or "cardFields" and/or "requesterLocal" and/or "assigneeLocal" field to return it. |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| manager | query | A manager to be used as parameter to define the processes. |  |
| order | query | Order by fields. It's possible to order by: processInstanceId, deadlineDate, processId, requesterCode, requesterName, startDate and endDate. If you want a "DESC" ordenation, put a minus (-) simbol before the order parameter. | -processInstanceId |
| page | query | Page number. | 1 |
| pageSize | query | Size of the page. | 0 |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| requester | query | Request's requester user code. |  |
| requesterLocals | query | Comma-separated list that contains the requester's local code that will be considered in the search. |  |
| statusRequired | query | List separated by comma containing all the status that are being requested, all other counters of the object will not be part of the search. If no values are specified, all status will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResponseEnvelopeVO  { "content": { "hasNext": "false", "total": "1", "items": [{ "percentageConcluded" : 100, // Reached percentage of the time passed on the requests sla. "deadlineDate" : "2017-03-24 00:00:00", // Deadline date of the request. "processInstanceId" : 1, // Process instance (Request) Id. "processId" : "PROCESS_ID", // Process id. "processDescription" : "Generic Process", // Process description. "requesterCode" : "user", // Requester's user code. "requesterName" : "User User", // Requester's full name. "remainingTime" : 0, // Remaining sla time of the request. "fullTime" : 10000, // Request's sla full time. "statusSla" : "EXPIRED", // Status of the SLA. 0 - OPEN, 1 - ON_TIME, 2 - WARNING, 3 - EXPIRED. "statusRequest" : "FINALIZED", // Status of the request. 0 - OPEN, 1 - CANCELED, 2 - FINALIZED. "startDate" : "2017-03-24 00:00:00", // Request's start date. "processVersion" : 1000, // Process version. "endDate" : "2017-03-24 00:00:00", // Request's finalized date. "warningDate" : "2017-03-24 00:00:00", // Request's warning date. "actualTasks" : { // Only returns if "expand" field is declared with "actualTasks". It's a list of RequestTaskSLAVO. "activityDescription" : "Activity", // Current task's activity description. "activityCode" : "Activity", // Current task's activity code. "assigneeName" : "User User", // Current task's assignee name (if the request is finalized this field is not present). "assigneeCode" : "user", // Current task's assignee code (if the request is finalized this field is not present). "assigneeLocal" : { // Only returns if "expand" field is declared with "assigneeLocals" and "actualTasks". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }, "cardFields": {}, "requesterLocal" : { // Only returns if "expand" field is declared with "requesterLocals". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }] }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/manager/me

Make a resume of the found requests with configurated SLA assuming that the logged user is a manager from the process.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Request's assignee user code. |  |
| assigneeLocals | query | Comma-separated list that contains the activity's responsible local code that will be considered in the search. |  |
| calculate | query | If the rest will bring the calculated variables related to time e percentage. | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "actualTasks" and/or "cardFields" and/or "requesterLocal" and/or "assigneeLocal" field to return it. |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| order | query | Order by fields. It's possible to order by: processInstanceId, deadlineDate, processId, requesterCode, requesterName, startDate and endDate. If you want a "DESC" ordenation, put a minus (-) simbol before the order parameter. | -processInstanceId |
| page | query | Page number. | 1 |
| pageSize | query | Size of the page. | 0 |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| requester | query | Request's requester user code. |  |
| requesterLocals | query | Comma-separated list that contains the requester's local code that will be considered in the search. |  |
| statusRequired | query | List separated by comma containing all the status that are being requested, all other counters of the object will not be part of the search. If no values are specified, all status will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResponseEnvelopeVO  { "content": { "hasNext": "false", "total": "1", "items": [{ "percentageConcluded" : 100, // Reached percentage of the time passed on the requests sla. "deadlineDate" : "2017-03-24 00:00:00", // Deadline date of the request. "processInstanceId" : 1, // Process instance (Request) Id. "processId" : "PROCESS_ID", // Process id. "processDescription" : "Generic Process", // Process description. "requesterCode" : "user", // Requester's user code. "requesterName" : "User User", // Requester's full name. "remainingTime" : 0, // Remaining sla time of the request. "fullTime" : 10000, // Request's sla full time. "statusSla" : "EXPIRED", // Status of the SLA. 0 - OPEN, 1 - ON_TIME, 2 - WARNING, 3 - EXPIRED. "statusRequest" : "FINALIZED", // Status of the request. 0 - OPEN, 1 - CANCELED, 2 - FINALIZED. "startDate" : "2017-03-24 00:00:00", // Request's start date. "processVersion" : 1000, // Process version. "endDate" : "2017-03-24 00:00:00", // Request's finalized date. "warningDate" : "2017-03-24 00:00:00", // Request's warning date. "actualTasks" : { // Only returns if "expand" field is declared with "actualTasks". It's a list of RequestTaskSLAVO. "activityDescription" : "Activity", // Current task's activity description. "activityCode" : "Activity", // Current task's activity code. "assigneeName" : "User User", // Current task's assignee name (if the request is finalized this field is not present). "assigneeCode" : "user", // Current task's assignee code (if the request is finalized this field is not present). "assigneeLocal" : { // Only returns if "expand" field is declared with "assigneeLocals" and "actualTasks". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }, "cardFields" : {}, "requesterLocal" : { // Only returns if "expand" field is declared with "requesterLocals". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }] }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/requester/me

Make a resume of the found requests with configurated SLA assuming that the logged user is the requester.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Tasks' assignees user code. |  |
| calculate | query | If the rest will bring the calculated variables related to time e percentage. | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "actualTasks" and/or "cardFields" and/or "requesterLocal" and/or "assigneeLocal" field to return it. |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| manager | query | A manager to be used as parameter to define the processes. |  |
| order | query | Order by fields. It's possible to order by: processInstanceId, deadlineDate, processId, requesterCode, requesterName, startDate and endDate. If you want a "DESC" ordenation, put a minus (-) simbol before the order parameter. | -processInstanceId |
| page | query | Page number. | 1 |
| pageSize | query | Size of the page. | 0 |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| statusRequired | query | List separated by comma containing all the status that are being requested, all other counters of the object will not be part of the search. If no values are specified, all status will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResponseEnvelopeVO  { "content": { "hasNext": "false", "total": "1", "items": [{ "percentageConcluded" : 100, // Reached percentage of the time passed on the requests sla. "deadlineDate" : "2017-03-24 00:00:00", // Deadline date of the request. "processInstanceId" : 1, // Process instance (Request) Id. "processId" : "PROCESS_ID", // Process id. "processDescription" : "Generic Process", // Process description. "requesterCode" : "user", // Requester's user code. "requesterName" : "User User", // Requester's full name. "remainingTime" : 0, // Remaining sla time of the request. "fullTime" : 10000, // Request's sla full time. "statusSla" : "EXPIRED", // Status of the SLA. 0 - OPEN, 1 - ON_TIME, 2 - WARNING, 3 - EXPIRED. "statusRequest" : "FINALIZED", // Status of the request. 0 - OPEN, 1 - CANCELED, 2 - FINALIZED. "startDate" : "2017-03-24 00:00:00", // Request's start date. "processVersion" : 1000, // Process version. "endDate" : "2017-03-24 00:00:00", // Request's finalized date. "warningDate" : "2017-03-24 00:00:00", // Request's warning date. "actualTasks" : { // Only returns if "expand" field is declared with "actualTasks". It's a list of RequestTaskSLAVO. "activityDescription" : "Activity", // Current task's activity description. "activityCode" : "Activity", // Current task's activity code. "assigneeName" : "User User", // Current task's assignee name (if the request is finalized this field is not present). "assigneeCode" : "user", // Current task's assignee code (if the request is finalized this field is not present). "assigneeLocal" : { // Only returns if "expand" field is declared with "assigneeLocals" and "actualTasks". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }, "cardFields: {}, "requesterLocal" : { // Only returns if "expand" field is declared with "requesterLocals". It's a LocalVO. "id" : "10", // Local id. "name" : "Joinville-SC", // Local name. "timezone": "America/Sao_Paulo", "latitude": 0, "longitude": 0, "radius": 0 } }] }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/assignee/me

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| calculate | query | To calculate SLA | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "cardFields" |  |
| finalStartDate | query | Final Start Date |  |
| initialStartDate | query | Initial Start Date |  |
| manager | query | Manager |  |
| page | query | Page | 1 |
| pageSize | query | Page Size | 0 |
| processId | query | Process Id |  |
| requester | query | Requester |  |
| statusTypeTaskRequest | query | 1 onTime; 2 warning, 3 Expired Status Required | 1 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/manager/me

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Assignee |  |
| calculate | query | To calculate SLA | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "cardFields" |  |
| finalStartDate | query | Final Start Date |  |
| initialStartDate | query | Initial Start Date |  |
| page | query | Page | 1 |
| pageSize | query | Page Size | 0 |
| processId | query | Process Id |  |
| requester | query | Requester |  |
| statusTypeTaskRequest | query | 1 onTime; 2 warning, 3 Expired Status Required | 1 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/requester/me

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Assignee |  |
| calculate | query | To calculate SLA | false |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| expand | query | Declare the expandable "cardFields" |  |
| finalStartDate | query | Final Start Date |  |
| initialStartDate | query | Initial Start Date |  |
| manager | query | Manager |  |
| page | query | Page | 1 |
| pageSize | query | Page Size | 0 |
| processId | query | Process Id |  |
| statusTypeTaskRequest | query | 1 onTime; 2 warning, 3 Expired Status Required | 1 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/resume/assignee/me

Make a resume of the found requests with configurated SLA considering that the logged user is an assignee of the request.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assigneeLocals | query | Comma-separated list that contains the activity's responsible local code that will be considered in the search. |  |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| countersRequired | query | Comma-separated list that contains all the counters that are being requested, all other counters of the object not return. If no values are specified, all counters will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| manager | query | A manager to be used as parameter to define the processes. |  |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| requester | query | Request's requester user code. |  |
| requesterLocals | query | Comma-separated list that contains the requester's local code that will be considered in the search. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResumeRequestsSLAVO  { "content": { "finishedRequests" : 1, // General finished requests counter. A number if the counter is requested, null if it's not. "finishedExpiredRequests" : 1, // Expired finished requests counter. A number if the counter is requested, null if it's not. "finishedOnTimeRequests" : 1, // Finished requests on time counter. A number if the counter is requested, null if it's not. "finishedWarningRequests" : 1, // Warned finished requests counter. A number if the counter is requested, null if it's not. "canceledRequests" : 1, // General canceled requests counter. A number if the counter is requested, null if it's not. "canceledExpiredRequests" : 1, // Expired canceled requests counter. A number if the counter is requested, null if it's not. "canceledOnTimeRequests" : 1, // Canceled requests on time counter. A number if the counter is requested, null if it's not. "canceledWarningRequests" : 1, // Warned canceled requests counter. A number if the counter is requested, null if it's not. "openRequests" : 1, // General open requests counter. A number if the counter is requested, null if it's not. "openExpiredRequests" : 1, // Expired open requests counter. A number if the counter is requested, null if it's not. "openOnTimeRequests" : 1, // Open requests on time counter. A number if the counter is requested, null if it's not. "openWarningRequests" : 1 // Warned open requests counter. A number if the counter is requested, null if it's not. }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/resume/manager/me

Make a resume of the found requests with configurated SLA considering that the logged user is a manager of the process.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Request's assignee user code. |  |
| assigneeLocals | query | Comma-separated list that contains the activity's responsible local code that will be considered in the search. |  |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| countersRequired | query | Comma-separated list that contains all the counters that are being requested, all other counters of the object not return. If no values are specified, all counters will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |
| requester | query | Request's requester user code. |  |
| requesterLocals | query | Comma-separated list that contains the requester's local code that will be considered in the search. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResumeRequestsSLAVO  { "content": { "finishedRequests" : 1, // General finished requests counter. A number if the counter is requested, null if it's not. "finishedExpiredRequests" : 1, // Expired finished requests counter. A number if the counter is requested, null if it's not. "finishedOnTimeRequests" : 1, // Finished requests on time counter. A number if the counter is requested, null if it's not. "finishedWarningRequests" : 1, // Warned finished requests counter. A number if the counter is requested, null if it's not. "canceledRequests" : 1, // General canceled requests counter. A number if the counter is requested, null if it's not. "canceledExpiredRequests" : 1, // Expired canceled requests counter. A number if the counter is requested, null if it's not. "canceledOnTimeRequests" : 1, // Canceled requests on time counter. A number if the counter is requested, null if it's not. "canceledWarningRequests" : 1, // Warned canceled requests counter. A number if the counter is requested, null if it's not. "openRequests" : 1, // General open requests counter. A number if the counter is requested, null if it's not. "openExpiredRequests" : 1, // Expired open requests counter. A number if the counter is requested, null if it's not. "openOnTimeRequests" : 1, // Open requests on time counter. A number if the counter is requested, null if it's not. "openWarningRequests" : 1 // Warned open requests counter. A number if the counter is requested, null if it's not. }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.6.1

### GET /2.0/workflows/requests/sla/resume/requester/me

Make a resume of the found requests with configurated SLA considering that the logged user is the requester.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query | Tasks' assignees user code. |  |
| cardFilters | query | Comma-separated list that contains the card fields of the requests that the resume will be filtered by. The card fields must be made by nameOfTheField:valueOfTheField and at least one process must be defined. If one or more processes defined do not have the field on their cards, the request will return a failure. |  |
| countersRequired | query | Comma-separated list that contains all the counters that are being requested, all other counters of the object not return. If no values are specified, all counters will be requested. The possible values are: finishedRequests, finishedExpiredRequests, finishedOnTimeRequests, finishedWarningRequests, canceledRequests, canceledExpiredRequests, canceledOnTimeRequests, canceledWarningRequests, openRequests, openExpiredRequests, openOnTimeRequests, openWarningRequests |  |
| finalDeadlineDate | query | The final date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalStartDate | query | The final date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| finalWarningDate | query | The final date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialDeadlineDate | query | The starting date requested for the request deadline date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialStartDate | query | The starting date requested for the request start date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| initialWarningDate | query | The starting date requested for the request warning date. All dates must be informed in the pattern yyyy-MM-dd. |  |
| manager | query | A manager to be used as parameter to define the processes. |  |
| processes | query | Comma-separated list that contains the process code of the processes that will be considered in the search. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a ResumeRequestsSLAVO  { "content": { "finishedRequests" : 1, // General finished requests counter. A number if the counter is requested, null if it's not. "finishedExpiredRequests" : 1, // Expired finished requests counter. A number if the counter is requested, null if it's not. "finishedOnTimeRequests" : 1, // Finished requests on time counter. A number if the counter is requested, null if it's not. "finishedWarningRequests" : 1, // Warned finished requests counter. A number if the counter is requested, null if it's not. "canceledRequests" : 1, // General canceled requests counter. A number if the counter is requested, null if it's not. "canceledExpiredRequests" : 1, // Expired canceled requests counter. A number if the counter is requested, null if it's not. "canceledOnTimeRequests" : 1, // Canceled requests on time counter. A number if the counter is requested, null if it's not. "canceledWarningRequests" : 1, // Warned canceled requests counter. A number if the counter is requested, null if it's not. "openRequests" : 1, // General open requests counter. A number if the counter is requested, null if it's not. "openExpiredRequests" : 1, // Expired open requests counter. A number if the counter is requested, null if it's not. "openOnTimeRequests" : 1, // Open requests on time counter. A number if the counter is requested, null if it's not. "openWarningRequests" : 1 // Warned open requests counter. A number if the counter is requested, null if it's not. }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/resume/assignee/me

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| finalStartDate | query |  |  |
| initialStartDate | query |  |  |
| manager | query |  |  |
| processId | query |  |  |
| requester | query |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/resume/manager/me

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query |  |  |
| finalStartDate | query |  |  |
| initialStartDate | query |  |  |
| processId | query |  |  |
| requester | query |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### GET /2.0/workflows/requests/tasks/resume/requester/me

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| assignee | query |  |  |
| finalStartDate | query |  |  |
| initialStartDate | query |  |  |
| manager | query |  |  |
| processId | query |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |
