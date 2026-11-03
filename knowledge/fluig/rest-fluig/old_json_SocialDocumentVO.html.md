---
content_hash: 68036e0678b16a10c2abf02b35d278179bd893840d6cbd00df21a185df3d576b
fetched_at: '2026-11-03T14:34:38.508481+00:00'
page_id: json_SocialDocumentVO
product: fluig
source: rest-fluig
title: Fluig REST — SocialDocumentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialDocumentVO.html
version: 1
---

# SocialDocumentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| folderId | number |  |
| communityAlias | string |  |
| description | string |  |
| name | string |  |
| base64document | string |  |
| documentId | number |  |
| documentExtension | string |  |
| Properties inherited from [Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html) | | |
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
  "folderId" : 12345,
  "communityAlias" : "...",
  "description" : "...",
  "name" : "...",
  "base64document" : "...",
  "documentId" : 12345,
  "documentExtension" : "...",
  "base64media" : "...",
  "mediaId" : 12345,
  "extension" : "JPEG",
  "mediaType" : "GALLERY_PHOTO",
  "mediaName" : "...",
  "mediaData" : "...",
  "galleryId" : 12345,
  "type" : "GALLERY_PHOTO",
  "parentId" : 12345,
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
