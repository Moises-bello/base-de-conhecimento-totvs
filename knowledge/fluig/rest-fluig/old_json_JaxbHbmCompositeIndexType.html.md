---
content_hash: 79b1333bb826186431cb0d64cdeb32678a82932ef3d2085aa9447ca421fd6636
fetched_at: '2026-11-03T14:34:37.339929+00:00'
page_id: json_JaxbHbmCompositeIndexType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmCompositeIndexType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmCompositeIndexType.html
version: 1
---

# JaxbHbmCompositeIndexType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| attributes | array of [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) |  |
| clazz | string |  |

Example

```
{
  "attributes" : [ {
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
  "clazz" : "..."
}
```
