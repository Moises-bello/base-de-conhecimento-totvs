---
content_hash: a43b060983d5ff0276ec43642d7c9c854c5295fba12c23884f7e4714ff56b9db
fetched_at: '2026-11-03T14:34:36.318816+00:00'
page_id: json_Base64MediaVO
product: fluig
source: rest-fluig
title: Fluig REST — Base64MediaVO Data Type
type: documentation
url: https://api.fluig.com/old/json_Base64MediaVO.html
version: 1
---

# Base64MediaVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| base64media | string |  |
| mediaId | number |  |
| extension | [MediaType](https://api.fluig.com/old/json_MediaType.html) |  |
| mediaType | [SocialMediaType](https://api.fluig.com/old/json_SocialMediaType.html) |  |
| mediaName | string |  |
| mediaData | string |  |
| Properties inherited from [GalleryVO](https://api.fluig.com/old/json_GalleryVO.html) | | |
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
  "base64media" : "...",
  "mediaId" : 12345,
  "extension" : "MP4",
  "mediaType" : "GALLERY_PHOTO",
  "mediaName" : "...",
  "mediaData" : "...",
  "galleryId" : 12345,
  "name" : "...",
  "type" : "GALLERY_PHOTO",
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
