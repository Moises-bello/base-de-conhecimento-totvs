---
content_hash: 0ece16adbf4abbebe7e41383f3e3709dd2613d011847e197a58a39fbf6c62b6b
fetched_at: '2026-11-03T14:34:37.332269+00:00'
page_id: json_JaxbHbmCompositeCollectionElementType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCompositeCollectionElementType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCompositeCollectionElementType.html
version: 1
---

# JaxbHbmCompositeCollectionElementType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |
| clazz | string |  |
| node | string |  |
| parent | [JaxbHbmParentType](https://api.fluig.com/old/json_JaxbHbmParentType.html) |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "attributes" : [ { }, { } ],
  "clazz" : "...",
  "node" : "...",
  "parent" : {
    "name" : "..."
  },
  "tuplizer" : [ {
    "clazz" : "...",
    "entityMode" : "MAP"
  }, {
    "clazz" : "...",
    "entityMode" : "MAP"
  } ],
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
