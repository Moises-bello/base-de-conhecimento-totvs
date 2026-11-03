---
content_hash: d648c519a233f7ec2565445bfb57fc6c096f50779836ec94bf119f8fdba2d92b
fetched_at: '2026-11-03T14:34:38.417049+00:00'
page_id: json_SociableDocumentDenouncementVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentDenouncementVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentDenouncementVO.html
version: 1
---

# SociableDocumentDenouncementVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| type | [SociableDenouncementType](https://api.fluig.com/old/json_SociableDenouncementType.html) |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |
| documentId | number |  |
| version | number |  |

Example

```
{
  "type" : "BLACKLIST",
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
    "followerStatus" : "PENDING",
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
    "participantStatus" : "ACCEPTED",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "NOT_RELATED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "documentId" : 12345,
  "version" : 12345
}
```
