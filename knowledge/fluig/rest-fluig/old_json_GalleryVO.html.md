---
content_hash: 43b3554cba769806d729d0ffb578461b731e289dbd86844d1f4a76148c235de3
fetched_at: '2026-11-03T14:34:37.067156+00:00'
page_id: json_GalleryVO
product: fluig
source: rest-fluig
title: Fluig REST — GalleryVO Data Type
type: documentation
url: https://api.fluig.com/old/json_GalleryVO.html
version: 1
---

# GalleryVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| galleryId | number |  |
| name | string |  |
| type | [SocialMediaType](https://api.fluig.com/old/json_SocialMediaType.html) |  |
| Properties inherited from [SocialFolderVO](https://api.fluig.com/old/json_SocialFolderVO.html) | | |
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
  "galleryId" : 12345,
  "name" : "...",
  "type" : "GALLERY_VIDEO",
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
