---
content_hash: 8a8385cdfd7d5f7b5795904bf75b88d7ef70a1cec555b0ca68b919613a803043
fetched_at: '2026-11-03T14:34:37.969181+00:00'
page_id: json_PluralAttributeInfoIdBagAdapter
product: fluig
source: rest-fluig
title: Fluig REST — PluralAttributeInfoIdBagAdapter Data Type
type: documentation
url: https://api.fluig.com/old/json_PluralAttributeInfoIdBagAdapter.html
version: 1
---

# PluralAttributeInfoIdBagAdapter Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| oneToMany | [JaxbHbmOneToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmOneToManyCollectionElementType.html) |  |  |
| inverse | boolean | required |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "oneToMany" : {
    "embedXml" : true,
    "node" : "...",
    "entityName" : "...",
    "notFound" : "EXCEPTION",
    "clazz" : "..."
  },
  "inverse" : true,
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
