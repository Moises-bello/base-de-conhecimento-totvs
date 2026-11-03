---
content_hash: d35b178a14be3585ab4454e885b6b112828e059b0ee6ffee04617a0d845de9de
fetched_at: '2026-11-03T14:34:37.327861+00:00'
page_id: json_JaxbHbmCompositeAttributeType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCompositeAttributeType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCompositeAttributeType.html
version: 1
---

# JaxbHbmCompositeAttributeType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| access | string |  |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |  |
| parent | [JaxbHbmParentType](https://api.fluig.com/old/json_JaxbHbmParentType.html) |  |  |
| optimisticLock | boolean | required |  |
| name | string |  |  |
| unique | boolean | required |  |
| insert | boolean | required |  |
| update | boolean | required |  |
| node | string |  |  |
| clazz | string |  |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| lazy | boolean | required |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "access" : "...",
  "tuplizer" : [ {
    "clazz" : "...",
    "entityMode" : "MAP"
  }, {
    "clazz" : "...",
    "entityMode" : "MAP"
  } ],
  "parent" : {
    "name" : "..."
  },
  "optimisticLock" : true,
  "name" : "...",
  "unique" : true,
  "insert" : true,
  "update" : true,
  "node" : "...",
  "clazz" : "...",
  "attributes" : [ { }, { } ],
  "lazy" : true,
  "toolingHints" : [ {
    "name" : "...",
    "inheritable" : true,
    "value" : "..."
  }, {
    "name" : "...",
    "inheritable" : true,
    "value" : "..."
  } ]
}
```
