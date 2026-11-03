---
content_hash: 68bc370bc934442c4a2c1d80c9a3290f06b55f491c5b263640319a8dd98f5667
fetched_at: '2026-11-03T14:34:39.482745+00:00'
page_id: resource_CommunityDocumentServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — CommunityDocumentServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CommunityDocumentServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CommunityDocumentServiceRest Resource

Document features for communities

### POST /social/community/document

Creates a document in a given folder/community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocumentVO](https://api.fluig.com/old/json_SocialDocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01", //REQUIRED community's alias  	"folderId" : "1",				//REQUIRED id of the folder the document will be created inside  	"description" : "Document 01",	//REQUIRED document's description  	"name" : "Document_01",			//REQUIRED document's name  	"base64media" : "7441010400",//REQUIRED document's content in base64 format  	"documentExtension" : ".png"	//REQUIRED document's extension  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | number (JSON) | ``` A plain integer value, that is the created document's id ``` |

### POST /social/community/folder

Creates a folder in a given community.
If the parentId is not given, the folder will be created in the root folder.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialFolderVO](https://api.fluig.com/old/json_SocialFolderVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01",	//community's alias  	"parentId" : "1",		//id of the parent folder. If it is 0, the folder will be created in the root folder  	"description" : "Folder 01"		//folder's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | number (JSON) | ``` A plain integer value, that is the created folder's id ``` |

### POST /social/community/document/remove

This method has been deprecated. on 1.3.4

Removes a document.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocumentVO](https://api.fluig.com/old/json_SocialDocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "1"	//document's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/community/document/update

This method has been deprecated. on 1.3.4

Updates a document in a given folder/community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocumentVO](https://api.fluig.com/old/json_SocialDocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "1",		//document's id  	"description" : "New Description"  //new document's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocDto](https://api.fluig.com/old/json_SocialDocDto.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "1",			//document's id  	"version" : "1000",			//document's version  	"documentDescription" : "New Desc",	//document's description  	"createDate" : "1784455120",	//date the document has been created (in miliseconds)  	"documentType" : "2",			//document's type  	"parentDocumentId" : "1",		//parent document/folder id  	"phisicalFilePath" : "/fluig",	//phisical path  	"userPermission" : "1"			//current user permission: (-1) - No permission, (0) - Read, (1) - Write, (2) - Modify, (3) - Total control  } ``` |

### GET /social/community/document/{documentId}

Returns the information about a given document.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | REQUIRED document's id | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocDto](https://api.fluig.com/old/json_SocialDocDto.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "1",			//document's id  	"version" : "1000",			//document's version  	"documentDescription" : "New Desc",	//document's description  	"createDate" : "1784455120",	//date the document has been created (in miliseconds)  	"documentType" : "2",			//document's type  	"parentDocumentId" : "1",		//parent document/folder id  	"phisicalFilePath" : "/fluig",	//phisical path  	"userPermission" : "1"			//current user permission: (-1) - No permission, (0) - Read, (1) - Write, (2) - Modify, (3) - Total control  } ``` |

### POST /social/community/folder/remove

This method has been deprecated. on 1.3.4

Removes a folder.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialFolderVO](https://api.fluig.com/old/json_SocialFolderVO.html) (JSON) | Request JSON (example):  ```  {  	"folderId" : "2"		//folder's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/community/folder/update

This method has been deprecated. on 1.3.4

Updates a folder.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialFolderVO](https://api.fluig.com/old/json_SocialFolderVO.html) (JSON) | Request JSON (example):  ```  {  	"folderId" : "2",		//folder's id  	"description" : "New Desc" //the new folder's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocDto](https://api.fluig.com/old/json_SocialDocDto.html) (JSON) | Response JSON (example):  ``` {  	"documentId" : "1",			//folder's id  	"version" : "1000",			//folder's version  	"documentDescription" : "New Desc",	//folder's description  	"createDate" : "1784455120",	//date the folder has been created (in miliseconds)  	"documentType" : "2",			//document's type  	"parentDocumentId" : "1",		//parent folder id  	"phisicalFilePath" : "/fluig",	//phisical path  	"userPermission" : "1"			//current user permission: (-1) - No permission, (0) - Read, (1) - Write, (2) - Modify, (3) - Total control  } ``` |

### GET /social/community/folder/{folderId}

This method has been deprecated. on 1.3.4

Returns the list of itens of a given folder.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| folderId | path | REQUIRED folder's id |  | int |
| 0 | query | the offset. Value default 0 | 0 | required |
| limit | query | limit of returned items. Value default 20 | 20 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [DocumentVO](https://api.fluig.com/old/json_DocumentVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "10",						  //document's id  	"version" : "1000", 				  //document's version  	"companyId" : "22", 				  //tenant's id  	"type" : "2",						  //document's type  	"description" : "Sample document", 	  //document's description  	"colleagueId" : "0988",				  //colleague id  	"publisherId" : "1114",				  //publsher id  	"createDate" : "1234045560",		  //date the document has been created (in miliseconds)  	"approvedDate" : "1234045560",		  //date the document has been approved (in miliseconds)  	"expirationDate" : "1234045560",	  //date the document will expire (in miliseconds)  	"validationStartDate" : "1234045560", //date the document has become valid (in miliseconds)  	"lastModifiedDate" : "1234045560",	  //date last time the document has been modified (in miliseconds)  	"parentId" : "10",					  //id of the parent folder  	"activeVersion" : "1000",			  //actual version of the document  	"phisicalFile" : "/home/doc.txt",	  //phisical path  	"attachments" : [{  		"fileName" : "att01"	//Attachment's name  		"principal" : "false"	//Indicates if this is the principal document  		"attachment" : "true"	//Indicates if this is an attachment  	}]  }] ``` |
