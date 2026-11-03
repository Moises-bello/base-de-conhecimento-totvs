---
content_hash: f5fc9c190196963658ce10741cee81fd245d4e4ab41bbc10284f2fc083e4e1b9
fetched_at: '2026-11-03T14:34:37.475233+00:00'
page_id: json_JaxbHbmListIndexType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmListIndexType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmListIndexType.html
version: 1
---

# JaxbHbmListIndexType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| column | [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| base | string |  |
| columnAttribute | string |  |

Example

```
{
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
  "base" : "...",
  "columnAttribute" : "..."
}
```
