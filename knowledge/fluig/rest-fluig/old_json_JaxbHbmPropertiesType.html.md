---
content_hash: 94205c825e3f10fe22450b569e4a5c1e8c8f523824f9dbbdbe7e8aa79638d553
fetched_at: '2026-11-03T14:34:37.608654+00:00'
page_id: json_JaxbHbmPropertiesType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmPropertiesType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmPropertiesType.html
version: 1
---

# JaxbHbmPropertiesType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| name | string |  |  |
| node | string |  |  |
| insert | boolean | required |  |
| optimisticLock | boolean | required |  |
| unique | boolean | required |  |
| update | boolean | required |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |

Example

```
{
  "name" : "...",
  "node" : "...",
  "insert" : true,
  "optimisticLock" : true,
  "unique" : true,
  "update" : true,
  "attributes" : [ { }, { } ]
}
```
