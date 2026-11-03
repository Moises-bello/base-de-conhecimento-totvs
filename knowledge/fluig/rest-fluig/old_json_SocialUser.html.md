---
content_hash: 5750c698952f35c5e374e96539e17d332c67b3c4eb3d3a0afc532383a70beeef
fetched_at: '2026-11-03T14:34:38.545154+00:00'
page_id: json_SocialUser
product: fluig
source: rest-fluig
title: Fluig REST — SocialUser Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialUser.html
version: 1
---

# SocialUser Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| foundationUserId | number |  |
| Properties inherited from [Social](https://api.fluig.com/old/json_Social.html) | | |
| customPage | boolean |  |
| forumId | number |  |
| resourceType | string |  |
| hidden | boolean |  |
| approvalRequired | boolean |  |
| alias | string |  |
| userAdmin | [SocialUser](https://api.fluig.com/old/json_SocialUser.html) |  |
| privateContent | boolean |  |
| page | string |  |
| type | [SocialType](https://api.fluig.com/old/json_SocialType.html) |  |
| visibility | [SocialVisibility](https://api.fluig.com/old/json_SocialVisibility.html) |  |
| state | [UserState](https://api.fluig.com/old/json_UserState.html) |  |
| name | string |  |
| securityCode | string |  |
| resourceDescription | string |  |
| description | string |  |
| Properties inherited from [SocialBaseEntity](https://api.fluig.com/old/json_SocialBaseEntity.html) | | |
| id | number |  |
| tenantId | number |  |
| creationDate | number |  |
| lastUpdateDate | number |  |

Example

```
{
  "foundationUserId" : 12345,
  "customPage" : true,
  "forumId" : 12345,
  "resourceType" : "...",
  "hidden" : true,
  "approvalRequired" : true,
  "alias" : "...",
  "userAdmin" : {
    "foundationUserId" : 12345,
    "customPage" : true,
    "forumId" : 12345,
    "resourceType" : "...",
    "hidden" : true,
    "approvalRequired" : true,
    "alias" : "...",
    "userAdmin" : { },
    "privateContent" : true,
    "page" : "...",
    "type" : "USER",
    "state" : "BLOCKED",
    "name" : "...",
    "securityCode" : "...",
    "resourceDescription" : "...",
    "description" : "...",
    "id" : 12345,
    "tenantId" : 12345,
    "creationDate" : 12345,
    "lastUpdateDate" : 12345
  },
  "privateContent" : true,
  "page" : "...",
  "type" : "COMMUNITY",
  "state" : "REMOVED",
  "name" : "...",
  "securityCode" : "...",
  "resourceDescription" : "...",
  "description" : "...",
  "id" : 12345,
  "tenantId" : 12345,
  "creationDate" : 12345,
  "lastUpdateDate" : 12345
}
```
