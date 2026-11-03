---
content_hash: 119093c50ee0673b26de94788ec1e5ece1428d82d0d39e63ff9f91482c460b82
fetched_at: '2026-11-03T14:34:36.200976+00:00'
page_id: json_ApproveDocumentVO
product: fluig
source: rest-fluig
title: Fluig REST — ApproveDocumentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ApproveDocumentVO.html
version: 1
---

# ApproveDocumentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| approved | boolean |  |  |
| documentId | number | required |  |
| observation | string |  |  |
| signed | boolean |  |  |
| version | number | required |  |
| serialversionuid | number | required |  |

Example

```
{
  "approved" : true,
  "documentId" : 12345,
  "observation" : "...",
  "signed" : true,
  "version" : 12345,
  "serialversionuid" : 12345
}
```
