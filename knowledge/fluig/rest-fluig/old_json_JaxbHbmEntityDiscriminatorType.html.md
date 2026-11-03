---
content_hash: f65ac6ae717626640971109eb8b2b50e5c7528728f0fb450f817fba6c99f4435
fetched_at: '2026-11-03T14:34:37.389342+00:00'
page_id: json_JaxbHbmEntityDiscriminatorType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmEntityDiscriminatorType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmEntityDiscriminatorType.html
version: 1
---

# JaxbHbmEntityDiscriminatorType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| length | number |  |  |
| force | boolean | required |  |
| formulaAttribute | string |  |  |
| columnAttribute | string |  |  |
| insert | boolean | required |  |
| type | string |  |  |
| notNull | boolean | required |  |
| column | [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |  |
| formula | string |  |  |

Example

```
{
  "length" : 12345,
  "force" : true,
  "formulaAttribute" : "...",
  "columnAttribute" : "...",
  "insert" : true,
  "type" : "...",
  "notNull" : true,
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
  "formula" : "..."
}
```
