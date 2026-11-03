---
content_hash: 45dbcaf2b5d0570c07058fb03aa27bf014b3d4850c98ee2c7c2cbd854a226368
fetched_at: '2026-11-03T14:34:38.928386+00:00'
page_id: json_WCMResourceComponent
product: fluig
source: rest-fluig
title: Fluig REST — WCMResourceComponent Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMResourceComponent.html
version: 1
---

# WCMResourceComponent Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| code | string |  |
| id | number |  |
| resources | array of [WCMResourceComponentFile](https://api.fluig.com/old/json_WCMResourceComponentFile.html) |  |

Example

```
{
  "code" : "...",
  "id" : 12345,
  "resources" : [ {
    "component" : {
      "code" : "...",
      "id" : 12345,
      "resources" : [ { }, { } ]
    },
    "resource" : "...",
    "type" : "...",
    "id" : 12345,
    "order" : 12345
  }, {
    "component" : {
      "code" : "...",
      "id" : 12345,
      "resources" : [ { }, { } ]
    },
    "resource" : "...",
    "type" : "...",
    "id" : 12345,
    "order" : 12345
  } ]
}
```
