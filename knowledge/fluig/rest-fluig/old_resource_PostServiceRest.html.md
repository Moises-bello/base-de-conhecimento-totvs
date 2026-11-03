---
content_hash: 1f9d958fa7a461bdb4cd199d6fa75ea82a3c1a7d49c9ed4d430a4b7e4bcd691e
fetched_at: '2026-11-03T14:34:40.066893+00:00'
page_id: resource_PostServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — PostServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_PostServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# PostServiceRest Resource

Timeline posts

### POST /social/post/create

This method has been deprecated. on 1.3.0

Create a post in user or community time-line, it depends on which alias
is used. The post visibility can be PUBLIC, PRIVATE (only followers and
participants) and CUSTOM. If CUSTOM then is necessary to send a list of
user IDS in customUsers field. The sociableObjectId is to attach an
sociable object to the post, like an image, video or a document. This
service supports multiple mentions on its content.   
In order to accept mentions feature, each mentioned user requires the
following format:   
**"some text" ... @[social.alias] ... "more text"**.   
**OBS:** It's not required sending additional text, only typing the
characters "@[" + "alias" + "]" make it functionality works.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PublicApiPostVO](https://api.fluig.com/old/json_PublicApiPostVO.html) (JSON) | Request JSON (example):  ``` {  	"text" : "A post to @[jose.silva] !",   //REQUIRED text to be posted. Supports mentions  	"visibility" : "CUSTOM",    //REQUIRED It can be PUBLIC, PRIVATE (just followers or participants) or CUSTOM  	"alias" : "community01",    //REQUIRED the alias of the space community or user (alias, idpId or userCode) the post will be created  	"customUsers" : ["01","02"], //if the visibility is CUSTOM, this field is used to tell which users can view this post  	"sociableObjectId" : "122"  //Used to attach an content to this post, like an image, video, document, etc.  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [TimelineVO](https://api.fluig.com/old/json_TimelineVO.html) (JSON) | Response JSON of the post created (example):  ``` {  	"postId" : "10",    //post id  	"text" : "A Post to @[jose.silva] and @[roberto.oliveira] !",   //post text  	"formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions  	"link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post  	"formattedLink" : "www.youtube.com/v/10", //formatted youtube link  	"youtubeVideoId" : "10",                //youtube video id  	"user" : {                          //User that has created the post  		"id" : "1",     //User's id  		"name" : "User 01",//User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01", //user's alias  		"type" : "USER",    //fixed  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",      //date the user has been created (in miliseconds)  		"numberModerations" : "1",     //number of the communities the user is moderator  		"state" : "ACTIVE"             //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                    //Where the post was created  		"id" : "1", //Community's id  		"name" : "Community 01",//community's name  		"description" : "Community 01 description", //community's description  		"alias" : "community01",    //community's alias  		"type" : "COMMUNITY",       //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  		"create" : "10008520",      //date the community has been created (in miliseconds)  		"numberParticipations" : "10", //number of users that participate of the community  		"numberModerations" : "1",     //number of the community's moderators  		"hidden" : "false",            //indicates if it is a hidden community  		"privateContent" : "false",    //indicates if community's content is private  		"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  		"admin" : "true",              //indicates if the current user is community's administrator  		"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"creationDate" : "10008520",    //timestamp the post has been created (in miliseconds)  	"tenantId" : "22",          //tenant's id  	"linkedObject" : "null",    //the object attached to the post (image, document, video, etc)  	"type" : "DEFAULT",         //post type. It can be "DEFAULT" or "RECOMMENDATION"  	"visibility" : "PUBLIC",    //It can be PUBLIC, PRIVATE or CUSTOM  	"comments" : [{  		"id" : "10",        //comment's id  		"comment" : "Comment on @[jose.silva]", //comment's text  		"user" : {},        //who commented (the same structure the "user" post's field)  		"creationDate" : "10008520",    //timestamp the commented has been created  		"formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions  	}],  	"numberLikes" : "1",    //number of post's like  	"numberShares" : "1",   //number of times the post has been shared  	"numberComments" : "1", //number of post's comments  	"numberDenouncements" : "1",    //number of times the post has been denounced  	"tags" : "tag tag02",       //tags in the post  	"url" : "/post/user/10",        //post's url  	"hasMentions" : "true", //Verify if has mentions in the comment  	"mentions" : [{  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}]  } ``` |

### POST /social/post/notify

Registers the logged user to be notified about new interactions in the
given post.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PublicApiPostVO](https://api.fluig.com/old/json_PublicApiPostVO.html) (JSON) | Request JSON (example):  ```  {  	"postId" : "1" //post's id (required)  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.6.1

### POST /social/post/publish

Create a post in user or community time-line, it depends on which alias
is used. The post visibility can be PUBLIC, PRIVATE (only followers and
participants) and CUSTOM. If CUSTOM then is necessary to send a list of
user IDS in customUsers field. The sociableObjectId is to attach an
sociable object to the post, like an image, video or a document. This
service supports multiple mentions on its content.   
In order to accept mentions feature, each mentioned user requires the
following format:   
**"some text" ... @[social.alias] ... "more text"**.   
**OBS:** It's not required sending additional text, only typing the
characters "@[" + "alias" + "]" make it functionality works.

Available Since
:   1.6.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PublicApiPostVO](https://api.fluig.com/old/json_PublicApiPostVO.html) (JSON) | Request JSON (example):  ```  {  	"text" : "A post to @[jose.silva] !",   //text to be posted. Supports mentions  	"visibility" : "CUSTOM",    //It can be PUBLIC, PRIVATE (just followers or participants) or CUSTOM  	"alias" : "community01",    //the alias of the space (community or user) the post will be created  	"customUsers" : ["user01"], //if ths visibility is CUSTOM, this field is used to tell which users can view this post  	"sociableObjectId" : "122",  //Used to attach an content to this post, like an image, video, document, etc.  	"attachments":["file001.jpg", file002.jpg", "file003.jpg"]  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Post ID ``` |

### POST /social/post/remove

Remove a post in the timeline

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PublicApiPostVO](https://api.fluig.com/old/json_PublicApiPostVO.html) (JSON) | Request JSON (example):  ```  {  	"postId" : "1" //post's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/post/stopNotify

Unregisters the logged user as a post's follower. The user will no longer
be notified about new post interactions.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PublicApiPostVO](https://api.fluig.com/old/json_PublicApiPostVO.html) (JSON) | Request JSON (example):  ```  {  	"postId" : "1" //post's id  (required)  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /social/post/{genericId}

This method has been deprecated. since 1.7.0. Use the method listSortedPostByLogin or listSortedPost.

Finds Posts by a given community alias. This service supports the mention
feature.

Request Parameters

| name | type | description |
| --- | --- | --- |
| genericId | path | REQUIRED Social identifier. For user can be alias, idpId or userCode, for community just alias. |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [TimelineVO](https://api.fluig.com/old/json_TimelineVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"postId" : "10",	//post id  	"text" : "A Post to @[jose.silva] and @[roberto.oliveira] !",	//post text  	"formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions  	"link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post  	"formattedLink" : "www.youtube.com/v/10", //formatted youtube link  	"youtubeVideoId" : "10",				//youtube video id  	"user" : {							//User that has created the post  		"id" : "1",		//User's id  		"name" : "User 01",//User's name  		"description" : "User 01 description",	//User's description  		"alias" : "user01",	//user's alias  		"type" : "USER",	//fixed  		"tenantId" : "22",			//tenant's id  		"lastUpdate" : "10008520",	//date of last time the user has been modified (in miliseconds)  		"create" : "10008520",		//date the user has been created (in miliseconds)  		"numberModerations" : "1",	   //number of the communities the user is moderator  		"state" : "ACTIVE"			   //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {					//Where the post was created  		"id" : "1",	//Community's id  		"name" : "Community 01",//community's name  		"description" : "Community 01 description",	//community's description  		"alias" : "community01",	//community's alias  		"type" : "COMMUNITY",		//it can be "USER" or "COMMUNITY"  		"tenantId" : "22",			//tenant's id  		"lastUpdate" : "10008520",	//date of last time the community has been modified (in miliseconds)  		"create" : "10008520",		//date the community has been created (in miliseconds)  		"numberParticipations" : "10", //number of users that participate of the community  		"numberModerations" : "1",	   //number of the community's moderators  		"hidden" : "false",			   //indicates if it is a hidden community  		"privateContent" : "false",	   //indicates if community's content is private  		"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  		"admin" : "true",			   //indicates if the current user is community's administrator  		"state" : "ACTIVE"			   //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"creationDate" : "10008520",	//timestamp the post has been created (in miliseconds)  	"tenantId" : "22",			//tenant's id  	"linkedObject" : "null",	//the object attached to the post (image, document, video, etc)  	"type" : "DEFAULT",			//post type. It can be "DEFAULT" or "RECOMMENDATION"  	"visibility" : "PUBLIC",	//It can be PUBLIC, PRIVATE or CUSTOM  	"comments" : [{  		"id" : "10",		//comment's id  		"comment" : "Comment on @[jose.silva]",	//comment's text  		"user" : {},		//who commented (the same structure the "user" post's field)  		"creationDate" : "10008520",	//timestamp the commented has been created  		"formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions  	}],  	"shareMentionVO":{ // mentions in sharing  		"formattedWithoutMention":"Maria Olivia please read teh post", //formatted post text without mentions  		"mentions":{"maria":"Maria Olivia"} // Mentions  	},  	"numberLikes" : "1",	//number of post's like  	"numberShares" : "1",	//number of times the post has been shared  	"numberComments" : "1",	//number of post's comments  	"numberDenouncements" : "1",	//number of times the post has been denounced  	"numberWatchers" : "1", //number of users that are notified about new post interactions  	"tags" : "tag tag02",		//tags in the post  	"url" : "/post/user/10",		//post's url  	"hasMentions" : "true", //Verify if has mentions in the comment  	"isSupported" : "true", //Indicates whether the post is supported or not  	"mentions" : [{  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}]  }] ``` |

### GET /social/post/list/{genericId}

This method has been deprecated. since 1.4.0. Use the method listSortedPostByLogin or listSortedPost.

Finds Posts by a given community alias. This service supports the mention
feature.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| genericId | path | REQUIRED Social identifier. For user can be alias, idpId or userCode, for community just alias. |  |
| lastPostId | query | the last post (it works like offset) | long |
| limit | query | limit of posts | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [TimelineVO](https://api.fluig.com/old/json_TimelineVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"postId" : "10",    //post id  	"text" : "A Post to @[jose.silva] and @[roberto.oliveira] !",   //post text  	"formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions  	"link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post  	"formattedLink" : "www.youtube.com/v/10", //formatted youtube link  	"youtubeVideoId" : "10",                //youtube video id  	"user" : {                          //User that has created the post  		"id" : "1",     //User's id  		"name" : "User 01",//User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01", //user's alias  		"type" : "USER",    //fixed  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",      //date the user has been created (in miliseconds)  		"numberModerations" : "1",     //number of the communities the user is moderator  		"state" : "ACTIVE"             //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                    //Where the post was created  		"id" : "1", //Community's id  		"name" : "Community 01",//community's name  		"description" : "Community 01 description", //community's description  		"alias" : "community01",    //community's alias  		"type" : "COMMUNITY",       //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  		"create" : "10008520",      //date the community has been created (in miliseconds)  		"numberParticipations" : "10", //number of users that participate of the community  		"numberModerations" : "1",     //number of the community's moderators  		"hidden" : "false",            //indicates if it is a hidden community  		"privateContent" : "false",    //indicates if community's content is private  		"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  		"admin" : "true",              //indicates if the current user is community's administrator  		"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"creationDate" : "10008520",    //timestamp the post has been created (in miliseconds)  	"tenantId" : "22",          //tenant's id  	"linkedObject" : "null",    //the object attached to the post (image, document, video, etc)  	"type" : "DEFAULT",         //post type. It can be "DEFAULT" or "RECOMMENDATION"  	"visibility" : "PUBLIC",    //It can be PUBLIC, PRIVATE or CUSTOM  	"comments" : [{  		"id" : "10",        //comment's id  		"comment" : "Comment on @[jose.silva]", //comment's text  		"user" : {},        //who commented (the same structure the "user" post's field)  		"creationDate" : "10008520",    //timestamp the commented has been created  		"formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions  	}],  	"shareMentionVO":{ // mentions in sharing  		"formattedWithoutMention":"Maria Olivia please read teh post", //formatted post text without mentions  		"mentions":{"maria":"Maria Olivia"} // Mentions  	},  	"numberLikes" : "1",    //number of post's like  	"numberShares" : "1",   //number of times the post has been shared  	"numberComments" : "1", //number of post's comments  	"numberDenouncements" : "1",    //number of times the post has been denounced  	"numberWatchers" : "1", //number of users that are notified about new post interactions  	"tags" : "tag tag02",       //tags in the post  	"url" : "/post/user/10",        //post's url  	"hasMentions" : "true", //Verify if has mentions in the comment  	"isSupported" : "true", //Indicates whether the post is supported or not  	"mentions" : [{  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}]  }] ``` |

Available Since
:   1.4.0

### GET /social/post/listSortedPost/{genericId}

List sorted posts by alias. This service supports the mention feature.

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED Social identifier. For user can be alias, idpId or userCode, for community just alias. |  |  |
| lastPostId | query | the last post (it works like offset) |  | long |
| limit | query | limit of posts. Default value 20. | 20 | required |
| orderingType | query | define how the list will be orKEdered. Possibles values are 'LAST\_UPDATE', 'CREATION\_DATE', 'MORE\_LIKE' and 'MY\_PUBLICATIONS'. |  | "CREATION\_DATE" or "LAST\_COMMENT" or "LAST\_UPDATE" or "MORE\_LIKE" or "MY\_PUBLICATIONS" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`{ "content": [{ "postId" : "10", //post id "text" : "A Post to @[jose.silva] and @[roberto.oliveira] !", //post text "formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions "link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post "formattedLink" : "www.youtube.com/v/10", //formatted youtube link "youtubeVideoId" : "10", //youtube video id "user" : { //User that has created the post "id" : "1", //User's id "name" : "User 01",//User's name "description" : "User 01 description", //User's description "alias" : "user01", //user's alias "type" : "USER", //fixed "tenantId" : "22", //tenant's id "lastUpdate" : "10008520", //date of last time the user has been modified (in miliseconds) "create" : "10008520", //date the user has been created (in miliseconds) "numberModerations" : "1", //number of the communities the user is moderator "state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED") }, "social" : { //Where the post was created "id" : "1", //Community's id "name" : "Community 01",//community's name "description" : "Community 01 description", //community's description "alias" : "community01", //community's alias "type" : "COMMUNITY", //it can be "USER" or "COMMUNITY" "tenantId" : "22", //tenant's id "lastUpdate" : "10008520", //date of last time the community has been modified (in miliseconds) "create" : "10008520", //date the community has been created (in miliseconds) "numberParticipations" : "10", //number of users that participate of the community "numberModerations" : "1", //number of the community's moderators "hidden" : "false", //indicates if it is a hidden community "privateContent" : "false", //indicates if community's content is private "approvalRequired" : "true", //indicates if it is necessary approval to join the community "admin" : "true", //indicates if the current user is community's administrator "state" : "ACTIVE" //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED") }, "creationDate" : "10008520", //timestamp the post has been created (in miliseconds) "updateDate" : "147765762", //timestamp the post has been edited(in miliseconds) "tenantId" : "22", //tenant's id "linkedObject" : "null", //the object attached to the post (image, document, video, etc) "type" : "DEFAULT", //post type. It can be "DEFAULT" or "RECOMMENDATION" "visibility" : "PUBLIC", //It can be PUBLIC, PRIVATE or CUSTOM "comments" : [{ "id" : "10", //comment's id "comment" : "Comment on @[jose.silva]", //comment's text "user" : {}, //who commented (the same structure the "user" post's field) "creationDate" : "10008520", //timestamp the commented has been created "formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions }], "shareMentionVO":{ // mentions in sharing "formattedWithoutMention":"Maria Olivia please read teh post", //formatted post text without mentions "mentions":{"maria":"Maria Olivia"} // Mentions }, "numberLikes" : "1", //number of post's like "numberShares" : "1", //number of times the post has been shared "numberComments" : "1", //number of post's comments "numberDenouncements" : "1", //number of times the post has been denounced "numberWatchers" : "1", //number of users that are notified about new post interactions "tags" : "tag tag02", //tags in the post "url" : "/post/user/10", //post's url "hasMentions" : "true", //Verify if has mentions in the comment "isSupported" : "true", //Indicates whether the post is supported or not "mentions" : [{ "jose.silva" : "Jose da Silva", "roberto.oliveira" : "Roberto Oliveira" }] }], "message": ""}` |

Available Since
:   1.6.4

### GET /social/post/listSortedPostByLogin/{login}

List sorted posts by alias. This service supports the mention feature.

Available Since
:   1.6.4

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| login | path | REQUIRED User's login. |  |  |
| lastPostId | query | the last post (it works like offset) |  | long |
| limit | query | limit of posts. Default value 20. | 20 | required |
| orderingType | query | define how the list will be ordered. Possibles values are 'LAST\_UPDATE', 'CREATION\_DATE', 'MORE\_LIKE' and 'MY\_PUBLICATIONS'. |  | "CREATION\_DATE" or "LAST\_COMMENT" or "LAST\_UPDATE" or "MORE\_LIKE" or "MY\_PUBLICATIONS" |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`{ "content": [{ "postId" : "10", //post id "text" : "A Post to @[jose.silva] and @[roberto.oliveira] !", //post text "formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions "link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post "formattedLink" : "www.youtube.com/v/10", //formatted youtube link "youtubeVideoId" : "10", //youtube video id "user" : { //User that has created the post "id" : "1", //User's id "name" : "User 01",//User's name "description" : "User 01 description", //User's description "alias" : "user01", //user's alias "type" : "USER", //fixed "tenantId" : "22", //tenant's id "lastUpdate" : "10008520", //date of last time the user has been modified (in miliseconds) "create" : "10008520", //date the user has been created (in miliseconds) "numberModerations" : "1", //number of the communities the user is moderator "state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED") }, "social" : { //Where the post was created "id" : "1", //Community's id "name" : "Community 01",//community's name "description" : "Community 01 description", //community's description "alias" : "community01", //community's alias "type" : "COMMUNITY", //it can be "USER" or "COMMUNITY" "tenantId" : "22", //tenant's id "lastUpdate" : "10008520", //date of last time the community has been modified (in miliseconds) "create" : "10008520", //date the community has been created (in miliseconds) "numberParticipations" : "10", //number of users that participate of the community "numberModerations" : "1", //number of the community's moderators "hidden" : "false", //indicates if it is a hidden community "privateContent" : "false", //indicates if community's content is private "approvalRequired" : "true", //indicates if it is necessary approval to join the community "admin" : "true", //indicates if the current user is community's administrator "state" : "ACTIVE" //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED") }, "creationDate" : "10008520", //timestamp the post has been created (in miliseconds) "updateDate" : "147765762", //timestamp the post has been edited(in miliseconds) "tenantId" : "22", //tenant's id "linkedObject" : "null", //the object attached to the post (image, document, video, etc) "type" : "DEFAULT", //post type. It can be "DEFAULT" or "RECOMMENDATION" "visibility" : "PUBLIC", //It can be PUBLIC, PRIVATE or CUSTOM "comments" : [{ "id" : "10", //comment's id "comment" : "Comment on @[jose.silva]", //comment's text "user" : {}, //who commented (the same structure the "user" post's field) "creationDate" : "10008520", //timestamp the commented has been created "formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions }], "shareMentionVO":{ // mentions in sharing "formattedWithoutMention":"Maria Olivia please read teh post", //formatted post text without mentions "mentions":{"maria":"Maria Olivia"} // Mentions }, "numberLikes" : "1", //number of post's like "numberShares" : "1", //number of times the post has been shared "numberComments" : "1", //number of post's comments "numberDenouncements" : "1", //number of times the post has been denounced "numberWatchers" : "1", //number of users that are notified about new post interactions "tags" : "tag tag02", //tags in the post "url" : "/post/user/10", //post's url "hasMentions" : "true", //Verify if has mentions in the comment "isSupported" : "true", //Indicates whether the post is supported or not "mentions" : [{ "jose.silva" : "Jose da Silva", "roberto.oliveira" : "Roberto Oliveira" }] }], "message": ""}` |

### GET /social/post/notifyList/{postId}

Returns users that are being notified about the interactions in the given
post.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| postId | path | REQUIRED the post id |  | long |
| limit | query | limit the number of registers in the returned list | 10 | int |
| offset | query | defines the first registry in the returned list | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [UserVO](https://api.fluig.com/old/json_UserVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

### GET /social/post/read/{postId}

This method has been deprecated. 1.4.0

Finds a post by id

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| postId | path | REQUIRED the id of post |  | long |
| limit | query | Limit of comments that will be loaded | 5 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"postId" : "10",    //post id  	"text" : "A Post to @[jose.silva] and @[roberto.oliveira] !",   //post text  	"formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions  	"link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post  	"formattedLink" : "www.youtube.com/v/10", //formatted youtube link  	"youtubeVideoId" : "10",                //youtube video id  	"user" : {                          //User that has created the post  		"id" : "1",     //User's id  		"name" : "User 01",//User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01", //user's alias  		"type" : "USER",    //fixed  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",      //date the user has been created (in miliseconds)  		"numberModerations" : "1",     //number of the communities the user is moderator  		"state" : "ACTIVE"             //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                    //Where the post was created  		"id" : "1", //Community's id  		"name" : "Community 01",//community's name  		"description" : "Community 01 description", //community's description  		"alias" : "community01",    //community's alias  		"type" : "COMMUNITY",       //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  		"create" : "10008520",      //date the community has been created (in miliseconds)  		"numberParticipations" : "10", //number of users that participate of the community  		"numberModerations" : "1",     //number of the community's moderators  		"hidden" : "false",            //indicates if it is a hidden community  		"privateContent" : "false",    //indicates if community's content is private  		"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  		"admin" : "true",              //indicates if the current user is community's administrator  		"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"creationDate" : "10008520",    //timestamp the post has been created (in miliseconds)  	"tenantId" : "22",          //tenant's id  	"linkedObject" : "null",    //the object attached to the post (image, document, video, etc)  	"type" : "DEFAULT",         //post type. It can be "DEFAULT" or "RECOMMENDATION"  	"visibility" : "PUBLIC",    //It can be PUBLIC, PRIVATE or CUSTOM  	"comments" : [{  		"id" : "10",        //comment's id  		"comment" : "Comment on @[jose.silva]", //comment's text  		"user" : {},        //who commented (the same structure the "user" post's field)  		"creationDate" : "10008520",    //timestamp the commented has been created  		"formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions  	}],  	"shareMentionVO":{ // mentions in sharing  		"formattedWithoutMention":"Maria Olivia please read teh post", //formatted post text without mentions  		"mentions":{"maria":"Maria Olivia"} // Mentions  	},  	"numberLikes" : "1",    //number of post's like  	"numberShares" : "1",   //number of times the post has been shared  	"numberComments" : "1", //number of post's comments  	"numberDenouncements" : "1",    //number of times the post has been denounced  	"tags" : "tag tag02",       //tags in the post  	"url" : "/post/user/10",        //post's url  	"hasMentions" : "true", //Verify if has mentions in the comment  	"mentions" : [{  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}]  }] ``` |

Available Since
:   1.3.0

### POST /social/post/create/with/upload

This method has been deprecated.

Create a post in user or community time-line, it depends on which alias
is used. The post visibility can be PUBLIC, PRIVATE (only followers and
participants) and CUSTOM. If CUSTOM then is necessary to send a list of
user IDS in customUsers field. The sociableObjectId is to attach an
sociable object to the post, like an image, video or a document. This
service supports multiple mentions on its content.   
In order to accept mentions feature, each mentioned user requires the
following format:   
**"some text" ... @[social.alias] ... "more text"**.   
**OBS:** It's not required sending additional text, only typing the
characters "@[" + "alias" + "]" make it functionality works.

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PublicApiPostVO](https://api.fluig.com/old/json_PublicApiPostVO.html) (JSON) | Request JSON (example):  ```  {  	"text" : "A post to @[jose.silva] !",   //text to be posted. Supports mentions  	"visibility" : "CUSTOM",    //It can be PUBLIC, PRIVATE (just followers or participants) or CUSTOM  	"alias" : "community01",    //the alias of the space (community or user) the post will be created  	"customUsers" : ["user01"], //if ths visibility is CUSTOM, this field is used to tell which users can view this post  	"sociableObjectId" : "122",  //Used to attach an content to this post, like an image, video, document, etc.  	"mediaVO" : {                                       //NOT REQUIRED  		"base64media" : "sadfsd5852dfa2d2fasdf344w5",  //REQUIRED Media on string base 64  		"mediaName" : "file.jpg",                       //REQUIRED Media name  		"mediaType" : "PHOTO"                           //REQUIRED Media type - PHOTO or VIDEO  	}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` Post ID ``` |

Available Since
:   1.4.0

### GET /social/post/read/post/{postId}

Finds a post by id

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| postId | path | REQUIRED the id of post |  | long |
| limit | query | Limit of comments that will be loaded | 2 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"postId" : "10",    //post id  	"text" : "A Post to @[jose.silva] and @[roberto.oliveira] !",   //post text  	"formattedWithoutMention": "A Post to Jose da Silva and Roberto Oliveira !", //formatted post text without mentions  	"link" : "http://www.youtube.com/watch?v=E2LM3ZlcDnk", //link attached to the post  	"formattedLink" : "www.youtube.com/v/10", //formatted youtube link  	"youtubeVideoId" : "10",                //youtube video id  	"user" : {                          //User that has created the post  		"id" : "1",     //User's id  		"name" : "User 01",//User's name  		"description" : "User 01 description",  //User's description  		"alias" : "user01", //user's alias  		"type" : "USER",    //fixed  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the user has been modified (in miliseconds)  		"create" : "10008520",      //date the user has been created (in miliseconds)  		"numberModerations" : "1",     //number of the communities the user is moderator  		"state" : "ACTIVE"             //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"social" : {                    //Where the post was created  		"id" : "1", //Community's id  		"name" : "Community 01",//community's name  		"description" : "Community 01 description", //community's description  		"alias" : "community01",    //community's alias  		"type" : "COMMUNITY",       //it can be "USER" or "COMMUNITY"  		"tenantId" : "22",          //tenant's id  		"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  		"create" : "10008520",      //date the community has been created (in miliseconds)  		"numberParticipations" : "10", //number of users that participate of the community  		"numberModerations" : "1",     //number of the community's moderators  		"hidden" : "false",            //indicates if it is a hidden community  		"privateContent" : "false",    //indicates if community's content is private  		"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  		"admin" : "true",              //indicates if the current user is community's administrator  		"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"creationDate" : "10008520",    //timestamp the post has been created (in miliseconds)  	"tenantId" : "22",          //tenant's id  	"linkedObject" : "null",    //the object attached to the post (image, document, video, etc)  	"type" : "DEFAULT",         //post type. It can be "DEFAULT" or "RECOMMENDATION"  	"visibility" : "PUBLIC",    //It can be PUBLIC, PRIVATE or CUSTOM  	"comments" : [{  		"id" : "10",        //comment's id  		"comment" : "Comment on @[jose.silva]", //comment's text  		"user" : {},        //who commented (the same structure the "user" post's field)  		"creationDate" : "10008520",    //timestamp the commented has been created  		"formattedTextWithoutMention" : "Comment on Jose da Silva" // formatted comment's text without mentions  	}],  	"shareMentionVO":{ // mentions in sharing  		"formattedWithoutMention":"Maria Olivia please read teh post", //formatted post text without mentions  		"mentions":{"maria":"Maria Olivia"} // Mentions  	},  	"numberLikes" : "1",    //number of post's like  	"numberShares" : "1",   //number of times the post has been shared  	"numberComments" : "1", //number of post's comments  	"numberDenouncements" : "1",    //number of times the post has been denounced  	"tags" : "tag tag02",       //tags in the post  	"url" : "/post/user/10",        //post's url  	"hasMentions" : "true", //Verify if has mentions in the comment  	"mentions" : [{  		"jose.silva" : "Jose da Silva",  		"roberto.oliveira" : "Roberto Oliveira"  	}]  }] ``` |
