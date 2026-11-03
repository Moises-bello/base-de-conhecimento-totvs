---
content_hash: 4fc72471eeafefa69b4c613755d84da951ede271dcf3b1941bad1c38a9d6efe0
fetched_at: '2026-11-03T14:34:37.348743+00:00'
page_id: json_JaxbHbmCompositeKeyManyToOneType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCompositeKeyManyToOneType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCompositeKeyManyToOneType.html
version: 1
---

# JaxbHbmCompositeKeyManyToOneType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| lazy | [JaxbHbmLazyEnum](https://api.fluig.com/old/json_JaxbHbmLazyEnum.html) |  |
| onDelete | [JaxbHbmOnDeleteEnum](https://api.fluig.com/old/json_JaxbHbmOnDeleteEnum.html) |  |
| access | string |  |
| clazz | string |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| entityName | string |  |
| name | string |  |
| columnAttribute | string |  |
| foreignKey | string |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "lazy" : "FALSE",
  "onDelete" : "CASCADE",
  "access" : "...",
  "clazz" : "...",
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
  "entityName" : "...",
  "name" : "...",
  "columnAttribute" : "...",
  "foreignKey" : "...",
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
