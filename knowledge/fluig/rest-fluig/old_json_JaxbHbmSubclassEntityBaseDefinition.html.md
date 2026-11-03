---
content_hash: 5902a8ba22078850d5f3545bc50a6cd52863e858a9ae6f365de29c744a3f453d
fetched_at: '2026-11-03T14:34:37.663746+00:00'
page_id: json_JaxbHbmSubclassEntityBaseDefinition
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmSubclassEntityBaseDefinition Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmSubclassEntityBaseDefinition.html
version: 1
---

# JaxbHbmSubclassEntityBaseDefinition Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| extends | string |  |
| Properties inherited from [JaxbHbmEntityBaseDefinition](https://api.fluig.com/old/json_JaxbHbmEntityBaseDefinition.html) | | |
| lazy | boolean |  |
| name | string |  |
| dynamicInsert | boolean |  |
| proxy | string |  |
| batchSize | number |  |
| node | string |  |
| entityName | string |  |
| persister | string |  |
| abstract | boolean |  |
| selectBeforeUpdate | boolean |  |
| dynamicUpdate | boolean |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "extends" : "...",
  "lazy" : true,
  "name" : "...",
  "dynamicInsert" : true,
  "proxy" : "...",
  "batchSize" : 12345,
  "node" : "...",
  "entityName" : "...",
  "persister" : "...",
  "abstract" : true,
  "selectBeforeUpdate" : true,
  "dynamicUpdate" : true,
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
