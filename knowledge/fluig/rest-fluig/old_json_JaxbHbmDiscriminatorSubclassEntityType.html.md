---
content_hash: c289162818466ecc792520b78b083141d40d5a2cd512c7c2bf98380808c7a49b
fetched_at: '2026-11-03T14:34:37.375868+00:00'
page_id: json_JaxbHbmDiscriminatorSubclassEntityType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmDiscriminatorSubclassEntityType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmDiscriminatorSubclassEntityType.html
version: 1
---

# JaxbHbmDiscriminatorSubclassEntityType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| sqlQuery | array of [JaxbHbmNamedNativeQueryType](https://api.fluig.com/old/json_JaxbHbmNamedNativeQueryType.html) |  |
| fetchProfile | array of [JaxbHbmFetchProfileType](https://api.fluig.com/old/json_JaxbHbmFetchProfileType.html) |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| subclass | array of [JaxbHbmDiscriminatorSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmDiscriminatorSubclassEntityType.html) |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |
| join | array of [JaxbHbmSecondaryTableType](https://api.fluig.com/old/json_JaxbHbmSecondaryTableType.html) |  |
| resultset | array of [JaxbHbmResultSetMappingType](https://api.fluig.com/old/json_JaxbHbmResultSetMappingType.html) |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| discriminatorValue | string |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| query | array of [JaxbHbmNamedQueryType](https://api.fluig.com/old/json_JaxbHbmNamedQueryType.html) |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |
| Properties inherited from [JaxbHbmSubclassEntityBaseDefinition](https://api.fluig.com/old/json_JaxbHbmSubclassEntityBaseDefinition.html) | | |
| extends | string |  |
| Properties inherited from [JaxbHbmEntityBaseDefinition](https://api.fluig.com/old/json_JaxbHbmEntityBaseDefinition.html) | | |
| lazy | boolean |  |
| name | string |  |
| dynamicInsert | boolean |  |
| proxy | string |  |
| batchSize | number |  |
| node | string |  |
| entityName | string |  |
| persister | string |  |
| abstract | boolean |  |
| selectBeforeUpdate | boolean |  |
| dynamicUpdate | boolean |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
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
    "flushMode" : "ALWAYS"
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
    "flushMode" : "ALWAYS"
  } ],
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
      "style" : "SELECT"
    }, {
      "association" : "...",
      "entity" : "...",
      "style" : "JOIN"
    } ],
    "name" : "..."
  } ],
  "sqlUpdate" : {
    "callable" : true,
    "value" : "...",
    "check" : "PARAM"
  },
  "subclass" : [ {
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
      "flushMode" : "AUTO"
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
      "flushMode" : "ALWAYS"
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
      "check" : "NONE"
    },
    "discriminatorValue" : "...",
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
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
      "flushMode" : "COMMIT",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "REFRESH",
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
      "flushMode" : "MANUAL"
    }, {
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
  } ],
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
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "fetch" : "SELECT",
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
  }, {
    "schema" : "...",
    "attributes" : [ { }, { } ],
    "subselectAttribute" : "...",
    "comment" : "...",
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "fetch" : "JOIN",
    "subselect" : "...",
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
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
    "check" : "NONE"
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
    "flushMode" : "AUTO",
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
}
```
