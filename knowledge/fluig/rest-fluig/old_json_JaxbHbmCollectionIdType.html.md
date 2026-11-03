---
content_hash: d7246d96cf42afe1d0ccdfbee38640e4c3f11271c56986fd2cf3fe47b0ea717f
fetched_at: '2026-11-03T14:34:37.318093+00:00'
page_id: json_JaxbHbmCollectionIdType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCollectionIdType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCollectionIdType.html
version: 1
---

# JaxbHbmCollectionIdType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| generator | [JaxbHbmGeneratorSpecificationType](https://api.fluig.com/old/json_JaxbHbmGeneratorSpecificationType.html) |  |
| columnAttribute | string |  |
| length | number |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| type | string |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "generator" : {
    "clazz" : "...",
    "configParameters" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ]
  },
  "columnAttribute" : "...",
  "length" : 12345,
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
  "type" : "...",
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
