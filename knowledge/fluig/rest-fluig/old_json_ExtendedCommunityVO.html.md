---
content_hash: c4fab10c49d7a5b4b6c6786516ac938a30694cdfd0d7932306704d35cf81f562
fetched_at: '2026-11-03T14:34:36.793189+00:00'
page_id: json_ExtendedCommunityVO
product: fluig
source: rest-fluig
title: Fluig REST — ExtendedCommunityVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ExtendedCommunityVO.html
version: 1
---

# ExtendedCommunityVO Data Type

Extended Visual Object for community. Contains social DOCUMENT, GALLERY\_PHOTO, GALLERY\_VIDEO, ARTICLE, FORM.

Properties

| name | data type | description |
| --- | --- | --- |
| document | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) | the document |
| galleryPhoto | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) | the galleryPhoto |
| galleryVideo | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) | the galleryVideo |
| article | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) | the article |
| form | [SocialDocsVO](https://api.fluig.com/old/json_SocialDocsVO.html) | the form |
| Properties inherited from [SocialVO](https://api.fluig.com/old/json_SocialVO.html) | | |
| numberFriends | number |  |
| approvalRequired | boolean |  |
| stateName | string |  |
| forumId | number |  |
| ecmInfo | map of object |  |
| lastUpdate | number |  |
| isAdmin | boolean |  |
| idpId | string |  |
| type | [SocialType](https://api.fluig.com/old/json_SocialType.html) |  |
| numberFollowing | number |  |
| numberParticipations | number |  |
| numberFollowers | number |  |
| favorite | boolean |  |
| userData | map of string |  |
| isCommunityAdmin | boolean |  |
| followerStatus | [SocialRelationStatus](https://api.fluig.com/old/json_SocialRelationStatus.html) |  |
| numberModerations | number |  |
| tenantId | number |  |
| isModerator | boolean |  |
| alias | string |  |
| customPage | boolean |  |
| page | string |  |
| foundationUserId | number |  |
| lastName | string |  |
| createDate | number |  |
| id | number |  |
| uriCommunity | string |  |
| permissions | array of string |  |
| name | string |  |
| tenantAdmin | boolean |  |
| privateContent | boolean |  |
| state | [UserState](https://api.fluig.com/old/json_UserState.html) |  |
| participantStatus | [SocialRelationStatus](https://api.fluig.com/old/json_SocialRelationStatus.html) |  |
| admin | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |
| description | string |  |
| followingStatus | [SocialRelationStatus](https://api.fluig.com/old/json_SocialRelationStatus.html) |  |
| email | string |  |
| fullName | string |  |
| userCode | string |  |
| tenantUUID | string |  |
| hasMobileWidget | boolean |  |
| hidden | boolean |  |

Example

```
{
  "document" : {
    "spaceAlias" : "...",
    "socialFolderWritePermission" : true,
    "tenantId" : 12345,
    "socialFolderEnabled" : true,
    "socialFolderSecurity" : true,
    "socialFolderDescription" : "...",
    "socialFolderId" : 12345,
    "userId" : "..."
  },
  "galleryPhoto" : {
    "spaceAlias" : "...",
    "socialFolderWritePermission" : true,
    "tenantId" : 12345,
    "socialFolderEnabled" : true,
    "socialFolderSecurity" : true,
    "socialFolderDescription" : "...",
    "socialFolderId" : 12345,
    "userId" : "..."
  },
  "galleryVideo" : {
    "spaceAlias" : "...",
    "socialFolderWritePermission" : true,
    "tenantId" : 12345,
    "socialFolderEnabled" : true,
    "socialFolderSecurity" : true,
    "socialFolderDescription" : "...",
    "socialFolderId" : 12345,
    "userId" : "..."
  },
  "article" : {
    "spaceAlias" : "...",
    "socialFolderWritePermission" : true,
    "tenantId" : 12345,
    "socialFolderEnabled" : true,
    "socialFolderSecurity" : true,
    "socialFolderDescription" : "...",
    "socialFolderId" : 12345,
    "userId" : "..."
  },
  "form" : {
    "spaceAlias" : "...",
    "socialFolderWritePermission" : true,
    "tenantId" : 12345,
    "socialFolderEnabled" : true,
    "socialFolderSecurity" : true,
    "socialFolderDescription" : "...",
    "socialFolderId" : 12345,
    "userId" : "..."
  },
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
  "type" : "USER",
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
  "state" : "BLOCKED",
  "participantStatus" : "ACCEPTED",
  "admin" : {
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
    "state" : "BLOCKED",
    "participantStatus" : "ITSELF",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "ITSELF",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "description" : "...",
  "followingStatus" : "ITSELF",
  "email" : "...",
  "fullName" : "...",
  "userCode" : "...",
  "tenantUUID" : "...",
  "hasMobileWidget" : true,
  "hidden" : true
}
```
