---
content_hash: d38eb01f3005b5046b43cd6fbbc3ca002ab76d98c62b08d4d0ecb5466a63b0fb
fetched_at: '2026-11-03T14:34:37.499877+00:00'
page_id: json_JaxbHbmManyToManyCollectionElementType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmManyToManyCollectionElementType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmManyToManyCollectionElementType.html
version: 1
---

# JaxbHbmManyToManyCollectionElementType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| node | string |  |  |
| entityName | string |  |  |
| columnAttribute | string |  |  |
| orderBy | string |  |  |
| fetch | [JaxbHbmFetchStyleEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleEnum.html) |  |  |
| formulaAttribute | string |  |  |
| unique | boolean | required |  |
| notFound | [JaxbHbmNotFoundEnum](https://api.fluig.com/old/json_JaxbHbmNotFoundEnum.html) |  |  |
| clazz | string |  |  |
| embedXml | boolean |  |  |
| propertyRef | string |  |  |
| foreignKey | string |  |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| columnOrFormula | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| lazy | [JaxbHbmLazyEnum](https://api.fluig.com/old/json_JaxbHbmLazyEnum.html) |  |  |
| where | string |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "filter" : [ {
    "content" : [ { }, { } ],
    "name" : "...",
    "condition" : "...",
    "autoAliasInjection" : "..."
  }, {
    "content" : [ { }, { } ],
    "name" : "...",
    "condition" : "...",
    "autoAliasInjection" : "..."
  } ],
  "node" : "...",
  "entityName" : "...",
  "columnAttribute" : "...",
  "orderBy" : "...",
  "fetch" : "SELECT",
  "formulaAttribute" : "...",
  "unique" : true,
  "notFound" : "IGNORE",
  "clazz" : "...",
  "embedXml" : true,
  "propertyRef" : "...",
  "foreignKey" : "...",
  "outerJoin" : "AUTO",
  "columnOrFormula" : [ { }, { } ],
  "lazy" : "PROXY",
  "where" : "...",
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
