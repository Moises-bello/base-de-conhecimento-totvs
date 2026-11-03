---
content_hash: 3933729e7b893cd16cc8157e0a9f7500909e6f443bf7d6f78341e328c5dd3fa0
fetched_at: '2026-11-03T14:34:38.414046+00:00'
page_id: json_SociableDocumentCommentVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentCommentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentCommentVO.html
version: 1
---

# SociableDocumentCommentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| mentions | map of string |  |
| comment | string |  |
| sociableObjectId | string |  |
| id | number |  |
| documentId | number |  |
| formattedTextWithoutMention | string |  |
| hasMentions | boolean |  |
| creationDate | number |  |
| sociableObjectClass | string |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |
| formattedDate | string |  |
| version | number |  |

Example

```
{
  "mentions" : {
    "property1" : "...",
    "property2" : "..."
  },
  "comment" : "...",
  "sociableObjectId" : "...",
  "id" : 12345,
  "documentId" : 12345,
  "formattedTextWithoutMention" : "...",
  "hasMentions" : true,
  "creationDate" : 12345,
  "sociableObjectClass" : "...",
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
    "followerStatus" : "BLOCKED",
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
    "participantStatus" : "PENDING",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "REJECTED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "formattedDate" : "...",
  "version" : 12345
}
```
