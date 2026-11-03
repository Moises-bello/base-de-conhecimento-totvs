---
content_hash: c97a77e9d638fdd2e7c576528ade1bc16ac4c77d3ed023d615db70ae1ed5fd17
fetched_at: '2026-11-03T14:34:36.981919+00:00'
page_id: json_FilterOrderVO
product: fluig
source: rest-fluig
title: Fluig REST — FilterOrderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FilterOrderVO.html
version: 1
---

# FilterOrderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| order | string |  |
| field | [FilterFieldVO](https://api.fluig.com/old/json_FilterFieldVO.html) |  |
| id | number |  |

Example

```
{
  "order" : "...",
  "field" : {
    "color" : "...",
    "orderPosition" : 12345,
    "visible" : true,
    "type" : "...",
    "fontWeight" : "...",
    "fontStyle" : "...",
    "fontSize" : 12345,
    "slotId" : 12345,
    "key" : "...",
    "id" : 12345,
    "label" : "...",
    "textDecoration" : "...",
    "value" : "...",
    "sensitiveData" : true
  },
  "id" : 12345
}
```
