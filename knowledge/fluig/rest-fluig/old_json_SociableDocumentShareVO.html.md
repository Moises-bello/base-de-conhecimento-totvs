---
content_hash: a11b0fe85481b3deb62b9f1cbd856b241f371e30eefaa279994e4edd72bf258a
fetched_at: '2026-11-03T14:34:38.434740+00:00'
page_id: json_SociableDocumentShareVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentShareVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentShareVO.html
version: 1
---

# SociableDocumentShareVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| placeName | string |  |
| text | string |  |
| postId | number |  |
| version | number |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |
| documentId | number |  |
| placeAlias | string |  |

Example

```
{
  "placeName" : "...",
  "text" : "...",
  "postId" : 12345,
  "version" : 12345,
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
    "state" : "REMOVED",
    "participantStatus" : "PENDING",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "PENDING",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "documentId" : 12345,
  "placeAlias" : "..."
}
```
