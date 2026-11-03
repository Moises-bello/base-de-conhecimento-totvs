---
content_hash: ab193f1ed05d01637fa292bddf0acc7293d85263108800c0ff04f23251e76b89
fetched_at: '2026-11-03T14:34:40.194868+00:00'
page_id: resource_SociableDocumentServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SociableDocumentServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SociableDocumentServiceRest Resource

Social features for documents

### POST /ecm/sociabledocument/comment

This method has been deprecated. Use /comment/v2 instead.

Comments a given document/version.This service supports multiple mentions on its content.   
In order to accept the mentions, the format user mentioned requires the following format:   
**"some text" ... @[social.alias] ... "more text"**.
  
**OBS:** It's not required to send additional text, only typing the characters "@[" + "alias" + "]" make it
works.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentCommentVO](https://api.fluig.com/old/json_SociableDocumentCommentVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10", 		//document's id  	"version" : "1000",  		//document's version  	"comment" : "Very nice @[jose.silva] !"	//comment's text with mention supported  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Response JSON (example):  ``` {  	"documentId" : "10",			//document's id  	"version" : "1000",			//document's version  	"numberLikes" : "2", 		//the number of users that have liked the document  	"numberShares" : "3", 		//the number of times the document has been shared  	"numberComments" : "1", 		//the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5", 		//number of users that follow the document  	"sociableId" : "12", 		//the id of the sociable object liked to the document  	"liked" : "true", 			//indicates if the current user have liked the document  	"following" : "false", 		//indicates if the current user is following the document  	"shared" : "true", 			//indicates if the current user have shared the document  	"commented" : "false",		//indicates if the current user have commented the document  	"denounced" : "false" 		//indicates if the current user have denounced the document  } ``` |

### POST /ecm/sociabledocument/denounce

Denounces a given document.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DenounceVO](https://api.fluig.com/old/json_DenounceVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10",	//document's id  	"version" : "1000",		//document's version  	"text" : "Bad content"	//Text that explains the denouncement's reason 	} 	 ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "10",			//document's id  	"version" : "1000",			//document's version  	"numberLikes" : "2", 		//the number of users that have liked the document  	"numberShares" : "3", 		//the number of times the document has been shared  	"numberComments" : "1", 		//the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5", 		//number of users that follow the document  	"sociableId" : "12", 		//the id of the sociable object liked to the document  	"liked" : "true", 			//indicates if the current user have liked the document  	"following" : "false", 		//indicates if the current user is following the document  	"shared" : "true", 			//indicates if the current user have shared the document  	"commented" : "false",		//indicates if the current user have commented the document  	"denounced" : "false" 		//indicates if the current user have denounced the document  } ``` |

### POST /ecm/sociabledocument/follow

Follows a given document.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10", //document's id  	"version" : "1000"	  //document's version  } 	 ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "10",			//document's id  	"version" : "1000",			//document's version  	"numberLikes" : "2", 		//the number of users that have liked the document  	"numberShares" : "3", 		//the number of times the document has been shared  	"numberComments" : "1", 		//the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5", 		//number of users that follow the document  	"sociableId" : "12", 		//the id of the sociable object liked to the document  	"liked" : "true", 			//indicates if the current user have liked the document  	"following" : "false", 		//indicates if the current user is following the document  	"shared" : "true", 			//indicates if the current user have shared the document  	"commented" : "false",		//indicates if the current user have commented the document  	"denounced" : "false" 		//indicates if the current user have denounced the document  } ``` |

### POST /ecm/sociabledocument/like

Likes a given document/version.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentLikeVO](https://api.fluig.com/old/json_SociableDocumentLikeVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10",	//document's id  	"version" : "1000"		//document's version  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "10",			//document's id  	"version" : "1000",			//document's version  	"numberLikes" : "2", 		//the number of users that have liked the document  	"numberShares" : "3", 		//the number of times the document has been shared  	"numberComments" : "1", 		//the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5", 		//number of users that follow the document  	"sociableId" : "12", 		//the id of the sociable object liked to the document  	"liked" : "true", 			//indicates if the current user have liked the document  	"following" : "false", 		//indicates if the current user is following the document  	"shared" : "true", 			//indicates if the current user have shared the document  	"commented" : "false",		//indicates if the current user have commented the document  	"denounced" : "false" 		//indicates if the current user have denounced the document  } ``` |

### POST /ecm/sociabledocument/share

Shares a given document.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ShareVO](https://api.fluig.com/old/json_ShareVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10",	//document's id  	"version" : "1000",		//document's version  	"type" : "COMMUNITY",	//The share type. It can be "FOLLOWERS" (only to users that follow you) or "COMMUNITY" (to communities you specify in the "aliases" list)  	"text" : "Look at this wonderful document!", 	//The share comment  	"aliases" : ["community1", "community2"]		//List of communities to share the document. If the "type" attribute is "FOLLOWERS", this value will be ignored.  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "10",			//document's id  	"version" : "1000",			//document's version  	"numberLikes" : "2", 		//the number of users that have liked the document  	"numberShares" : "3", 		//the number of times the document has been shared  	"numberComments" : "1", 		//the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5", 		//number of users that follow the document  	"sociableId" : "12", 		//the id of the sociable object liked to the document  	"liked" : "true", 			//indicates if the current user have liked the document  	"following" : "false", 		//indicates if the current user is following the document  	"shared" : "true", 			//indicates if the current user have shared the document  	"commented" : "false",		//indicates if the current user have commented the document  	"denounced" : "false" 		//indicates if the current user have denounced the document  } ``` |

### POST /ecm/sociabledocument/comment/denounce

Denounces a given comment.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [DenounceCommentVO](https://api.fluig.com/old/json_DenounceCommentVO.html) (JSON) | Request JSON (example):  ```  {  	"commentId" : "100",			//comment's id  	"text" : "Not a valid comment!" //text that explains the denouncement reason.  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /ecm/sociabledocument/comment/remove

Removes a given comment.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentCommentVO](https://api.fluig.com/old/json_SociableDocumentCommentVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "100" //the comment's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.11

### POST /ecm/sociabledocument/comment/v2

Comments a given document/version.This service supports multiple mentions on its content.   
In order to accept the mentions, the format user mentioned requires the following format:   
**"some text" ... @[social.alias] ... "more text"**.
  
**OBS:** It's not required to send additional text, only typing the characters "@[" + "alias" + "]" make it
works.

Available Since
:   1.4.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentCommentVO](https://api.fluig.com/old/json_SociableDocumentCommentVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10",        //document's id  	"version" : "1000",         //document's version  	"comment" : "Very nice @[jose.silva] !" //comment's text with mention supported  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {"content": {  	"documentId" : "10",         //document's id  	"version" : "1000",          //document's version  	"numberLikes" : "2",         //the number of users that have liked the document  	"numberShares" : "3",        //the number of times the document has been shared  	"numberComments" : "1",      //the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5",       //number of users that follow the document  	"sociableId" : "12",         //the id of the sociable object liked to the document  	"liked" : "true",            //indicates if the current user have liked the document  	"following" : "false",       //indicates if the current user is following the document  	"shared" : "true",           //indicates if the current user have shared the document  	"commented" : "false",       //indicates if the current user have commented the document  	"denounced" : "false"        //indicates if the current user have denounced the document  }, //Response content  "message": null} // Message if returns exception ``` |

Available Since
:   1.4.11

### POST /ecm/sociabledocument/like/v2

Likes a given document/version.

Available Since
:   1.4.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentLikeVO](https://api.fluig.com/old/json_SociableDocumentLikeVO.html) (JSON) | Request JSON (example):  ```  {  	"documentId" : "10",    //document's id  	"version" : "1000"      //document's version  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {"content": {  	"documentId" : "10",         //document's id  	"version" : "1000",          //document's version  	"numberLikes" : "2",         //the number of users that have liked the document  	"numberShares" : "3",        //the number of times the document has been shared  	"numberComments" : "1",      //the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5",       //number of users that follow the document  	"sociableId" : "12",         //the id of the sociable object liked to the document  	"liked" : "true",            //indicates if the current user have liked the document  	"following" : "false",       //indicates if the current user is following the document  	"shared" : "true",           //indicates if the current user have shared the document  	"commented" : "false",       //indicates if the current user have commented the document  	"denounced" : "false"        //indicates if the current user have denounced the document  }, //Response content  "message": null} // Message if returns exception ``` |

### GET /ecm/sociabledocument/comment/{id}/{version}

This method has been deprecated. Use /comment/v2 instead

Returns a list of the document's comments. This service supports the mention feature.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |
| limit | query | the limit of elements returned | int |
| offset | query | the offset | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SociableDocumentCommentVO](https://api.fluig.com/old/json_SociableDocumentCommentVO.html) (JSON) | Response List of JSON (example):  ``` [{  	"id" : "1",					//comment's id  	"documentId" : "10",		//document's id  	"version" : "1000",			//document's version  	"sociableObjectClass" : "com.totvs.technology.social.document.10", //the object's class  	"sociableObjectId" : "10", // the object's id  	"formattedTextWithoutMention" : "It's very useful Jose da Silva e Roberto Oliveira !", //Comment without mentions  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}  	"comment" : "It's very useful @[jose.silva] and @[roberto.oliveira] !", //The text of the comment  	"hasMentions" : "true", //Verify if have mention  	"mentions" : {  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}  }] ``` |

### GET /ecm/sociabledocument/counter/{id}/{version}

This method has been deprecated. Use /counter/v2 instead.

Returns the social counters of a given document and version:
number of likes, comments, denounces, shares and follows.
If the version was given, returns if the logged user is
following and has liked, commented or shared the document/version.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SociableDocumentVO](https://api.fluig.com/old/json_SociableDocumentVO.html) (JSON) | Response JSON (example):  ```  {  	"documentId" : "10",			//document's id  	"version" : "1000",			//document's version  	"numberLikes" : "2", 		//the number of users that have liked the document  	"numberShares" : "3", 		//the number of times the document has been shared  	"numberComments" : "1", 		//the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5", 		//number of users that follow the document  	"sociableId" : "12", 		//the id of the sociable object liked to the document  	"liked" : "true", 			//indicates if the current user have liked the document  	"following" : "false", 		//indicates if the current user is following the document  	"shared" : "true", 			//indicates if the current user have shared the document  	"commented" : "false",		//indicates if the current user have commented the document  	"denounced" : "false" 		//indicates if the current user have denounced the document  } ``` |

### GET /ecm/sociabledocument/denouncement/{id}/{version}

Returns a list of the document's denouncements.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SociableDocumentDenouncementVO](https://api.fluig.com/old/json_SociableDocumentDenouncementVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"documentId" : "10",  	"version" : "1000",  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}  }] ``` |

### GET /ecm/sociabledocument/follow/{id}/{version}

Returns a list of the document's followers.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SociableDocumentFollowVO](https://api.fluig.com/old/json_SociableDocumentFollowVO.html) (JSON) | Response List of JSON (example):  ``` [{  	"documentId" : "10",  	"version" : "1000",  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}  }] ``` |

### GET /ecm/sociabledocument/like/{id}/{version}

This method has been deprecated. Use /like/v2/ instead.

Returns the list of users that have liked the document/version.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |
| limit | query | the limit of elements returned | int |
| offset | query | the offset | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SociableDocumentLikeVO](https://api.fluig.com/old/json_SociableDocumentLikeVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"documentId" : "10", //the id of the document  	"version" : "1000", // the document's version  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}  }] ``` |

### GET /ecm/sociabledocument/share/{id}/{version}

Returns a list of the document's shares.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SociableDocumentShareVO](https://api.fluig.com/old/json_SociableDocumentShareVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"documentId" : "10",  	"version" : "1000",  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	} 	}] 	 ``` |

Available Since
:   1.4.11

### GET /ecm/sociabledocument/comment/v2/{id}/{version}

Returns a list of the document's comments. This service supports the mention feature.

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |
| limit | query | the limit of elements returned | int |
| offset | query | the offset | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ``` [{"content" : {  	"id" : "1",                 //comment's id  	"documentId" : "10",        //document's id  	"version" : "1000",         //document's version  	"sociableObjectClass" : "com.totvs.technology.social.document.10", //the object's class  	"sociableObjectId" : "10", // the object's id  	"formattedTextWithoutMention" : "It's very useful Jose da Silva e Roberto Oliveira !", //Comment without mentions  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}  	"comment" : "It's very useful @[jose.silva] and @[roberto.oliveira] !", //The text of the comment  	"hasMentions" : "true", //Verify if have mention  	"mentions" : {  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}  }, //Response content  "message": null} // Message if returns exception ```  ] |

Available Since
:   1.4.11

### GET /ecm/sociabledocument/counter/v2/{id}/{version}

Returns the social counters of a given document and version:
number of likes, comments, denounces, shares and follows.
If the version was given, returns if the logged user is
following and has liked, commented or shared the document/version.

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {"content": {  	"documentId" : "10",         //document's id  	"version" : "1000",          //document's version  	"numberLikes" : "2",         //the number of users that have liked the document  	"numberShares" : "3",        //the number of times the document has been shared  	"numberComments" : "1",      //the number of times the document has been commented  	"numberDenouncements" : "0", //the number of times the document has been denounced  	"numberFollows" : "5",       //number of users that follow the document  	"sociableId" : "12",         //the id of the sociable object liked to the document  	"liked" : "true",            //indicates if the current user have liked the document  	"following" : "false",       //indicates if the current user is following the document  	"shared" : "true",           //indicates if the current user have shared the document  	"commented" : "false",       //indicates if the current user have commented the document  	"denounced" : "false"        //indicates if the current user have denounced the document  }, //Response content  "message": null} // Message if returns exception ``` |

### GET /ecm/sociabledocument/folder/{tenant}/{alias}/{feature}

Returns the id of the folder used as storage of the given feature of a given community.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |
| feature | path | REQUIRED (DOCUMENT | GALLERY\_PHOTO | GALLERY\_VIDEO | ARTICLE | FORM) |  |
| tenant | path | REQUIRED tenant's code that community belongs | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) (JSON) | Response JSON (example):  ```  {  	"tenantId" : "22",			//tenant's id  	"userId" : "1",				//the community's id  	"spaceAlias" : "community1",//the community's alias  	"socialFolderId" : "12",	//id of the folder used as storage for the given feature  	"socialFolderDescription" : "Folder", //folder's description  	"socialFolderEnabled" : "true",		  //indicates if the feature is enabled for the community  	"socialFolderSecurity" : "false",	  //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  	"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  } ``` |

Available Since
:   1.4.11

### GET /ecm/sociabledocument/like/v2/{id}/{version}

Returns the list of users that have liked the document/version.

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| id | path | REQUIRED document's id | int |
| version | path | REQUIRED document's version | int |
| limit | query | the limit of elements returned | int |
| offset | query | the offset | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"documentId" : "10", //the id of the document  	"version" : "1000", // the document's version  	"user" : {"content": {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	}  }, //Response content  "message": null} // Message if returns exception] ``` |

### GET /ecm/sociabledocument/enabled/{tenant}/{userCode}/{alias}/{feature}

Returns the flags that indicate if the given feature is
enabled for the given social. It checks if the given user has permission
to access these features.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |
| feature | path | REQUIRED (DOCUMENT | PHOTO | VIDEO | ARTICLE | FORM) |  |
| tenant | path | REQUIRED tenant's code that community belongs | long |
| userCode | path | REQUIRED user that is going to use the feature |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) (JSON) | Response JSON (example):  ```  { 		"tenantId" : "22",			//tenant's id 		"userId" : "1",				//the community's id 		"spaceAlias" : "community1",//the community's alias 		"socialFolderId" : "12",	//id of the folder used as storage for the given feature 		"socialFolderDescription" : "Folder", //folder's description 		"socialFolderEnabled" : "true",		  //indicates if the feature is enabled for the community 		"socialFolderSecurity" : "false",	  //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value) 		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder 	} 	 ``` |
