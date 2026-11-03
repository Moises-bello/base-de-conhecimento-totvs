---
content_hash: f1e403886fb7d89556d55d0a07b66bed785f36d1e12a245a5ba780ff88c8872b
fetched_at: '2026-11-03T14:34:38.151245+00:00'
page_id: json_PublisherFileVO
product: fluig
source: rest-fluig
title: Fluig REST — PublisherFileVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PublisherFileVO.html
version: 1
---

# PublisherFileVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| attachmentSource | [AttachmentSource](https://api.fluig.com/old/json_AttachmentSource.html) |  |  |
| main | boolean | required |  |
| source | string |  |  |
| filename | string |  |  |

Example

```
{
  "attachmentSource" : "FTP_FOLDER",
  "main" : true,
  "source" : "...",
  "filename" : "..."
}
```
