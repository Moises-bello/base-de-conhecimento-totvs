---
content_hash: 0d3800a1ddf24ced5d3d268dc1173cb433f3e33cc2f854a31551418757b1127a
fetched_at: '2026-11-03T14:34:38.019481+00:00'
page_id: json_ProcessAttachmentVO_dtos
product: fluig
source: rest-fluig
title: Fluig REST — ProcessAttachmentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessAttachmentVO_dtos.html
version: 1
---

# ProcessAttachmentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| crc | number |  |  |
| originalMovementSequence | number |  |  |
| streamControlUrl | string |  |  |
| createDateTimestamp | number |  |  |
| description | string |  |  |
| documentType | string |  |  |
| createDate | number |  |  |
| documentId | number |  |  |
| colleagueName | string |  |  |
| fileName | string |  |  |
| attachments | array of [Attachment](https://api.fluig.com/old/json_Attachment.html) |  |  |
| version | number |  |  |
| attachmentSequence | number | required |  |
| permission | string |  |  |
| size | number | required |  |
| newAttach | boolean |  |  |
| deleted | boolean |  |  |
| processInstanceId | number | required |  |
| companyId | number | required |  |
| colleagueId | string |  |  |

Example

```
{
  "crc" : 12345,
  "originalMovementSequence" : 12345,
  "streamControlUrl" : "...",
  "createDateTimestamp" : 12345,
  "description" : "...",
  "documentType" : "...",
  "createDate" : 12345,
  "documentId" : 12345,
  "colleagueName" : "...",
  "fileName" : "...",
  "attachments" : [ {
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
  }, {
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
  } ],
  "version" : 12345,
  "attachmentSequence" : 12345,
  "permission" : "...",
  "size" : 12345.0,
  "newAttach" : true,
  "deleted" : true,
  "processInstanceId" : 12345,
  "companyId" : 12345,
  "colleagueId" : "..."
}
```
