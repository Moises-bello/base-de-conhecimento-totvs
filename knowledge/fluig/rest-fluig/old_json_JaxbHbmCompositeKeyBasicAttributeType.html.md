---
content_hash: 48a5bc953a992875e960a5f9aa1aaa60eef4c6a5d2b7ac8f69a3d67ad84b7549
fetched_at: '2026-11-03T14:34:37.344121+00:00'
page_id: json_JaxbHbmCompositeKeyBasicAttributeType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCompositeKeyBasicAttributeType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCompositeKeyBasicAttributeType.html
version: 1
---

# JaxbHbmCompositeKeyBasicAttributeType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| length | number |  |
| node | string |  |
| typeAttribute | string |  |
| type | [JaxbHbmTypeSpecificationType](https://api.fluig.com/old/json_JaxbHbmTypeSpecificationType.html) |  |
| columnAttribute | string |  |
| access | string |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| name | string |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "length" : 12345,
  "node" : "...",
  "typeAttribute" : "...",
  "type" : {
    "name" : "...",
    "configParameters" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ]
  },
  "columnAttribute" : "...",
  "access" : "...",
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
