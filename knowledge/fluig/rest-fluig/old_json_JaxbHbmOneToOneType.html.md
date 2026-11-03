---
content_hash: e4ca5413f1a804fd579cbe77f29043a0dd9a5c36b3f0565cf88c126a3c179fcb
fetched_at: '2026-11-03T14:34:37.584514+00:00'
page_id: json_JaxbHbmOneToOneType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmOneToOneType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmOneToOneType.html
version: 1
---

# JaxbHbmOneToOneType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| cascade | string |  |  |
| entityName | string |  |  |
| propertyRef | string |  |  |
| formula | array of string |  |  |
| access | string |  |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| name | string |  |  |
| node | string |  |  |
| fetch | [JaxbHbmFetchStyleEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleEnum.html) |  |  |
| constrained | boolean | required |  |
| clazz | string |  |  |
| onDelete | [JaxbHbmOnDeleteEnum](https://api.fluig.com/old/json_JaxbHbmOnDeleteEnum.html) |  |  |
| formulaAttribute | string |  |  |
| embedXml | boolean |  |  |
| foreignKey | string |  |  |
| lazy | [JaxbHbmLazyWithNoProxyEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithNoProxyEnum.html) |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "cascade" : "...",
  "entityName" : "...",
  "propertyRef" : "...",
  "formula" : [ "...", "..." ],
  "access" : "...",
  "outerJoin" : "FALSE",
  "name" : "...",
  "node" : "...",
  "fetch" : "SELECT",
  "constrained" : true,
  "clazz" : "...",
  "onDelete" : "CASCADE",
  "formulaAttribute" : "...",
  "embedXml" : true,
  "foreignKey" : "...",
  "lazy" : "FALSE",
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
