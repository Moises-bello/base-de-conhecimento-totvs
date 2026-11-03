---
content_hash: fa84c291a8117255afe5a13e9f19d328a7d88f19852e867926487819557717f3
fetched_at: '2026-11-03T14:34:38.934426+00:00'
page_id: json_WCMResourceKit
product: fluig
source: rest-fluig
title: Fluig REST — WCMResourceKit Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMResourceKit.html
version: 1
---

# WCMResourceKit Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| code | string |  |
| resources | array of [WCMResourceKitFile](https://api.fluig.com/old/json_WCMResourceKitFile.html) |  |
| id | number |  |

Example

```
{
  "code" : "...",
  "resources" : [ {
    "kit" : {
      "code" : "...",
      "resources" : [ { }, { } ],
      "id" : 12345
    },
    "id" : 12345,
    "type" : "...",
    "order" : 12345,
    "resource" : "..."
  }, {
    "kit" : {
      "code" : "...",
      "resources" : [ { }, { } ],
      "id" : 12345
    },
    "id" : 12345,
    "type" : "...",
    "order" : 12345,
    "resource" : "..."
  } ],
  "id" : 12345
}
```
