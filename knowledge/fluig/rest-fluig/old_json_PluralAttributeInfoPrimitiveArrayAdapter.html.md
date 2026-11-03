---
content_hash: 0c38865d886c80d9cb9e3ab66f12da6e9f424ff8d8f956417bf6c953193e28b0
fetched_at: '2026-11-03T14:34:37.975217+00:00'
page_id: json_PluralAttributeInfoPrimitiveArrayAdapter
product: fluig
source: rest-fluig
title: Fluig REST — PluralAttributeInfoPrimitiveArrayAdapter Data Type
type: documentation
url: https://api.fluig.com/old/json_PluralAttributeInfoPrimitiveArrayAdapter.html
version: 1
---

# PluralAttributeInfoPrimitiveArrayAdapter Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| manyToMany | [JaxbHbmManyToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToManyCollectionElementType.html) |  |  |
| oneToMany | [JaxbHbmOneToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmOneToManyCollectionElementType.html) |  |  |
| manyToAny | [JaxbHbmManyToAnyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToAnyCollectionElementType.html) |  |  |
| cascade | string |  |  |
| inverse | boolean | required |  |
| compositeElement | [JaxbHbmCompositeCollectionElementType](https://api.fluig.com/old/json_JaxbHbmCompositeCollectionElementType.html) |  |  |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| lazy | [JaxbHbmLazyWithExtraEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithExtraEnum.html) |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "manyToMany" : {
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
    "fetch" : "JOIN",
    "formulaAttribute" : "...",
    "unique" : true,
    "notFound" : "EXCEPTION",
    "clazz" : "...",
    "embedXml" : true,
    "propertyRef" : "...",
    "foreignKey" : "...",
    "outerJoin" : "FALSE",
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
  },
  "oneToMany" : {
    "embedXml" : true,
    "node" : "...",
    "entityName" : "...",
    "notFound" : "IGNORE",
    "clazz" : "..."
  },
  "manyToAny" : {
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
    "metaValue" : [ {
      "value" : "...",
      "clazz" : "..."
    }, {
      "value" : "...",
      "clazz" : "..."
    } ],
    "idType" : "...",
    "metaType" : "..."
  },
  "cascade" : "...",
  "inverse" : true,
  "compositeElement" : {
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
  },
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
  "lazy" : "EXTRA",
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
