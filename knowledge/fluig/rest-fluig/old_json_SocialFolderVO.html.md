---
content_hash: 775a5235fa9694b56dff02eba0489518ab3858234c29740c3e9626210a17580d
fetched_at: '2026-11-03T14:34:38.519984+00:00'
page_id: json_SocialFolderVO
product: fluig
source: rest-fluig
title: Fluig REST — SocialFolderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialFolderVO.html
version: 1
---

# SocialFolderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| parentId | number |  |
| folderId | number |  |
| communityAlias | string |  |
| description | string |  |
| Properties inherited from [SocialDocsDto](https://api.fluig.com/old/json_SocialDocsDto.html) | | |
| spaceAlias | string |  |
| userId | string |  |
| socialFolderDescription | string |  |
| socialFolderSecurity | boolean |  |
| socialFolderWritePermission | boolean |  |
| socialFolderEnabled | boolean |  |
| socialType | string |  |
| socialFolderId | number |  |
| tenantId | number |  |

Example

```
{
  "parentId" : 12345,
  "folderId" : 12345,
  "communityAlias" : "...",
  "description" : "...",
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
