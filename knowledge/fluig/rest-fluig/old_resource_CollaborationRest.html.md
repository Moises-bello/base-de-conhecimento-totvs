---
content_hash: 0f1073037b5da89e986848fbe77df1a394a9e96e5d46e588559daebd38eca286
fetched_at: '2026-11-03T14:34:39.467414+00:00'
page_id: resource_CollaborationRest
product: fluig
source: rest-fluig
title: Fluig REST — CollaborationRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CollaborationRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CollaborationRest Resource

Collaboration

Available Since
:   1.5.5

### GET /2.0/collaboration/getCollaborationStatus

Retrive collaboration status for a document  
  
Return a collaboration status

Available Since
:   1.5.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | query | - Document id | int |
| documentVersion | query | - Document version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns a collaboration status and a message with the result status   [{  	"content": {  		"inCollaboration": true,  		"link": "LINK",  		"isActive": false,  		"appCode": "googledrive",  		"appEnabled": "false",  },  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### GET /2.0/collaboration/listApps

Retrieve a list of apps  
  
Return a list of apps avaliable in the server.

Available Since
:   1.5.5

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns List of apps and a message with the result status   [{  	"content": {[  		"id": 1,  		"tenantId": 2,  		"code": "googledrive",  		"name": "Google Drive",  		"jndiName": "jndiName/jndi",  		"clientId": "clientId",  		"clientSecret": "clientSecret",  		"enabled": false  ]},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### POST /2.0/collaboration/updateApp

Update one app  
  
Return a message with the result status

Available Since
:   1.5.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CollaborationAppVO](https://api.fluig.com/old/json_CollaborationAppVO.html) (JSON) | Request JSON (example):  ```  {  		"id": 1,  		"tenantId": 2,  		"code": "googledrive",  		"name": "Google Drive",  		"clientId": "clientId",  		"clientSecret": "clientSecret",  		"enabled": false  }  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns a message with the result status   [{  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### POST /2.0/collaboration/addGuests/{collaborationId}

Add guests in one collaboration  
  
Return a message with the result status

Available Since
:   1.5.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| collaborationId | path | - Collaboration id | long |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of string (JSON) | Request JSON (example):  ```  {  ["maria","joao"] //lista com os alias  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns a message with the result status   [{  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### GET /2.0/collaboration/checkConnect/{appKey}

Check external connect for one app  
  
Return a message with the result status

Available Since
:   1.5.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path | - the code for appKey collaboration |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns a message with the result status   [{  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### GET /2.0/collaboration/get/{collaborationId}

Get the specified collaboration  
  
Return the collaborations specified by the id.

Available Since
:   1.5.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| collaborationId | path |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns one app and a message with the result status   {  	"content": {  		"collaborationId": 1,  		"oauthCode": null,  		"documentId": 18,  		"endDate": "2015-12-17 20:13:39",  		"startDate": "2015-12-17 19:23:22",  		"uploaderLogin": "adm",  		"documentVersion": 1000,  		"tenantId": 2,  		"guests": []  }  } ``` |

Available Since
:   1.5.5

### GET /2.0/collaboration/getApp/{appKey}

Retrieve one app  
  
Return a app avaliable in the server.

Available Since
:   1.5.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns one app and a message with the result status   [{  	"content": {  		"id": 1,  		"tenantId": 2,  		"code": "googledrive",  		"name": "Google Drive",  		"jndiName": "jndiName/jndi",  		"clientId": "clientId",  		"clientSecret": "clientSecret",  		"enabled": false  },  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### GET /2.0/collaboration/listCollaborators/{collaborationId}

Retrieve a list of collaborators invited for one collaboration  
  
Return a list of collaborators.

Available Since
:   1.5.5

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| collaborationId | path | - Collaboration id |  | long |
| limit | query | **(optional - default = 20)** | 20 | required |
| offset | query | **(optional - default = 0)** | 0 | required |
| pattern | query | **(optional - default = "")** |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns List of apps and a message with the result status   [{  	"content": {[  		"id": 1,  		"login": "joao",  		"email": "joao@joao.com.be",  		"firstName": "Joao",  		"lastName": "Silva",  		"fullName": "João Pereira Silva"  ]},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.5

### POST /2.0/collaboration/startCollaboration/{appKey}

Start the flow for Collaboration  
  
Return the link to redirect user for collaboration page.

Available Since
:   1.5.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path | - the code for appKey collaboration |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CollaborationVO](https://api.fluig.com/old/json_CollaborationVO.html) (JSON) | Request JSON (example):  ```  {  		"documentId": "59" // ID do documento no ECM que vai ser enviado para a colaboração  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns the URL for redirect the user and a message with the result status   {  	"content": "URL",  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.5

### POST /2.0/collaboration/startGuestCollaboration/{appKey}

Start the flow for Collaboration Guest  
  
Return the link to redirect user for collaboration page.

Available Since
:   1.5.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path | - the code for appKey collaboration |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CollaborationVO](https://api.fluig.com/old/json_CollaborationVO.html) (JSON) | Request JSON (example):  ```  {  		"documentId": "59" // ID do documento no ECM que vai ser enviado para a colaboração  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns the URL for redirect the user and a message with the result status   {  	"content": "URL",  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.5

### POST /2.0/collaboration/uploadFlow/{appKey}

Start the upload flow for Collaboration  
  
Return the link to redirect user for collaboration page.

Available Since
:   1.5.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path | - the code for appKey collaboration |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CollaborationVO](https://api.fluig.com/old/json_CollaborationVO.html) (JSON) | Request JSON (example):  ```  {  		"collaborationId": "59",                       // ID da colaboração  		"oauthCode": "code",                           //Código oauth enviado para a autenticação  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | The return in this case is a Map, based in Key : Value in according to the application |

Available Since
:   1.5.5

### POST /2.0/collaboration/startEditingByGuest/{appKey}/{guestLogin}

Start the editing flow for Collaboration Guest  
  
Return the link to redirect user for collaboration page.

Available Since
:   1.5.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path | - the code for appKey collaboration |
| guestLogin | path | - Guest login |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CollaborationVO](https://api.fluig.com/old/json_CollaborationVO.html) (JSON) | Request JSON (example):  ```  {  		"collaborationId": "59", // ID do documento no ECM que vai ser enviado para a colaboração  		"oauthCode": "code",     //Código oauth enviado para a autenticação  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | The return in this case is a Map, based in Key : Value in according to the application |

Available Since
:   1.8.0

### GET /2.0/collaboration/validateUserPermissionToEdit/{documentId}/{documentVersion}/{userCode}

Validates if the user has editing permission on the document  
  
Return user permission editing document

Available Since
:   1.8.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| documentId | path | - Document id | int |
| documentVersion | path | - Document version | int |
| userCode | path | - User code |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  [{  	"content": "OK",  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO",  	}  }  ] ``` |
