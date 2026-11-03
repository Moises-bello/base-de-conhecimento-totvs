---
content_hash: 551267749cd97801b75c0c78426d1675a459225aa4f4d98ba85503820cadff50
fetched_at: '2026-11-03T14:34:37.487090+00:00'
page_id: json_JaxbHbmListType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmListType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmListType.html
version: 1
---

# JaxbHbmListType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| optimisticLock | boolean | required |  |
| inverse | boolean | required |  |
| listIndex | [JaxbHbmListIndexType](https://api.fluig.com/old/json_JaxbHbmListIndexType.html) |  |  |
| schema | string |  |  |
| catalog | string |  |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |  |
| cache | [JaxbHbmCacheType](https://api.fluig.com/old/json_JaxbHbmCacheType.html) |  |  |
| where | string |  |  |
| node | string |  |  |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| fetch | [JaxbHbmFetchStyleWithSubselectEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleWithSubselectEnum.html) |  |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |  |
| cascade | string |  |  |
| name | string |  |  |
| oneToMany | [JaxbHbmOneToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmOneToManyCollectionElementType.html) |  |  |
| mutable | boolean | required |  |
| subselect | string |  |  |
| subselectAttribute | string |  |  |
| element | [JaxbHbmBasicCollectionElementType](https://api.fluig.com/old/json_JaxbHbmBasicCollectionElementType.html) |  |  |
| batchSize | number | required |  |
| manyToMany | [JaxbHbmManyToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToManyCollectionElementType.html) |  |  |
| index | [JaxbHbmIndexType](https://api.fluig.com/old/json_JaxbHbmIndexType.html) |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| sqlDeleteAll | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |  |
| check | string |  |  |
| compositeElement | [JaxbHbmCompositeCollectionElementType](https://api.fluig.com/old/json_JaxbHbmCompositeCollectionElementType.html) |  |  |
| comment | string |  |  |
| collectionType | string |  |  |
| embedXml | boolean |  |  |
| lazy | [JaxbHbmLazyWithExtraEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithExtraEnum.html) |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| persister | string |  |  |
| table | string |  |  |
| access | string |  |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| manyToAny | [JaxbHbmManyToAnyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToAnyCollectionElementType.html) |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "optimisticLock" : true,
  "inverse" : true,
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
  "schema" : "...",
  "catalog" : "...",
  "synchronize" : [ {
    "table" : "..."
  }, {
    "table" : "..."
  } ],
  "cache" : {
    "region" : "...",
    "usage" : "READ_WRITE",
    "include" : "NON_LAZY"
  },
  "where" : "...",
  "node" : "...",
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
  "fetch" : "JOIN",
  "key" : {
    "onDelete" : "CASCADE",
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
  "cascade" : "...",
  "name" : "...",
  "oneToMany" : {
    "embedXml" : true,
    "node" : "...",
    "entityName" : "...",
    "notFound" : "EXCEPTION",
    "clazz" : "..."
  },
  "mutable" : true,
  "subselect" : "...",
  "subselectAttribute" : "...",
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
  "batchSize" : 12345,
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
    "notFound" : "IGNORE",
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
  "sqlInsert" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "sqlDeleteAll" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "loader" : {
    "queryRef" : "..."
  },
  "check" : "...",
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
  "comment" : "...",
  "collectionType" : "...",
  "embedXml" : true,
  "lazy" : "TRUE",
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "persister" : "...",
  "table" : "...",
  "access" : "...",
  "outerJoin" : "FALSE",
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
