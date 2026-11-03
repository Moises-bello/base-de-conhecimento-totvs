---
content_hash: 186b22b56c7dfff63d7656a549ee94a59213dca1178b118497415696d8fb9655
fetched_at: '2026-11-03T14:34:36.276569+00:00'
page_id: json_Attachment
product: fluig
source: rest-fluig
title: Fluig REST — Attachment Data Type
type: documentation
url: https://api.fluig.com/old/json_Attachment.html
version: 1
---

# Attachment Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| filecontent | string |  |  |
| pathName | string |  |  |
| fileModificationDate | number |  |  |
| fileSelected | [Attachment](https://api.fluig.com/old/json_Attachment.html) |  |  |
| attach | boolean |  |  |
| displayFileName | string |  |  |
| editing | boolean |  |  |
| iconPath | string |  |  |
| principal | boolean |  |  |
| fullPatch | string |  |  |
| mobile | boolean |  |  |
| supportedNewViewer | boolean |  |  |
| descriptor | boolean |  |  |
| fileSize | number | required |  |
| fileName | string |  |  |

Example

```
{
  "filecontent" : "...",
  "pathName" : "...",
  "fileModificationDate" : 12345,
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
}
```
