---
content_hash: c6623e5865c3ab630d1787c9630cb4d5cca86fc8242438bfe00de3c92f569a1e
fetched_at: '2026-11-03T14:34:38.555695+00:00'
page_id: json_SocialVO
product: fluig
source: rest-fluig
title: Fluig REST — SocialVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialVO.html
version: 1
---

# SocialVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
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
  "state" : "REMOVED",
  "participantStatus" : "ITSELF",
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
    "participantStatus" : "REJECTED",
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
  "description" : "...",
  "followingStatus" : "REJECTED",
  "email" : "...",
  "fullName" : "...",
  "userCode" : "...",
  "tenantUUID" : "...",
  "hasMobileWidget" : true,
  "hidden" : true
}
```
