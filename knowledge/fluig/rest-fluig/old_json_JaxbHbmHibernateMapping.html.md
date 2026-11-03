---
content_hash: b0788efdd4b43e160e488b72fbc0bc2db8f21fc2219f71b06345a6f2f50ae756
fetched_at: '2026-11-03T14:34:37.425322+00:00'
page_id: json_JaxbHbmHibernateMapping
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmHibernateMapping Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmHibernateMapping.html
version: 1
---

# JaxbHbmHibernateMapping Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| resultset | array of [JaxbHbmResultSetMappingType](https://api.fluig.com/old/json_JaxbHbmResultSetMappingType.html) |  |  |
| sqlQuery | array of [JaxbHbmNamedNativeQueryType](https://api.fluig.com/old/json_JaxbHbmNamedNativeQueryType.html) |  |  |
| defaultCascade | string |  |  |
| autoImport | boolean | required |  |
| databaseObject | array of [JaxbHbmAuxiliaryDatabaseObjectType](https://api.fluig.com/old/json_JaxbHbmAuxiliaryDatabaseObjectType.html) |  |  |
| unionSubclass | array of [JaxbHbmUnionSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmUnionSubclassEntityType.html) |  |  |
| query | array of [JaxbHbmNamedQueryType](https://api.fluig.com/old/json_JaxbHbmNamedQueryType.html) |  |  |
| schema | string |  |  |
| filterDef | array of [JaxbHbmFilterDefinitionType](https://api.fluig.com/old/json_JaxbHbmFilterDefinitionType.html) |  |  |
| typedef | array of [JaxbHbmTypeDefinitionType](https://api.fluig.com/old/json_JaxbHbmTypeDefinitionType.html) |  |  |
| import | array of [JaxbHbmClassRenameType](https://api.fluig.com/old/json_JaxbHbmClassRenameType.html) |  |  |
| clazz | array of [JaxbHbmRootEntityType](https://api.fluig.com/old/json_JaxbHbmRootEntityType.html) |  |  |
| fetchProfile | array of [JaxbHbmFetchProfileType](https://api.fluig.com/old/json_JaxbHbmFetchProfileType.html) |  |  |
| joinedSubclass | array of [JaxbHbmJoinedSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmJoinedSubclassEntityType.html) |  |  |
| package | string |  |  |
| identifierGenerator | array of [JaxbHbmIdentifierGeneratorDefinitionType](https://api.fluig.com/old/json_JaxbHbmIdentifierGeneratorDefinitionType.html) |  |  |
| defaultLazy | boolean | required |  |
| subclass | array of [JaxbHbmDiscriminatorSubclassEntityType](https://api.fluig.com/old/json_JaxbHbmDiscriminatorSubclassEntityType.html) |  |  |
| catalog | string |  |  |
| defaultAccess | string |  |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

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
    "cacheMode" : "REFRESH",
    "fetchSize" : 12345,
    "resultsetRef" : "...",
    "content" : [ { }, { } ],
    "name" : "...",
    "flushMode" : "ALWAYS"
  } ],
  "defaultCascade" : "...",
  "autoImport" : true,
  "databaseObject" : [ {
    "dialectScope" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ],
    "definition" : {
      "clazz" : "..."
    },
    "drop" : "...",
    "create" : "..."
  }, {
    "dialectScope" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ],
    "definition" : {
      "clazz" : "..."
    },
    "drop" : "...",
    "create" : "..."
  } ],
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
      "flushMode" : "COMMIT",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "PUT",
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
      "cacheMode" : "REFRESH",
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
      "cacheMode" : "GET",
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
      "cacheMode" : "PUT",
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
      "cacheMode" : "IGNORE",
      "fetchSize" : 12345,
      "resultsetRef" : "...",
      "content" : [ { }, { } ],
      "name" : "...",
      "flushMode" : "AUTO"
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
    "cacheMode" : "PUT",
    "readOnly" : true
  } ],
  "schema" : "...",
  "filterDef" : [ {
    "content" : [ { }, { } ],
    "name" : "...",
    "condition" : "..."
  }, {
    "content" : [ { }, { } ],
    "name" : "...",
    "condition" : "..."
  } ],
  "typedef" : [ {
    "name" : "...",
    "clazz" : "...",
    "configParameters" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ]
  }, {
    "name" : "...",
    "clazz" : "...",
    "configParameters" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ]
  } ],
  "import" : [ {
    "rename" : "...",
    "clazz" : "..."
  }, {
    "rename" : "...",
    "clazz" : "..."
  } ],
  "clazz" : [ {
    "rowid" : "...",
    "discriminatorValue" : "...",
    "subclass" : [ {
      "sqlQuery" : [ { }, { } ],
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "subclass" : [ { }, { } ],
      "synchronize" : [ { }, { } ],
      "join" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "sqlInsert" : { },
      "discriminatorValue" : "...",
      "sqlDelete" : { },
      "query" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    }, {
      "sqlQuery" : [ { }, { } ],
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "subclass" : [ { }, { } ],
      "synchronize" : [ { }, { } ],
      "join" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "sqlInsert" : { },
      "discriminatorValue" : "...",
      "sqlDelete" : { },
      "query" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    } ],
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "MAP"
    }, {
      "clazz" : "...",
      "entityMode" : "MAP"
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
      "flushMode" : "COMMIT",
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
      "cacheMode" : "GET",
      "readOnly" : true
    } ],
    "id" : {
      "unsavedValue" : "...",
      "length" : 12345,
      "name" : "...",
      "access" : "...",
      "column" : [ { }, { } ],
      "type" : { },
      "generator" : { },
      "columnAttribute" : "...",
      "node" : "...",
      "typeAttribute" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "multiTenancy" : {
      "columnAttribute" : "...",
      "shared" : true,
      "bindAsParam" : true,
      "formula" : "...",
      "column" : { },
      "formulaAttribute" : "..."
    },
    "joinedSubclass" : [ {
      "sqlQuery" : [ { }, { } ],
      "table" : "...",
      "catalog" : "...",
      "sqlInsert" : { },
      "sqlUpdate" : { },
      "attributes" : [ { }, { } ],
      "sqlDelete" : { },
      "fetchProfile" : [ { }, { } ],
      "subselect" : "...",
      "schema" : "...",
      "query" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "comment" : "...",
      "synchronize" : [ { }, { } ],
      "discriminatorValue" : "...",
      "loader" : { },
      "key" : { },
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
      "toolingHints" : [ { }, { } ]
    }, {
      "sqlQuery" : [ { }, { } ],
      "table" : "...",
      "catalog" : "...",
      "sqlInsert" : { },
      "sqlUpdate" : { },
      "attributes" : [ { }, { } ],
      "sqlDelete" : { },
      "fetchProfile" : [ { }, { } ],
      "subselect" : "...",
      "schema" : "...",
      "query" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "comment" : "...",
      "synchronize" : [ { }, { } ],
      "discriminatorValue" : "...",
      "loader" : { },
      "key" : { },
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
      "toolingHints" : [ { }, { } ]
    } ],
    "catalog" : "...",
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "optimisticLock" : "DIRTY",
    "timestamp" : {
      "source" : "DB",
      "unsavedValue" : "NULL",
      "columnAttribute" : "...",
      "name" : "...",
      "generated" : "ALWAYS",
      "access" : "...",
      "node" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "compositeId" : {
      "generator" : { },
      "access" : "...",
      "node" : "...",
      "unsavedValue" : "UNDEFINED",
      "clazz" : "...",
      "keyPropertyOrKeyManyToOne" : [ { }, { } ],
      "mapped" : true,
      "name" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "discriminator" : {
      "length" : 12345,
      "force" : true,
      "formulaAttribute" : "...",
      "columnAttribute" : "...",
      "insert" : true,
      "type" : "...",
      "notNull" : true,
      "column" : { },
      "formula" : "..."
    },
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
    "attributes" : [ { }, { } ],
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "unionSubclass" : [ {
      "resultset" : [ { }, { } ],
      "comment" : "...",
      "query" : [ { }, { } ],
      "sqlDelete" : { },
      "sqlInsert" : { },
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "check" : "...",
      "synchronize" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "table" : "...",
      "subselect" : "...",
      "subselectAttribute" : "...",
      "sqlQuery" : [ { }, { } ],
      "schema" : "...",
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    }, {
      "resultset" : [ { }, { } ],
      "comment" : "...",
      "query" : [ { }, { } ],
      "sqlDelete" : { },
      "sqlInsert" : { },
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "check" : "...",
      "synchronize" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "table" : "...",
      "subselect" : "...",
      "subselectAttribute" : "...",
      "sqlQuery" : [ { }, { } ],
      "schema" : "...",
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    } ],
    "check" : "...",
    "sqlInsert" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
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
      "unsavedValue" : "NEGATIVE",
      "column" : [ { }, { } ],
      "type" : "...",
      "columnAttribute" : "...",
      "name" : "...",
      "generated" : "ALWAYS",
      "access" : "...",
      "node" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "cache" : {
      "region" : "...",
      "usage" : "READ_WRITE",
      "include" : "NON_LAZY"
    },
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
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
      "flushMode" : "ALWAYS"
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
  }, {
    "rowid" : "...",
    "discriminatorValue" : "...",
    "subclass" : [ {
      "sqlQuery" : [ { }, { } ],
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "subclass" : [ { }, { } ],
      "synchronize" : [ { }, { } ],
      "join" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "sqlInsert" : { },
      "discriminatorValue" : "...",
      "sqlDelete" : { },
      "query" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    }, {
      "sqlQuery" : [ { }, { } ],
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "subclass" : [ { }, { } ],
      "synchronize" : [ { }, { } ],
      "join" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "sqlInsert" : { },
      "discriminatorValue" : "...",
      "sqlDelete" : { },
      "query" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    } ],
    "tuplizer" : [ {
      "clazz" : "...",
      "entityMode" : "POJO"
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
      "flushMode" : "MANUAL",
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
      "column" : [ { }, { } ],
      "type" : { },
      "generator" : { },
      "columnAttribute" : "...",
      "node" : "...",
      "typeAttribute" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "multiTenancy" : {
      "columnAttribute" : "...",
      "shared" : true,
      "bindAsParam" : true,
      "formula" : "...",
      "column" : { },
      "formulaAttribute" : "..."
    },
    "joinedSubclass" : [ {
      "sqlQuery" : [ { }, { } ],
      "table" : "...",
      "catalog" : "...",
      "sqlInsert" : { },
      "sqlUpdate" : { },
      "attributes" : [ { }, { } ],
      "sqlDelete" : { },
      "fetchProfile" : [ { }, { } ],
      "subselect" : "...",
      "schema" : "...",
      "query" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "comment" : "...",
      "synchronize" : [ { }, { } ],
      "discriminatorValue" : "...",
      "loader" : { },
      "key" : { },
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
      "toolingHints" : [ { }, { } ]
    }, {
      "sqlQuery" : [ { }, { } ],
      "table" : "...",
      "catalog" : "...",
      "sqlInsert" : { },
      "sqlUpdate" : { },
      "attributes" : [ { }, { } ],
      "sqlDelete" : { },
      "fetchProfile" : [ { }, { } ],
      "subselect" : "...",
      "schema" : "...",
      "query" : [ { }, { } ],
      "resultset" : [ { }, { } ],
      "tuplizer" : [ { }, { } ],
      "comment" : "...",
      "synchronize" : [ { }, { } ],
      "discriminatorValue" : "...",
      "loader" : { },
      "key" : { },
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
      "toolingHints" : [ { }, { } ]
    } ],
    "catalog" : "...",
    "sqlDelete" : {
      "callable" : true,
      "value" : "...",
      "check" : "PARAM"
    },
    "optimisticLock" : "ALL",
    "timestamp" : {
      "source" : "VM",
      "unsavedValue" : "NULL",
      "columnAttribute" : "...",
      "name" : "...",
      "generated" : "INSERT",
      "access" : "...",
      "node" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "compositeId" : {
      "generator" : { },
      "access" : "...",
      "node" : "...",
      "unsavedValue" : "NONE",
      "clazz" : "...",
      "keyPropertyOrKeyManyToOne" : [ { }, { } ],
      "mapped" : true,
      "name" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "discriminator" : {
      "length" : 12345,
      "force" : true,
      "formulaAttribute" : "...",
      "columnAttribute" : "...",
      "insert" : true,
      "type" : "...",
      "notNull" : true,
      "column" : { },
      "formula" : "..."
    },
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
    "attributes" : [ { }, { } ],
    "sqlUpdate" : {
      "callable" : true,
      "value" : "...",
      "check" : "COUNT"
    },
    "unionSubclass" : [ {
      "resultset" : [ { }, { } ],
      "comment" : "...",
      "query" : [ { }, { } ],
      "sqlDelete" : { },
      "sqlInsert" : { },
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "check" : "...",
      "synchronize" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "table" : "...",
      "subselect" : "...",
      "subselectAttribute" : "...",
      "sqlQuery" : [ { }, { } ],
      "schema" : "...",
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
    }, {
      "resultset" : [ { }, { } ],
      "comment" : "...",
      "query" : [ { }, { } ],
      "sqlDelete" : { },
      "sqlInsert" : { },
      "fetchProfile" : [ { }, { } ],
      "sqlUpdate" : { },
      "check" : "...",
      "synchronize" : [ { }, { } ],
      "attributes" : [ { }, { } ],
      "table" : "...",
      "subselect" : "...",
      "subselectAttribute" : "...",
      "sqlQuery" : [ { }, { } ],
      "schema" : "...",
      "tuplizer" : [ { }, { } ],
      "loader" : { },
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
      "toolingHints" : [ { }, { } ]
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
      "unsavedValue" : "NULL",
      "column" : [ { }, { } ],
      "type" : "...",
      "columnAttribute" : "...",
      "name" : "...",
      "generated" : "NEVER",
      "access" : "...",
      "node" : "...",
      "toolingHints" : [ { }, { } ]
    },
    "cache" : {
      "region" : "...",
      "usage" : "NONSTRICT_READ_WRITE",
      "include" : "ALL"
    },
    "fetchProfile" : [ {
      "fetch" : [ { }, { } ],
      "name" : "..."
    }, {
      "fetch" : [ { }, { } ],
      "name" : "..."
    } ],
    "subselectAttribute" : "...",
    "table" : "...",
    "polymorphism" : "IMPLICIT",
    "subselect" : "...",
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
      "flushMode" : "AUTO"
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
  } ],
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
  "joinedSubclass" : [ {
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
      "flushMode" : "ALWAYS"
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
      "flushMode" : "ALWAYS",
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
      "cacheMode" : "REFRESH",
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
      "flushMode" : "AUTO"
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
      "check" : "COUNT"
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
  "package" : "...",
  "identifierGenerator" : [ {
    "clazz" : "...",
    "name" : "..."
  }, {
    "clazz" : "...",
    "name" : "..."
  } ],
  "defaultLazy" : true,
  "subclass" : [ {
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
      "cacheMode" : "GET",
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
      "cacheMode" : "GET",
      "readOnly" : true
    } ],
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
      "flushMode" : "AUTO",
      "cacheRegion" : "...",
      "timeout" : 12345,
      "fetchSize" : 12345,
      "cacheMode" : "IGNORE",
      "readOnly" : true
    } ],
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
  "defaultAccess" : "...",
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
