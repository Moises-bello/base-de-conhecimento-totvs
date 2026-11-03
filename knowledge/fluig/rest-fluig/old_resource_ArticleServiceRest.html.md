---
content_hash: 3d10bed0011e2d11d2e8c066fc8923a19d7fe7a3945cabd9ddb1a2d6740eabd5
fetched_at: '2026-11-03T14:34:39.403380+00:00'
page_id: resource_ArticleServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — ArticleServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_ArticleServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# ArticleServiceRest Resource

Articles (in communities)

### POST /social/article/remove

Removes an article

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10" //article's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/article/save

Create or update an article.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleVO](https://api.fluig.com/old/json_ArticleVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10",		//article's id to update. To create an article, this value needs to be passe as null  	"categoryId" : "1",	//OPTIONAL: category's id this article belongs. If it is null, the article will be created in the root articles folder.  	"name" : "Article",	//article's name  	"description" : "Article 01",	 //article's description  	"version" : "1000", 			 //article's version (only for update)  	"alias" : "community01", 		 //community's alias where this article is going to be published  	"topicId" : "1", 				 //id of the article's subject  	"expirationDate" : "1000101220", //OPTIONAL: date the article will expire (in miliseconds)  	"keyWord" : "article new",		 //key words for the article  	"content" : "This is an article!"//article's content  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | number (JSON) | ```  An integer value that is the id of the saved article ``` |

### POST /social/article/category/create

Creates a category.   
**Note1:** If the parent id is null will be created a category on the root folder.
**Note1:** A category is phisically an ECM folder.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Request JSON (example):  ```  {  	"alias" : "communnity01",	//community's alias  	"parentId" : "1",			//OPTIONAL: id of the parent category. If it is null, the category will be created in the root articles folder.  	"name" : "Category 01",		//category's name  	"description" : "Nice cat"	//category's description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "2",					//category's id  	"parentId" : "1",			//parent category's id  	"name" : "Category 01", 	//category's name  	"description" : "Nice cat",	//category's description  	"totalDocs" : "0",			//number of articles in this category  	"type" : "CATEGORY",		//fixed  	"url" : "/fluig/cat01",		//category's url  	"alias" : "communnity01"	//alias of community this category belongs  } ``` |

### POST /social/article/category/remove

Remove a category.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10" //category's id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### POST /social/article/category/update

Updates a description of category

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10",		//category's id  	"alias" : "community01",  //community's alias the category belongs  	"description" : "New category description" //new description  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

### GET /social/article/order/{categoryId}

Get current category order.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| categoryId | path | REQUIRED category's id | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | ```  This method returns a plain value, that can be:  				CREATION_DATE_ASC, CREATION_DATE_DESC, DESCRIPTION_ASC, DESCRIPTION_DESC, NA 			 ``` |

### GET /social/article/{alias}/{categoryId}

List articles with pagination   
**Note 1:** If no limit is provided it'll be considered no limit   
**Note 2:** If no offset is provided it'll be considered the value 0.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |
| categoryId | path | REQUIRED the id of the article's category | long |
| limit | query | the limit of records returned | int |
| offset | query | the offset | int |
| orderBy | query | (CREATION\_DATE\_ASC | CREATION\_DATE\_DESC | DESCRIPTION\_ASC | DESCRIPTION\_DESC | NA) |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [ArticleVO](https://api.fluig.com/old/json_ArticleVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1",							//article's id  	"categoryId" : "4",					//id of the category this article belongs  	"name" : "Article 01",				//article's name  	"description" : "Art description",	//article's description  	"url" : "/fluig/article01",			//article's URL  	"file" : "article01.html",			//file with the article's content  	"version" : "1000",					//article's version  	"alias" : "community01",			//alias of community where this article has been published  	"type" : "ARTICLE",					//fixed  	"numberMedias" : "1",				//number of files the article has  	"socialObjectId" : "10",			//social id  	"canEdit" : "true",					//indicates if the article can be edited  	"topicId" : "1",					//id of the article's subject  	"topicDescription" : "subject",		//article's subject description  	"publicationDate" : "1441100015",	//date the article has been published (in miliseconds)  	"expirationDate" : "1441100015",	//date the article expires  	"keyWord" : "art",					//key word  	"creationDate" : "1441100015",		//date the article has been created (in miliseconds)  	"content" : "This is an article!",	//article's content  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"accessCount" : "10",		//number of times the article has been accessed  	"totalDocs" : "2",			//number of files the article has  	"expires" : "true"			//indicates if the article expires  }] ``` |

### GET /social/article/category/{alias}/{parentId}

List all the categories of alias

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |  |
| parentId | path | REQUIRED the id of the category's parent |  | int |
| limit | query | the limit of returned records. To return all categories don't use this parameter. | 2147483647 | int |
| offset | query | the offset. DEFAULT VALUE = 0. | 0 | int |
| pattern | query | filter the category description. DEFAULT VALUE = "", in this case return all the categories. |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "2",					//category's id  	"parentId" : "1",			//parent category's id  	"name" : "Category 01", 	//category's name  	"description" : "Nice cat",	//category's description  	"totalDocs" : "0",			//number of articles in this category  	"type" : "CATEGORY",		//fixed  	"url" : "/fluig/cat01",		//category's url  	"alias" : "communnity01"	//alias of community this category belongs  }] ``` |

### GET /social/article/byid/{alias}/{categoryId}/{articleId}

Looks for an article by its id

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |
| articleId | path | REQUIRED article's id | long |
| categoryId | path | REQUIRED id of the article's category | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleLiveURLVO](https://api.fluig.com/old/json_ArticleLiveURLVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",							//article's id  	"categoryId" : "4",					//id of the category this article belongs  	"name" : "Article 01",				//article's name  	"description" : "Art description",	//article's description  	"url" : "/fluig/article01",			//article's URL  	"file" : "article01.html",			//file with the article's content  	"version" : "1000",					//article's version  	"alias" : "community01",			//alias of community where this article has been published  	"type" : "ARTICLE",					//fixed  	"numberMedias" : "1",				//number of files the article has  	"socialObjectId" : "10",			//social id  	"canEdit" : "true",					//indicates if the article can be edited  	"topicId" : "1",					//id of the article's subject  	"topicDescription" : "subject",		//article's subject description  	"publicationDate" : "1441100015",	//date the article has been published (in miliseconds)  	"expirationDate" : "1441100015",	//date the article expires  	"keyWord" : "art",					//key word  	"creationDate" : "1441100015",		//date the article has been created (in miliseconds)  	"content" : "This is an article!",	//article's content  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"accessCount" : "10",		//number of times the article has been accessed  	"totalDocs" : "2",			//number of files the article has  	"expires" : "true",			//indicates if the article expires  	"liveURL" : "http://fluig.com/1234"		//url to access the article with security token ``` |

### GET /social/article/category/byid/{alias}/{id}

Looks for a category by its id

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |
| id | path |  | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCategoryVO](https://api.fluig.com/old/json_ArticleCategoryVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "2",					//category's id  	"parentId" : "1",			//parent category's id  	"name" : "Category 01", 	//category's name  	"description" : "Nice cat",	//category's description  	"totalDocs" : "0",			//number of articles in this category  	"type" : "CATEGORY",		//fixed  	"url" : "/fluig/cat01",		//category's url  	"alias" : "communnity01"	//alias of community this category belongs  } ``` |

### GET /social/article/categoryarticle/{alias}/{parentId}/{categoryId}

- List all the categories of alias   
- List articles with pagination   
**Note 1:** If no limit is provided it'll be considered no limit   
**Note 2:** If no offset is provided it'll be considered the value 0.

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |  |
| categoryId | path | REQUIRED category's id to list all the articles that belong to this category |  | long |
| parentId | path | REQUIRED id of parent category. If it is 0, it will return the categories in the root folder |  | int |
| limit | query | the limit of returned records. It is applied to the articles, not for the categories. | 30 | int |
| offset | query | the offset | 0 | int |
| orderBy | query | (CREATION\_DATE\_ASC | CREATION\_DATE\_DESC | DESCRIPTION\_ASC | DESCRIPTION\_DESC | NA) |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) (JSON) | Response List of JSON (example):  ```  [{  	"categories" : [{  		"id" : "2",					//category's id  		"parentId" : "1",			//parent category's id  		"name" : "Category 01", 	//category's name  		"description" : "Nice cat",	//category's description  		"totalDocs" : "0",			//number of articles in this category  		"type" : "CATEGORY",		//fixed  		"url" : "/fluig/cat01",		//category's url  		"alias" : "communnity01"	//alias of community this category belongs  	}],  	"articles" : [{  		"id" : "1",							//article's id  		"categoryId" : "4",					//id of the category this article belongs  		"name" : "Article 01",				//article's name  		"description" : "Art description",	//article's description  		"url" : "/fluig/article01",			//article's URL  		"file" : "article01.html",			//file with the article's content  		"version" : "1000",					//article's version  		"alias" : "community01",			//alias of community where this article has been published  		"type" : "ARTICLE",					//fixed  		"numberMedias" : "1",				//number of files the article has  		"socialObjectId" : "10",			//social id  		"canEdit" : "true",					//indicates if the article can be edited  		"topicId" : "1",					//id of the article's subject  		"topicDescription" : "subject",		//article's subject description  		"publicationDate" : "1441100015",	//date the article has been published (in miliseconds)  		"expirationDate" : "1441100015",	//date the article expires  		"keyWord" : "art",					//key word  		"creationDate" : "1441100015",		//date the article has been created (in miliseconds)  		"content" : "This is an article!",	//article's content  		"user" : {  			"id" : "3", //the id of the user  			"name" : "User", //the name of the user  			"description" : "user description", //the description of the user  			"alias" : "user", //the user alias  			"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  			"tenantId" : "22", //the tenant id  			"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  			"createDate" : "100082255845", //date that user has been created (in miliseconds)  			"numberFriends" : "52", //number of user's friends  			"numberParticipations" : "10", //number of communities the user participates  			"numberFollowing" : "10", //number of users that this user is following  			"numberFollowers" : "10", //number of users that are folloing this user  			"numberModerations" : "10", //number of communities this user is moderator  			"hidden" : "false", //This attribute is always false if the type is "USER"  			"privateContent" : "false", //This attribute is always false if the type is "USER"  			"approvalRequired" : "false", //This attribute is always false if the type is "USER"  			"admin" : "true", //Indicates if this user is the tenant admin  			"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  		},  		"accessCount" : "10",		//number of times the article has been accessed  		"totalDocs" : "2",			//number of files the article has  		"expires" : "true"			//indicates if the article expires  	}]  } ``` |

### GET /social/article/editbyid/{alias}/{categoryId}/{articleId}

Looks for an article by its id for edition purpose.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | REQUIRED community's alias |  |
| articleId | path | REQUIRED article's id | long |
| categoryId | path | REQUIRED id of the article's category | int |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleVO](https://api.fluig.com/old/json_ArticleVO.html) (JSON) | Response JSON (example):  ```  {  	"id" : "1",							//article's id  	"categoryId" : "4",					//id of the category this article belongs  	"name" : "Article 01",				//article's name  	"description" : "Art description",	//article's description  	"url" : "/fluig/article01",			//article's URL  	"file" : "article01.html",			//file with the article's content  	"version" : "1000",					//article's version  	"alias" : "community01",			//alias of community where this article has been published  	"type" : "ARTICLE",					//fixed  	"numberMedias" : "1",				//number of files the article has  	"socialObjectId" : "10",			//social id  	"canEdit" : "true",					//indicates if the article can be edited  	"topicId" : "1",					//id of the article's subject  	"topicDescription" : "subject",		//article's subject description  	"publicationDate" : "1441100015",	//date the article has been published (in miliseconds)  	"expirationDate" : "1441100015",	//date the article expires  	"keyWord" : "art",					//key word  	"creationDate" : "1441100015",		//date the article has been created (in miliseconds)  	"content" : "This is an article!",	//article's content  	"user" : {  		"id" : "3", //the id of the user  		"name" : "User", //the name of the user  		"description" : "user description", //the description of the user  		"alias" : "user", //the user alias  		"type" : "USER", //the user type (it can be "USER" or "COMMUNITY")  		"tenantId" : "22", //the tenant id  		"lastUpdate" : "100082255845", //date of last user update (in miliseconds)  		"createDate" : "100082255845", //date that user has been created (in miliseconds)  		"numberFriends" : "52", //number of user's friends  		"numberParticipations" : "10", //number of communities the user participates  		"numberFollowing" : "10", //number of users that this user is following  		"numberFollowers" : "10", //number of users that are folloing this user  		"numberModerations" : "10", //number of communities this user is moderator  		"hidden" : "false", //This attribute is always false if the type is "USER"  		"privateContent" : "false", //This attribute is always false if the type is "USER"  		"approvalRequired" : "false", //This attribute is always false if the type is "USER"  		"admin" : "true", //Indicates if this user is the tenant admin  		"state" : "ACTIVE" //Indicates the status of the user (it can be "UNCONFIRMED", "ACTIVE", "BLOCKED" or "REMOVED")  	},  	"accessCount" : "10",		//number of times the article has been accessed  	"totalDocs" : "2",			//number of files the article has  	"expires" : "true",			//indicates if the article expires  	"liveURL" : "http://fluig.com/1234"		//url to access the article with security token  } ``` |
