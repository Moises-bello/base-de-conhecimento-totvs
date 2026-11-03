---
content_hash: da049b995666f077541b26c99a04c592d416aad9b21dcd36a7fa6e39d056da15
fetched_at: '2026-11-03T14:34:37.443218+00:00'
page_id: json_JaxbHbmIndexManyToAnyType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmIndexManyToAnyType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmIndexManyToAnyType.html
version: 1
---

# JaxbHbmIndexManyToAnyType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| idType | string |  |
| metaType | string |  |

Example

```
{
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
  "idType" : "...",
  "metaType" : "..."
}
```
