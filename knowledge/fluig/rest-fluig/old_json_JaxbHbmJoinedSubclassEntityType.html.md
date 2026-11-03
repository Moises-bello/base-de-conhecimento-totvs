---
content_hash: 5408212dfee23d3fa00669116b8ea550d7c165e95247920fd3e3106a495bb096
fetched_at: '2026-11-03T14:34:37.460381+00:00'
page_id: json_JaxbHbmJoinedSubclassEntityType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmJoinedSubclassEntityType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmJoinedSubclassEntityType.html
version: 1
---

# JaxbHbmJoinedSubclassEntityType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| sqlQuery | array of [JaxbHbmNamedNativeQueryType](https://api.fluig.com/old/json_JaxbHbmNamedNativeQueryType.html) |  |
| table | string |  |
| catalog | string |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| fetchProfile | array of [JaxbHbmFetchProfileType](https://api.fluig.com/old/json_JaxbHbmFetchProfileType.html) |  |
| subselect | string |  |
| schema | string |  |
| query | array of [JaxbHbmNamedQueryType](https://api.fluig.com/old/json_JaxbHbmNamedQueryType.html) |  |
| resultset | array of [JaxbHbmResultSetMappingType](https://api.fluig.com/old/json_JaxbHbmResultSetMappingType.html) |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |
| comment | string |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |
| discriminatorValue | string |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |
| subselectAttribute | string |  |
| joinedSubclass | array of [JaxbHbmJoinedSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmJoinedSubclassEntityType.html) |  |
| check | string |  |
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
    "cacheMode" : "IGNORE",
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
    "flushMode" : "AUTO"
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
    "check" : "NONE"
  },
  "attributes" : [ { }, { } ],
  "sqlDelete" : {
    "callable" : true,
    "value" : "...",
    "check" : "NONE"
  },
  "fetchProfile" : [ {
    "fetch" : [ {
      "association" : "...",
      "entity" : "...",
      "style" : "SELECT"
    }, {
      "association" : "...",
      "entity" : "...",
      "style" : "SELECT"
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
    "cacheMode" : "GET",
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
    "cacheMode" : "PUT",
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
  "subselectAttribute" : "...",
  "joinedSubclass" : [ {
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
      "flushMode" : "ALWAYS"
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
    "table" : "...",
    "catalog" : "...",
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
      "flushMode" : "ALWAYS",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "REFRESH",
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
      "entityMode" : "MAP"
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
      "cacheMode" : "IGNORE",
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
      "flushMode" : "COMMIT"
    } ],
    "table" : "...",
    "catalog" : "...",
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
    },
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "NONE"
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
      "flushMode" : "AUTO",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
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
  } ],
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
}
```
