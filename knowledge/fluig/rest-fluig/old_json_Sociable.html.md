---
content_hash: e0ef460fd8fb6739c2e6f62a97d90c2c9b82538d4ba7e124865c4a92fe55d90f
fetched_at: '2026-11-03T14:34:38.398755+00:00'
page_id: json_Sociable
product: fluig
source: rest-fluig
title: Fluig REST — Sociable Data Type
type: documentation
url: https://api.fluig.com/old/json_Sociable.html
version: 1
---

# Sociable Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| editionDate | number |  |
| width | number |  |
| mimeType | string |  |
| numberComments | number |  |
| numberDenouncements | number |  |
| sociableType | string |  |
| numberWatchers | number |  |
| customData | string |  |
| removed | boolean |  |
| tags | string |  |
| numberShares | number |  |
| height | number |  |
| social | [Social](https://api.fluig.com/old/json_Social.html) |  |
| user | [SocialUser](https://api.fluig.com/old/json_SocialUser.html) |  |
| numberLikes | number |  |
| url | string |  |
| Properties inherited from [SocialBaseEntity](https://api.fluig.com/old/json_SocialBaseEntity.html) | | |
| id | number |  |
| tenantId | number |  |
| creationDate | number |  |
| lastUpdateDate | number |  |

Example

```
{
  "editionDate" : 12345,
  "width" : 12345,
  "mimeType" : "...",
  "numberComments" : 12345,
  "numberDenouncements" : 12345,
  "sociableType" : "...",
  "numberWatchers" : 12345,
  "customData" : "...",
  "removed" : true,
  "tags" : "...",
  "numberShares" : 12345,
  "height" : 12345,
  "social" : {
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
      "state" : "REMOVED",
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
  "user" : {
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
  "numberLikes" : 12345,
  "url" : "...",
  "id" : 12345,
  "tenantId" : 12345,
  "creationDate" : 12345,
  "lastUpdateDate" : 12345
}
```
