---
content_hash: a6160d0403475a750b0b958972ae24ae418a72ed545b4302e2c7e43f8b89d840
fetched_at: '2026-11-03T14:34:36.192283+00:00'
page_id: json_ApplicationRenderVO
product: fluig
source: rest-fluig
title: Fluig REST — ApplicationRenderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ApplicationRenderVO.html
version: 1
---

# ApplicationRenderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| content | string |  |
| resources | array of [ApplicationRenderResourceVO](https://api.fluig.com/old/json_ApplicationRenderResourceVO.html) |  |

Example

```
{
  "content" : "...",
  "resources" : [ {
    "type" : "...",
    "resource" : "..."
  }, {
    "type" : "...",
    "resource" : "..."
  } ]
}
```
