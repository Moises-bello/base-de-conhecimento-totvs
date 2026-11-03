---
content_hash: d9bd5ccf97c51764c926509cdf4088fdb0ae58518588c004ec05316b16d25934
fetched_at: '2026-11-03T14:34:40.224523+00:00'
page_id: resource_SocialBreadcrumbRest
product: fluig
source: rest-fluig
title: Fluig REST — SocialBreadcrumbRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SocialBreadcrumbRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SocialBreadcrumbRest Resource

SocialBreadcrumb - v2

Available Since
:   1.5.4

### GET /2.0/communities/breadcrumb/get/{alias}/{documentId}

Retrieve bredcrumb items for a social document/article/image  
  
Return a VO with a list of breadcrumb items, within url an description for each item

Available Since
:   1.5.4

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | the community's alias where the item is published |  |
| documentId | path | The document's id to get a breadcrumb | long |
| folderType | query | A string indicating which social folder is the document. The parameter value should be "ARTICLE", "GALLERY\_VIDEO", "GALLERY\_PHOTO", "DOCUMENT" or "FORM". |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of breadcrumb items and a message with the result status   {  	"content": {  		"items": [{  			"url": "subject/community-public",  			"description": "Public Community "  		}, {  			"url": "articles/community-public/78",  			"description": "Article Root Folder"  		}, {  			"url": "articles/community-public/140",  			"description": "Sub Categoria 1"  		}, {  			"url": "articles/community-public/142",  			"description": "Sub Categoria 2"  		}, {  			"url": "articles/community-public/143",  			"description": "Sub Categoria 3"  		}, {  			"url": "144",  			"description": "Novo Artigo"  		}]  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |
