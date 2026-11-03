---
content_hash: 32502ec62ae34534338bd15aa4f37ec0de06c7720e2828fdfca86badb6eac5c9
fetched_at: '2026-11-03T14:34:39.690760+00:00'
page_id: resource_DocumentRest
product: fluig
source: rest-fluig
title: Fluig REST — DocumentRest Resource
type: documentation
url: https://api.fluig.com/old/resource_DocumentRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# DocumentRest Resource

Document

Available Since
:   1.5.12

### POST /2.0/documents/createDocument

Creates a simple document. It is necessary that the document is in the
folder upload user.
  
  
Suggestion: To upload the file using FTP: ftp://serverUrl:21
  
  
Use: createDocument

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentCreateVO](https://api.fluig.com/old/json_DocumentCreateVO.html) (JSON) | Request JSON (example):`{ "documentDescription" : "fluig.docx", //document's description REQUIRED "parentDocumentId" : "8", //parent folder id REQUIRED "inheritSecurity" : false, //inheritSecurity REQUIRED "internalVisualizer" : true //internalVisualizer REQUIRED }` |
| application/xml | [documentCreateVO](https://api.fluig.com/old/xml_ns0_documentCreateVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": { "id" : "10", //document's id "version" : "1000", //document's version "companyId" : "22", //tenant's id "type" : "2", //document's type "description" : "Sample document", //document's description "additionalComments" : "comment", //document's comment "colleagueId" : "0988", //colleague id "iconPath" : "/webdesk/icone/icon-doc.png" //icon document "publisherId" : "1114", //publisher id "publisherName" : "Administrador Adm", //publisher name "immutable" : false, //immutable "createDate" : "2014-11-22", //date the document has been created "approvedDate" : "2014-11-22", //date the document has been approved "expirationDate" : "2014-11-22", //date the document will expire "validationStartDate" : "2014-11-22", //date the document has become valid "lastModifiedDate" : "2014-11-22", //date last time the document has been modified "parentId" : "10", //id of the parent folder "activeVersion" : true, //actual version of the document "phisicalFile" : "/home/doc.txt", //phisical path "securityLevel" : "1", //User permission -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total "onCheckout" : false, //in checkout "forApproval" : false, //in approval "removed" : false, //document was removed "isPrivate" : false, //document is private "crc" : 5458495849, //document's crc "userPermission" : "1", //User permission -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total "attachments" : [{ "fileName" : "att01" //Attachment's name "principal" : "false" //Indicates if this is the principal document "attachment" : "true" //Indicates if this is an attachment }] "documentPropertyNumber" : "10", //id of the parent form when the document is a record "documentPropertyVersion" : "1000", //version of the parent form when the record was created }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null }` |

Available Since
:   1.5.12

### POST /2.0/documents/createPrivateDocument

Create a new private document

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentCreateVO](https://api.fluig.com/old/json_DocumentCreateVO.html) (JSON) | Request JSON (example):`{ "tenantId" : "1", //tenantId REQUIRED "colleagueId" : "fluig", //colleagueId REQUIRED "documentDescription" : "fluig.docx", //document's name placed on upload folder REQUIRED "phisicalFile" : "/fluigVolume/upload/fluig/fluig.docx" //document's phisical file REQUIRED }` |
| application/xml | [documentCreateVO](https://api.fluig.com/old/xml_ns0_documentCreateVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": { "id" : "10", //document's id "version" : "1000", //document's version "companyId" : "22", //tenant's id "type" : "2", //document's type "description" : "Sample document", //document's description "additionalComments" : "comment", //document's comment "colleagueId" : "0988", //colleague id "iconPath" : "/webdesk/icone/icon-doc.png" //icon document "publisherId" : "1114", //publisher id "publisherName" : "Administrador Adm", //publisher name "immutable" : false, //immutable "createDate" : "2014-11-22", //date the document has been created "approvedDate" : "2014-11-22", //date the document has been approved "expirationDate" : "2014-11-22", //date the document will expire "validationStartDate" : "2014-11-22", //date the document has become valid "lastModifiedDate" : "2014-11-22", //date last time the document has been modified "parentId" : "10", //id of the parent folder "activeVersion" : true, //actual version of the document "phisicalFile" : "/home/doc.txt", //phisical path "securityLevel" : "1", //User permission -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total "onCheckout" : false, //in checkout "forApproval" : false, //in approval "removed" : false, //document was removed "isPrivate" : false, //document is private "crc" : 5458495849, //document's crc "userPermission" : "1", //User permission -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total "documentPropertyNumber" : "10", //id of the parent form when the document is a record "documentPropertyVersion" : "1000", //version of the parent form when the record was created }, "message": { "message": "OK", "detail": "OK", "type": "INFO" }` |

Available Since
:   1.5.12

### POST /2.0/documents/setDocumentPermissions

Set document permissions

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentCreatePermissionVO](https://api.fluig.com/old/json_DocumentCreatePermissionVO.html) (JSON) | Request JSON (example):`{ "documentId" : 411, "documentPermissionVO" :[{ "attributionType" : 1, "attributionValue" : "fluig", "downloadEnabled" : true, "securityLevel" : 3, "downloadEnabled" : true, "showContent": true }] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": "OK" "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |

Available Since
:   1.5.12

### POST /2.0/documents/updateFile

Update an existent document
  
  
Suggestion: To upload the file using FTP: ftp://serverUrl:21

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentCreateVO](https://api.fluig.com/old/json_DocumentCreateVO.html) (JSON) | Request JSON (example):`{ "documentId" : "418", //document id REQUIRED "version" : 1000, //document's version REQUIRED "documentDescription" : "fluig.docx", //document's name placed on upload folder REQUIRED "versionAction" : "", //document version action REQUIRED "additionalComments" : "Update document" //document's additionalComments REQUIRED }` |
| application/xml | [documentCreateVO](https://api.fluig.com/old/xml_ns0_documentCreateVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": { "id" : "10", //document's id "version" : "1000", //document's version "companyId" : "22", //tenant's id "type" : "2", //document's type "description" : "Sample document", //document's description "additionalComments" : "comment", //document's comment "colleagueId" : "0988", //colleague id "iconPath" : "/webdesk/icone/icon-doc.png" //icon document "publisherId" : "1114", //publisher id "publisherName" : "Administrador Adm", //publisher name "immutable" : false, //immutable "createDate" : "2014-11-22", //date the document has been created "approvedDate" : "2014-11-22", //date the document has been approved "expirationDate" : "2014-11-22", //date the document will expire "validationStartDate" : "2014-11-22", //date the document has become valid "lastModifiedDate" : "2014-11-22", //date last time the document has been modified "parentId" : "10", //id of the parent folder "activeVersion" : true, //actual version of the document "phisicalFile" : "/home/doc.txt", //phisical path "securityLevel" : "1", //User permission -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total "onCheckout" : false, //in checkout "forApproval" : false, //in approval "removed" : false, //document was removed "isPrivate" : false, //document is private "crc" : 5458495849, //document's crc "userPermission" : "1", //User permission -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total "documentPropertyNumber" : "10", //id of the parent form when the document is a record "documentPropertyVersion" : "1000", //version of the parent form when the record was created }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null }` |

Available Since
:   1.5.12

### POST /2.0/documents/approveDocument/{documentId}

Approve or reprove a document

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED id of document | int |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ApproveDocumentVO](https://api.fluig.com/old/json_ApproveDocumentVO.html) (JSON) | Request JSON (example):`{ "approved" : true, "observation" : "foo bar", "version" : 1000, "signed" : false }` |
| application/xml | [approveDocumentVO](https://api.fluig.com/old/xml_ns0_approveDocumentVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": "OK" "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |

Available Since
:   1.5.12

### POST /2.0/documents/copyDocumentToUploadArea/{documentId}

Copy a specific document to upload area

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | 15644 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": [1] 0 : "file.docx" "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |

Available Since
:   1.5.12

### POST /2.0/documents/deleteDocument/{documentId}

Delete a document

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | 15644 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return:  { "content": "OK" "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5

### GET /2.0/documents/getActive/{documentId}

Retrieve document active

Available Since
:   1.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | :15644 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return document   	{  		"content": {   		"tenantId": 1,   		"documentId": 170,   		"version": 1000,   		"documentTypeId": "",   		"languageId": null,   		"iconId": 0,   		"topicId": 0,   		"colleagueId": "login.user",   		"documentDescription": "teste-api-publica",   		"phisicalFile": "",   		"keyWord": "",   		"createDate": "2015-07-03",   		"approvedDate": null,   		"lastModifiedDate": "2015-07-03",   		"documentType": "1",   		"expirationDate": "2015-07-03",   		"accessCount": 0,   		"atualizationId": null,   		"parentDocumentId": 169,   		"visualization": null,   		"relatedFiles": null,   		"activeVersion": true,   		"versionDescription": "",   		"approvalAndOr": null,   		"externalDocumentId": "",   		"downloadEnabled": false,   		"approved": true,   		"validationStartDate": "2015-07-03",   		"publisherId": "login.user",   		"cardDescription": null,   		"allowMuiltiCardsPerUser": true,   		"documentPropertyNumber": null,   		"documentPropertyVersion": null,   		"privateDocument": false,   		"privateColleagueId": null,   		"indexed": false,   		"priority": null,   		"translated": false,   		"userNotify": false,   		"expires": false,   		"volumeId": "Default",   		"updateIsoProperties": false,   		"lastModifiedTime": null,   		"deleted": false,   		"imutable": null,   		"internalVisualizer": null,   		"crc": 0,   		"phisicalFileSize": 0,   		"permissionType": 0,   		"restrictionType": 0,   		"siteCode": "Fluig",   		"draft": false,   		"onCheckout": false,   		"uuid": "D472AB96-FBDF-445C-8895-717210129E27"   	},   	"message": {   		"message": "OK",   		"detail": "OK",   		"type": "INFO"   	}   } ``` |

Available Since
:   1.6.2

### GET /2.0/documents/getCurrentUserPermission/{documentId}

Retrieve the current user permission for the document

Available Since
:   1.6.2

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | :6658 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	{  		"content": {  			"document": {   			"tenantId": 1,   			"documentId": 170,   			"version": 1000,   			"documentTypeId": "",   			"languageId": null,   			"iconId": 0,   			"topicId": 0,   			"colleagueId": "login.user",   			"documentDescription": "teste-api-publica",   			"phisicalFile": "",   			"keyWord": "",   			"createDate": "2015-07-03",   			"approvedDate": null,   			"lastModifiedDate": "2015-07-03",   			"documentType": "1",   			"expirationDate": "2015-07-03",   			"accessCount": 0,   			"atualizationId": null,   			"parentDocumentId": 169,   			"visualization": null,   			"relatedFiles": null,   			"activeVersion": true,   			"versionDescription": "",   			"approvalAndOr": null,   			"externalDocumentId": "",   			"downloadEnabled": false,   			"approved": true,   			"validationStartDate": "2015-07-03",   			"publisherId": "login.user",   			"cardDescription": null,   			"allowMuiltiCardsPerUser": true,   			"documentPropertyNumber": null,   			"documentPropertyVersion": null,   			"privateDocument": false,   			"privateColleagueId": null,   			"indexed": false,   			"priority": null,   			"translated": false,   			"userNotify": false,   			"expires": false,   			"volumeId": "Default",   			"updateIsoProperties": false,   			"lastModifiedTime": null,   			"deleted": false,   			"imutable": null,   			"internalVisualizer": null,   			"crc": 0,   			"phisicalFileSize": 0,   			"permissionType": 0,   			"restrictionType": 0,   			"siteCode": "Fluig",   			"draft": false,   			"onCheckout": false,   			"uuid": "D472AB96-FBDF-445C-8895-717210129E27",  			},   		"securityLevel": -1,   		"showContent": false,   		"downloadEnabled": true,   	},   	"message": {   		"message": "OK",   		"detail": "OK",   		"type": "INFO"   	}   } ``` |

Available Since
:   1.5.12

### GET /2.0/documents/getDocumentApprovalHistory/{documentId}

Get document approval history

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | 15644 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": [ { documentVersion: 1000, iterationSequence: 1, levelId: 1, movementSequence: 1, colleagueId: "fluig", approvementDate: "2016-09-14", status: 0, observation: "approved", signed: false, colleagueName: "fluig" } ], "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |

Available Since
:   1.5.12

### GET /2.0/documents/getDocumentApprovers/{documentId}

Retrieve all approvers from a document

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED id of document | int |
| checkInheritance | query |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": [ { "approverType": 0, "colleagueId": "fluig", "levelId": 1, "approvalMode": 2, "digitalSignature": false, "levelDescription": "1", "alias": "fluig", "fullName": "Fluig ", "email": "fluig@fluig.com", "approvalStatus": "2", "approvalObservation": "", "companyId": 1 } ], "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |

Available Since
:   1.5.12

### GET /2.0/documents/getDownloadURL/{documentId}

Get document URL download

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | 15644 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return:  { "content": "http://servidor-fluig:8080/volume/stream/Rmx1aWc=/P3Q9MSZ2b2w9RGVmYXVsdCZpZD0zOTYmdmVyPTEwMDAmZmlsZT1UT0RPJmNyYz0xOTQxMDE1MDAxJnNpemU9NC4xRS00JnVJZD0zJmZTSWQ9MSZ1U0lkPTE=", "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5

### GET /2.0/documents/getUserPermissions/{documentId}

Retrieve permissions of an user to a file

Available Since
:   1.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | :15644 | int |
| user | query | :admin |  |
| version | query | :1.5 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return permission and message   	- Sem permissão - -1 ```  - Leitura - `0` - Gravação - `1` - Modificação - `2` - Controle Total - `3`  { "content": 2, "message": { "message": "OK", "detail": "OK", "type": "INFO" } } |

Available Since
:   1.5.12

### POST /2.0/documents/setDocumentApprovers/{documentId}

Set a list of approvers

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED id of document | long |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentSecurityVO](https://api.fluig.com/old/json_DocumentSecurityVO.html) (JSON) | Request JSON (example):`{ "documentPermissionVO" :[{ "attributionDescription": "fluig", "attributionType": 1, "attributionValue": "fluig", "downloadEnabled": true, "inheritSecurity": true, "securityLevel": 3, "securityVersion": null, "showContent": true }], "documentApproverVO" :[{ "approvalMode": 2, "approverType": 0, "colleagueId": "fluig", "levelDescription": "1", "levelId": 1, "digitalSignature": false, "alias": "fluig", "fullName": "Fluig ", "email": "fluig@fluig.com", "approvalStatus": "", "approvalObservation": "", "companyId": 1 }] }` |
| application/xml | [documentSecurityVO](https://api.fluig.com/old/xml_ns0_documentSecurityVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": "OK" "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |

Available Since
:   1.5.8

### GET /2.0/documents/getAllocatedDocument/{documentId}/{version}

Retrieve the allocated document entity for a given documentId and version, whether it's the source or destination document.

Available Since
:   1.5.8

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | :13 | int |
| version | path | :1000 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return an allocatedDocument  { "content": { "companyId": 1, "sourceDocument": 170, "sourceVersion": 1000, "destinationDocument": 22, "colleagueId": "adm", "checkoutDate": "2015-07-03", "checkoutTime": "080420", "checkinDate": null, "checkinTime": null, "comment": null, "active": true, "checkoutAllowed": null, "colleagueName": null }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.12

### GET /2.0/documents/getDocumentPermissions/{documentId}/{version}

Get document permissions

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | 15644document id | required |
| version | path | 1000document version | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content": [{"securityLevel" : 3, "securityVersion":null, "inheritSecurity":false, "downloadEnabled" : true, "showContent": true, "attributionDescription":null, "attributionType" : 1, "attributionValue" : "fluig", }], "content": "OK" "message": { "message": "OK" "detail": "OK" "type": "INFO" "errorCode": null } }` |
