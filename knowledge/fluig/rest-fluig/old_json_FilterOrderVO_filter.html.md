---
content_hash: 0ab4d43fab2e08f0887f94e610e1654f6969daa0449648bb4e4a81be12a83fc4
fetched_at: '2026-11-03T14:34:36.984725+00:00'
page_id: json_FilterOrderVO_filter
product: fluig
source: rest-fluig
title: Fluig REST — FilterOrderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FilterOrderVO_filter.html
version: 1
---

# FilterOrderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| field | [FilterFieldVO](https://api.fluig.com/old/json_FilterFieldVO_filter.html) |  |
| order | string |  |

Example

```
{
  "id" : 12345,
  "field" : {
    "id" : 12345,
    "value" : "...",
    "label" : "...",
    "sensitiveData" : true,
    "fontWeight" : "...",
    "fontStyle" : "...",
    "fontSize" : 12345,
    "textDecoration" : "...",
    "key" : "...",
    "type" : "...",
    "color" : "...",
    "visible" : true,
    "orderPosition" : 12345,
    "slotId" : 12345
  },
  "order" : "..."
}
```
