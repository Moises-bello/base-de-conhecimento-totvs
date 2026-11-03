---
content_hash: c2f02d04f88f8136d8e26d45400fd861ef24ef272b8f83247bad36e692404dd6
fetched_at: '2026-11-03T14:34:39.848705+00:00'
page_id: resource_GroupRest
product: fluig
source: rest-fluig
title: Fluig REST — GroupRest Resource
type: documentation
url: https://api.fluig.com/old/resource_GroupRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# GroupRest Resource

Group

Available Since
:   1.5

### POST /2.0/groups/create

Create a new Group

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GroupCreateVO](https://api.fluig.com/old/json_GroupCreateVO.html) (JSON) | Request JSON (example):  ```  {  	"code" : "654654", // code  	"description" : "description", // description  	"isInternal" : "true", // is Internal  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status, successful message  	{ 		 content: null 		 message: { 			 message: "Grupo  criado com sucesso!" 			 detail: "Grupo  criado com sucesso!" 			 type: "INFO" 		} 	} ``` |

Available Since
:   1.5

### POST /2.0/groups/addUsers/{groupCode}

Add list user

Request Parameters

| name | type | description |
| --- | --- | --- |
| groupCode | path | :15644 |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of string (JSON) | Request JSON (example):`[ "adm", "user1" ]` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message   {  	content: null  	message: {  		message: "Usuários adicionados com sucesso ao grupo 99."  		detail: "Usuários adicionados com sucesso ao grupo 99."  		type: "INFO"  	}  }    ```  @since 1.5 ``` ``` |

Available Since
:   1.5.9

### GET /2.0/groups/findGroupsByUser/{genericId}

Available Since
:   1.5.9

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| genericId | path | User's generic indentifier, can be (login, idpId or userCode) |  |
| pattern | query | **(optional - default = "")** |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message   {  	 content: null  	 message: {  		 message: "OK"  		 detail: "OK"  		 type: "INFO"  	}  } ``` |

Available Since
:   1.6

### GET /2.0/groups/listUsersByGroup/{groupId}

Available Since
:   1.6

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| groupId | path | Group code to find users |  |  |
| limit | query | **(optional - default = "20")** | 20 | required |
| offset | query | **(optional - default = "0")** | 0 | required |
| orderby | query |  |  |  |
| pattern | query | **(optional - default = "")** |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, successful message   {  	 content: null  	 message: {  		 message: "OK"  		 detail: "OK"  		 type: "INFO"  	 }  } ``` |

Available Since
:   1.5

### GET /2.0/groups/containsUser/{groupCode}/{genericId}

Add list user

Available Since
:   1.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | :User's generic indentifier, can be (login, idpId or userCode) |
| groupCode | path | :15644 |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return boolean: true / false ``` |
