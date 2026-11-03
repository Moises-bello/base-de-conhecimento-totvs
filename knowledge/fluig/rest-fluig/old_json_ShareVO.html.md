---
content_hash: b035a71ebffc369d80f6848ac11dd39a444c613a576aeb21afe889b613b20fe2
fetched_at: '2026-11-03T14:34:38.388348+00:00'
page_id: json_ShareVO
product: fluig
source: rest-fluig
title: Fluig REST — ShareVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ShareVO.html
version: 1
---

# ShareVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| type | [SociableShareType](https://api.fluig.com/old/json_SociableShareType.html) |  |
| aliases | array of string |  |
| Properties inherited from [DenounceVO](https://api.fluig.com/old/json_DenounceVO.html) | | |
| documentId | number |  |
| version | number |  |
| text | string |  |

Example

```
{
  "type" : "COMMUNITY",
  "aliases" : [ "...", "..." ],
  "documentId" : 12345,
  "version" : 12345,
  "text" : "..."
}
```
