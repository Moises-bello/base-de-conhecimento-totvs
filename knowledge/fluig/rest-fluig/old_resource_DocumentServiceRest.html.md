---
content_hash: c718d7ce06a5ac4ed43eb74dc65cfba4e307d40e38b10772f03fa183a0a22edd
fetched_at: '2026-11-03T14:34:39.758720+00:00'
page_id: resource_DocumentServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — DocumentServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_DocumentServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# DocumentServiceRest Resource

Documents

Available Since
:   1.4.0

### POST /ecm/document/checkin

Checkin of a document

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id"          : "10",                          //id document REQUIRED "version"     : "1000",                        //document version REQUIRED "description" : "Description of the check out" //document version REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /ecm/document/checkout

Check out of a document

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id"          : "10",                          //id document REQUIRED "version"     : "1000",                        //document version REQUIRED "description" : "Description of the check out" //document version REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.5.3

### GET /ecm/document/chunkedUploadURL

Get the chunked upload url
With this URL it is possible to send chunked parts of one file, instead the entire file.

Available Since
:   1.5.3

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | URL for upload  ```  {  	"content": "http://127.0.0.1:8080/ecm/chunkupload",  	"message": ""} ``` |

### POST /ecm/document/create

This method has been deprecated.

Creates a simple document. It is necessary that the document is in the
folder upload user.
  
  
Suggestion: To upload the file using FTP: ftp://serverUrl:21
  
  
Use: createDocument

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"description" : "Simple document",                //document's description REQUIRED "parentId"    : "8",                              //parent folder id REQUIRED "attachments" : [{  		"fileName" : "atch01" //attachment file name REQUIRED ]}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.4.0

### POST /ecm/document/createDocument

Creates a simple document. It is necessary that the document is in the
folder upload user.
  
  
Suggestion: To upload the file using FTP: ftp://serverUrl:21

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"description" : "Simple document",                //document's description REQUIRED "parentId"    : "8",                              //parent folder id REQUIRED "attachments" : [{  		"fileName" : "atch01" //attachment file name REQUIRED ]}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

### POST /ecm/document/createFolder

Creates a simple folder. It is necessary that the document is in the
folder upload user.
  
  
Suggestion: To upload the file using FTP: ftp://serverUrl:21

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"description" : "Simple document",//document's description REQUIRED "parentId"    : "8"               //parent folder id REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.4.0

### GET /ecm/document/loggedUser

This method has been deprecated. As of release 1.5.0, replaced by /social/user/logged

Get information the user logged

Available Since
:   1.4.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"            : 5,                             //user's id  	"login"         : "adm",                         //user's login  	"firstName"     : "Administrator",               //user's first name  	"lastName"      : "of System",                   //user's last name  	"fullName"      : "Administrator of System",     //user's full name  	"email"         : "adm@fluig.com",               //user's email  	"birthDay"      : "2014-01-01"                   //user's birthday  	"tenantId"      : 1,                             //user's tenantId  	"locationId"    : 1,                             //user's location  	"tenantCode"    : "01",                          //user's tenant code  	"userCode"      : "adm",                         //user's code  }  "message": ""} ``` |

Available Since
:   1.4.0

### GET /ecm/document/maxUploadSize

Get the max upload size parameter

Available Since
:   1.4.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Max upload size |

### POST /ecm/document/notify

Registers the logged user to be notified about modifications in the given
document.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id"      : "1",   //document id REQUIRED "version" : "1000" //document version REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /ecm/document/permissions

