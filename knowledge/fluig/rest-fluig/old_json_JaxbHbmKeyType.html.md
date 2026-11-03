---
content_hash: 02dc19c25c8d908403ced494970ab66adcdda577c94220c609bd6afabecae787
fetched_at: '2026-11-03T14:34:37.464194+00:00'
page_id: json_JaxbHbmKeyType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmKeyType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmKeyType.html
version: 1
---

# JaxbHbmKeyType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| onDelete | [JaxbHbmOnDeleteEnum](https://api.fluig.com/old/json_JaxbHbmOnDeleteEnum.html) |  |
| foreignKey | string |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| unique | boolean |  |
| columnAttribute | string |  |
| notNull | boolean |  |
| propertyRef | string |  |
| update | boolean |  |

Example

```
{
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
}
```
