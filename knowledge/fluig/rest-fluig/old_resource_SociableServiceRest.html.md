---
content_hash: b056e516288b6c46fbc7a64ee1b2cbfb4fd5fdc76fd27c8a88da7926448d990d
fetched_at: '2026-11-03T14:34:40.219027+00:00'
page_id: resource_SociableServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — SociableServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SociableServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SociableServiceRest Resource

Social features

Available Since
:   1.3.0

### POST /sociable/comment

Comment any sociable

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommentVO](https://api.fluig.com/old/json_CommentVO.html) (JSON) | Request JSON (example):  ```  {  	"sociableId" : "21",                                     //REQUIRED the id of sociable  	"comment" : "This is a comment for @alberto.batista"     //REQUIRED the comment that supports mentions  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"value":"2"   //New comment ID  } ``` |

Available Since
:   1.4.0

### POST /sociable/comment/post

Comment a post with return

Available Since
:   1.4.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommentVO](https://api.fluig.com/old/json_CommentVO.html) (JSON) | Request JSON (example):  ```  {  	"sociableId" : "21",                                      //REQUIRED the id of sociable  	"comment" : "This is a comment for @alberto.batista"     //REQUIRED the comment that supports mentions,  	"customData" : {  	"link":"http://www.teste.com.br"  }  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {  	"comment" : "hi @julio.batista",                //Comment including mentions  	"creationDate" : "12/04/1874",                  //Creation date  	"commentWithoutMention" : "hi Julio Batista",   //Comment without mentions, with a plan text  	"mention" : "true",                             //True if it has mentions  	"user" : {                                      //User that has created the post  		"id" : "1",                             //User's id  		"name" : "User 01",                     //User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01",                     //user's alias  		"type" : "USER",                        //fixed  		"tenantId" : "22",                      //tenant's id  		"lastUpdate" : "10008520",              //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",                  //date the user has been created (in miliseconds)  		"numberModerations" : "1",              //number of the communities the user is moderator  		"state" : "ACTIVE"                      //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                                    //Where the post was created  		"id" : "1",                             //Community or user id  		"name" : "Community 01",                //community or name  		"description" : "Community 01 description", //community or user description  		"alias" : "community01",                //community or user alias  		"type" : "COMMUNITY",                   //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",                      //tenant's id  		"lastUpdate" : "10008520",              //date of last time the community or user has been modified (in miliseconds)  		"create" : "10008520",                  //date the community or user has been created (in miliseconds)  		"numberParticipations" : "10",          //number of users that participate of the community  		"numberModerations" : "1",              //number of the community's moderators  		"hidden" : "false",                     //indicates if it is a hidden community  		"privateContent" : "false",             //indicates if community's content is private  		"approvalRequired" : "true",            //indicates if it is necessary approval to join the community  		"admin" : "true",                       //indicates if the current user is community's administrator  		"state" : "ACTIVE"                      //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"mentions" : {                                  //List of mentions  		"julio.batista":"Julio Batista"             //Map with key(alias) and value(name) of the mentions  	}  } ``` |

Available Since
:   1.3.0

### GET /sociable/comments/{sociableId}

This method has been deprecated. Use /comments/v2 instead.

List comments from a sociable.

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| sociableId | path | - the sociable id | long |
| limit | query | - limit | required |
| offset | query | - offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {  	"comment" : "hi @julio.batista",                //Comment including mentions  	"creationDate" : "12/04/1874",                  //Creation date  	"commentWithoutMention" : "hi Julio Batista",   //Comment without mentions, with a plan text  	"mention" : "true",                             //True if it has mentions  	"user" : {                                      //User that has created the post  		"id" : "1",                             //User's id  		"name" : "User 01",                     //User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01",                     //user's alias  		"type" : "USER",                        //fixed  		"tenantId" : "22",                      //tenant's id  		"lastUpdate" : "10008520",              //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",                  //date the user has been created (in miliseconds)  		"numberModerations" : "1",              //number of the communities the user is moderator  		"state" : "ACTIVE"                      //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                                    //Where the post was created  		"id" : "1",                             //Community or user id  		"name" : "Community 01",                //community or name  		"description" : "Community 01 description", //community or user description  		"alias" : "community01",                //community or user alias  		"type" : "COMMUNITY",                   //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",                      //tenant's id  		"lastUpdate" : "10008520",              //date of last time the community or user has been modified (in miliseconds)  		"create" : "10008520",                  //date the community or user has been created (in miliseconds)  		"numberParticipations" : "10",          //number of users that participate of the community  		"numberModerations" : "1",              //number of the community's moderators  		"hidden" : "false",                     //indicates if it is a hidden community  		"privateContent" : "false",             //indicates if community's content is private  		"approvalRequired" : "true",            //indicates if it is necessary approval to join the community  		"admin" : "true",                       //indicates if the current user is community's administrator  		"state" : "ACTIVE"                      //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"mentions" : {                                  //List of mentions  		"julio.batista":"Julio Batista"             //Map with key(alias) and value(name) of the mentions  	}  } ``` |

Available Since
:   1.3.0

### POST /sociable/deleteStreamedFile/{fileName}

Removes a previously uploaded file into the streamed content area

Request Parameters

| name | type | description |
| --- | --- | --- |
| fileName | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.3.0

### POST /sociable/like/{sociableObjectId}

Like or unlike any sociable. Sociable being understood as any post or comment.

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| sociableObjectId | path | the sociableObject ID | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### GET /sociable/likers/{sociableId}

This method has been deprecated. Use /likers/v2/ instead.

List likes from a sociable.

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| sociableId | path | the sociable id | long |
| limit | query | limit | required |
| offset | query | offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {  	"name" : "Alberto",             //the name of the liker  	"alias" : "alberto.freitas",     //the alias of the liker  	"lastUpdateDate" : "20/9/1955",  } ``` |

Available Since
:   1.3.0

### POST /sociable/comment/remove/{commentId}

Remove a comment

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| commentId | path |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.4.11

### GET /sociable/comments/v2/{sociableId}

List comments from a sociable.

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| sociableId | path | - the sociable id | long |
| limit | query | - limit | required |
| offset | query | - offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {"content": {  	"comment" : "hi @julio.batista",                //Comment including mentions  	"creationDate" : "12/04/1874",                  //Creation date  	"commentWithoutMention" : "hi Julio Batista",   //Comment without mentions, with a plan text  	"mention" : "true",                             //True if it has mentions  	"user" : {                                      //User that has created the post  		"id" : "1",                             //User's id  		"name" : "User 01",                     //User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01",                     //user's alias  		"type" : "USER",                        //fixed  		"tenantId" : "22",                      //tenant's id  		"lastUpdate" : "10008520",              //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",                  //date the user has been created (in miliseconds)  		"numberModerations" : "1",              //number of the communities the user is moderator  		"state" : "ACTIVE"                      //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                                    //Where the post was created  		"id" : "1",                             //Community or user id  		"name" : "Community 01",                //community or name  		"description" : "Community 01 description", //community or user description  		"alias" : "community01",                //community or user alias  		"type" : "COMMUNITY",                   //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",                      //tenant's id  		"lastUpdate" : "10008520",              //date of last time the community or user has been modified (in miliseconds)  		"create" : "10008520",                  //date the community or user has been created (in miliseconds)  		"numberParticipations" : "10",          //number of users that participate of the community  		"numberModerations" : "1",              //number of the community's moderators  		"hidden" : "false",                     //indicates if it is a hidden community  		"privateContent" : "false",             //indicates if community's content is private  		"approvalRequired" : "true",            //indicates if it is necessary approval to join the community  		"admin" : "true",                       //indicates if the current user is community's administrator  		"state" : "ACTIVE"                      //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"mentions" : {                                  //List of mentions  		"julio.batista":"Julio Batista"             //Map with key(alias) and value(name) of the mentions  	}  }, //Response content  "message": null} // Message if returns exception ``` |

Available Since
:   1.4.11

### GET /sociable/likers/v2/{sociableId}

List likes from a sociable.

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| sociableId | path | the sociable id | long |
| limit | query | limit | required |
| offset | query | offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {"content": {  	"name" : "Alberto",             //the name of the liker  	"alias" : "alberto.freitas",     //the alias of the liker  	"lastUpdateDate" : "20/9/1955",  }, //Response content  "message": null} // Message if returns exception ``` |

Available Since
:   1.3.0

### POST /sociable/upload/stream/form/{fileName}

Uploads a file using InputStream and returns the file name stored in the stream content area

Request Parameters

| name | type | description |
| --- | --- | --- |
| fileName | path | just the file name and extension |

Request Body

| media type | data type |
| --- | --- |
| multipart/form-data | object |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | \*  ```  {  	"content": "IMG-160217-17212498170661200109346.png",  	"message": null  } ``` |

Available Since
:   1.3.0

### POST /sociable/upload/stream/octet/{fileName}

Uploads a file using InputStream and returns the file name stored in the stream content area

Request Parameters

| name | type | description |
| --- | --- | --- |
| fileName | path | just the file name and extension |

Request Body

| media type | data type |
| --- | --- |
| application/octet-stream | object |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | \*  ```  {  	"content": "IMG-160217-17212498170661200109346.png",  	"message": null  } ``` |