Get information of permission of a documents list

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | list DocumentVORequest JSON (example):  ```  [{  	"id" : "10" //document's id  },  {  	"id" : "11" //document's id  },  {  	"id" : "12" //document's id  }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Document list |

### POST /ecm/document/remove

Removes a document or folder

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10" //document's id REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /ecm/document/stopNotify

Unregisters the logged user as a document's follower. The user will no
longer be notified about modifications on the document.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id"      : "1",   //document id REQUIRED "version" : "1000" //document version REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.4.0

### POST /ecm/document/undoCheckout

Cancel check out of a document

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10", //id document REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.4

### POST /ecm/document/updateDescription

Updates a document or folder.

Available Since
:   1.3.4

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id"          : "2",       //document's id REQUIRED "description" : "New Desc" //the new folder's description REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.4.0

### POST /ecm/document/updateDocumentFolder

Update a document or folder.

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"id"       : "2",       //document's id REQUIRED "parentId" : "56"       //new parent id REQUIRED } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.4.0

### POST /ecm/document/updateFile

Update a file

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| X-Fluig-Viewer | header |  |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [FileUploadData](https://api.fluig.com/old/json_FileUploadData.html) (JSON) | Request JSON (example):  ```  {  	"id"            : "2",               //document's id REQUIRED "version"       : "1000",            //document's version REQUIRED "versionAction" : "NEW_VERSION",     //if NEW_VERSION the version will be increased, NEW_REVISIO the revision  will be increased or KEEP_VERSION the version will be maintained. It only works with mutable documents  	"fileName"      : "Document.docx",   //physical file name REQUIRED "comments"      : "My comments"      //comments on document  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.4.0

### GET /ecm/document/uploadURL

Get the user upload url
  
  
In Fluig the upload process is done in two steps:

1. User get URL of the repository link;
2. With the URL, he sends the file and uploads it.

Important informations: Some information have to be set in request header for upload.
  

1. Authorization: Is an information group required for server confirmation that you are really you. More information: <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>
2. Content-Type: Example: "image/jpeg", "application/xml", "application/ms-word"...
3. Accept: "application/json";
4. companyId: User's Company id . More information: <http://yourserver/api/public/ecm/drive/config;>
5. userId: User's id. More information: <http://yourserver/api/public/ecm/document/loggedUser;>

Available Since
:   1.4.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | URL for upload |

### GET /ecm/document/activeDocumentFile/{documentId}

This method has been deprecated. As of release 1.4.3-EP4, replaced by /public/ecm/document/downloadURL/{documentId}

Get active version document file

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | Document file |

Available Since
:   1.4.0

### GET /ecm/document/activedocument/{documentId}

Get information metadata active document.

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  	"accessCount"			  : 19								//number of hits in the document  	"versionDescription"	  : ""								//version description  	"colleagueName"		      : null							//colleague name  	"phisicalFileSize"		  : 0.000102043						//file size  	"favorite"				  : false							//is favorite  	"articleContent"		  : null							//article content  	"userAnswerForm"		  : true							//if have user answer form  	"allowMuiltiCardsPerUser" : true							//if allow muilti cards per user  	"expiredForm"			  : false							//if form has expired  	"sociableDocumentDto"	  : null							//sociable document  	"activeUserApprover"	  : null							//user approver  	"fileURL"				  : "http://10.80.72.126:8080/volume/stream/Rmx1aWc=/Pgfsdgsfdgh.txt" //file url  }  "message": ""} ``` |

### GET /ecm/document/allDocumentHits/{documentId}

Returns all hits of all versions the given document.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | List long companyId; String colleagueId; int documentId; int version; String versionDescription; Calendar lastView; Calendar firstView; |

Available Since
:   1.5.3

### POST /ecm/document/cancelChunkedUpload/{uploadId}

Cancel a chunked upload, to delete files from the upload folder avoiding unnecessary storage.

Available Since
:   1.5.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| uploadId | path | REQUIRED upload id |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"content" : true  } ``` |

Available Since
:   1.4.0

### POST /ecm/document/createDocument/{uploadId}

Creates a simple document. It is necessary that the document is in the
folder upload user.
  
  
Important: Read upload process. <http://yourserver/api/public/ecm/document/uploadURL>
  
  
Suggestion: To upload the file using FTP: ftp://serverUrl:21

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| uploadId | path | REQUIRED upload's id |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"description" : "Simple document",                //document's description REQUIRED "parentId"    : "8",                              //parent folder id REQUIRED "attachments" : [{  		"fileName" : "atch01" //attachment file name REQUIRED ]}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.4.0

### GET /ecm/document/downloadURL/{documentId}

Get the user download url.
  
  
In Fluig the download process is done in two steps:

1. User get URL of the document link;
2. With the URL, he gets the file and download it.

Important informations: Some information have to be set in request header for download.
  

1. Authorization: Is an information group required for server confirmation that you are really you. More information: <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>
2. Content-Type: Example: "image/jpeg", "application/xml", "application/ms-word"...

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id \* | int |
| fileName | query | attached file name. Default: the main file name |  |
| version | query | document's version. Default: active version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | URL for upload |

### GET /ecm/document/getDocumentByDatasetName/{datasetName}

Request Parameters

| name | type | description |
| --- | --- | --- |
| datasetName | path | REQUIRED Dataset's Name |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {       	"id"                      : "10",                          //document's id       	"version"                 : "1000",                        //document's version       	"companyId"               : "22",                          //tenant's id       	"type"                    : "2",                           //document's type       	"description"             : "Sample document",             //document's description       	"additionalComments"      : "comment",                     //document's comment       	"colleagueId"             : "0988",                        //colleague id       	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document       	"publisherId"             : "1114",                        //publisher id       	"publisherName"           : "Administrador Adm",           //publisher name       	"immutable"               :  false,                        //immutable       	"createDate"              : "2014-11-22",                  //date the document has been created       	"approvedDate"            : "2014-11-22",                  //date the document has been approved       	"expirationDate"          : "2014-11-22",                  //date the document will expire       	"validationStartDate"     : "2014-11-22",                  //date the document has become valid       	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified       	"parentId"                : "10",                          //id of the parent folder       	"activeVersion"           : true,                          //actual version of the document       	"phisicalFile"            : "/home/doc.txt",               //phisical path       	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total       	"onCheckout"              : false,                         //in checkout       	"forApproval"             : false,                         //in approval       	"removed"                 : false,                         //document was removed       	"isPrivate                : false,                         //document is private       	"crc                      : 5458495849,                    //document's crc       	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total       	"attachments"             : [{                                       		"fileName"   : "att01"  //Attachment's name                                       		"principal"  : "false"  //Indicates if this is the principal document                                       		"attachment" : "true"   //Indicates if this is an attachment                                   	}]       	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record       	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""}    @since 1.5.0  @throws Exception ``` |

