---
content_hash: 0fdfa9cc14250e53a498d2ded12ce28820a4538af96d2002e614073dd488d3c0
fetched_at: '2026-11-03T14:34:36.347180+00:00'
page_id: json_CancelInstancesVO
product: fluig
source: rest-fluig
title: Fluig REST — CancelInstancesVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CancelInstancesVO.html
version: 1
---

# CancelInstancesVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| cancelInstanceList | array of [CancelInstanceVO](https://api.fluig.com/old/json_CancelInstanceVO.html) |  |
| cancelText | string |  |

Example

```
{
  "cancelInstanceList" : [ {
    "processInstanceId" : 12345,
    "cancelText" : "...",
    "replacedId" : "..."
  }, {
    "processInstanceId" : 12345,
    "cancelText" : "...",
    "replacedId" : "..."
  } ],
  "cancelText" : "..."
}
```
