---
content_hash: 940000bf676877126450ce8fc03739fec70d086d173ebc0d4b63acaba2792874
fetched_at: '2026-11-03T14:34:38.937575+00:00'
page_id: json_WCMResourceKitFile
product: fluig
source: rest-fluig
title: Fluig REST — WCMResourceKitFile Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMResourceKitFile.html
version: 1
---

# WCMResourceKitFile Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| kit | [WCMResourceKit](https://api.fluig.com/old/json_WCMResourceKit.html) |  |
| id | number |  |
| type | string |  |
| order | number |  |
| resource | string |  |

Example

```
{
  "kit" : {
    "code" : "...",
    "resources" : [ {
      "kit" : { },
      "id" : 12345,
      "type" : "...",
      "order" : 12345,
      "resource" : "..."
    }, {
      "kit" : { },
      "id" : 12345,
      "type" : "...",
      "order" : 12345,
      "resource" : "..."
    } ],
    "id" : 12345
  },
  "id" : 12345,
  "type" : "...",
  "order" : 12345,
  "resource" : "..."
}
```
