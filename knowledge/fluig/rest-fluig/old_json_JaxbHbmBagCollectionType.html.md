---
content_hash: d255f27542444ce63651f59730f926fbd8d3288e582d09666cdafed6d10d5326
fetched_at: '2026-11-03T14:34:37.290775+00:00'
page_id: json_JaxbHbmBagCollectionType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmBagCollectionType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmBagCollectionType.html
version: 1
---

# JaxbHbmBagCollectionType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| lazy | [JaxbHbmLazyWithExtraEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithExtraEnum.html) |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| check | string |  |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |  |
| comment | string |  |  |
| embedXml | boolean |  |  |
| subselect | string |  |  |
| orderBy | string |  |  |
| fetch | [JaxbHbmFetchStyleWithSubselectEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleWithSubselectEnum.html) |  |  |
| collectionType | string |  |  |
| cache | [JaxbHbmCacheType](https://api.fluig.com/old/json_JaxbHbmCacheType.html) |  |  |
| access | string |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| element | [JaxbHbmBasicCollectionElementType](https://api.fluig.com/old/json_JaxbHbmBasicCollectionElementType.html) |  |  |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| subselectAttribute | string |  |  |
| optimisticLock | boolean | required |  |
| table | string |  |  |
| where | string |  |  |
| inverse | boolean | required |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |  |
| schema | string |  |  |
| compositeElement | [JaxbHbmCompositeCollectionElementType](https://api.fluig.com/old/json_JaxbHbmCompositeCollectionElementType.html) |  |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| cascade | string |  |  |
| mutable | boolean | required |  |
| manyToMany | [JaxbHbmManyToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToManyCollectionElementType.html) |  |  |
| manyToAny | [JaxbHbmManyToAnyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToAnyCollectionElementType.html) |  |  |
| node | string |  |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |  |
| catalog | string |  |  |
| name | string |  |  |
| oneToMany | [JaxbHbmOneToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmOneToManyCollectionElementType.html) |  |  |
| sqlDeleteAll | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| persister | string |  |  |
| batchSize | number | required |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "lazy" : "TRUE",
  "sqlInsert" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "check" : "...",
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
  "comment" : "...",
  "embedXml" : true,
  "subselect" : "...",
  "orderBy" : "...",
  "fetch" : "JOIN",
  "collectionType" : "...",
  "cache" : {
    "region" : "...",
    "usage" : "READ_ONLY",
    "include" : "NON_LAZY"
  },
  "access" : "...",
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
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
  "subselectAttribute" : "...",
  "optimisticLock" : true,
  "table" : "...",
  "where" : "...",
  "inverse" : true,
  "synchronize" : [ {
    "table" : "..."
  }, {
    "table" : "..."
  } ],
  "schema" : "...",
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
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "cascade" : "...",
  "mutable" : true,
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
  "node" : "...",
  "loader" : {
    "queryRef" : "..."
  },
  "catalog" : "...",
  "name" : "...",
  "oneToMany" : {
    "embedXml" : true,
    "node" : "...",
    "entityName" : "...",
    "notFound" : "EXCEPTION",
    "clazz" : "..."
  },
  "sqlDeleteAll" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "persister" : "...",
  "batchSize" : 12345,
  "outerJoin" : "TRUE",
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
