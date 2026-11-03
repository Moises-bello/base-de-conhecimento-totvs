---
content_hash: fb804c54a1487b57a68e7c12b31dbb64036a92022d8a429bb8f5b292bba920eb
fetched_at: '2026-11-03T14:34:38.460820+00:00'
page_id: json_Social
product: fluig
source: rest-fluig
title: Fluig REST — Social Data Type
type: documentation
url: https://api.fluig.com/old/json_Social.html
version: 1
---

# Social Data Type

Properties

| name | data type | description |
| --- | --- | --- |
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
| ~~visibility~~ | ~~[SocialVisibility](https://api.fluig.com/old/json_SocialVisibility.html)~~ |  |
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
    "type" : "EVENT",
    "state" : "ACTIVE",
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
  "type" : "APPLICATION",
  "state" : "UNCONFIRMED",
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
