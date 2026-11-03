---
content_hash: 5c4eb458ca28d4013f9b0aa80a1032a699f212b8c3e081caa5e0047beb09f044
fetched_at: '2026-11-03T14:34:36.237729+00:00'
page_id: json_ArticleLiveURLVO
product: fluig
source: rest-fluig
title: Fluig REST — ArticleLiveURLVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleLiveURLVO.html
version: 1
---

# ArticleLiveURLVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| liveURL | string |  |
| Properties inherited from [ArticleVO](https://api.fluig.com/old/json_ArticleVO.html) | | |
| content | string |  |
| type | [SocialDocumentType](https://api.fluig.com/old/json_SocialDocumentType.html) |  |
| id | number |  |
| description | string |  |
| expirationDate | number |  |
| expired | boolean |  |
| publicationDate | number |  |
| versionDescription | string |  |
| userNotify | boolean |  |
| articleCoverVO | [ArticleCoverVO](https://api.fluig.com/old/json_ArticleCoverVO_vo.html) |  |
| name | string |  |
| topicId | number |  |
| numberWatchs | number |  |
| categoryId | number |  |
| url | string |  |
| publisherId | string |  |
| approved | boolean |  |
| expires | boolean |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |
| viewedDocument | boolean |  |
| securityLevel | [SECURITY\_LEVEL](https://api.fluig.com/old/json_SECURITY_LEVEL.html) |  |
| numberMedias | number |  |
| sociable | [SociableVO](https://api.fluig.com/old/json_SociableVO.html) |  |
| file | string |  |
| creationDate | number |  |
| draft | boolean |  |
| socialObjectId | number |  |
| topicDescription | string |  |
| customData | map of string |  |
| keyWord | string |  |
| canEdit | boolean |  |
| totalDocs | number |  |
| accessCount | number |  |
| covers | array of [AttachmentVO](https://api.fluig.com/old/json_AttachmentVO.html) |  |
| additionalComments | string |  |
| attachments | array of string |  |
| version | number |  |
| favorited | boolean |  |
| alias | string |  |

Example

```
{
  "liveURL" : "...",
  "content" : "...",
  "type" : "CATEGORY",
  "id" : 12345,
  "description" : "...",
  "expirationDate" : 12345,
  "expired" : true,
  "publicationDate" : 12345,
  "versionDescription" : "...",
  "userNotify" : true,
  "articleCoverVO" : {
    "height" : 12345,
    "windowWidth" : 12345,
    "coordinateY" : 12345,
    "base64media" : "...",
    "pictureName" : "...",
    "image" : "...",
    "windowHeight" : 12345,
    "coordinateX" : 12345,
    "pictureId" : "...",
    "width" : 12345,
    "path" : "..."
  },
  "name" : "...",
  "topicId" : 12345,
  "numberWatchs" : 12345,
  "categoryId" : 12345,
  "url" : "...",
  "publisherId" : "...",
  "approved" : true,
  "expires" : true,
  "user" : {
    "numberFriends" : 12345,
    "approvalRequired" : true,
    "stateName" : "...",
    "forumId" : 12345,
    "ecmInfo" : {
      "property1" : { },
      "property2" : { }
    },
    "lastUpdate" : 12345,
    "isAdmin" : true,
    "idpId" : "...",
    "type" : "EVENT",
    "numberFollowing" : 12345,
    "numberParticipations" : 12345,
    "numberFollowers" : 12345,
    "favorite" : true,
    "userData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "isCommunityAdmin" : true,
    "followerStatus" : "ITSELF",
    "numberModerations" : 12345,
    "tenantId" : 12345,
    "isModerator" : true,
    "alias" : "...",
    "customPage" : true,
    "page" : "...",
    "foundationUserId" : 12345,
    "lastName" : "...",
    "createDate" : 12345,
    "id" : 12345,
    "uriCommunity" : "...",
    "permissions" : [ "...", "..." ],
    "name" : "...",
    "tenantAdmin" : true,
    "privateContent" : true,
    "state" : "ACTIVE",
    "participantStatus" : "NOT_RELATED",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "BLOCKED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "viewedDocument" : true,
  "securityLevel" : "SECURITY_SAVE",
  "numberMedias" : 12345,
  "sociable" : {
    "numberDenouncements" : 12345,
    "numberLikes" : 12345,
    "id" : 12345,
    "numberShares" : 12345,
    "numberComments" : 12345,
    "url" : "...",
    "objectId" : "...",
    "name" : "...",
    "objectClass" : "...",
    "userId" : 12345,
    "tags" : "...",
    "alias" : "...",
    "thumbURL" : "...",
    "sociableType" : "..."
  },
  "file" : "...",
  "creationDate" : 12345,
  "draft" : true,
  "socialObjectId" : 12345,
  "topicDescription" : "...",
  "customData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "keyWord" : "...",
  "canEdit" : true,
  "totalDocs" : 12345,
  "accessCount" : 12345,
  "covers" : [ {
    "filename" : "...",
    "principal" : true,
    "attachmentSource" : "DOCUMENT_FOLDER",
    "iconPath" : "...",
    "editing" : true,
    "descriptor" : true,
    "filecontent" : "...",
    "fileModificationDate" : 12345,
    "renameFrom" : "...",
    "mobile" : true,
    "supportedNewViewer" : true,
    "fileName" : "...",
    "fileSize" : 12345,
    "fileSelected" : {
      "filecontent" : "...",
      "pathName" : "...",
      "fileModificationDate" : 12345,
      "fileSelected" : { },
      "attach" : true,
      "displayFileName" : "...",
      "editing" : true,
      "iconPath" : "...",
      "principal" : true,
      "fullPatch" : "...",
      "mobile" : true,
      "supportedNewViewer" : true,
      "descriptor" : true,
      "fileSize" : 12345,
      "fileName" : "..."
    },
    "realFileName" : "..."
  }, {
    "filename" : "...",
    "principal" : true,
    "attachmentSource" : "FILE_CONTENT_ATTR",
    "iconPath" : "...",
    "editing" : true,
    "descriptor" : true,
    "filecontent" : "...",
    "fileModificationDate" : 12345,
    "renameFrom" : "...",
    "mobile" : true,
    "supportedNewViewer" : true,
    "fileName" : "...",
    "fileSize" : 12345,
    "fileSelected" : {
      "filecontent" : "...",
      "pathName" : "...",
      "fileModificationDate" : 12345,
      "fileSelected" : { },
      "attach" : true,
      "displayFileName" : "...",
      "editing" : true,
      "iconPath" : "...",
      "principal" : true,
      "fullPatch" : "...",
      "mobile" : true,
      "supportedNewViewer" : true,
      "descriptor" : true,
      "fileSize" : 12345,
      "fileName" : "..."
    },
    "realFileName" : "..."
  } ],
  "additionalComments" : "...",
  "attachments" : [ "...", "..." ],
  "version" : 12345,
  "favorited" : true,
  "alias" : "..."
}
```
