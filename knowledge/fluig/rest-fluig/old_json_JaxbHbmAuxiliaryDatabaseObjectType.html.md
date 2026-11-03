---
content_hash: e97b6393b11ce661dd06d3c14955945b9b633bc8ee1200b9d017b6cb5688172d
fetched_at: '2026-11-03T14:34:37.279477+00:00'
page_id: json_JaxbHbmAuxiliaryDatabaseObjectType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmAuxiliaryDatabaseObjectType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmAuxiliaryDatabaseObjectType.html
version: 1
---

# JaxbHbmAuxiliaryDatabaseObjectType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| dialectScope | array of [JaxbHbmDialectScopeType](https://api.fluig.com/old/json_JaxbHbmDialectScopeType.html) |  |
| definition | [JaxbHbmDefinition](https://api.fluig.com/old/json_JaxbHbmDefinition.html) |  |
| drop | string |  |
| create | string |  |

Example

```
{
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
}
```
