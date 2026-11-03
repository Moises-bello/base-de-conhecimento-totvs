---
content_hash: 8b6afc74ea37124d5b193be6875f45190b147ed5751d023fd5fe3e9ba19a09da
fetched_at: '2026-11-03T14:34:37.385193+00:00'
page_id: json_JaxbHbmEntityBaseDefinition
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmEntityBaseDefinition Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmEntityBaseDefinition.html
version: 1
---

# JaxbHbmEntityBaseDefinition Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| lazy | boolean |  |  |
| name | string |  |  |
| dynamicInsert | boolean | required |  |
| proxy | string |  |  |
| batchSize | number | required |  |
| node | string |  |  |
| entityName | string |  |  |
| persister | string |  |  |
| abstract | boolean |  |  |
| selectBeforeUpdate | boolean | required |  |
| dynamicUpdate | boolean | required |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
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
