---
content_hash: cdcdeeb0fe63d6753699b19810756e449cb8e990bbff6037b1bfe25c79767572
fetched_at: '2026-11-03T14:34:37.570698+00:00'
page_id: json_JaxbHbmNestedCompositeElementType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmNestedCompositeElementType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmNestedCompositeElementType.html
version: 1
---

# JaxbHbmNestedCompositeElementType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| name | string |  |
| clazz | string |  |
| parent | [JaxbHbmParentType](https://api.fluig.com/old/json_JaxbHbmParentType.html) |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |
| node | string |  |
| access | string |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |

Example

```
{
  "name" : "...",
  "clazz" : "...",
  "parent" : {
    "name" : "..."
  },
  "tuplizer" : [ {
    "clazz" : "...",
    "entityMode" : "MAP"
  }, {
    "clazz" : "...",
    "entityMode" : "MAP"
  } ],
  "node" : "...",
  "access" : "...",
  "attributes" : [ { }, { } ]
}
```
