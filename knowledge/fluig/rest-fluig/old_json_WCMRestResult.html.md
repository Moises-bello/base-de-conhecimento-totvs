---
content_hash: 3a371532e9ae4a904f3f2008bdfb1527f9342c62da09d1ba99acb86843a89faa
fetched_at: '2026-11-03T14:34:38.942319+00:00'
page_id: json_WCMRestResult
product: fluig
source: rest-fluig
title: Fluig REST — WCMRestResult Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMRestResult.html
version: 1
---

# WCMRestResult Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| message | [FDNMessage](https://api.fluig.com/old/json_FDNMessage.html) |  |
| content | object |  |

Example

```
{
  "message" : {
    "message" : "...",
    "type" : "ERROR",
    "param" : { },
    "errorCode" : "...",
    "detail" : "..."
  },
  "content" : { }
}
```
