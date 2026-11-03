---
content_hash: 77da46caa6be11abeef9ced968666aca7f65501e6a065e6b00f522548b13703f
fetched_at: '2026-11-03T14:34:37.654014+00:00'
page_id: json_JaxbHbmSetType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmSetType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmSetType.html
version: 1
---

# JaxbHbmSetType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| mutable | boolean | required |  |
| cache | [JaxbHbmCacheType](https://api.fluig.com/old/json_JaxbHbmCacheType.html) |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| cascade | string |  |  |
| schema | string |  |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |  |
| element | [JaxbHbmBasicCollectionElementType](https://api.fluig.com/old/json_JaxbHbmBasicCollectionElementType.html) |  |  |
| subselectAttribute | string |  |  |
| name | string |  |  |
| fetch | [JaxbHbmFetchStyleWithSubselectEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleWithSubselectEnum.html) |  |  |
| where | string |  |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| table | string |  |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |  |
| manyToMany | [JaxbHbmManyToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToManyCollectionElementType.html) |  |  |
| check | string |  |  |
| lazy | [JaxbHbmLazyWithExtraEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithExtraEnum.html) |  |  |
| oneToMany | [JaxbHbmOneToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmOneToManyCollectionElementType.html) |  |  |
| sqlDeleteAll | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| manyToAny | [JaxbHbmManyToAnyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToAnyCollectionElementType.html) |  |  |
| batchSize | number | required |  |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| persister | string |  |  |
| catalog | string |  |  |
| embedXml | boolean |  |  |
| subselect | string |  |  |
| optimisticLock | boolean | required |  |
| sort | string |  |  |
| comment | string |  |  |
| node | string |  |  |
| collectionType | string |  |  |
| access | string |  |  |
| orderBy | string |  |  |
| compositeElement | [JaxbHbmCompositeCollectionElementType](https://api.fluig.com/old/json_JaxbHbmCompositeCollectionElementType.html) |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| inverse | boolean | required |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "mutable" : true,
  "cache" : {
    "region" : "...",
    "usage" : "NONSTRICT_READ_WRITE",
    "include" : "ALL"
  },
  "sqlInsert" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "cascade" : "...",
  "schema" : "...",
  "loader" : {
    "queryRef" : "..."
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
  "subselectAttribute" : "...",
  "name" : "...",
  "fetch" : "JOIN",
  "where" : "...",
  "outerJoin" : "FALSE",
  "table" : "...",
  "synchronize" : [ {
    "table" : "..."
  }, {
    "table" : "..."
  } ],
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
  "check" : "...",
  "lazy" : "TRUE",
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
    "check" : "PARAM"
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
  "batchSize" : 12345,
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
  "persister" : "...",
  "catalog" : "...",
  "embedXml" : true,
  "subselect" : "...",
  "optimisticLock" : true,
  "sort" : "...",
  "comment" : "...",
  "node" : "...",
  "collectionType" : "...",
  "access" : "...",
  "orderBy" : "...",
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
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
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
