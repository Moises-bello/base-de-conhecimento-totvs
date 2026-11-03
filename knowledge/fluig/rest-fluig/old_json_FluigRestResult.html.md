---
content_hash: b187e7e66d5eaff039a2d9fe4a7e62e7da4a24c2637851b6821f3661c58eb67c
fetched_at: '2026-11-03T14:34:37.013277+00:00'
page_id: json_FluigRestResult
product: fluig
source: rest-fluig
title: Fluig REST — FluigRestResult Data Type
type: documentation
url: https://api.fluig.com/old/json_FluigRestResult.html
version: 1
---

# FluigRestResult Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| content | object |  |
| message | [FluigMessage](https://api.fluig.com/old/json_FluigMessage.html) |  |

Example

```
{
  "content" : { },
  "message" : {
    "message" : "...",
    "detail" : "...",
    "errorCode" : "...",
    "type" : "ERROR"
  }
}
```
