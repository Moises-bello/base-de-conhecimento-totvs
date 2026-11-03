---
content_hash: 2fbd6d08944f23bcc1718e7bc7278ca231b9233f1035a5bacccd779aad3c7a00
fetched_at: '2026-11-03T14:34:40.355025+00:00'
page_id: resource_TasksRest
product: fluig
source: rest-fluig
title: Fluig REST — TasksRest Resource
type: documentation
url: https://api.fluig.com/old/resource_TasksRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# TasksRest Resource

Tasks

Available Since
:   1.5.6

### POST /2.0/tasks/transfer

Transfer pending tasks from one user to another

Available Since
:   1.5.6

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [TaskTransferVO](https://api.fluig.com/old/json_TaskTransferVO.html) (JSON) | Request JSON (example):`{ "userTo": "user", "userFrom": "adm", "transferActiveDocuments": true, "transferMyDocumentsInApproval": true, "transferPendingWorkflow": true, "transferOpenWorkflow": true, "transferApprovers": true, "transferApprovals": true, "transferDocumentSecurity": true, "instanceIdInitial": 0, "instanceIdFinal": 9999999, "documentIdInitial": 0, "documentIdFinal": 9999999 }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| text/plain | object | `{ "content": "=== Checking Transfer of Folder Writing Permission=== [INFO] All permissions were transferred. ================================================================================ === Checking Transfer of Active Documents === [INFO] Document X - testdocument transferred [INFO] ================================================================================ === Checking Transfer of Documents Pending Approval === [INFO] Document X - testdocument transferred ================================================================================ === Checking Transfer of Pending Workflow Tasks === [WARN] No record found. ================================================================================ === Checking Transfer of Open Workflow === [WARN] No record found. ================================================================================ === Checking Transfer of Folders/Documents Approver === [INFO] Transferred to the document approver X ================================================================================ === Verificando Transferência de Aprovação de Documento === [INFO] Document approval transferred: X ================================================================================ === Checking Transfer of Task Central Tasks === ================================================================================ " "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.12

### GET /2.0/tasks/findApprovalDocumentsByUser/{colleagueId}

Returns documents that is in approval or was disapproved

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method returns an array of VOs Documents for approval.  { "content": { "tenantId": 1, "documentId": 170, "version": 1000, "documentTypeId": "", "languageId": null, "iconId": 0, "topicId": 0, "colleagueId": "login.user", "documentDescription": "teste-api-publica", "phisicalFile": "", "keyWord": "", "createDate": "2015-07-03", "approvedDate": null, "lastModifiedDate": "2015-07-03", "documentType": "1", "expirationDate": "2015-07-03", "accessCount": 0, "atualizationId": null, "parentDocumentId": 169, "visualization": null, "relatedFiles": null, "activeVersion": true, "versionDescription": "", "approvalAndOr": null, "externalDocumentId": "", "downloadEnabled": false, "approved": true, "validationStartDate": "2015-07-03", "publisherId": "login.user", "cardDescription": null, "allowMuiltiCardsPerUser": true, "documentPropertyNumber": null, "documentPropertyVersion": null, "privateDocument": false, "privateColleagueId": null, "indexed": false, "priority": null, "translated": false, "userNotify": false, "expires": false, "volumeId": "Default", "updateIsoProperties": false, "lastModifiedTime": null, "deleted": false, "imutable": null, "internalVisualizer": null, "crc": 0, "phisicalFileSize": 0, "permissionType": 0, "restrictionType": 0, "siteCode": "Fluig", "draft": false, "onCheckout": false, "uuid": "D472AB96-FBDF-445C-8895-717210129E27" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.4

### GET /2.0/tasks/findDocsInAgreement/{colleagueId}

Search for all documents in agreement with the specified user

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"content": [  		{  			"documentId": 531,  			"version": 1000,  			"documentDescription": "Marketing.pptx",  			"colleagueName": "admin",  			"lastModifiedDate": "2015-11-17",  			"documentType": "2",  			"approved": 0,  			"approvedString": null,  			"know": true  		}  	],  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### GET /2.0/tasks/findDocsInCheckout/{colleagueId}

Search for all documents with checkout status

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"content": [  		{  			"documentId": 533,  			"version": 1000,  			"documentDescription": "Intro.mp4",  			"colleagueName": "admin",  			"lastModifiedDate": "2015-11-17",  			"documentType": "2",  			"approved": 0,  			"approvedString": null,  			"know": false  		}  	],  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.3

### GET /2.0/tasks/findDocumentsToApprove/{colleagueId}

Returns the documents to approve

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs documents to approve.   {  	"content": {  		"tenantId": 1,  		"documentId": 170,  		"version": 1000,  		"documentTypeId": "",  		"languageId": null,  		"iconId": 0,  		"topicId": 0,  		"colleagueId": "login.user",  		"documentDescription": "teste-api-publica",  		"phisicalFile": "",  		"keyWord": "",  		"createDate": "2015-07-03",  		"approvedDate": null,  		"lastModifiedDate": "2015-07-03",  		"documentType": "1",  		"expirationDate": "2015-07-03",  		"accessCount": 0,  		"atualizationId": null,  		"parentDocumentId": 169,  		"visualization": null,  		"relatedFiles": null,  		"activeVersion": true,  		"versionDescription": "",  		"approvalAndOr": null,  		"externalDocumentId": "",  		"downloadEnabled": false,  		"approved": true,  		"validationStartDate": "2015-07-03",  		"publisherId": "login.user",  		"cardDescription": null,  		"allowMuiltiCardsPerUser": true,  		"documentPropertyNumber": null,  		"documentPropertyVersion": null,  		"privateDocument": false,  		"privateColleagueId": null,  		"indexed": false,  		"priority": null,  		"translated": false,  		"userNotify": false,  		"expires": false,  		"volumeId": "Default",  		"updateIsoProperties": false,  		"lastModifiedTime": null,  		"deleted": false,  		"imutable": null,  		"internalVisualizer": null,  		"crc": 0,  		"phisicalFileSize": 0,  		"permissionType": 0,  		"restrictionType": 0,  		"siteCode": "Fluig",  		"draft": false,  		"onCheckout": false,  		"uuid": "D472AB96-FBDF-445C-8895-717210129E27"  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.3

### GET /2.0/tasks/findExpiredWorkflowTasks/{colleagueId}

Expired requests

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid values: "userId", Pool:Group:"groupId" or Pool:Role:"roleId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs Workflow Expired Requests.   {  	"content": {  		"processDescription": "Processo Simples",  		"processId": "Processo Simples",  		"companyId": 1,  		"processInstanceId": 1,  		"version": 1,  		"requesterId": "adm",  		"requesterName": "adm",  		"active": true,  		"attachmentSeqId": 1,  		"sourceProcess": 0,  		"sourceThreadSequence": 0,  		"stateId": 1,  		"stateDescription": "Início",  		"deadlineDate": null,  		"deadlineText": "Sem prazo definido",  		"documentDescription": "7 Outubro, 2015 - Administrador",  		"colleagueName": "Administrador",  		"movementSequence": 1,  		"mainAttachmentDocumentId": 21,  		"mainAttachmentDocumentVersion": 0,  		"rowId": 0,  		"movementHour": "07/10/2015 15:19:21",  		"mobileReady": false,  		"canTake": false,  		"url": null,  		"code": null,  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.3

### GET /2.0/tasks/findMyDocuments/{colleagueId}

Returns my Documents

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs Documents for approval.   {  	"content": {  		"tenantId": 1,  		"documentId": 170,  		"version": 1000,  		"documentTypeId": "",  		"languageId": null,  		"iconId": 0,  		"topicId": 0,  		"colleagueId": "login.user",  		"documentDescription": "teste-api-publica",  		"phisicalFile": "",  		"keyWord": "",  		"createDate": "2015-07-03",  		"approvedDate": null,  		"lastModifiedDate": "2015-07-03",  		"documentType": "1",  		"expirationDate": "2015-07-03",  		"accessCount": 0,  		"atualizationId": null,  		"parentDocumentId": 169,  		"visualization": null,  		"relatedFiles": null,  		"activeVersion": true,  		"versionDescription": "",  		"approvalAndOr": null,  		"externalDocumentId": "",  		"downloadEnabled": false,  		"approved": true,  		"validationStartDate": "2015-07-03",  		"publisherId": "login.user",  		"cardDescription": null,  		"allowMuiltiCardsPerUser": true,  		"documentPropertyNumber": null,  		"documentPropertyVersion": null,  		"privateDocument": false,  		"privateColleagueId": null,  		"indexed": false,  		"priority": null,  		"translated": false,  		"userNotify": false,  		"expires": false,  		"volumeId": "Default",  		"updateIsoProperties": false,  		"lastModifiedTime": null,  		"deleted": false,  		"imutable": null,  		"internalVisualizer": null,  		"crc": 0,  		"phisicalFileSize": 0,  		"permissionType": 0,  		"restrictionType": 0,  		"siteCode": "Fluig",  		"draft": false,  		"onCheckout": false,  		"uuid": "D472AB96-FBDF-445C-8895-717210129E27"  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.3

### GET /2.0/tasks/findMyRequests/{colleagueId}

My Opened requests

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs Workflow My Opened Requests.   {  	"content": {  		"processDescription": "Processo Simples",  		"processId": "Processo Simples",  		"companyId": 1,  		"processInstanceId": 1,  		"version": 1,  		"requesterId": "adm",  		"requesterName": "adm",  		"active": true,  		"attachmentSeqId": 1,  		"sourceProcess": 0,  		"sourceThreadSequence": 0,  		"stateId": 1,  		"stateDescription": "Início",  		"deadlineDate": null,  		"deadlineText": "Sem prazo definido",  		"documentDescription": "7 Outubro, 2015 - Administrador",  		"colleagueName": "Administrador",  		"movementSequence": 1,  		"mainAttachmentDocumentId": 21,  		"mainAttachmentDocumentVersion": 0,  		"rowId": 0,  		"movementHour": "07/10/2015 15:19:21",  		"mobileReady": false,  		"canTake": false,  		"url": null,  		"code": null,  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### GET /2.0/tasks/findTasksInAgreement/{colleagueId}

Get tasks in agreement

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "userId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"content": {  		"processDescription": "consenso",  		"processId": "consenso",  		"companyId": 1,  		"processInstanceId": 11,  		"version": 2,  		"requesterId": "admin",  		"requesterName": "Administrator",  		"active": true,  		"attachmentSeqId": 0,  		"sourceProcess": 0,  		"sourceThreadSequence": 0,  		"stateId": 2,  		"stateDescription": "Activity",  		"deadlineDate": null,  		"deadlineText": "No deadline",  		"documentDescription": "",  		"colleagueName": "Administrator\nJohn",  		"movementSequence": 2,  		"mainAttachmentDocumentId": null,  		"mainAttachmentDocumentVersion": 0,  		"rowId": 0,  		"movementHour": null,  		"mobileReady": false,  		"canCancel": false,  		"canTake": false,  		"url": null,  		"code": null  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.3

### GET /2.0/tasks/findWorkflowTasks/{colleagueId}

Pending requests

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid values: "userId", Pool:Group:"groupId" or Pool:Role:"roleId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns an array of VOs Workflow Pending Requests.               {              	"content": {              		"processDescription": "Processo Simples",              		"processId": "Processo Simples",              		"companyId": 1,              		"processInstanceId": 1,              		"version": 1,              		"requesterId": "adm",              		"requesterName": "adm",              		"active": true,              		"attachmentSeqId": 1,              		"sourceProcess": 0,              		"sourceThreadSequence": 0,              		"stateId": 1,              		"stateDescription": "Início",              		"deadlineDate": null,              		"deadlineText": "Sem prazo definido",              		"documentDescription": "7 Outubro, 2015 - Administrador",              		"colleagueName": "Administrador",              		"movementSequence": 1,              		"mainAttachmentDocumentId": 21,              		"mainAttachmentDocumentVersion": 0,              		"rowId": 0,              		"movementHour": "07/10/2015 15:19:21",              		"mobileReady": false,              		"canTake": false,              		"url": null,              		"code": null,              	},              	"message": {              		"message": "OK",              		"detail": "OK",              		"type": "INFO"              	}              } ``` |

Available Since
:   1.5.4

### GET /2.0/tasks/getResumedTasks/{colleagueId}

Gets a resumed view of tasks for the specified user

Available Since
:   1.5.4

Request Parameters

| name | type | description |
| --- | --- | --- |
| colleagueId | path | Valid value: "colleagueId" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` There are three types of states: process, document and learn.           "children" nodes are only used in pool tasks, for the specified groups or roles.   { 	"content": [ 		{ 			"type": "open", 			"name": null, 			"taskId": null, 			"state": "process", 			"customURL": null, 			"totalTask": 3, 			"children": null 		}, 		{ 			"type": "requests", 			"name": null, 			"taskId": null, 			"state": "process", 			"customURL": null, 			"totalTask": 3, 			"children": null 		}, 		{ 			"type": "agreement", 			"name": null, 			"taskId": null, 			"state": "process", 			"customURL": null, 			"totalTask": 0, 			"children": null 		}, 		{ 			"type": "mydocs", 			"name": null, 			"taskId": null, 			"state": "document", 			"customURL": null, 			"totalTask": 0, 			"children": null 		}, 		{ 			"type": "toapprove", 			"name": null, 			"taskId": null, 			"state": "document", 			"customURL": null, 			"totalTask": 0, 			"children": null 		}, 		{ 			"type": "docagreement", 			"name": null, 			"taskId": null, 			"state": "document", 			"customURL": null, 			"totalTask": 0, 			"children": null 		}, 		{ 			"type": "checkout", 			"name": null, 			"taskId": null, 			"state": "document", 			"customURL": null, 			"totalTask": 0, 			"children": null 		}, 		{ 			"type": "learning", 			"name": null, 			"taskId": null, 			"state": "learn", 			"customURL": null, 			"totalTask": 0, 			"children": null 		}, 		{ 			"type": "poolgroup", 			"name": null, 			"taskId": null, 			"state": "process", 			"customURL": null, 			"totalTask": 2, 			"children": [ 				{ 					"type": "pool", 					"name": "Analistas", 					"taskId": "Pool:Group:Analistas", 					"state": "process", 					"customURL": null, 					"totalTask": 2, 					"children": null 				} 			] 		}, 		{ 			"type": "poolrole", 			"name": null, 			"taskId": null, 			"state": "process", 			"customURL": null, 			"totalTask": 0, 			"children": [] 		} 	], 	"message": { 		"message": "OK", 		"detail": "OK", 		"type": "INFO" 	} } ``` |
