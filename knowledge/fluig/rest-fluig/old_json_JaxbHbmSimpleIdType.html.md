---
content_hash: fe240b57fbe1bfb282a225baeea485fae15ad80b9f945c5364aa4c990de983de
fetched_at: '2026-11-03T14:34:37.658793+00:00'
page_id: json_JaxbHbmSimpleIdType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmSimpleIdType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmSimpleIdType.html
version: 1
---

# JaxbHbmSimpleIdType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| unsavedValue | string |  |
| length | number |  |
| name | string |  |
| access | string |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| type | [JaxbHbmTypeSpecificationType](https://api.fluig.com/old/json_JaxbHbmTypeSpecificationType.html) |  |
| generator | [JaxbHbmGeneratorSpecificationType](https://api.fluig.com/old/json_JaxbHbmGeneratorSpecificationType.html) |  |
| columnAttribute | string |  |
| node | string |  |
| typeAttribute | string |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "unsavedValue" : "...",
  "length" : 12345,
  "name" : "...",
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
  "node" : "...",
  "typeAttribute" : "...",
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
