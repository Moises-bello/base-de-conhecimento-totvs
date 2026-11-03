---
content_hash: 440635246e4f1e82911d64906850a6f10d6773fae052103e55d72368afd7ae6d
fetched_at: '2026-11-03T14:34:38.427786+00:00'
page_id: json_SociableDocumentLikeVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentLikeVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentLikeVO.html
version: 1
---

# SociableDocumentLikeVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| version | number |  |
| documentId | number |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |

Example

```
{
  "version" : 12345,
  "documentId" : 12345,
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
    "followerStatus" : "NOT_RELATED",
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
    "state" : "UNCONFIRMED",
    "participantStatus" : "NOT_RELATED",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "ACCEPTED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  }
}
```
