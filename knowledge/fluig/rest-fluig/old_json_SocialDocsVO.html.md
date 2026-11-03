---
content_hash: 5a2d7954a2a05188f1e55c346f45263398011151aa851581161950102045d0d0
fetched_at: '2026-11-03T14:34:38.497284+00:00'
page_id: json_SocialDocsVO
product: fluig
source: rest-fluig
title: Fluig REST — SocialDocsVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialDocsVO.html
version: 1
---

# SocialDocsVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| spaceAlias | string |  |  |
| socialFolderWritePermission | boolean |  |  |
| tenantId | number | required |  |
| socialFolderEnabled | boolean |  |  |
| socialFolderSecurity | boolean |  |  |
| socialFolderDescription | string |  |  |
| socialFolderId | number |  |  |
| userId | string |  |  |

Example

```
{
  "spaceAlias" : "...",
  "socialFolderWritePermission" : true,
  "tenantId" : 12345,
  "socialFolderEnabled" : true,
  "socialFolderSecurity" : true,
  "socialFolderDescription" : "...",
  "socialFolderId" : 12345,
  "userId" : "..."
}
```
