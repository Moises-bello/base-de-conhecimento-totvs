---
content_hash: 32abaaf1b2af23b6cc515359ea0ccff2f5ac5e447a394a15d843f4c2b1bba87c
fetched_at: '2026-11-03T14:34:37.337151+00:00'
page_id: json_JaxbHbmCompositeIdType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCompositeIdType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCompositeIdType.html
version: 1
---

# JaxbHbmCompositeIdType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| generator | [JaxbHbmGeneratorSpecificationType](https://api.fluig.com/old/json_JaxbHbmGeneratorSpecificationType.html) |  |  |
| access | string |  |  |
| node | string |  |  |
| unsavedValue | [JaxbHbmUnsavedValueCompositeIdEnum](https://api.fluig.com/old/json_JaxbHbmUnsavedValueCompositeIdEnum.html) |  |  |
| clazz | string |  |  |
| keyPropertyOrKeyManyToOne | array of [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) |  |  |
| mapped | boolean | required |  |
| name | string |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

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
  "access" : "...",
  "node" : "...",
  "unsavedValue" : "ANY",
  "clazz" : "...",
  "keyPropertyOrKeyManyToOne" : [ {
    "toolingHints" : [ {
      "name" : "...",
      "inheritable" : true,
      "value" : "..."
    }, {
      "name" : "...",
      "inheritable" : true,
      "value" : "..."
    } ]
  }, {
    "toolingHints" : [ {
      "name" : "...",
      "inheritable" : true,
      "value" : "..."
    }, {
      "name" : "...",
      "inheritable" : true,
      "value" : "..."
    } ]
  } ],
  "mapped" : true,
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
