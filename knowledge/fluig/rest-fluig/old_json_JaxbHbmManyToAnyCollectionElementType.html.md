---
content_hash: e54ff5e5268be38618645c4244d9bb379bd4167ce942eb6fef3da37cddabf568
fetched_at: '2026-11-03T14:34:37.492481+00:00'
page_id: json_JaxbHbmManyToAnyCollectionElementType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmManyToAnyCollectionElementType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmManyToAnyCollectionElementType.html
version: 1
---

# JaxbHbmManyToAnyCollectionElementType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| metaValue | array of [JaxbHbmAnyValueMappingType](https://api.fluig.com/old/json_JaxbHbmAnyValueMappingType.html) |  |
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
  "metaValue" : [ {
    "value" : "...",
    "clazz" : "..."
  }, {
    "value" : "...",
    "clazz" : "..."
  } ],
  "idType" : "...",
  "metaType" : "..."
}
```
