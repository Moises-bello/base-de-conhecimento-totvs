---
content_hash: 0b1bee967ecda87c9eb31e54c3d984e1d668cf1d97c0556ba4cab20d5c5d3bbf
fetched_at: '2026-11-03T14:34:37.604729+00:00'
page_id: json_JaxbHbmPrimitiveArrayType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmPrimitiveArrayType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmPrimitiveArrayType.html
version: 1
---

# JaxbHbmPrimitiveArrayType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| comment | string |  |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| where | string |  |  |
| cache | [JaxbHbmCacheType](https://api.fluig.com/old/json_JaxbHbmCacheType.html) |  |  |
| index | [JaxbHbmIndexType](https://api.fluig.com/old/json_JaxbHbmIndexType.html) |  |  |
| element | [JaxbHbmBasicCollectionElementType](https://api.fluig.com/old/json_JaxbHbmBasicCollectionElementType.html) |  |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |  |
| subselect | string |  |  |
| node | string |  |  |
| access | string |  |  |
| collectionType | string |  |  |
| sqlDeleteAll | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| listIndex | [JaxbHbmListIndexType](https://api.fluig.com/old/json_JaxbHbmListIndexType.html) |  |  |
| batchSize | number | required |  |
| subselectAttribute | string |  |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |  |
| mutable | boolean | required |  |
| embedXml | boolean |  |  |
| table | string |  |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |  |
| check | string |  |  |
| fetch | [JaxbHbmFetchStyleWithSubselectEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleWithSubselectEnum.html) |  |  |
| name | string |  |  |
| persister | string |  |  |
| optimisticLock | boolean | required |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| catalog | string |  |  |
| schema | string |  |  |
| Properties inherited from [PluralAttributeInfoPrimitiveArrayAdapter](https://api.fluig.com/old/json_PluralAttributeInfoPrimitiveArrayAdapter.html) | | | |
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
  "comment" : "...",
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "sqlInsert" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "where" : "...",
  "cache" : {
    "region" : "...",
    "usage" : "READ_WRITE",
    "include" : "NON_LAZY"
  },
  "index" : {
    "length" : 12345,
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
    "type" : "...",
    "columnAttribute" : "..."
  },
  "element" : {
    "columnAttribute" : "...",
    "notNull" : true,
    "typeAttribute" : "...",
    "length" : 12345,
    "node" : "...",
    "formulaAttribute" : "...",
    "scale" : 12345,
    "columnOrFormula" : [ { }, { } ],
    "precision" : 12345,
    "unique" : true,
    "type" : {
      "name" : "...",
      "configParameters" : [ { }, { } ]
    }
  },
  "loader" : {
    "queryRef" : "..."
  },
  "subselect" : "...",
  "node" : "...",
  "access" : "...",
  "collectionType" : "...",
  "sqlDeleteAll" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "listIndex" : {
    "column" : {
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
    },
    "base" : "...",
    "columnAttribute" : "..."
  },
  "batchSize" : 12345,
  "subselectAttribute" : "...",
  "synchronize" : [ {
    "table" : "..."
  }, {
    "table" : "..."
  } ],
  "mutable" : true,
  "embedXml" : true,
  "table" : "...",
  "key" : {
    "onDelete" : "NOACTION",
    "foreignKey" : "...",
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
    "unique" : true,
    "columnAttribute" : "...",
    "notNull" : true,
    "propertyRef" : "...",
    "update" : true
  },
  "check" : "...",
  "fetch" : "SUBSELECT",
  "name" : "...",
  "persister" : "...",
  "optimisticLock" : true,
  "outerJoin" : "FALSE",
  "catalog" : "...",
  "schema" : "...",
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
    "fetch" : "SELECT",
    "formulaAttribute" : "...",
    "unique" : true,
    "notFound" : "EXCEPTION",
    "clazz" : "...",
    "embedXml" : true,
    "propertyRef" : "...",
    "foreignKey" : "...",
    "outerJoin" : "TRUE",
    "columnOrFormula" : [ { }, { } ],
    "lazy" : "FALSE",
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
    "notFound" : "EXCEPTION",
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
      "entityMode" : "POJO"
    }, {
      "clazz" : "...",
      "entityMode" : "POJO"
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
