---
content_hash: 94705185deffebeb40803965255de9f0c83a54e971365a97940d4576fc959b05
fetched_at: '2026-11-03T14:34:37.446285+00:00'
page_id: json_JaxbHbmIndexManyToManyType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmIndexManyToManyType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmIndexManyToManyType.html
version: 1
---

# JaxbHbmIndexManyToManyType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| clazz | string |  |
| entityName | string |  |
| columnAttribute | string |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| foreignKey | string |  |

Example

```
{
  "clazz" : "...",
  "entityName" : "...",
  "columnAttribute" : "...",
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
  "foreignKey" : "..."
}
```
