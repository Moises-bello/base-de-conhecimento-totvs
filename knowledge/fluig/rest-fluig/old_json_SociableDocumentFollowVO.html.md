---
content_hash: 7ec294d5d2e0570048f1394dc0d71fc5cd02778b5c11e2c0e9bbfe1d40fe002d
fetched_at: '2026-11-03T14:34:38.425006+00:00'
page_id: json_SociableDocumentFollowVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentFollowVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentFollowVO.html
version: 1
---

# SociableDocumentFollowVO Data Type

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
    "followerStatus" : "ACCEPTED",
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
    "participantStatus" : "BLOCKED",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "NOT_RELATED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  }
}
```
