---
content_hash: 96aaddc57ea9e6276b3042ebfbfc0ba7305d52fa1054153dc3acc6aba7b2f48d
fetched_at: '2026-11-03T14:34:39.365503+00:00'
page_id: resource_ArticleRest
product: fluig
source: rest-fluig
title: Fluig REST — ArticleRest Resource
type: documentation
url: https://api.fluig.com/old/resource_ArticleRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# ArticleRest Resource

Articles - V2

Available Since
:   1.5.4

### POST /2.0/communities/articles/changeCover

Update the cover image of an existing article.  
  
Return the article that was updated in a community.

Available Since
:   1.5.4

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCreateVO](https://api.fluig.com/old/json_ArticleCreateVO.html) (JSON) | Request JSON (example):  ```  {  	"id"                : "15"                  // Id do artigo que será atualizado (REQUIRED)  	"alias"             : "recursos-humanos"    // Alias da comunidade onde o artigo foi publicado (REQUIRED)  	"description"       : "Titulo"              // Titulo do Artigo (REQUIRED)  	"version"           : "1000"                // Versão do artigo que será atualizado (REQUIRED)  	"keyWord"           : "tags artigo novo",   // Tags de indexação de pesquisa (separadas por espaço)  	"content"           : "conteudo do artigo", // Conteudo do Artigo (aceita tags html) (REQUIRED)  	"categoryId"        : "6",                  // Id da categoria do artigo (pasta onde o artigo será salvo) (REQUIRED)  	"expirationDate"    : "2015-10-30",         // Data de expiração do artigo  	"draft"             : false,                // Indica se o artigo será criado em modo rascunho  	"topicId"           : "1",                  // Assunto do ECM o qual o artigo será relacionado  	"userNotify"        : false,                // Indica se irá notificar  	"articleCoverVO": {                         // Objeto utilizado para criar imagem de capa do artigo (REQUIRED)  		"width": 508,                           // Largura da imagem de capa  		"height": 101,                          // Altura da imagem de capa  		"coordinateX": 53,                      // Cordenada X do posicionamento da imagem de capa  		"coordinateY": 77,                      // Cordenada Y do posicionamento da imagem de capa  		"pictureName": "coala.jpg",             // Nome do arquivo que foi enviado para a area de upload do ECM  		"pictureId": "59"                       // ID da imagem no ECM, para os casos de uso de imagem do repositorio do ECM  	"}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (vers��o original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### POST /2.0/communities/articles/create

Create an article.  
  
Return the article that was created and published in a community.

Available Since
:   1.5.4

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCreateVO](https://api.fluig.com/old/json_ArticleCreateVO.html) (JSON) | Request JSON (example):  ```  {  	"alias"             : "recursos-humanos"    // Alias da comunidade onde o artigo será publicado (REQUIRED)  	"description"       : "Titulo"              // Titulo do Artigo (REQUIRED)  	"keyWord"           : "tags artigo novo",   // Tags de indexação de pesquisa (separadas por espaço)  	"content"           : "conteudo do artigo", // Conteudo do Artigo (aceita tags html) (REQUIRED)  	"categoryId"        : "6",                  // Id da categoria do artigo (pasta onde o artigo será salvo) (REQUIRED)  	"expirationDate"    : "2015-10-30",         // Data de expiração do artigo  	"draft"             : false,                // Indica se o artigo será criado em modo rascunho  	"topicId"           : "1",                  // Assunto do ECM o qual o artigo será relacionado  	"userNotify"        : false,                // Indica se irá notificar  	"articleCoverVO": {                         // Objeto utilizado para criar imagem de capa do artigo (REQUIRED)  		"width": 508,                           // Largura da imagem de capa  		"height": 101,                          // Altura da imagem de capa  		"coordinateX": 53,                      // Cordenada X do posicionamento da imagem de capa  		"coordinateY": 77,                      // Cordenada Y do posicionamento da imagem de capa  		"pictureName": "coala.jpg",             // Nome do arquivo que foi enviado para a area de upload do ECM  		"pictureId": "59"                       // ID da imagem no ECM, para os casos de uso de imagem do repositorio do ECM  	"}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### POST /2.0/communities/articles/createDraft

Create an article in draft mode.  
  
Return the article that was created in a draft mode.

Available Since
:   1.5.4

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCreateVO](https://api.fluig.com/old/json_ArticleCreateVO.html) (JSON) | Request JSON (example):  ```  {  	"alias"             : "recursos-humanos"    // Alias da comunidade onde o artigo será salvo (REQUIRED)  	"description"       : "Titulo"              // Titulo do Artigo (Opcional para Rascunho de Artigo)  	"content"           : "conteudo do artigo", // Conteudo do Artigo (aceita tags html) (REQUIRED)  	"categoryId"        : "6",                  // Id da categoria do artigo (pasta onde o artigo será salvo) (REQUIRED)  	"articleCoverVO": {                         // Objeto utilizado para criar imagem de capa do artigo (REQUIRED)  		"width": 508,                           // Largura da imagem de capa  		"height": 101,                          // Altura da imagem de capa  		"coordinateX": 53,                      // Cordenada X do posicionamento da imagem de capa  		"coordinateY": 77,                      // Cordenada Y do posicionamento da imagem de capa  		"pictureName": "coala.jpg",             // Nome do arquivo que foi enviado para a area de upload do ECM  		"pictureId": "59"                       // ID da imagem no ECM, para os casos de uso de imagem do repositorio do ECM  	"}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": true,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### POST /2.0/communities/articles/removeCover

Remove the cover image of an existing article.  
  
Return the article that was updated in a community.

Available Since
:   1.5.4

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCreateVO](https://api.fluig.com/old/json_ArticleCreateVO.html) (JSON) | Request JSON (example):  ```  {  	"id"                : "15"                  // Id do artigo que será atualizado (REQUIRED)  	"alias"             : "recursos-humanos"    // Alias da comunidade onde o artigo foi publicado (REQUIRED)  	"description"       : "Titulo"              // Titulo do Artigo (REQUIRED)  	"version"           : "1000"                // Versão do artigo que será atualizado (REQUIRED)  	"keyWord"           : "tags artigo novo",   // Tags de indexação de pesquisa (separadas por espaço)  	"content"           : "conteudo do artigo", // Conteudo do Artigo (aceita tags html) (REQUIRED)  	"categoryId"        : "6",                  // Id da categoria do artigo (pasta onde o artigo será salvo) (REQUIRED)  	"expirationDate"    : "2015-10-30",         // Data de expiração do artigo  	"draft"             : false,                // Indica se o artigo será criado em modo rascunho  	"topicId"           : "1",                  // Assunto do ECM o qual o artigo será relacionado  	"userNotify"        : false,                // Indica se irá notificar  	"articleCoverVO": {                         // Objeto utilizado para criar imagem de capa do artigo (REQUIRED)  		"width": 508,                           // Largura da imagem de capa  		"height": 101,                          // Altura da imagem de capa  		"coordinateX": 53,                      // Cordenada X do posicionamento da imagem de capa  		"coordinateY": 77,                      // Cordenada Y do posicionamento da imagem de capa  		"pictureName": "coala.jpg",             // Nome do arquivo que foi enviado para a area de upload do ECM  		"pictureId": "59"                       // ID da imagem no ECM, para os casos de uso de imagem do repositorio do ECM  	"}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### POST /2.0/communities/articles/update

Update an article.  
  
Return the article that was updated in a community.

Available Since
:   1.5.4

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ArticleCreateVO](https://api.fluig.com/old/json_ArticleCreateVO.html) (JSON) | Request JSON (example):  ```  {  	"id"                : "15"                  // Id do artigo que será atualizado (REQUIRED)  	"alias"             : "recursos-humanos"    // Alias da comunidade onde o artigo foi publicado (REQUIRED)  	"description"       : "Titulo"              // Titulo do Artigo (REQUIRED)  	"version"           : "1000"                // Versão do artigo que será atualizado (REQUIRED)  	"keyWord"           : "tags artigo novo",   // Tags de indexação de pesquisa (separadas por espaço)  	"content"           : "conteudo do artigo", // Conteudo do Artigo (aceita tags html) (REQUIRED)  	"categoryId"        : "6",                  // Id da categoria do artigo (pasta onde o artigo será salvo) (REQUIRED)  	"expirationDate"    : "2015-10-30",         // Data de expiração do artigo  	"draft"             : false,                // Indica se o artigo será criado em modo rascunho  	"topicId"           : "1",                  // Assunto do ECM o qual o artigo será relacionado  	"userNotify"        : false,                // Indica se irá notificar  	"articleCoverVO": {                         // Objeto utilizado para criar imagem de capa do artigo (REQUIRED)  		"width": 508,                           // Largura da imagem de capa  		"height": 101,                          // Altura da imagem de capa  		"coordinateX": 53,                      // Cordenada X do posicionamento da imagem de capa  		"coordinateY": 77,                      // Cordenada Y do posicionamento da imagem de capa  		"pictureName": "coala.jpg",             // Nome do arquivo que foi enviado para a area de upload do ECM  		"pictureId": "59"                       // ID da imagem no ECM, para os casos de uso de imagem do repositorio do ECM  	"}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### POST /2.0/communities/articles/delete/{articleId}

Remove an article  
  
Remove an article by his id

Available Since
:   1.5.4

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| articleId | path | the Id of a article that will be removed | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns HTTP 200 status and a message with the result status   {  	content: null  	message: {  	message: "Artigo removido com sucesso!"  	detail: "Artigo removido com sucesso!"  	type: "INFO"  	}-  } ``` |

Available Since
:   1.5.4

### POST /2.0/communities/articles/deleteDraft/{alias}/{articleId}

Remove a version in draft of article  
  
Remove a draft version of article by his id. If the article isn't in draft, a Error message wil be returned

Available Since
:   1.5.4

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alias | path | the community's alias where the article is published |  |
| articleId | path | the Id of a article that the draft version will be removed | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns HTTP 200 status and a message with the result status   {  	content: null  	message: {  	message: "Draft removido com sucesso!"  	detail: "Draft removido com sucesso!"  	type: "INFO"  	}-  } ``` |

Available Since
:   1.5.4

### GET /2.0/communities/articles/get/{alias}/{articleId}

Retrieve an article  
  
Return an article published in a community.

Available Since
:   1.5.4

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | the community's alias where the article is published |  |  |
| articleId | path | The article's id |  | long |
| draft | query | **(optional - default = false)**  `true` if retrieving a draft version of the article  `false` if retrieving a published version of the article | false | required |
| updateDocumentHits | query |  | true | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.4

### GET /2.0/communities/articles/list/{alias}/{categoryId}

Retrieve a list of articles  
  
Return a list of article published in a community.

Available Since
:   1.5.4

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| alias | path | the community's alias where the article is published |  |  |
| categoryId | path |  |  | long |
| filterBy | query | **(optional - default = "")** | ALL\_ARTICLES |  |
| limit | query | **(optional - default = 5)** | 5 | int |
| offset | query | **(optional - default = 0)** | 0 | int |
| orderBy | query | **(optional - default = 0)** | UPDATE\_DATE\_DESC |  |
| searchBy | query | **(optional - default = "UPDATE\_DATE\_DESC")** |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns List of article and a message with the result status   [{  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  		"viewedDocument": true  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  }  ] ``` |

Available Since
:   1.5.4

### GET /2.0/communities/articles/getNextOrPrev/{folderId}/{articleId}/{order}

Retrive the next or previous article of one specific article.  
  
Return the article that is the next or previous of the article passed by parameter.

Available Since
:   1.5.4

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| articleId | path | The article's Id that will be retrieved the next or previous. | long |
| folderId | path | The folder's id where the next or previous will be searched. | long |
| order | path | The order to get next or previous article. Use the string 'next' retrieve the next article. |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method returns VO of article and a message with the result status   {  	"content": {  		"id": 15,  		"categoryId": 6,  		"name": null,  		"alias": "tecnologia",  		"content": "Conteudo do artigo",  		"topicId": 1,  		"draft": false,  		"keyWord": "tags artigo novo",  		"expires": false,  		"description": "Titulo do Artigo",  		"version": 1000,  		"publicationDate": "2015-10-20 16:03:31",  		"expirationDate": "2015-10-20 16:03:31",  		"publisherId": "admin.fluig",  		"attachments": [],  		"covers": {  			"cover_image": "url da imagem de capa do artigo (versão cropada)",  			"cover_image_original": "url da imagem de capa do artigo (versão original)"  		},  		"user": {  			"id": 2,  			"name": "Admin Fluig",  			"alias": "admin.fluig",  			"tenantId": 123,  			"tenantAdmin": true,  		},  		"userNotify": false,  		"socialObjectId": 107  	},  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |
