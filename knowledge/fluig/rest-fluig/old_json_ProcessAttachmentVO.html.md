---
content_hash: 0a664b74388820d92e1538adeb578c4308eae63457590c5aa22c4df2c786c060
fetched_at: '2026-11-03T14:34:38.011377+00:00'
page_id: json_ProcessAttachmentVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessAttachmentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessAttachmentVO.html
version: 1
---

# ProcessAttachmentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| colleagueId | string |  |  |
| attachedDate | number |  |  |
| version | number | required |  |
| originalMovementSequence | number | required |  |
| documentId | number | required |  |
| description | string |  |  |

Example

```
{
  "colleagueId" : "...",
  "attachedDate" : 12345,
  "version" : 12345,
  "originalMovementSequence" : 12345,
  "documentId" : 12345,
  "description" : "..."
}
```
