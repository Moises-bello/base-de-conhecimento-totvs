---
content_hash: 127d0a98ff785c1c17c2442a083ee1e290541f7ff93818ca345660b609aebd2e
fetched_at: '2026-11-03T14:34:37.642455+00:00'
page_id: json_JaxbHbmSecondaryTableType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmSecondaryTableType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmSecondaryTableType.html
version: 1
---

# JaxbHbmSecondaryTableType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| schema | string |  |  |
| attributes | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| subselectAttribute | string |  |  |
| comment | string |  |  |
| sqlInsert | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| sqlDelete | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| fetch | [JaxbHbmFetchStyleEnum](https://api.fluig.com/old/json_JaxbHbmFetchStyleEnum.html) |  |  |
| subselect | string |  |  |
| sqlUpdate | [JaxbHbmCustomSqlDmlType](https://api.fluig.com/old/json_JaxbHbmCustomSqlDmlType.html) |  |  |
| inverse | boolean | required |  |
| catalog | string |  |  |
| optional | boolean | required |  |
| key | [JaxbHbmKeyType](https://api.fluig.com/old/json_JaxbHbmKeyType.html) |  |  |
| table | string |  |  |

Example

```
{
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
  "table" : "..."
}
```
