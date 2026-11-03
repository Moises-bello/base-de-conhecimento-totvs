---
content_hash: 829718027dc4b64781c6475716f5eb3efd86a2b41874c55062fa442499926b9c
fetched_at: '2026-11-03T14:34:37.537124+00:00'
page_id: json_JaxbHbmMultiTenancyType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmMultiTenancyType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmMultiTenancyType.html
version: 1
---

# JaxbHbmMultiTenancyType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| columnAttribute | string |  |  |
| shared | boolean | required |  |
| bindAsParam | boolean | required |  |
| formula | string |  |  |
| column | [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |  |
| formulaAttribute | string |  |  |

Example

```
{
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
}
```
