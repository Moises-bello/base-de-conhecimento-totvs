---
content_hash: b193e5eab96728c5d193ce5005952c7d6ca66f8da555772ed3ce225b1a743edd
fetched_at: '2026-11-03T14:34:37.635955+00:00'
page_id: json_JaxbHbmRootEntityType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmRootEntityType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmRootEntityType.html
version: 1
---

# JaxbHbmRootEntityType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| rowid | string |  |  |
| discriminatorValue | string |  |  |
| subclass | array of [JaxbHbmDiscriminatorSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmDiscriminatorSubclassEntityType.html) |  |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |  |
| mutable | boolean | required |  |
| filter | array of [JaxbHbmFilterType](https://api.fluig.com/old/json_JaxbHbmFilterType.html) |  |  |
| query | array of [JaxbHbmNamedQueryType](https://api.fluig.com/old/json_JaxbHbmNamedQueryType.html) |  |  |
| id | [JaxbHbmSimpleIdType](https://api.fluig.com/old/json_JaxbHbmSimpleIdType.html) |  |  |
| multiTenancy | [JaxbHbmMultiTenancyType](https://api.fluig.com/old/json_JaxbHbmMultiTenancyType.html) |  |  |
| joinedSubclass | array of [JaxbHbmJoinedSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmJoinedSubclassEntityType.html) |  |  |
| catalog | string |  |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| optimisticLock | [OptimisticLockStyle](https://api.fluig.com/old/json_OptimisticLockStyle.html) |  |  |
| timestamp | [JaxbHbmTimestampAttributeType](https://api.fluig.com/old/json_JaxbHbmTimestampAttributeType.html) |  |  |
| compositeId | [JaxbHbmCompositeIdType](https://api.fluig.com/old/json_JaxbHbmCompositeIdType.html) |  |  |
| discriminator | [JaxbHbmEntityDiscriminatorType](https://api.fluig.com/old/json_JaxbHbmEntityDiscriminatorType.html) |  |  |
| join | array of [JaxbHbmSecondaryTableType](https://api.fluig.com/old/json_JaxbHbmSecondaryTableType.html) |  |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| unionSubclass | array of [JaxbHbmUnionSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmUnionSubclassEntityType.html) |  |  |
| check | string |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |  |
| resultset | array of [JaxbHbmResultSetMappingType](https://api.fluig.com/old/json_JaxbHbmResultSetMappingType.html) |  |  |
| where | string |  |  |
| naturalId | [JaxbHbmNaturalIdType](https://api.fluig.com/old/json_JaxbHbmNaturalIdType.html) |  |  |
| version | [JaxbHbmVersionAttributeType](https://api.fluig.com/old/json_JaxbHbmVersionAttributeType.html) |  |  |
| cache | [JaxbHbmCacheType](https://api.fluig.com/old/json_JaxbHbmCacheType.html) |  |  |
| fetchProfile | array of [JaxbHbmFetchProfileType](https://api.fluig.com/old/json_JaxbHbmFetchProfileType.html) |  |  |
| subselectAttribute | string |  |  |
| table | string |  |  |
| polymorphism | [JaxbHbmPolymorphismEnum](https://api.fluig.com/old/json_JaxbHbmPolymorphismEnum.html) |  |  |
| subselect | string |  |  |
| sqlQuery | array of [JaxbHbmNamedNativeQueryType](https://api.fluig.com/old/json_JaxbHbmNamedNativeQueryType.html) |  |  |
| naturalIdCache | [JaxbHbmNaturalIdCacheType](https://api.fluig.com/old/json_JaxbHbmNaturalIdCacheType.html) |  |  |
| comment | string |  |  |
| schema | string |  |  |
| Properties inherited from [JaxbHbmEntityBaseDefinition](https://api.fluig.com/old/json_JaxbHbmEntityBaseDefinition.html) | | | |
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
  "rowid" : "...",
  "discriminatorValue" : "...",
  "subclass" : [ {
    "sqlQuery" : [ {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "PUT",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "MANUAL"
    }, {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "IGNORE",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "MANUAL"
    } ],
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "subclass" : [ { }, { } ],
    "synchronize" : [ {
      "table" : "..."
    }, {
      "table" : "..."
    } ],
    "join" : [ {
      "schema" : "...",
      "attributes" : [ { }, { } ],
      "subselectAttribute" : "...",
      "comment" : "...",
      "sqlInsert" : { },
      "sqlDelete" : { },
      "fetch" : "JOIN",
      "subselect" : "...",
      "sqlUpdate" : { },
      "inverse" : true,
      "catalog" : "...",
      "optional" : true,
      "key" : { },
      "table" : "..."
    }, {
      "schema" : "...",
      "attributes" : [ { }, { } ],
      "subselectAttribute" : "...",
      "comment" : "...",
      "sqlInsert" : { },
      "sqlDelete" : { },
      "fetch" : "JOIN",
      "subselect" : "...",
      "sqlUpdate" : { },
      "inverse" : true,
      "catalog" : "...",
      "optional" : true,
      "key" : { },
      "table" : "..."
    } ],
    "resultset" : [ {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    }, {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    } ],
    "attributes" : [ { }, { } ],
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "discriminatorValue" : "...",
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "query" : [ {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "COMMIT",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "PUT",
      "readOnly" : true
    }, {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "MANUAL",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "PUT",
      "readOnly" : true
    } ],
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "POJO"
    }, {
      "clazz" : "...",
      "entityMode" : "MAP"
    } ],
    "loader" : {
      "queryRef" : "..."
    },
    "extends" : "...",
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
  }, {
    "sqlQuery" : [ {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "REFRESH",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "MANUAL"
    }, {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "REFRESH",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "MANUAL"
    } ],
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "subclass" : [ { }, { } ],
    "synchronize" : [ {
      "table" : "..."
    }, {
      "table" : "..."
    } ],
    "join" : [ {
      "schema" : "...",
      "attributes" : [ { }, { } ],
      "subselectAttribute" : "...",
      "comment" : "...",
      "sqlInsert" : { },
      "sqlDelete" : { },
      "fetch" : "SELECT",
      "subselect" : "...",
      "sqlUpdate" : { },
      "inverse" : true,
      "catalog" : "...",
      "optional" : true,
      "key" : { },
      "table" : "..."
    }, {
      "schema" : "...",
      "attributes" : [ { }, { } ],
      "subselectAttribute" : "...",
      "comment" : "...",
      "sqlInsert" : { },
      "sqlDelete" : { },
      "fetch" : "SELECT",
      "subselect" : "...",
      "sqlUpdate" : { },
      "inverse" : true,
      "catalog" : "...",
      "optional" : true,
      "key" : { },
      "table" : "..."
    } ],
    "resultset" : [ {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    }, {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    } ],
    "attributes" : [ { }, { } ],
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "discriminatorValue" : "...",
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "query" : [ {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "COMMIT",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
      "readOnly" : true
    }, {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "MANUAL",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
      "readOnly" : true
    } ],
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "POJO"
    }, {
      "clazz" : "...",
      "entityMode" : "POJO"
    } ],
    "loader" : {
      "queryRef" : "..."
    },
    "extends" : "...",
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
  } ],
  "tuplizer" : [ {
    "clazz" : "...",
    "entityMode" : "MAP"
  }, {
    "clazz" : "...",
    "entityMode" : "POJO"
  } ],
  "mutable" : true,
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
  "query" : [ {
    "content" : [ { }, { } ],
    "cacheable" : true,
    "name" : "...",
    "comment" : "...",
    "flushMode" : "ALWAYS",
    "cacheRegion" : "...",
    "timeout" : 12345,
    "fetchSize" : 12345,
    "cacheMode" : "PUT",
    "readOnly" : true
  }, {
    "content" : [ { }, { } ],
    "cacheable" : true,
    "name" : "...",
    "comment" : "...",
    "flushMode" : "COMMIT",
    "cacheRegion" : "...",
    "timeout" : 12345,
    "fetchSize" : 12345,
    "cacheMode" : "GET",
    "readOnly" : true
  } ],
  "id" : {
    "unsavedValue" : "...",
    "length" : 12345,
    "name" : "...",
    "access" : "...",
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
    "type" : {
      "name" : "...",
      "configParameters" : [ { }, { } ]
    },
    "generator" : {
      "clazz" : "...",
      "configParameters" : [ { }, { } ]
    },
    "columnAttribute" : "...",
    "node" : "...",
    "typeAttribute" : "...",
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
  "multiTenancy" : {
    "columnAttribute" : "...",
    "shared" : true,
    "bindAsParam" : true,
    "formula" : "...",
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
    "formulaAttribute" : "..."
  },
  "joinedSubclass" : [ {
    "sqlQuery" : [ {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "IGNORE",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "ALWAYS"
    }, {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "REFRESH",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "MANUAL"
    } ],
    "table" : "...",
    "catalog" : "...",
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "attributes" : [ { }, { } ],
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "subselect" : "...",
    "schema" : "...",
    "query" : [ {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "AUTO",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
      "readOnly" : true
    }, {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "COMMIT",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "GET",
      "readOnly" : true
    } ],
    "resultset" : [ {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    }, {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    } ],
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "MAP"
    }, {
      "clazz" : "...",
      "entityMode" : "POJO"
    } ],
    "comment" : "...",
    "synchronize" : [ {
      "table" : "..."
    }, {
      "table" : "..."
    } ],
    "discriminatorValue" : "...",
    "loader" : {
      "queryRef" : "..."
    },
    "key" : {
      "onDelete" : "NOACTION",
      "foreignKey" : "...",
      "column" : [ { }, { } ],
      "unique" : true,
      "columnAttribute" : "...",
      "notNull" : true,
      "propertyRef" : "...",
      "update" : true
    },
    "subselectAttribute" : "...",
    "joinedSubclass" : [ { }, { } ],
    "check" : "...",
    "extends" : "...",
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
  }, {
    "sqlQuery" : [ {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "NORMAL",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "COMMIT"
    }, {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "PUT",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "COMMIT"
    } ],
    "table" : "...",
    "catalog" : "...",
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "attributes" : [ { }, { } ],
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "subselect" : "...",
    "schema" : "...",
    "query" : [ {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "AUTO",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
      "readOnly" : true
    }, {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "MANUAL",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "REFRESH",
      "readOnly" : true
    } ],
    "resultset" : [ {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    }, {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    } ],
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "POJO"
    }, {
      "clazz" : "...",
      "entityMode" : "POJO"
    } ],
    "comment" : "...",
    "synchronize" : [ {
      "table" : "..."
    }, {
      "table" : "..."
    } ],
    "discriminatorValue" : "...",
    "loader" : {
      "queryRef" : "..."
    },
    "key" : {
      "onDelete" : "CASCADE",
      "foreignKey" : "...",
      "column" : [ { }, { } ],
      "unique" : true,
      "columnAttribute" : "...",
      "notNull" : true,
      "propertyRef" : "...",
      "update" : true
    },
    "subselectAttribute" : "...",
    "joinedSubclass" : [ { }, { } ],
    "check" : "...",
    "extends" : "...",
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
  } ],
  "catalog" : "...",
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "optimisticLock" : "NONE",
  "timestamp" : {
    "source" : "DB",
    "unsavedValue" : "NULL",
    "columnAttribute" : "...",
    "name" : "...",
    "generated" : "NEVER",
    "access" : "...",
    "node" : "...",
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
  "compositeId" : {
    "generator" : {
      "clazz" : "...",
      "configParameters" : [ { }, { } ]
    },
    "access" : "...",
    "node" : "...",
    "unsavedValue" : "UNDEFINED",
    "clazz" : "...",
    "keyPropertyOrKeyManyToOne" : [ {
      "toolingHints" : [ { }, { } ]
    }, {
      "toolingHints" : [ { }, { } ]
    } ],
    "mapped" : true,
    "name" : "...",
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
  "discriminator" : {
    "length" : 12345,
    "force" : true,
    "formulaAttribute" : "...",
    "columnAttribute" : "...",
    "insert" : true,
    "type" : "...",
    "notNull" : true,
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
    "formula" : "..."
  },
  "join" : [ {
    "schema" : "...",
    "attributes" : [ { }, { } ],
    "subselectAttribute" : "...",
    "comment" : "...",
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
    "fetch" : "JOIN",
    "subselect" : "...",
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "inverse" : true,
    "catalog" : "...",
    "optional" : true,
    "key" : {
      "onDelete" : "CASCADE",
      "foreignKey" : "...",
      "column" : [ { }, { } ],
      "unique" : true,
      "columnAttribute" : "...",
      "notNull" : true,
      "propertyRef" : "...",
      "update" : true
    },
    "table" : "..."
  }, {
    "schema" : "...",
    "attributes" : [ { }, { } ],
    "subselectAttribute" : "...",
    "comment" : "...",
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "fetch" : "JOIN",
    "subselect" : "...",
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "inverse" : true,
    "catalog" : "...",
    "optional" : true,
    "key" : {
      "onDelete" : "NOACTION",
      "foreignKey" : "...",
      "column" : [ { }, { } ],
      "unique" : true,
      "columnAttribute" : "...",
      "notNull" : true,
      "propertyRef" : "...",
      "update" : true
    },
    "table" : "..."
  } ],
  "attributes" : [ { }, { } ],
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "unionSubclass" : [ {
    "resultset" : [ {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    }, {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    } ],
    "comment" : "...",
    "query" : [ {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "MANUAL",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "NORMAL",
      "readOnly" : true
    }, {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "ALWAYS",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
      "readOnly" : true
    } ],
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "check" : "...",
    "synchronize" : [ {
      "table" : "..."
    }, {
      "table" : "..."
    } ],
    "attributes" : [ { }, { } ],
    "table" : "...",
    "subselect" : "...",
    "subselectAttribute" : "...",
    "sqlQuery" : [ {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "IGNORE",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "COMMIT"
    }, {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "GET",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "COMMIT"
    } ],
    "schema" : "...",
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "MAP"
    }, {
      "clazz" : "...",
      "entityMode" : "MAP"
    } ],
    "loader" : {
      "queryRef" : "..."
    },
    "unionSubclass" : [ { }, { } ],
    "catalog" : "...",
    "extends" : "...",
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
  }, {
    "resultset" : [ {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    }, {
      "name" : "...",
      "valueMappingSources" : [ { }, { } ]
    } ],
    "comment" : "...",
    "query" : [ {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "AUTO",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "NORMAL",
      "readOnly" : true
    }, {
      "content" : [ { }, { } ],
      "cacheable" : true,
      "name" : "...",
      "comment" : "...",
      "flushMode" : "AUTO",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "GET",
      "readOnly" : true
    } ],
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "check" : "...",
    "synchronize" : [ {
      "table" : "..."
    }, {
      "table" : "..."
    } ],
    "attributes" : [ { }, { } ],
    "table" : "...",
    "subselect" : "...",
    "subselectAttribute" : "...",
    "sqlQuery" : [ {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "GET",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "AUTO"
    }, {
      "cacheRegion" : "...",
      "readOnly" : true,
      "timeout" : 12345,
      "comment" : "...",
      "cacheable" : true,
      "callable" : true,
      "cacheMode" : "PUT",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "MANUAL"
    } ],
    "schema" : "...",
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "POJO"
    }, {
      "clazz" : "...",
      "entityMode" : "MAP"
    } ],
    "loader" : {
      "queryRef" : "..."
    },
    "unionSubclass" : [ { }, { } ],
    "catalog" : "...",
    "extends" : "...",
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
  } ],
  "check" : "...",
  "sqlInsert" : {
    "callable" : true,
    "value" : "...",
    "check" : "COUNT"
  },
  "loader" : {
    "queryRef" : "..."
  },
  "synchronize" : [ {
    "table" : "..."
  }, {
    "table" : "..."
  } ],
  "resultset" : [ {
    "name" : "...",
    "valueMappingSources" : [ { }, { } ]
  }, {
    "name" : "...",
    "valueMappingSources" : [ { }, { } ]
  } ],
  "where" : "...",
  "naturalId" : {
    "attributes" : [ { }, { } ],
    "mutable" : true
  },
  "version" : {
    "insert" : true,
    "unsavedValue" : "UNDEFINED",
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
    "columnAttribute" : "...",
    "name" : "...",
    "generated" : "ALWAYS",
    "access" : "...",
    "node" : "...",
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
  "cache" : {
    "region" : "...",
    "usage" : "READ_WRITE",
    "include" : "ALL"
  },
  "fetchProfile" : [ {
    "fetch" : [ {
      "association" : "...",
      "entity" : "...",
      "style" : "JOIN"
    }, {
      "association" : "...",
      "entity" : "...",
      "style" : "JOIN"
    } ],
    "name" : "..."
  }, {
    "fetch" : [ {
      "association" : "...",
      "entity" : "...",
      "style" : "JOIN"
    }, {
      "association" : "...",
      "entity" : "...",
      "style" : "JOIN"
    } ],
    "name" : "..."
  } ],
  "subselectAttribute" : "...",
  "table" : "...",
  "polymorphism" : "EXPLICIT",
  "subselect" : "...",
  "sqlQuery" : [ {
    "cacheRegion" : "...",
    "readOnly" : true,
    "timeout" : 12345,
    "comment" : "...",
    "cacheable" : true,
    "callable" : true,
    "cacheMode" : "PUT",
    "fetchSize" : 12345,
    "resultsetRef" : "...",
    "content" : [ { }, { } ],
    "name" : "...",
    "flushMode" : "COMMIT"
  }, {
    "cacheRegion" : "...",
    "readOnly" : true,
    "timeout" : 12345,
    "comment" : "...",
    "cacheable" : true,
    "callable" : true,
    "cacheMode" : "REFRESH",
    "fetchSize" : 12345,
    "resultsetRef" : "...",
    "content" : [ { }, { } ],
    "name" : "...",
    "flushMode" : "MANUAL"
  } ],
  "naturalIdCache" : {
    "region" : "..."
  },
  "comment" : "...",
  "schema" : "...",
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
