---
content_hash: dfba3da4c535e8eb6a691489b4433ff8864a06dfac6b8c0770a5f763682fd86e
fetched_at: '2026-11-03T14:34:37.710079+00:00'
page_id: json_JaxbHbmUnionSubclassEntityType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmUnionSubclassEntityType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmUnionSubclassEntityType.html
version: 1
---

# JaxbHbmUnionSubclassEntityType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| resultset | array of [JaxbHbmResultSetMappingType](https://api.fluig.com/old/json_JaxbHbmResultSetMappingType.html) |  |
| comment | string |  |
| query | array of [JaxbHbmNamedQueryType](https://api.fluig.com/old/json_JaxbHbmNamedQueryType.html) |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| fetchProfile | array of [JaxbHbmFetchProfileType](https://api.fluig.com/old/json_JaxbHbmFetchProfileType.html) |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |
| check | string |  |
| synchronize | array of [JaxbHbmSynchronizeType](https://api.fluig.com/old/json_JaxbHbmSynchronizeType.html) |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |
| table | string |  |
| subselect | string |  |
| subselectAttribute | string |  |
| sqlQuery | array of [JaxbHbmNamedNativeQueryType](https://api.fluig.com/old/json_JaxbHbmNamedNativeQueryType.html) |  |
| schema | string |  |
| tuplizer | array of [JaxbHbmTuplizerType](https://api.fluig.com/old/json_JaxbHbmTuplizerType.html) |  |
| loader | [JaxbHbmLoaderType](https://api.fluig.com/old/json_JaxbHbmLoaderType.html) |  |
| unionSubclass | array of [JaxbHbmUnionSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmUnionSubclassEntityType.html) |  |
| catalog | string |  |
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
    "cacheMode" : "NORMAL",
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
    "check" : "NONE"
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
      "style" : "SELECT"
    } ],
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
    "cacheMode" : "PUT",
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
    "flushMode" : "COMMIT"
  } ],
  "schema" : "...",
  "tuplizer" : [ {
    "clazz" : "...",
    "entityMode" : "MAP"
  }, {
    "clazz" : "...",
    "entityMode" : "POJO"
  } ],
  "loader" : {
    "queryRef" : "..."
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
      "flushMode" : "COMMIT",
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
      "cacheMode" : "NORMAL",
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
      "cacheMode" : "NORMAL",
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
      "entityMode" : "POJO"
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
      "cacheMode" : "REFRESH",
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
      "cacheMode" : "GET",
      "readOnly" : true
    } ],
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
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
      "check" : "NONE"
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
      "cacheMode" : "REFRESH",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "COMMIT"
    } ],
    "schema" : "...",
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
}
```
