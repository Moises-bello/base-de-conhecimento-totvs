---
content_hash: e7c23804c42e98fbbc4e88733b0e7f36acaf02478d793947627804354d2e8416
fetched_at: '2026-11-03T14:34:37.508727+00:00'
page_id: json_JaxbHbmManyToOneType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmManyToOneType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmManyToOneType.html
version: 1
---

# JaxbHbmManyToOneType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| columnAttribute | string |  |  |
| cascade | string |  |  |
| foreignKey | string |  |  |
| formulaAttribute | string |  |  |
| columnOrFormula | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| notFound | [JaxbHbmNotFoundEnum](https://api.fluig.com/old/json_JaxbHbmNotFoundEnum.html) |  |  |
| fetch | [JaxbHbmFetchStyleEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleEnum.html) |  |  |
| propertyRef | string |  |  |
| clazz | string |  |  |
| entityName | string |  |  |
| embedXml | boolean |  |  |
| unique | boolean | required |  |
| index | string |  |  |
| uniqueKey | string |  |  |
| name | string |  |  |
| lazy | [JaxbHbmLazyWithNoProxyEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithNoProxyEnum.html) |  |  |
| access | string |  |  |
| update | boolean | required |  |
| onDelete | [JaxbHbmOnDeleteEnum](https://api.fluig.com/old/json_JaxbHbmOnDeleteEnum.html) |  |  |
| insert | boolean | required |  |
| node | string |  |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| notNull | boolean |  |  |
| optimisticLock | boolean | required |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "columnAttribute" : "...",
  "cascade" : "...",
  "foreignKey" : "...",
  "formulaAttribute" : "...",
  "columnOrFormula" : [ { }, { } ],
  "notFound" : "IGNORE",
  "fetch" : "JOIN",
  "propertyRef" : "...",
  "clazz" : "...",
  "entityName" : "...",
  "embedXml" : true,
  "unique" : true,
  "index" : "...",
  "uniqueKey" : "...",
  "name" : "...",
  "lazy" : "FALSE",
  "access" : "...",
  "update" : true,
  "onDelete" : "NOACTION",
  "insert" : true,
  "node" : "...",
  "outerJoin" : "AUTO",
  "notNull" : true,
  "optimisticLock" : true,
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