Available Since
:   1.5.2

### GET /ecm/document/getLastVersionNonDraft/{documentId}

Get latest non draft document's version.

Available Since
:   1.5.2

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"content" : "1000", //document's version  }  "message": ""} ``` |

Available Since
:   1.4.6

### GET /ecm/document/lastDocument/{documentId}

Get information document metadata.

Available Since
:   1.4.6

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }  "message": ""} ``` |

Available Since
:   1.3.4

### GET /ecm/document/listDocument/{folderId}

Returns the list of itens of a given folder.

Available Since
:   1.3.4

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| folderId | path | REQUIRED folder's id |  | int |
| limit | query | limit of returned items. Value default 20 | 20 | required |
| offset | query | the offset. Value default 0 | 0 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  {	"content": [{  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"downloadEnabled"         : true,                          //download is enabled for document   	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }]  "message": ""} ``` |

Available Since
:   1.4.0

### GET /ecm/document/listDocumentWithChildren/{folderId}

Returns the tree of folders and documents of a given folder. It's method so much util when you to want to download a folder with subfolders and documents.
  
  
Important: It isn't possible to list the root folder, because affect the performance of server.
  
  
Suggestion: For to list a folder's documents use the method listDocument/{folderId}.

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| folderId | path | REQUIRED folder's id |  | int |
| limit | query | limit of returned items. Value default 50 | 20 | required |
| offset | query | the offset. Value default 0 | 0 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  {	"content": [{  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  }]  "message": ""} ``` |

### GET /ecm/document/liveurl/{documentId}

Returns the URL to access the document content with security token.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | ``` The URL to access the document ``` |

Available Since
:   1.4.0

### GET /ecm/document/{documentId}/{versionId}

Get information document metadata.

Available Since
:   1.4.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | int |
| versionId | path | REQUIRED document's version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"id"                      : "10",                          //document's id  	"version"                 : "1000",                        //document's version  	"companyId"               : "22",                          //tenant's id  	"type"                    : "2",                           //document's type  	"description"             : "Sample document",             //document's description  	"additionalComments"      : "comment",                     //document's comment  	"colleagueId"             : "0988",                        //colleague id  	"iconPath"                : "/webdesk/icone/icon-doc.png"  //icon document  	"publisherId"             : "1114",                        //publisher id  	"publisherName"           : "Administrador Adm",           //publisher name  	"immutable"               :  false,                        //immutable  	"createDate"              : "2014-11-22",                  //date the document has been created  	"approvedDate"            : "2014-11-22",                  //date the document has been approved  	"expirationDate"          : "2014-11-22",                  //date the document will expire  	"validationStartDate"     : "2014-11-22",                  //date the document has become valid  	"lastModifiedDate"        : "2014-11-22",                  //date last time the document has been modified  	"parentId"                : "10",                          //id of the parent folder  	"activeVersion"           : true,                          //actual version of the document  	"phisicalFile"            : "/home/doc.txt",               //phisical path  	"securityLevel"           : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"onCheckout"              : false,                         //in checkout  	"forApproval"             : false,                         //in approval  	"removed"                 : false,                         //document was removed  	"isPrivate                : false,                         //document is private  	"crc                      : 5458495849,                    //document's crc  	"userPermission"          : "1",                           //User permission  -1 - No permission, 0 - Reading, 1 - Writing, 2 - Modification, 3 - Total  	"attachments"             : [{  		"fileName"   : "att01"  //Attachment's name  		"principal"  : "false"  //Indicates if this is the principal document  		"attachment" : "true"   //Indicates if this is an attachment  	}]  	"documentPropertyNumber"  : "10",                           //id of the parent form when the document is a record  	"documentPropertyVersion" : "1000",                         //version of the parent form when the record was created  	"accessCount"			  : 19								//number of hits in the document  	"versionDescription"	  : ""								//version description  	"colleagueName"		      : null							//colleague name  	"phisicalFileSize"		  : 0.000102043						//file size  	"favorite"				  : false							//is favorite  	"articleContent"		  : null							//article content  	"userAnswerForm"		  : true							//if have user answer form  	"allowMuiltiCardsPerUser" : true							//if allow muilti cards per user  	"expiredForm"			  : false							//if form has expired  	"sociableDocumentDto"	  : null							//sociable document  	"activeUserApprover"	  : null							//user approver  	"fileURL"				  : "http://10.80.72.126:8080/volume/stream/Rmx1aWc=/Pgfsdgsfdgh.txt" //file url  }  "message": ""} ``` |

