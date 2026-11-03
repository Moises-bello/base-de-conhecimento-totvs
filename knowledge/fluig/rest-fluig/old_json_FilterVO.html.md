---
content_hash: a02b162637256986636e4cdc20a0892b1a35d63a963fd3a90c2f6935b2255730
fetched_at: '2026-11-03T14:34:36.997583+00:00'
page_id: json_FilterVO
product: fluig
source: rest-fluig
title: Fluig REST — FilterVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FilterVO.html
version: 1
---

# FilterVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| name | string |  |  |
| type | string |  |  |
| isPublic | boolean | required |  |
| fields | array of [FilterFieldVO](https://api.fluig.com/old/json_FilterFieldVO_filter.html) |  |  |
| id | number |  |  |
| filterOrder | [FilterOrderVO](https://api.fluig.com/old/json_FilterOrderVO_filter.html) |  |  |
| processId | string |  |  |

Example

```
{
  "name" : "...",
  "type" : "...",
  "isPublic" : true,
  "fields" : [ {
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
  }, {
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
  } ],
  "id" : 12345,
  "filterOrder" : {
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
  },
  "processId" : "..."
}
```
