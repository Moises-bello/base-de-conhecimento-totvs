---
content_hash: 2affd89ec9113a3f7bb1696c38860bc969aebb9958a6ce394d31124968075481
fetched_at: '2026-11-03T14:34:36.499522+00:00'
page_id: json_CompleteFilterVO
product: fluig
source: rest-fluig
title: Fluig REST — CompleteFilterVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CompleteFilterVO.html
version: 1
---

# CompleteFilterVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| shared | boolean | required |  |
| filterOrder | [FilterOrderVO](https://api.fluig.com/old/json_FilterOrderVO.html) |  |  |
| permission | number |  |  |
| fields | array of [FilterFieldVO](https://api.fluig.com/old/json_FilterFieldVO.html) |  |  |
| processId | string |  |  |
| Properties inherited from [FilterVO](https://api.fluig.com/old/json_FilterVO_vo.html) | | | |
| type | string |  |  |
| shared | boolean | required |  |
| id | number |  |  |
| name | string |  |  |

Example

```
{
  "shared" : true,
  "filterOrder" : {
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
  },
  "permission" : 12345,
  "fields" : [ {
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
  }, {
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
  } ],
  "processId" : "...",
  "type" : "...",
  "id" : 12345,
  "name" : "..."
}
```
