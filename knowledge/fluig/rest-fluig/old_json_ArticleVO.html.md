---
content_hash: 3ae5ebc96aba48013bb568e75e5cb73d3b4e64b3c36c456e01a3a07de796d797
fetched_at: '2026-11-03T14:34:36.255454+00:00'
page_id: json_ArticleVO
product: fluig
source: rest-fluig
title: Fluig REST — ArticleVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleVO.html
version: 1
---

# ArticleVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| content | string |  |  |
| type | [SocialDocumentType](https://api.fluig.com/old/json_SocialDocumentType.html) |  |  |
| id | number |  |  |
| description | string |  |  |
| expirationDate | number |  |  |
| expired | boolean | required |  |
| publicationDate | number |  |  |
| versionDescription | string |  |  |
| userNotify | boolean | required |  |
| articleCoverVO | [ArticleCoverVO](https://api.fluig.com/old/json_ArticleCoverVO_vo.html) |  |  |
| name | string |  |  |
| topicId | number |  |  |
| numberWatchs | number | required |  |
| categoryId | number |  |  |
| url | string |  |  |
| publisherId | string |  |  |
| approved | boolean | required |  |
| expires | boolean | required |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |  |
| viewedDocument | boolean | required |  |
| securityLevel | [SECURITY\_LEVEL](https://api.fluig.com/old/json_SECURITY_LEVEL.html) |  |  |
| numberMedias | number |  |  |
| sociable | [SociableVO](https://api.fluig.com/old/json_SociableVO.html) |  |  |
| file | string |  |  |
| creationDate | number |  |  |
| draft | boolean | required |  |
| socialObjectId | number |  |  |
| topicDescription | string |  |  |
| customData | map of string |  |  |
| keyWord | string |  |  |
| canEdit | boolean | required |  |
| totalDocs | number |  |  |
| accessCount | number |  |  |
| covers | array of [AttachmentVO](https://api.fluig.com/old/json_AttachmentVO.html) |  |  |
| additionalComments | string |  |  |
| attachments | array of string |  |  |
| version | number |  |  |
| favorited | boolean | required |  |
| alias | string |  |  |

Example

```
{
  "content" : "...",
  "type" : "ARTICLE",
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
    "type" : "COMMUNITY",
    "numberFollowing" : 12345,
    "numberParticipations" : 12345,
    "numberFollowers" : 12345,
    "favorite" : true,
    "userData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "isCommunityAdmin" : true,
    "followerStatus" : "REJECTED",
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
    "participantStatus" : "ACCEPTED",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "ACCEPTED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "viewedDocument" : true,
  "securityLevel" : "SECURITY_DENIED",
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
    "attachmentSource" : "UPLOAD_FOLDER",
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
