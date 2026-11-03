---
content_hash: d7642e905811d6125d39857e3ddd349c88844e6c861668691116c635c7950d1b
fetched_at: '2026-11-03T14:34:40.293234+00:00'
page_id: resource_SocialCloudServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — SocialCloudServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SocialCloudServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SocialCloudServiceRest Resource

Cloud

Available Since
:   1.3.0

### GET /socialcloud/defaultgroup

Return the default group

Available Since
:   1.3.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Response :  ```  {  	"groupDescription" : "Group default " //Group description  } ``` |

Available Since
:   1.5.0

### POST /socialcloud/add/securitygroups

Add security group(s) to the cloud

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  {  	"groupCode" : "GRP-1" // Code of the cloud (REQUIRED) "securityGroupCodes" : ["group-clients","group-manager"] // Alias for the security groups (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.5.0

### POST /socialcloud/cloud/create

Create a new relationship cloud

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request JSON (example):  ```  {  	"groupCode" : "CLOUD CODE",    // Code of the group (REQUIRED) "description" : "CLOUD DESCRIPTION" // Description of the group (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ``` {  	"content" : {  	"groupCode" : "CLOUD CODE",    // Code of the group  	"groupDescription" : "CLOUD DESCRIPTION" // Description of the group  },  "message" : "OK" // Messsage  } ``` |

Available Since
:   1.5.0

### GET /socialcloud/cloud/getDefault

Get the default relationship cloud of current talent

Available Since
:   1.5.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content" : {  	"groupDescription" : "Default tenant access group",  	"tenantId" : "1",  	"groupCode" : "DefaultGroup-1",  	"groupType" : "cloud",  	"id" : "2"  },  "message" : "null" // Messsage  } ``` |

Available Since
:   1.5.0

### GET /socialcloud/cloud/isEnabled

Return the status of relationship cloud.
True if is ON, false if is OFF

Available Since
:   1.5.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"value" : "true"//relationship cloud status  }] ``` |

### POST /socialcloud/cloud/remove

Remove an list of clouds

Request Body

| media type | data type |
| --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.5.0

### POST /socialcloud/cloud/update

Update a description of an relationship cloud

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request JSON (example):  ```  {  	"groupCode" : "CLOUD CODE",    // Code of the group (REQUIRED) "description" : "CLOUD DESCRIPTION" // Description of the group (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content" : {  	"groupCode" : "CLOUD CODE",    // Code of the group  	"groupDescription" : "CLOUD DESCRIPTION" // Description of the group  },  "message" : "OK" // Messsage  } ``` |

Available Since
:   1.3.0

### GET /socialcloud/list/allgroups

Return list of groups

Available Since
:   1.3.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | required |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [FDNGroupVO](https://api.fluig.com/old/json_FDNGroupVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"groupId" : "1",                               //Group id  	"groupDescription" : "Group default ",         //Group description  	"groupCode" : "group-default",                 //Group code  	"childGroupCode" : "",  	"groupUserRoleId" : "",  	"roleCode" : "",  	"login" : "jose.silva",  	"tenantId" : "1"  }] ``` |

Available Since
:   1.5.0

### POST /socialcloud/remove/securitygroups

Remove security group(s) from cloud

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  {  	"groupCode" : "GRP-1" // Code of the cloud (REQUIRED) "securityGroupCodes" : ["group-clients","group-manager"] // Alias for the security groups (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /socialcloud/add/community/group

Add a community to the group

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  { 		"groupCode" : "GRP-1" // Code of the group (REQUIRED) "socialAlias" : "nickname" // Alias for the community (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /socialcloud/add/user/group

Add a user to the group

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  { 		"groupCode" : "GRP-1" // Code of the group (REQUIRED) "socialAlias" : "nickname" // Alias for the community (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.5.0

### POST /socialcloud/cloud/enable/{enabled}

Turn on/off the relationship cloud

Available Since
:   1.5.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| enabled | path | true if relationship is ON, false if OFF | boolean |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.5.0

### POST /socialcloud/cloud/setDefault/{cloudCode}

Set an relationship cloud default of current tenant

Available Since
:   1.5.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| cloudCode | path | Code of the group |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.5.0

### GET /socialcloud/list/clouds/search

Search clouds by group code

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | required |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query |  | GROUP\_CODE\_ASC | "DESCRIPTION\_ASC" or "DESCRIPTION\_DESC" or "GROUP\_CODE\_ASC" or "GROUP\_CODE\_DESC" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  [{  	"content" : [{  	"groupCode" : "CLOUD_CODE",    // Code of the group  	"groupDescription" : "CLOUD DESCRIPTION" // Description of the group  	}],  	"message" : "OK" // Messsage  }] ``` |

### GET /socialcloud/list/communities/group

This method has been deprecated.

Return a list of communities in the given group.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| groupCode | query | Code of the group |  |  |
| offset | query | limit the number of registers in the returned list. Default value 20 | 20 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.5.0

### GET /socialcloud/list/findCloud/{code}

Search a single relationship cloud by cloud code

Available Since
:   1.5.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| code | path | Code of the group |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  [{  	"content" : [{  	"groupCode" : "CLOUD_CODE",    // Code of the group  	"groupDescription" : "CLOUD DESCRIPTION" // Description of the group  	}],  	"message" : "OK" // Messsage  }] ``` |

### GET /socialcloud/list/users/group

This method has been deprecated.

Return list of users in the given group

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| groupCode | query | Code of the group |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | required |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.5.0

### GET /socialcloud/listCloud/in/{genericId}

List cloud associated with social

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED Social identifier. For user can be alias, idpId or userCode, for community just alias. |  |  |
| limit | query | Limit. Default value 30 | 30 | required |
| offset | query | Defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query | Order options (DESC\_ASC | DESC\_DESC | CODE\_ASC | CODE\_DESC) | CODE\_ASC | "CODE\_ASC" or "CODE\_DESC" or "DESC\_ASC" or "DESC\_DESC" |
| pattern | query | Filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{"content":[{  	"id":47,  	"groupDescription":"Grupo de clientes"  	"groupCode":"cliente"  	}],  	"message": null  	} ``` |

Available Since
:   1.5.0

### GET /socialcloud/listCloud/out/{genericId}

List cloud without association with social

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED Social identifier. For user can be alias, idpId or userCode, for community just alias. |  |  |
| limit | query | Limit. Default value 30 | 30 | required |
| offset | query | Defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query | Order options (DESC\_ASC | DESC\_DESC | CODE\_ASC | CODE\_DESC) | CODE\_ASC | "CODE\_ASC" or "CODE\_DESC" or "DESC\_ASC" or "DESC\_DESC" |
| pattern | query | Filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{"content":[{  	"id":47,  	"groupDescription":"Grupo de clientes"  	"groupCode":"cliente"  	}],  	"message": null  	} ``` |

Available Since
:   1.5.0

### GET /socialcloud/listSecurityGroup/in/{cloudCode}

List security groups associated with cloud

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| cloudCode | path | REQUIRED Cloud code |  |  |
| limit | query | Limit. Default value 30 | 30 | required |
| offset | query | Defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query | Order options (DESC\_ASC | DESC\_DESC | CODE\_ASC | CODE\_DESC) | CODE\_ASC | "CODE\_ASC" or "CODE\_DESC" or "DESC\_ASC" or "DESC\_DESC" |
| pattern | query | Filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{"content":[{  	"id":47,  	"groupDescription":"Grupo de clientes"  	"groupCode":"cliente"  	}],  	"message": null  	} ``` |

Available Since
:   1.5.0

### GET /socialcloud/listSecurityGroup/out/{cloudCode}

List security group without association with cloud

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| cloudCode | path | REQUIRED Cloud code |  |  |
| limit | query | Limit. Default value 30 | 30 | required |
| offset | query | Defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query | Order options (DESC\_ASC | DESC\_DESC | CODE\_ASC | CODE\_DESC) | CODE\_ASC | "CODE\_ASC" or "CODE\_DESC" or "DESC\_ASC" or "DESC\_DESC" |
| pattern | query | Filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{"content":[{  	"id":47,  	"groupDescription":"Grupo de clientes"  	"groupCode":"cliente"  	}],  	"message": null  	} ``` |

Available Since
:   1.5.0

### POST /socialcloud/remove/communities/group

Remove 'n' communities from the group

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ``` {  	"groupCode" : "GRP-1" // Code of the group (REQUIRED) "socialsAlias" : ["nickname","othernickname"] // List comunities alias (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /socialcloud/remove/community/group

Remove a community from the group

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  { 		"groupCode" : "GRP-1" // Code of the group (REQUIRED) "socialAlias" : "nickname" // Alias for the community (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /socialcloud/remove/user/group

Remove a user from the group

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  { 		"groupCode" : "GRP-1" // Code of the group (REQUIRED) "socialAlias" : "nickname" // Alias for the community (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.5.0

### POST /socialcloud/remove/users/group

Remove 'n' users from the group

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  {  	"groupCode" : "GRP-1" // Code of the group (REQUIRED) "socialsAlias" : ["nickname","othernickname"] // Alias for the community (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /socialcloud/list/allcommunities/notin/group

This method has been deprecated.

Return list all communities NOT in the given group

Request Parameters

| name | type | description |
| --- | --- | --- |
| groupCode | query | Code of the group |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.5.0

### GET /socialcloud/list/clouds/community/{alias}

Return cloud list of a social entity. Could be a community.

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | communtiy alias |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | required |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query |  | GROUP\_CODE\_ASC | "DESCRIPTION\_ASC" or "DESCRIPTION\_DESC" or "GROUP\_CODE\_ASC" or "GROUP\_CODE\_DESC" |
| pattern | query | filter to search clouds of community |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  [{  	"content" : [{  	"groupCode" : "CLOUD_CODE",    // Code of the group  	"groupDescription" : "CLOUD DESCRIPTION" // Description of the group  }],  	"message" : "OK" // Messsage  }] ``` |

Available Since
:   1.5.0

### GET /socialcloud/list/clouds/user/{genericId}

Return cloud list of a social entity. Could be a user.

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | required |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query |  | GROUP\_CODE\_ASC | "DESCRIPTION\_ASC" or "DESCRIPTION\_DESC" or "GROUP\_CODE\_ASC" or "GROUP\_CODE\_DESC" |
| pattern | query | filter to search clouds of social |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  [{  	"content" : [{  	"groupCode" : "CLOUD_CODE",    // Code of the group  	"groupDescription" : "CLOUD DESCRIPTION" // Description of the group  }],  	"message" : "OK" // Messsage  }] ``` |

### GET /socialcloud/list/users/notin/group

This method has been deprecated.

Return list of users NOT in the given group

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| groupCode | query | Code of the group |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 | 20 | required |
| offset | query | defines the first registry in the returned list. Default value 0 | 0 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.5.0

### GET /socialcloud/listSocial/in/{socialType}/{cloudCode}

List users that are associated with the cloud

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| cloudCode | path | REQUIRED Cloud code |  |  |
| socialType | path | REQUIRED Social (USER | COMMUNITY) |  | "APPLICATION" or "COMMUNITY" or "EVENT" or "USER" |
| limit | query | Limit. Default value 30 | 15 | required |
| offset | query | Defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query | Order options (NAME\_ASC | NAME\_DESC | STATUS\_ASC | STATUS\_DESC) | NAME\_ASC | "NAME\_ASC" or "NAME\_DESC" or "STATUS\_ASC" or "STATUS\_DESC" |
| pattern | query | Filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{"content":[{  	"id":37,  	"name":"Maria",  	"alias":"maria",  	"type":"USER",  	"tenantId":1,  	"lastUpdate":1404739789000,  	"createDate":1401308464000,  	"numberFriends":0,  	"isModerator":false,  	"isAdmin":false,  	"state":"ACTIVE",  	"page":"social/maria"  	}],  	"message": null  	} ``` |

Available Since
:   1.5.0

### GET /socialcloud/listSocial/out/{socialType}/{cloudCode}

List users that aren't associated with the cloud

Available Since
:   1.5.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| cloudCode | path | REQUIRED Cloud code |  |  |
| socialType | path | REQUIRED Social (USER | COMMUNITY) |  | "APPLICATION" or "COMMUNITY" or "EVENT" or "USER" |
| limit | query | Limit. Default value 30 | 15 | required |
| offset | query | Defines the first registry in the returned list. Default value 0 | 0 | required |
| orderby | query | Order (NAME\_ASC | NAME\_DESC | STATUS\_ASC | STATUS\_DESC) | NAME\_ASC | "NAME\_ASC" or "NAME\_DESC" or "STATUS\_ASC" or "STATUS\_DESC" |
| pattern | query | Filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  	{"content":[{  	"id":37,  	"name":"Maria",  	"alias":"maria",  	"type":"USER",  	"tenantId":1,  	"lastUpdate":1404739789000,  	"createDate":1401308464000,  	"numberFriends":0,  	"isModerator":false,  	"isAdmin":false,  	"state":"ACTIVE",  	"page":"social/maria"  	}],  	"message": null  	} ``` |

Available Since
:   1.5.0

### POST /socialcloud/remove/groups/social/{socialType}

Remove 'n' groups from social

Available Since
:   1.5.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| socialType | path | (USER | COMMUNITY) | "APPLICATION" or "COMMUNITY" or "EVENT" or "USER" |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CloudVO](https://api.fluig.com/old/json_CloudVO.html) (JSON) | Request Object JSON (example):  ```  {  	"socialAlias" : "nickname" // Alias for the social (REQUIRED) "groupCodes" : ["customer","users"] // Group codes (REQUIRED) } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |
