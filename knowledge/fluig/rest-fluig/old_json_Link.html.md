---
content_hash: 2dce1e895b9e3330ee13958f8e72a9d467adcb355d3a581c315870f64ff9f889
fetched_at: '2026-11-03T14:34:37.764001+00:00'
page_id: json_Link
product: fluig
source: rest-fluig
title: Fluig REST — Link Data Type
type: documentation
url: https://api.fluig.com/old/json_Link.html
version: 1
---

# Link Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| uri | string |  |
| uriBuilder | [UriBuilder](https://api.fluig.com/old/json_UriBuilder.html) |  |
| rels | array of string |  |
| type | string |  |
| rel | string |  |
| title | string |  |
| params | map of string |  |

Example

```
{
  "uri" : "...",
  "uriBuilder" : { },
  "rels" : [ "...", "..." ],
  "type" : "...",
  "rel" : "...",
  "title" : "...",
  "params" : {
    "property1" : "...",
    "property2" : "..."
  }
}
```
