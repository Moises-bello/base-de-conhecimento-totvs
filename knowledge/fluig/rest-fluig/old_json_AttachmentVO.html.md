---
content_hash: fec78858b61694e72907e35e19ef1486dce9059b8b98dff853088e4887e2e926
fetched_at: '2026-11-03T14:34:36.290876+00:00'
page_id: json_AttachmentVO
product: fluig
source: rest-fluig
title: Fluig REST — AttachmentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AttachmentVO.html
version: 1
---

# AttachmentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| filename | string |  |  |
| principal | boolean | required |  |
| attachmentSource | [AttachmentSource](https://api.fluig.com/old/json_AttachmentSource.html) |  |  |
| iconPath | string |  |  |
| editing | boolean |  |  |
| descriptor | boolean |  |  |
| filecontent | string |  |  |
| fileModificationDate | number |  |  |
| ~~fullPatch~~ | ~~string~~ |  |  |
| renameFrom | string |  |  |
| ~~pathName~~ | ~~string~~ |  |  |
| mobile | boolean | required |  |
| supportedNewViewer | boolean |  |  |
| fileName | string |  |  |
| fileSize | number | required |  |
| fileSelected | [Attachment](https://api.fluig.com/old/json_Attachment.html) |  |  |
| realFileName | string |  |  |
| ~~attach~~ | ~~boolean~~ |  |  |

Example

```
{
  "filename" : "...",
  "principal" : true,
  "attachmentSource" : "FTP_FOLDER",
  "iconPath" : "...",
  "editing" : true,
  "descriptor" : true,
  "filecontent" : "...",
  "fileModificationDate" : 12345,
  "renameFrom" : "...",
  "mobile" : true,
  "supportedNewViewer" : true,
  "fileName" : "...",
  "fileSize" : 12345,
  "fileSelected" : {
    "filecontent" : "...",
    "pathName" : "...",
    "fileModificationDate" : 12345,
    "fileSelected" : { },
    "attach" : true,
    "displayFileName" : "...",
    "editing" : true,
    "iconPath" : "...",
    "principal" : true,
    "fullPatch" : "...",
    "mobile" : true,
    "supportedNewViewer" : true,
    "descriptor" : true,
    "fileSize" : 12345,
    "fileName" : "..."
  },
  "realFileName" : "..."
}
```
