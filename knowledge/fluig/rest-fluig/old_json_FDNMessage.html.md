---
content_hash: 86f31601783a51eb605d798b680a59047152189bb57887f5af54a4ff18162f92
fetched_at: '2026-11-03T14:34:36.843667+00:00'
page_id: json_FDNMessage
product: fluig
source: rest-fluig
title: Fluig REST — FDNMessage Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNMessage.html
version: 1
---

# FDNMessage Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| message | string |  |
| type | [FDNMessageType](https://api.fluig.com/old/json_FDNMessageType.html) |  |
| param | object |  |
| errorCode | string |  |
| detail | string |  |

Example

```
{
  "message" : "...",
  "type" : "QUESTION",
  "param" : { },
  "errorCode" : "...",
  "detail" : "..."
}
```
