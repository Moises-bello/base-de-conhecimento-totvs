---
content_hash: e141078427e4289f028469ccc86ae810834547a897a151d47d7a1418ad8b867b
fetched_at: '2026-11-03T14:34:38.493552+00:00'
page_id: json_SocialDocsDto
product: fluig
source: rest-fluig
title: Fluig REST — SocialDocsDto Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialDocsDto.html
version: 1
---

# SocialDocsDto Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| spaceAlias | string |  |  |
| userId | string |  |  |
| socialFolderDescription | string |  |  |
| socialFolderSecurity | boolean |  |  |
| socialFolderWritePermission | boolean |  |  |
| socialFolderEnabled | boolean |  |  |
| socialType | string |  |  |
| socialFolderId | number |  |  |
| tenantId | number | required |  |

Example

```
{
  "spaceAlias" : "...",
  "userId" : "...",
  "socialFolderDescription" : "...",
  "socialFolderSecurity" : true,
  "socialFolderWritePermission" : true,
  "socialFolderEnabled" : true,
  "socialType" : "...",
  "socialFolderId" : 12345,
  "tenantId" : 12345
}
```
