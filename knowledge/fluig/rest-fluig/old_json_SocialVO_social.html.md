---
content_hash: a2f082a05c2c810a323e20e25c64d4cec909798481edf9f0fd178ca9817c6f5c
fetched_at: '2026-11-03T14:34:38.562204+00:00'
page_id: json_SocialVO_social
product: fluig
source: rest-fluig
title: Fluig REST — SocialVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialVO_social.html
version: 1
---

# SocialVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| customPage | boolean |  |
| numberModerations | number |  |
| favorite | boolean |  |
| description | string |  |
| fullName | string |  |
| alias | string |  |
| lastName | string |  |
| privateContent | boolean |  |
| email | string |  |
| tenantId | number |  |
| numberParticipations | number |  |
| numberFollowing | number |  |
| createDate | number |  |
| tenantAdmin | boolean |  |
| isCommunityAdmin | boolean |  |
| isModerator | boolean |  |
| lastUpdate | number |  |
| numberFollowers | number |  |
| userData | map of string |  |
| numberFriends | number |  |
| id | number |  |
| hidden | boolean |  |
| approvalRequired | boolean |  |
| isAdmin | boolean |  |
| name | string |  |

Example

```
{
  "customPage" : true,
  "numberModerations" : 12345,
  "favorite" : true,
  "description" : "...",
  "fullName" : "...",
  "alias" : "...",
  "lastName" : "...",
  "privateContent" : true,
  "email" : "...",
  "tenantId" : 12345,
  "numberParticipations" : 12345,
  "numberFollowing" : 12345,
  "createDate" : 12345,
  "tenantAdmin" : true,
  "isCommunityAdmin" : true,
  "isModerator" : true,
  "lastUpdate" : 12345,
  "numberFollowers" : 12345,
  "userData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "numberFriends" : 12345,
  "id" : 12345,
  "hidden" : true,
  "approvalRequired" : true,
  "isAdmin" : true,
  "name" : "..."
}
```
