---
content_hash: b106f349c4644597c92bb0c7fd551c04d5c990dc5d9268d38c5705e85d73a933
fetched_at: '2026-11-03T14:34:37.380131+00:00'
page_id: json_JaxbHbmDynamicComponentType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmDynamicComponentType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmDynamicComponentType.html
version: 1
---

# JaxbHbmDynamicComponentType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| insert | boolean | required |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| unique | boolean | required |  |
| name | string |  |  |
| optimisticLock | boolean | required |  |
| update | boolean | required |  |
| access | string |  |  |
| node | string |  |  |

Example

```
{
  "insert" : true,
  "attributes" : [ { }, { } ],
  "unique" : true,
  "name" : "...",
  "optimisticLock" : true,
  "update" : true,
  "access" : "...",
  "node" : "..."
}
```