### GET /ecm/document/documentFileWithoutZip/{documentId}/{versionId}

Get document file of version specific, compressed in zip format

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | required |
| versionId | path | REQUIRED document's version | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | Document file |

### GET /ecm/document/documentHitsByVersion/{documentId}/{version}

Returns the 30 first hits of the given document and returns total
quantity of hits.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | required |
| version | path | REQUIRED document's version | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | HashMap - Index is "totalHits" and "hitsList" |

### GET /ecm/document/documentfile/{documentId}/{versionId}

Get document file of version specific.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | required |
| versionId | path | REQUIRED document's version | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | Document file |

### GET /ecm/document/notifyList/{documentId}/{versionId}

Returns users that are being notified about the modifications on the
given document.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| documentId | path | REQUIRED document's id |  | int |
| versionId | path | REQUIRED document's version |  | int |
| limit | query | limit the number of registers in the returned list | 10 | int |
| offset | query | defines the first registry in the returned list | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [UserVO](https://api.fluig.com/old/json_UserVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id"          : "1",                 //user's id  	"name"        : "John Fluig",        //user's name  	"description" : "Software Engineer", //user's description  	"alias"       : "john.fluig",        //user's alias  	"lastUpdate"  : "100001582"          //last time the user has been updated (in miliseconds)  }] ``` |

### GET /ecm/document/documentFileThumbnail/{documentId}/{versionId}/{thumbnail}

Get thumbnail document of version specific.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | required |
| thumbnail | path | REQUIRED document's image size in pixel |  |
| versionId | path | REQUIRED document's version | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | First request return document file, after twice return image document |
