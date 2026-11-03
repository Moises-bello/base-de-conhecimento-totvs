---
content_hash: 06505be2e586d352b4e114e7107740ef3cdf7f38a160c2dceb765c0a09d3db9a
fetched_at: '2026-11-03T14:34:38.931605+00:00'
page_id: json_WCMResourceComponentFile
product: fluig
source: rest-fluig
title: Fluig REST — WCMResourceComponentFile Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMResourceComponentFile.html
version: 1
---

# WCMResourceComponentFile Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| component | [WCMResourceComponent](https://api.fluig.com/old/json_WCMResourceComponent.html) |  |
| resource | string |  |
| type | string |  |
| id | number |  |
| order | number |  |

Example

```
{
  "component" : {
    "code" : "...",
    "id" : 12345,
    "resources" : [ {
      "component" : { },
      "resource" : "...",
      "type" : "...",
      "id" : 12345,
      "order" : 12345
    }, {
      "component" : { },
      "resource" : "...",
      "type" : "...",
      "id" : 12345,
      "order" : 12345
    } ]
  },
  "resource" : "...",
  "type" : "...",
  "id" : 12345,
  "order" : 12345
}
```
