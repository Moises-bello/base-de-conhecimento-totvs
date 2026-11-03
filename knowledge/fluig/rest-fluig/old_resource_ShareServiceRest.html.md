---
content_hash: f49aeb84d3c6b6b405a7a8fc85f6e8068d1cd1414e795b9771fb4efc774887d8
fetched_at: '2026-11-03T14:34:40.152782+00:00'
page_id: resource_ShareServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — ShareServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_ShareServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# ShareServiceRest Resource

Share

Available Since
:   1.3.0

### POST /social/share/share

This method has been deprecated. As of release 1.5.0, replaced by [shareContent](https://api.fluig.com/old/json_ShareServiceRest.html)

Share the content.

Available Since
:   1.3.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ShareVO](https://api.fluig.com/old/json_ShareVO_service.html) (JSON) | Response List of JSON (example):  ```  [{  	"contentId" : "10",                             //The content id  	"type" : "FOLLOWERS",                           //The type of target user is sharing. The values can be FOLLOWERS, USER or COMMUNITY  	"text": "I'm sharing this for you",             //The share text  	"aliasTargets" : ["paulo", "maria", "joao"],   //The social alias of targets.  	"shareType" : "SOCIAL"                          //The type of source user is sharing. The values can be SOCIAL or SOCIABLE  	}]  }] ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  The id of new created share ``` |

Available Since
:   1.5.0

### POST /social/share/shareContent

Share content

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ShareVO](https://api.fluig.com/old/json_ShareVO_service.html) (JSON) | Request Object JSON (example):  ```  {  	"contentId" : "1121" // REQUIRED - Code of the conent shared  	"text" : "Note of share" // REQUIRED - Note of author about share  	"aliasTargets" : ["mark.anthony","james.brown", "community-news"] // REQUIRED - target alias to share  	"shareType" : "Type of source content shared" // REQUIRED - [SOCIAL] to users of system OR [SOCIABLE] to generated content ``` |

"contentType" : "POST" //Type of content shared
"originUrl" : "videos/community-news/42" // The url origin of share
}

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |
