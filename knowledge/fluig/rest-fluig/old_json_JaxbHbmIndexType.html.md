---
content_hash: a203749d97afec9ed042997f986a586828c36ea91a5b77ad3686170d36e9e6a5
fetched_at: '2026-11-03T14:34:37.449271+00:00'
page_id: json_JaxbHbmIndexType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmIndexType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmIndexType.html
version: 1
---

# JaxbHbmIndexType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| length | number |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| type | string |  |
| columnAttribute | string |  |

Example

```
{
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
}
```
