---
content_hash: 71d8d3cc33f2fd3ae529ab160b5c4bc05ffa86d7731d71ce9fb0a277628efe4b
fetched_at: '2026-11-03T14:34:36.263671+00:00'
page_id: json_ArticleVO_social
product: fluig
source: rest-fluig
title: Fluig REST — ArticleVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleVO_social.html
version: 1
---

# ArticleVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| viewedDocument | boolean | required |  |
| articleCoverVO | [ArticleCoverVO](https://api.fluig.com/old/json_ArticleCoverVO.html) |  |  |
| userNotify | boolean | required |  |
| socialObjectId | number |  |  |
| securityLevel | string |  |  |
| topicId | number |  |  |
| content | string |  |  |
| draft | boolean | required |  |
| publicationDate | number |  |  |
| keyWord | string |  |  |
| covers | map of string |  |  |
| sociable | [SociableVO](https://api.fluig.com/old/json_SociableVO_social.html) |  |  |
| approved | boolean | required |  |
| alias | string |  |  |
| version | number |  |  |
| description | string |  |  |
| categoryId | number |  |  |
| expirationDate | number |  |  |
| expires | boolean | required |  |
| numberWatchs | number | required |  |
| attachments | array of string |  |  |
| accessCount | number |  |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO_social.html) |  |  |
| id | number |  |  |
| publisherId | string |  |  |

Example

```
{
  "viewedDocument" : true,
  "articleCoverVO" : {
    "coordinateX" : 12345,
    "path" : "...",
    "image" : "...",
    "windowHeight" : 12345,
    "height" : 12345,
    "pictureId" : "...",
    "base64media" : "...",
    "windowWidth" : 12345,
    "coordinateY" : 12345,
    "width" : 12345,
    "pictureName" : "...",
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
    }
  },
  "userNotify" : true,
  "socialObjectId" : 12345,
  "securityLevel" : "...",
  "topicId" : 12345,
  "content" : "...",
  "draft" : true,
  "publicationDate" : 12345,
  "keyWord" : "...",
  "covers" : {
    "property1" : "...",
    "property2" : "..."
  },
  "sociable" : {
    "alias" : "...",
    "objectClass" : "...",
    "numberLikes" : 12345,
    "name" : "...",
    "numberDenouncements" : 12345,
    "sociableType" : "...",
    "numberComments" : 12345,
    "url" : "...",
    "userId" : 12345,
    "objectId" : "...",
    "tags" : "...",
    "id" : 12345,
    "thumbURL" : "...",
    "numberShares" : 12345
  },
  "approved" : true,
  "alias" : "...",
  "version" : 12345,
  "description" : "...",
  "categoryId" : 12345,
  "expirationDate" : 12345,
  "expires" : true,
  "numberWatchs" : 12345,
  "attachments" : [ "...", "..." ],
  "accessCount" : 12345,
  "user" : {
    "customPage" : true,
    "numberModerations" : 12345,
    "favorite" : true,
    "description" : "...",
    "fullName" : "...",
    "alias" : "...",
    "lastName" : "...",
    "privateContent" : true,
    "email" : "...",
    "tenantId" : 12345,
    "numberParticipations" : 12345,
    "numberFollowing" : 12345,
    "createDate" : 12345,
    "tenantAdmin" : true,
    "isCommunityAdmin" : true,
    "isModerator" : true,
    "lastUpdate" : 12345,
    "numberFollowers" : 12345,
    "userData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "numberFriends" : 12345,
    "id" : 12345,
    "hidden" : true,
    "approvalRequired" : true,
    "isAdmin" : true,
    "name" : "..."
  },
  "id" : 12345,
  "publisherId" : "..."
}
```
