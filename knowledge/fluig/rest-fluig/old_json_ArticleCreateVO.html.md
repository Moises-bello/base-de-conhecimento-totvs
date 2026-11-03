---
content_hash: 9a62ae7ad1a6badbc3c72388d9d36864f30dab28a491959f32f44b714e36d40c
fetched_at: '2026-11-03T14:34:36.228431+00:00'
page_id: json_ArticleCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — ArticleCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleCreateVO.html
version: 1
---

# ArticleCreateVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| name | string |  |  |
| categoryId | number |  |  |
| keyWord | string |  |  |
| expires | boolean | required |  |
| description | string |  |  |
| version | number |  |  |
| publicationDate | number |  |  |
| expirationDate | number |  |  |
| publisherId | string |  |  |
| additionalComments | string |  |  |
| alias | string |  |  |
| content | string |  |  |
| id | number |  |  |
| draft | boolean | required |  |
| attachments | array of string |  |  |
| topicId | number |  |  |
| articleCoverVO | [ArticleCoverVO](https://api.fluig.com/old/json_ArticleCoverVO_article.html) |  |  |
| userNotify | boolean | required |  |

Example

```
{
  "name" : "...",
  "categoryId" : 12345,
  "keyWord" : "...",
  "expires" : true,
  "description" : "...",
  "version" : 12345,
  "publicationDate" : 12345,
  "expirationDate" : 12345,
  "publisherId" : "...",
  "additionalComments" : "...",
  "alias" : "...",
  "content" : "...",
  "id" : 12345,
  "draft" : true,
  "attachments" : [ "...", "..." ],
  "topicId" : 12345,
  "articleCoverVO" : {
    "path" : "...",
    "pictureName" : "...",
    "image" : "...",
    "coordinateX" : 12345,
    "coordinateY" : 12345,
    "width" : 12345,
    "height" : 12345,
    "base64media" : "...",
    "canvasData" : {
      "left" : 12345,
      "top" : 12345,
      "width" : 12345,
      "height" : 12345
    },
    "boxData" : {
      "left" : 12345,
      "top" : 12345,
      "width" : 12345,
      "height" : 12345
    },
    "pictureId" : "...",
    "windowWidth" : 12345,
    "windowHeight" : 12345
  },
  "userNotify" : true
}
```
