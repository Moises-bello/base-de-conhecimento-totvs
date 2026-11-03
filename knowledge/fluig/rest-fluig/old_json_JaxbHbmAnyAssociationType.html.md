---
content_hash: 7b3e588bba0e2e07b05e984bfd2b126eea077623f4b7fd7299bf7a25c94b511f
fetched_at: '2026-11-03T14:34:37.256355+00:00'
page_id: json_JaxbHbmAnyAssociationType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmAnyAssociationType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmAnyAssociationType.html
version: 1
---

# JaxbHbmAnyAssociationType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| cascade | string |  |  |
| index | string |  |  |
| metaValue | array of [JaxbHbmAnyValueMappingType](https://api.fluig.com/old/json_JaxbHbmAnyValueMappingType.html) |  |  |
| optimisticLock | boolean | required |  |
| update | boolean | required |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |  |
| name | string |  |  |
| idType | string |  |  |
| insert | boolean | required |  |
| node | string |  |  |
| lazy | boolean | required |  |
| metaType | string |  |  |
| access | string |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "cascade" : "...",
  "index" : "...",
  "metaValue" : [ {
    "value" : "...",
    "clazz" : "..."
  }, {
    "value" : "...",
    "clazz" : "..."
  } ],
  "optimisticLock" : true,
  "update" : true,
  "column" : [ {
    "length" : 12345,
    "unique" : true,
    "scale" : 12345,
    "comment" : "...",
    "precision" : 12345,
    "sqlType" : "...",
    "read" : "...",
    "write" : "...",
    "index" : "...",
    "name" : "...",
    "notNull" : true,
    "check" : "...",
    "uniqueKey" : "...",
    "default" : "..."
  }, {
    "length" : 12345,
    "unique" : true,
    "scale" : 12345,
    "comment" : "...",
    "precision" : 12345,
    "sqlType" : "...",
    "read" : "...",
    "write" : "...",
    "index" : "...",
    "name" : "...",
    "notNull" : true,
    "check" : "...",
    "uniqueKey" : "...",
    "default" : "..."
  } ],
  "name" : "...",
  "idType" : "...",
  "insert" : true,
  "node" : "...",
  "lazy" : true,
  "metaType" : "...",
  "access" : "...",
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
