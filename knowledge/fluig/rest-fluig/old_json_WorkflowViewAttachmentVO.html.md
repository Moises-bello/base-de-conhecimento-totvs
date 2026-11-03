---
content_hash: f8d0ca2712ccf9124282bf71c4d7c8f36431ae4212c3e8f4ce2e782cfa6317e6
fetched_at: '2026-11-03T14:34:39.176684+00:00'
page_id: json_WorkflowViewAttachmentVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewAttachmentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewAttachmentVO.html
version: 1
---

# WorkflowViewAttachmentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| id | number | required |  |
| version | number |  |  |
| fileName | string |  |  |
| colleagueId | string |  |  |
| deleted | boolean |  |  |
| iconUrl | boolean |  |  |
| enableEditContent | boolean |  |  |
| attachments | array of [WorkflowViewAttachmentAttachVO](https://api.fluig.com/old/json_WorkflowViewAttachmentAttachVO.html) |  |  |
| fromFormField | boolean |  |  |
| physicalFileName | string |  |  |
| name | string |  |  |
| uploadId | string |  |  |
| documentId | number |  |  |
| iconPath | string |  |  |
| enableEdit | boolean |  |  |
| documentType | string |  |  |
| iconClass | string |  |  |
| fullPath | string |  |  |
| description | string |  |  |
| enablePublish | boolean |  |  |
| newAttach | boolean |  |  |
| hasOwnSubMenu | boolean |  |  |
| droppedZipZone | boolean |  |  |

Example

```
{
  "id" : 12345,
  "version" : 12345,
  "fileName" : "...",
  "colleagueId" : "...",
  "deleted" : true,
  "iconUrl" : true,
  "enableEditContent" : true,
  "attachments" : [ {
    "principal" : true,
    "fileName" : "...",
    "attach" : true
  }, {
    "principal" : true,
    "fileName" : "...",
    "attach" : true
  } ],
  "fromFormField" : true,
  "physicalFileName" : "...",
  "name" : "...",
  "uploadId" : "...",
  "documentId" : 12345,
  "iconPath" : "...",
  "enableEdit" : true,
  "documentType" : "...",
  "iconClass" : "...",
  "fullPath" : "...",
  "description" : "...",
  "enablePublish" : true,
  "newAttach" : true,
  "hasOwnSubMenu" : true,
  "droppedZipZone" : true
}
```
