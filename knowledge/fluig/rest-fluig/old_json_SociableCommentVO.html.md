---
content_hash: 419d8d4918aac2816c94d1cfb85d78f47f8c3912256d563ac238f0e0f64ba57b
fetched_at: '2026-11-03T14:34:38.407237+00:00'
page_id: json_SociableCommentVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableCommentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableCommentVO.html
version: 1
---

# SociableCommentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| sociableId | number |  |  |
| social | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |  |
| formattedTextWithoutMention | string |  |  |
| mentions | map of string |  |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |  |
| comment | string |  |  |
| hasMentions | boolean |  |  |
| id | number |  |  |
| link | string |  |  |
| creationDate | number |  |  |
| updateDate | number |  |  |
| editionDate | number |  |  |
| supported | boolean | required |  |
| customData | map of string |  |  |
| Properties inherited from [SociableVO](https://api.fluig.com/old/json_SociableVO.html) | | | |
| numberDenouncements | number |  |  |
| numberLikes | number |  |  |
| id | number |  |  |
| numberShares | number |  |  |
| numberComments | number |  |  |
| url | string |  |  |
| objectId | string |  |  |
| name | string |  |  |
| objectClass | string |  |  |
| userId | number |  |  |
| tags | string |  |  |
| alias | string |  |  |
| thumbURL | string |  |  |
| sociableType | string |  |  |

Example

```
{
  "sociableId" : 12345,
  "social" : {
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
    "state" : "REMOVED",
    "participantStatus" : "NOT_RELATED",
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
  "formattedTextWithoutMention" : "...",
  "mentions" : {
    "property1" : "...",
    "property2" : "..."
  },
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
    "type" : "APPLICATION",
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
  },
  "comment" : "...",
  "hasMentions" : true,
  "id" : 12345,
  "link" : "...",
  "creationDate" : 12345,
  "updateDate" : 12345,
  "editionDate" : 12345,
  "supported" : true,
  "customData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "numberDenouncements" : 12345,
  "numberLikes" : 12345,
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
}
```
