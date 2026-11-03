---
content_hash: bba902c3874b0ee63a1024a746ed85b65f78f2b421b0b423614d6842c4c74e66
fetched_at: '2026-11-03T14:34:40.037732+00:00'
page_id: resource_PostRest
product: fluig
source: rest-fluig
title: Fluig REST — PostRest Resource
type: documentation
url: https://api.fluig.com/old/resource_PostRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# PostRest Resource

Post

Available Since
:   1.5

### POST /2.0/posts/create

Create a new Post  
  
Create a new Post: fill object PostCreateVO

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PostCreateVO](https://api.fluig.com/old/json_PostCreateVO.html) (JSON) | Request JSON (example):`{ "text": "Content description post", "visibility": "visibility", "sociableObjectId": "1", "alias": "alias.community1435946503679", "customUsers": [ 1 ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "id": null, "text": "Content description post", "visibility": "visibility", "alias": "alias.community1435946503679", "customUsers": [ 1 ], "sociableObjectId": 1 }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.12

### POST /2.0/posts/editComment

Edit the text of comment by id

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PostCreateVO](https://api.fluig.com/old/json_PostCreateVO.html) (JSON) | Request JSON (example):`{ "sociableObjectId" : "1", //comment id "text" : "This is my new comment text" // new text of comment }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### POST /2.0/posts/editPost

Edit the text of post by id

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PostCreateVO](https://api.fluig.com/old/json_PostCreateVO.html) (JSON) | Request JSON (example):`{ "sociableObjectId" : "1", // post id "text" : "This is my new post text" // new text of post }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### GET /2.0/posts/findComment/{commentId}

Find a comment by id

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| commentId | path | REQUIRED ID of comment | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):"content": { "sociableId": 2525, "sociableParentId": 2525, "comment": "Content of comment", "creationDate": "1475610784284", "updateDate": "1475610794609", // if null, comment wasn't edited "commentWithoutMention": "Content of comment", "mention": false, "mentions": "{}", "customData": "{}", "userName": "Sergey Page", "userAlias": "sergey", }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } } |

Available Since
:   1.5.9

### POST /2.0/posts/create/with/upload

Create a new Post  
  
Create a new Post: fill object PostCreateVO

Available Since
:   1.5.9

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [PostCreateVO](https://api.fluig.com/old/json_PostCreateVO.html) (JSON) | Request JSON (example):`{ "text": "Content description post", "visibility": "visibility", "sociableObjectId": "1", "alias": "alias.community1435946503679", "mediaVO" : { //NOT REQUIRED "mediaName" : "file.jpg", //REQUIRED Media name "mediaType" : "PHOTO", //OPTIONAL Media type - PHOTO, VIDEO or DOCUMENT if you don't send, the Media Type is based in media name extension "mediaId" : "512", //OPTIONAL You can send one upload id or one document id "mediaVersion" : "2000", //OPTIONAL version for ECM documents, default is the first version } "customUsers": [ 1 ] }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "id": null, "text": "Content description post", "visibility": "visibility", "alias": "alias.community1435946503679", "customUsers": [ 1 ], "sociableObjectId": 1 }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |
