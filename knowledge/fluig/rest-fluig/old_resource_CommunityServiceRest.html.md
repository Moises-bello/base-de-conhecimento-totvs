---
content_hash: a87c7e8b452ddb147552d416c4163a59f870df7d8473e747db088429986e4287
fetched_at: '2026-11-03T14:34:39.585244+00:00'
page_id: resource_CommunityServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — CommunityServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CommunityServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CommunityServiceRest Resource

Communities

### POST /social/community/addGroups

Add the users from the given group as participants to the given
community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GroupsVO](https://api.fluig.com/old/json_GroupsVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community02",   //REQUIRED community's alias  	"groupCodes" : ["group01", "group02"]   //REQUIRED alias of users to be included as community's participant  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/community/addParticipants

Add participants to the given community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AddParticipantsVO](https://api.fluig.com/old/json_AddParticipantsVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community02",   //REQUIRED community's alias  	"userAliases" : ["user01", "user02"]    //REQUIRED (alias, idpId or userCode) of users to be included as community's participant  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /social/community/changeImage

Change the communitys's image
  
Accepted media types: PNG, JPG, JPEG.

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community01", //REQUIRED the community's alias  	"base64media" : "4747545" //REQUIRED media's content in base64 format  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/community/create

This method has been deprecated. As of release 1.5.0, replaced by [newCommunity](https://api.fluig.com/old/json_CommunityServiceRest.html)

Creates a new community

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommunityVO](https://api.fluig.com/old/json_CommunityVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community02",    //REQUIRED community's alias  	"name" : "Community 02",    //REQUIRED community's name  	"description" : "This is the community 02", //REQUIRED community's description  	"admin" : {  		"id":"1", // The id of the admin user  		"alias" // The alias of the admin user  	}, //REQUIRED The user that is going to be the administrator of the created community  	"hidden" : "false",     //Indicates if it will be a hidden community  	"privateContent" : "false", //Indicates if the community's content will be private  	"approvalRequired" : "true", //Indicates if it's necessary approval to join the community  	"socialEcmVO" : {  		"ecmVideoFolderId" : "9" //Folder's id where the video's community is stored. Set value = 0 to exclude association with folder  		"ecmPhotoFolderId" : "10" //Folder's id where the photo's community is stored. Set value = 0 to exclude association with folder  		"ecmDocumentFolderId" : "3" //Folder's id where the document's community is stored. Set value = 0 to exclude association with folder  		"ecmArticleFolderId" : "4" //Folder's id where the article's community is stored. Set value = 0 to exclude association with folder  		"ecmFormsFolderId" : "4" //Folder's id where the form's community is stored. Set value = 0 to exclude association with folder  		"ecmDocumentApplySecurity" : "true" //Indicates if document security validation should be applied  	}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` {"value" : "alias"} ``` |

Available Since
:   1.3.0

### GET /social/community/listCommunities

List alll communities.

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |
| pattern | query | filter to search |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  {  	"content": {[{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }]  }  "message": ""} ``` |

Available Since
:   1.4.0

### GET /social/community/listCommunitiesWithRelevance

List communities with relevance and ordenation type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.4.0

### GET /social/community/listFavoriteCommunitiesWithRelevance

List favorite communities with relevance and ordenation type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.5.7

### GET /social/community/listPagesWithComunities

Find fluig pages: send data query param

Available Since
:   1.5.7

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| filter | query | REQUIRED filter |  |  |
| internalPages | query | selected also internalPages when true | false | boolean |
| isMobile | query | filter to search only mobile pages/comunities | false | boolean |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { "content": [{ "pageId": 29, "pageIcon": "portal/api/servlet/image/1/page/pagefavorites.png", "title": "Documentos favoritos", "description": "Documentos favoritos", "searchLevel": 0, "pageCode": "pagefavorites", "children": [], "parentPageCode": "principalfavorites", "uri": "portal/p/1/pagefavorites", "friendlyURL": null }, { "pageId": 31, "pageIcon": "portal/api/servlet/image/1/page/pageprocessfavorites.png", "title": "Processos favoritos", "description": "Processos favoritos", "searchLevel": 0, "pageCode": "pageprocessfavorites", "children": [], "parentPageCode": "principalfavorites", "uri": "portal/p/1/pageprocessfavorites", "friendlyURL": null }, { "pageId": 33, "pageIcon": "portal/api/servlet/image/1/page/pagecontactfavorites.png", "title": "Contatos Favoritos", "description": "Contatos Favoritos", "searchLevel": 0, "pageCode": "pagecontactfavorites", "children": [], "parentPageCode": "principalfavorites", "uri": "portal/p/1/pagecontactfavorites", "friendlyURL": null }], "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   in 1.5.0

### POST /social/community/new

Creates a new community

Available Since
:   in 1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommunityVO](https://api.fluig.com/old/json_CommunityVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community02",    //REQUIRED community's alias  	"name" : "Community 02",    //REQUIRED community's name  	"description" : "This is the community 02", //REQUIRED community's description  	"admin" : {  		"id":"1", // The id of the admin user  		"alias" // The alias of the admin user  	}, //REQUIRED The user that is going to be the administrator of the created community  	"hidden" : "false",     //Indicates if it will be a hidden community  	"privateContent" : "false", //Indicates if the community's content will be private  	"approvalRequired" : "true", //Indicates if it's necessary approval to join the community  	"socialEcmVO" : {  		"ecmVideoFolderId" : "9" //Folder's id where the video's community is stored. Set value = 0 to exclude association with folder  		"ecmPhotoFolderId" : "10" //Folder's id where the photo's community is stored. Set value = 0 to exclude association with folder  		"ecmDocumentFolderId" : "3" //Folder's id where the document's community is stored. Set value = 0 to exclude association with folder  		"ecmArticleFolderId" : "4" //Folder's id where the article's community is stored. Set value = 0 to exclude association with folder  		"ecmFormsFolderId" : "4" //Folder's id where the form's community is stored. Set value = 0 to exclude association with folder  		"ecmDocumentApplySecurity" : "true" //Indicates if document security validation should be applied  	},  	"cloudCodes" : ["cliente","convidado"],  	"addInCloud" : "true",     //Associate community admin with selected clouds  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

### POST /social/community/notify

Registers the logged user to be notified about new interactions
in the given community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community-fluig" //community's alias (required)  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /social/community/removeGroups

Remove the users from the given group as participants to the given
community.

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GroupsVO](https://api.fluig.com/old/json_GroupsVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community02",   //REQUIRED community's alias  	"groupCodes" : ["group01", "group02"]   //REQUIRED alias of users to be included as community's participant  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/community/request

Request participation in the community.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RequestParticipationVO](https://api.fluig.com/old/json_RequestParticipationVO.html) (JSON) | Request JSON (example):  ```  {  	"communityAlias" : "community02",   //community's alias  	"requesterAlias" : "user01" //alias of user that wants to enjoy the community  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/community/stopNotify

Unregisters the logged user as a community's follower.
The user will no longer be notified about new community interactions.
NOTE: This method does NOT remove the user as participant.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community-fluig" //community's alias (required)  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /social/community/update

Updates a community

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommunityVO](https://api.fluig.com/old/json_CommunityVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "community02",    //REQUIRED community's alias  	"name" : "Community 02",    //community's name  	"description" : "This is the community 02", //community's description  	"admin" : {  		"id":"1", // The id of the admin user  		"alias" // The alias of the admin user  	}, //REQUIRED The user that is going to be the administrator of the created community  	"hidden" : "false",     //Indicates if it will be a hidden community  	"privateContent" : "false", //Indicates if the community's content will be private  	"approvalRequired" : "true", //Indicates if it's necessary approval to join the community  	"socialEcmVO" : [{  		"ecmVideoFolderId" : "9" //Folder's id where the video's community is stored. Set value = 0 to exclude association with folder  		"ecmPhotoFolderId" : "10" //Folder's id where the photo's community is stored. Set value = 0 to exclude association with folder  		"ecmDocumentFolderId" : "3" //Folder's id where the document's community is stored. Set value = 0 to exclude association with folder  		"ecmArticleFolderId" : "4" //Folder's id where the article's community is stored. Set value = 0 to exclude association with folder  		"ecmFormsFolderId" : "4" //Folder's id where the form's community is stored. Set value = 0 to exclude association with folder  		"ecmDocumentApplySecurity" : "true" //Indicates if document security validation should be applied  	}]  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {{  	"id" : "1",             //Community's id  	"tenantId" : "1",       //Tenant' id  	"creationDate" : "1441394384000",      //date the community has been created (in miliseconds)  	"lastUpdateDate" : "1441394385000",    //date of last time the community has been modified (in miliseconds)  	"alias" : "Community_Alias",       //Community's Alias  	"name" : "Community_Name",         //Community's Name  	"description" : "Community Description",  //Community's Description  	"type" : "COMMUNITY",      //indicates if this social is a COMMUNITY or USER  	"state" : "ACTIVE", //indicates if this community is ACTIVE or INACTIVE  	"hidden" : "false",     //indicates if it is a hidden community  	"privateContent" : "false",            //indicates if community's content is private  	"approvalRequired" : "false",    //indicates if it is necessary approval to join the community  	"customPage" : "true",   //indicates if this community has a custom page  	"userAdmin" : {              //Admin object  	"id" : "2",              //Admin's Id  	"tenantId" : "1",        //Tenant's Id  	"creationDate" : "1441390079000",      //date the user has been created (in miliseconds)  	"lastUpdateDate" : "1441390423000",    //date of last time the user has been modified (in miliseconds)  	"alias" : "admin.fluig", //Admin's Alias  	"name" : "Admin Fluig",  //Admin's Name  	"description" : "Admin do Fluig",   //Admin's description  	"type" : "USER",        //indicates if this social is a COMMUNITY or USER  	"state" : "ACTIVE",     //indicates if the Admin is ACTIVE or INACTIVE  	"resourceType" : "USER",  //indicates if the resource type is a COMMUNITY or USER  	"resourceDescription" : "Resource for: admin.fluig",  //Resource description  	"page" : "social/admin.fluig",    //Admin's Page  	"securityCode":"admin.fluig_2"    //Admin's Security Page  	},  	"resourceType" : "COMMUNITY",  //indicates if the resource type is a COMMUNITY or USER  	"resourceDescription" : "Resource for: Community_Alias",  //Resource description  	"page" : "subject/Community_Alias",     //Community's Page  	"visibility" : "PUBLIC",    //indicates the community's visibility, PUBLIC or PRIVATE  	"securityCode" : "Community_Alias_8",   //Community's Security Page  }  }  "message": ""} ``` |

### GET /social/community/{alias}

This method has been deprecated. Use /v2/ instead.

Get a community by its alias

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED the community's alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ExtendedCommunityVO](https://api.fluig.com/old/json_ExtendedCommunityVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE",             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	"document" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community document  	"galleryPhoto" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community photo gallery  	"galleryVideo" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community video gallery  	"article" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community article  	"form" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community form  	"userData":{  		"UserRamal":"11 1111111",  		"UserProjects":"VP Fluig",  		"UserSpecialization":"Programadora Java",  		"UserEmailHTML":null} // User data  } ``` |

Available Since
:   1.3.0

### POST /social/community/changeStatus/{alias}

Change the community status. If the community is Active becomes Inactive, if the community is Inactive becomes Active.

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED the community's alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### GET /social/community/communitiesOrderFavorites/{genericId}

This method has been deprecated. Use /communitiesOrderFavorites/v2/ instead.

List communities ordered by favorites.

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |
| pattern | query | filter to search |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.3.0

### GET /social/community/communityMember/{alias}

Returns if logged user is community participant.

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED the community's alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GenericVO](https://api.fluig.com/old/json_GenericVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"value" : "true"//community's status  }] ``` |

Available Since
:   1.3.0

### GET /social/community/enabled/{alias}

Returns if the community is active.

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED the community's alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GenericVO](https://api.fluig.com/old/json_GenericVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"value" : "true"//community's status  }] ``` |

### GET /social/community/image/{alias}

Returns the communitys's profile image based on its alias

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED the communitys's alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | A application/octet-stream with the image file |

Available Since
:   1.4.0

### GET /social/community/listModeratorsWithRelevance/{alias}

Return list moderators of community with relevance and order type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |  |
| limit | query | limit the number of registers in the returned list. Default value 20 |  | required |
| offset | query | defines the first registry in the returned list. Default value 0 |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | User name used like filter. Empty value returns all users |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.4.0

### GET /social/community/listMyCommunitiesWithRelevance/{genericId}

List my communities or communities where social is participant with relevance and ordenation type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |  |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",   //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.4.0

### GET /social/community/listMyCommunitiesWithRelevanceByLogin/{login}

List my communities or communities where social is participant with relevance and ordenation type

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| login | path | REQUIRED User's login |  |  |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",   //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.4.0

### GET /social/community/listParticipantsWithRelevance/{alias}

Get the participants of a community with relevance and ordenation type.

Available Since
:   1.4.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |  |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.5.9

### GET /social/community/listPendingRequestsWithRelevance/{alias}

Get the users with pending request for a community with relevance and ordenation type.

Available Since
:   1.5.9

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |  |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| orderType | query | selected order to return registers | DEFAULT | "ASC" or "DEFAULT" or "DESC" or "NEWEST" or "OLDER" |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`[{ "id" : "1", //Community's id "name" : "Community 01",//community's name "description" : "Community 01 description", //community's description "alias" : "community01", //community's alias "type" : "COMMUNITY", //fixed "tenantId" : "22", //tenant's id "lastUpdate" : "10008520", //date of last time the community has been modified (in miliseconds) "create" : "10008520", //date the community has been created (in miliseconds) "numberParticipations" : "10", //number of users that participate of the community "numberModerations" : "1", //number of the community's moderators "hidden" : "false", //indicates if it is a hidden community "privateContent" : "false", //indicates if community's content is private "approvalRequired" : "true", //indicates if it is necessary approval to join the community "admin" : "true", //indicates if the current user is community's administrator "state" : "ACTIVE" //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED") }]` |

Available Since
:   1.3.0

### GET /social/community/moderators/{alias}

List community moderators.

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",     //User's id  	"name" : "Moderator 01",//User's name  	"description" : "Moderator 01 description",  //User's description  	"alias" : "moderator01", //user's alias  	"type" : "USER",    //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the user has been modified (in miliseconds)  	"create" : "10008520",      //date the user has been created (in miliseconds)  	"numberModerations" : "1",     //number of the communities the user is moderator  	"state" : "ACTIVE"             //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  } ``` |

Available Since
:   1.3.0

### GET /social/community/notifyList/{alias}

Returns users that are being notified about the interactions in the
given community.

Available Since
:   1.3.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |  |
| limit | query | limit the number of registers in the returned list | 10 | int |
| offset | query | defines the first registry in the returned list | 0 | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [UserVO](https://api.fluig.com/old/json_UserVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",                               //user's id  	"name" : "John Fluig",                   //user's name  	"description" : "Software Engineer",      //user's description  	"alias" : "john.fluig",                   //user's alias  	"lastUpdate" : "100001582"                //last time the user has been updated (in miliseconds)  }] ``` |

Available Since
:   1.3.0

### GET /social/community/participants/{alias}

This method has been deprecated. Use /participants/v2/ instead.

Get the participants of a community.

Available Since
:   1.3.0

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |  |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |

Available Since
:   1.4.0

### GET /social/community/relationStatus/{aliasCommunity}

Return the status relation between the logged user and community

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| aliasCommunity | path | community alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  [{  	"content" : "ACCEPTED", // The options are  ACCEPTED, REJECTED, PENDING, BLOCKED, NOT_RELATED, ITSELF  	"message" : "OK" // Messsage  }] ``` |

Available Since
:   1.4.11

### GET /social/community/v2/{alias}

Get a community by its alias

Available Since
:   1.4.11

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED the community's alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{"content": {  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE",             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	"document" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community document  	"galleryPhoto" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community photo gallery  	"galleryVideo" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community video gallery  	"article" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community article  	"form" : {  		"tenantId" : "22",          //tenant's id  		"userId" : "1",             //the community's id  		"spaceAlias" : "community1",//the community's alias  		"socialFolderId" : "12",    //id of the folder used as storage for the given feature  		"socialFolderDescription" : "Folder", //folder's description  		"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  		"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  		"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  }, // Community form  	"userData":{  		"UserRamal":"11 1111111",  		"UserProjects":"VP Fluig",  		"UserSpecialization":"Programadora Java",  		"UserEmailHTML":null} // User data  }, //Response content  "message": null} // Message if returns exception ``` |

Available Since
:   1.4.8

### POST /social/community/{alias}/forceAllMembersWatch

Force all participants to watch the community

Available Since
:   1.4.8

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | community alias |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | List of users that has been forced to watch the community (users that was previously watching the community won't be listed)  ```  { 	"content": [    	{        	"id": 4,        	"name": "John Smith",        	"lastName": null,        	"fullName": null,        	"description": null,        	"alias": "john",        	"type": "USER",        	"tenantId": 1,        	"tenantUUID": null,        	"lastUpdate": 1423073061000,        	"createDate": 1423073061000,        	"customPage": false,        	"email": null,        	"numberFriends": 0,        	"numberParticipations": 1,        	"numberFollowing": 0,        	"numberFollowers": 0,        	"numberModerations": 0,        	"isModerator": false,        	"isAdmin": false,        	"hidden": false,        	"privateContent": false,        	"favorite": false,        	"approvalRequired": true,        	"tenantAdmin": false,        	"admin": null,        	"state": "ACTIVE",        	"ecmInfo": null,        	"followerStatus": null,        	"followingStatus": "NOT_RELATED",        	"participantStatus": "ACCEPTED",        	"userData": {            	"email": "john@company.com"        	},        	"page": "social/john"    	},    	{        	"id": 5,        	"name": "Jane Watson",        	"lastName": null,        	"fullName": null,        	"description": null,        	"alias": "jane",        	"type": "USER",        	"tenantId": 1,        	"tenantUUID": null,        	"lastUpdate": 1423073125000,        	"createDate": 1423073125000,        	"customPage": false,        	"email": null,        	"numberFriends": 0,        	"numberParticipations": 2,        	"numberFollowing": 0,        	"numberFollowers": 0,        	"numberModerations": 0,        	"isModerator": false,        	"isAdmin": false,        	"hidden": false,        	"privateContent": false,        	"favorite": false,        	"approvalRequired": true,        	"tenantAdmin": false,        	"admin": null,        	"state": "ACTIVE",        	"ecmInfo": null,        	"followerStatus": null,        	"followingStatus": "NOT_RELATED",        	"participantStatus": "ACCEPTED",        	"userData": {            	"email": "jane@company.com.br"        	},        	"page": "social/jane"    	} 	], 	"message": null} ``` |

Available Since
:   1.5.9

### POST /social/community/accept/{communityAlias}/{requesterGenericId}

Accept a solicitation of a user to join a community.

Available Since
:   1.5.9

Request Parameters

| name | type | description |
| --- | --- | --- |
| communityAlias | path | REQUIRED Alias of the community |
| requesterGenericId | path | REQUIRED Alias of participation requester |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.3.0

### POST /social/community/addModerator/{communityAlias}/{genericId}

Add new moderator to community. Since 1.3.

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| communityAlias | path | REQUIRED the community's alias |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /social/community/changeAdmin/{communityAlias}/{genericId}

Change community administrator.

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| communityAlias | path | REQUIRED the community's alias |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.11

### GET /social/community/communitiesOrderFavorites/v2/{genericId}

List communities ordered by favorites.

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |  |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |
| pattern | query | filter to search |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{"content": {  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }, //Response content  "message": null} // Message if returns exception] ``` |

### GET /social/community/folder/{alias}/{feature}

Returns the id of the folder used as storage of the given feature of a given community.

Request Parameters

| name | type | description |
| --- | --- | --- |
| alias | path | REQUIRED community's alias |
| feature | path | REQUIRED (DOCUMENT | GALLERY\_PHOTO | GALLERY\_VIDEO | ARTICLE | FORM) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) (JSON) | Response JSON (example):  ```  {  	"tenantId" : "22",          //tenant's id  	"userId" : "1",             //the community's id  	"spaceAlias" : "community1",//the community's alias  	"socialFolderId" : "12",    //id of the folder used as storage for the given feature  	"socialFolderDescription" : "Folder", //folder's description  	"socialFolderEnabled" : "true",       //indicates if the feature is enabled for the community  	"socialFolderSecurity" : "false",     //indicates if the security applied to the folder is the ECM's security(true value) or the community's security(false value)  	"socialFolderWritePermission" : "true"//indicates if the current user has write permission in the folder  } ``` |

Available Since
:   1.3.0

### GET /social/community/imageBySize/{alias}/{size}

Returns the communitys's profile image based on its alias and size

Available Since
:   1.3.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED the communitys's alias |  |
| size | path | REQUIRED image size. Possible values: 80|160|320|432|640|864|1060. | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/octet-stream | object | A application/octet-stream with the image file |

Available Since
:   1.4.0

### GET /social/community/isCommunityAdmin/{aliasCommunity}/{genericId}

Verify if user is community admin

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| aliasCommunity | path | community alias |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  [{  	"content" : "true", //If user is community admin  	"message" : "OK" // Messsage  }] ``` |

Available Since
:   1.4.0

### GET /social/community/isCommunityModerator/{aliasCommunity}/{genericId}

Verify if teh logged user is community admin

Available Since
:   1.4.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| aliasCommunity | path | community alias |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  [{  	"content" : "true", //If user is community admin  	"message" : "OK" // Messsage  }] ``` |

Available Since
:   1.4.11

### GET /social/community/participants/v2/{alias}

Get the participants of a community.

Available Since
:   1.4.11

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED the community's alias |  |  |
| limit | query | limit of records returned |  | required |
| offset | query | the offset |  | required |
| pattern | query | filter to search |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{"content": {  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }, //Response content  "message": null} // Message if returns exception] ``` |

Available Since
:   1.5.9

### POST /social/community/reject/{communityAlias}/{requesterGenericId}

Reject a solicitation of a user to join a community.

Available Since
:   1.5.9

Request Parameters

| name | type | description |
| --- | --- | --- |
| communityAlias | path | REQUIRED Alias of the community |
| requesterGenericId | path | REQUIRED Alias of participation requester |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.3.0

### POST /social/community/removeModerator/{communityAlias}/{genericId}

Removes community moderator

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| communityAlias | path | REQUIRED the community's alias |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.0

### POST /social/community/removeParticipant/{communityAlias}/{genericId}

Removes community participant.

Available Since
:   1.3.0

Request Parameters

| name | type | description |
| --- | --- | --- |
| communityAlias | path | REQUIRED the community's alias |
| genericId | path | REQUIRED the user's generic identifier, can be (alias, idpId or userCode) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### GET /social/community/comunity/participant/{communityId}/{pattern}

This method has been deprecated. on 1.3.0

Get the participants of a community.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| communityId | path | REQUIRED the community's id | long |
| pattern | path | REQUIRED filter to search |  |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [SocialVO](https://api.fluig.com/old/json_SocialVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",             //Community's id  	"name" : "Community 01",//community's name  	"description" : "Community 01 description", //community's description  	"alias" : "community01",    //community's alias  	"type" : "COMMUNITY",       //fixed  	"tenantId" : "22",          //tenant's id  	"lastUpdate" : "10008520",  //date of last time the community has been modified (in miliseconds)  	"create" : "10008520",      //date the community has been created (in miliseconds)  	"numberParticipations" : "10", //number of users that participate of the community  	"numberModerations" : "1",     //number of the community's moderators  	"hidden" : "false",            //indicates if it is a hidden community  	"privateContent" : "false",    //indicates if community's content is private  	"approvalRequired" : "true",   //indicates if it is necessary approval to join the community  	"admin" : "true",              //indicates if the current user is community's administrator  	"state" : "ACTIVE"             //Indicates the status of the community (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  }] ``` |
