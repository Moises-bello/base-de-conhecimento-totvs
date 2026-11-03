---
content_hash: 866489e0374f2de847d0c60a76017a8c7364e5c3e638bd546222f5c0c1b602a6
fetched_at: '2026-11-03T14:34:37.815069+00:00'
page_id: json_MediaType_core
product: fluig
source: rest-fluig
title: Fluig REST — MediaType Data Type
type: documentation
url: https://api.fluig.com/old/json_MediaType_core.html
version: 1
---

# MediaType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| subtype | string |  |  |
| type | string |  |  |
| parameters | map of string |  |  |
| wildcardType | boolean | required |  |
| wildcardSubtype | boolean | required |  |

Example

```
{
  "subtype" : "...",
  "type" : "...",
  "parameters" : {
    "property1" : "...",
    "property2" : "..."
  },
  "wildcardType" : true,
  "wildcardSubtype" : true
}
```
