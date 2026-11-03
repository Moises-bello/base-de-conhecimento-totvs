---
content_hash: 444c193cfca5a56ca41099a9bd529b554f9cd763ff16ae51843b4789291080b5
fetched_at: '2026-11-03T14:34:37.533347+00:00'
page_id: json_JaxbHbmMapType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmMapType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmMapType.html
version: 1
---

# JaxbHbmMapType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| manyToAny | [JaxbHbmManyToAnyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToAnyCollectionElementType.html) |  |  |
| mutable | boolean | required |  |
| batchSize | number | required |  |
| table | string |  |  |
| subselect | string |  |  |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| cache | [JaxbHbmCacheType](https://api.fluig.com/old/json_JaxbHbmCacheType.html) |  |  |
| compositeIndex | [JaxbHbmCompositeIndexType](https://api.fluig.com/old/json_JaxbHbmCompositeIndexType.html) |  |  |
| collectionType | string |  |  |
| subselectAttribute | string |  |  |
| sqlDeleteAll | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| indexManyToAny | [JaxbHbmIndexManyToAnyType](https://api.fluig.com/old/json_JaxbHbmIndexManyToAnyType.html) |  |  |
| persister | string |  |  |
| schema | string |  |  |
| mapKeyManyToMany | [JaxbHbmMapKeyManyToManyType](https://api.fluig.com/old/json_JaxbHbmMapKeyManyToManyType.html) |  |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |  |
| fetch | [JaxbHbmFetchStyleWithSubselectEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleWithSubselectEnum.html) |  |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| cascade | string |  |  |
| oneToMany | [JaxbHbmOneToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmOneToManyCollectionElementType.html) |  |  |
| inverse | boolean | required |  |
| orderBy | string |  |  |
| indexManyToMany | [JaxbHbmIndexManyToManyType](https://api.fluig.com/old/json_JaxbHbmIndexManyToManyType.html) |  |  |
| compositeMapKey | [JaxbHbmMapKeyCompositeType](https://api.fluig.com/old/json_JaxbHbmMapKeyCompositeType.html) |  |  |
| node | string |  |  |
| comment | string |  |  |
| manyToMany | [JaxbHbmManyToManyCollectionElementType](https://api.fluig.com/old/json_JaxbHbmManyToManyCollectionElementType.html) |  |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |  |
| lazy | [JaxbHbmLazyWithExtraEnum](https://api.fluig.com/old/json_JaxbHbmLazyWithExtraEnum.html) |  |  |
| access | string |  |  |
| compositeElement | [JaxbHbmCompositeCollectionElementType](https://api.fluig.com/old/json_JaxbHbmCompositeCollectionElementType.html) |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |  |
| embedXml | boolean |  |  |
| name | string |  |  |
| mapKey | [JaxbHbmMapKeyBasicType](https://api.fluig.com/old/json_JaxbHbmMapKeyBasicType.html) |  |  |
| catalog | string |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| outerJoin | [JaxbHbmOuterJoinEnum](https://api.fluig.com/old/json_JaxbHbmOuterJoinEnum.html) |  |  |
| where | string |  |  |
| optimisticLock | boolean | required |  |
| sort | string |  |  |
| element | [JaxbHbmBasicCollectionElementType](https://api.fluig.com/old/json_JaxbHbmBasicCollectionElementType.html) |  |  |
| check | string |  |  |
| index | [JaxbHbmIndexType](https://api.fluig.com/old/json_JaxbHbmIndexType.html) |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
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
  "mutable" : true,
  "batchSize" : 12345,
  "table" : "...",
  "subselect" : "...",
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
  "cache" : {
    "region" : "...",
    "usage" : "TRANSACTIONAL",
    "include" : "NON_LAZY"
  },
  "compositeIndex" : {
    "attributes" : [ {
      "toolingHints" : [ { }, { } ]
    }, {
      "toolingHints" : [ { }, { } ]
    } ],
    "clazz" : "..."
  },
  "collectionType" : "...",
  "subselectAttribute" : "...",
  "sqlDeleteAll" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "indexManyToAny" : {
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
    "idType" : "...",
    "metaType" : "..."
  },
  "persister" : "...",
  "schema" : "...",
  "mapKeyManyToMany" : {
    "columnOrFormula" : [ { }, { } ],
    "foreignKey" : "...",
    "columnAttribute" : "...",
    "entityName" : "...",
    "clazz" : "...",
    "formulaAttribute" : "..."
  },
  "synchronize" : [ {
    "table" : "..."
  }, {
    "table" : "..."
  } ],
  "fetch" : "JOIN",
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "cascade" : "...",
  "oneToMany" : {
    "embedXml" : true,
    "node" : "...",
    "entityName" : "...",
    "notFound" : "IGNORE",
    "clazz" : "..."
  },
  "inverse" : true,
  "orderBy" : "...",
  "indexManyToMany" : {
    "clazz" : "...",
    "entityName" : "...",
    "columnAttribute" : "...",
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
    "foreignKey" : "..."
  },
  "compositeMapKey" : {
    "clazz" : "...",
    "attributes" : [ {
      "toolingHints" : [ { }, { } ]
    }, {
      "toolingHints" : [ { }, { } ]
    } ]
  },
  "node" : "...",
  "comment" : "...",
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
    "outerJoin" : "AUTO",
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
  "lazy" : "TRUE",
  "access" : "...",
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
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "loader" : {
    "queryRef" : "..."
  },
  "embedXml" : true,
  "name" : "...",
  "mapKey" : {
    "typeAttribute" : "...",
    "node" : "...",
    "columnOrFormula" : [ { }, { } ],
    "type" : {
      "name" : "...",
      "configParameters" : [ { }, { } ]
    },
    "columnAttribute" : "...",
    "formulaAttribute" : "...",
    "length" : 12345
  },
  "catalog" : "...",
  "sqlInsert" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "outerJoin" : "AUTO",
  "where" : "...",
  "optimisticLock" : true,
  "sort" : "...",
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
  "check" : "...",
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
