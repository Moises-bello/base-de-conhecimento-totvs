---
content_hash: e243771c3d4f06b984916e3888c217c1062bedef16a8b9cafa25629704e4d1bb
fetched_at: '2026-11-03T14:34:36.488307+00:00'
page_id: json_CommunityVO
product: fluig
source: rest-fluig
title: Fluig REST — CommunityVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CommunityVO.html
version: 1
---

# CommunityVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| name | string |  |
| description | string |  |
| alias | string |  |
| type | [SocialType](https://api.fluig.com/old/json_SocialType.html) |  |
| numberFriends | number |  |
| numberParticipations | number |  |
| numberFollowing | number |  |
| numberFollowers | number |  |
| numberModerations | number | the numberModerations |
| hidden | boolean | the hidden |
| privateContent | boolean | the privateContent |
| approvalRequired | boolean | the approvalRequired |
| tenantId | number |  |
| lastUpdate | number |  |
| state | [UserState](https://api.fluig.com/old/json_UserState.html) |  |
| createDate | number | the createDate |
| admin | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) | the admin |
| customPage | boolean |  |
| socialEcmVO | [SocialEcmVO](https://api.fluig.com/old/json_SocialEcmVO.html) |  |
| ecmInfo | map of object |  |
| page | string |  |
| cloudCodes | array of string |  |
| addInCloud | boolean |  |

Example

```
{
  "id" : 12345,
  "name" : "...",
  "description" : "...",
  "alias" : "...",
  "type" : "COMMUNITY",
  "numberFriends" : 12345,
  "numberParticipations" : 12345,
  "numberFollowing" : 12345,
  "numberFollowers" : 12345,
  "numberModerations" : 12345,
  "hidden" : true,
  "privateContent" : true,
  "approvalRequired" : true,
  "tenantId" : 12345,
  "lastUpdate" : 12345,
  "state" : "BLOCKED",
  "createDate" : 12345,
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
    "state" : "BLOCKED",
    "participantStatus" : "REJECTED",
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
  "customPage" : true,
  "socialEcmVO" : {
    "ecmPhotoFolderId" : "...",
    "ecmDocumentFolderId" : "...",
    "ecmArticleFolderId" : "...",
    "ecmFormsFolderId" : "...",
    "ecmVideoFolderId" : "..."
  },
  "ecmInfo" : {
    "property1" : { },
    "property2" : { }
  },
  "page" : "...",
  "cloudCodes" : [ "...", "..." ],
  "addInCloud" : true
}
```
