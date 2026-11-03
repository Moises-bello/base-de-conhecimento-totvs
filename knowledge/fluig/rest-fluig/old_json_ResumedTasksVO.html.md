---
content_hash: a928b172f76099c5a81e373e11dc826e01a26e74679f088ae7b98e538e6990a3
fetched_at: '2026-11-03T14:34:38.283488+00:00'
page_id: json_ResumedTasksVO
product: fluig
source: rest-fluig
title: Fluig REST — ResumedTasksVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ResumedTasksVO.html
version: 1
---

# ResumedTasksVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| state | string |  |  |
| children | array of [ResumedTasksVO](https://api.fluig.com/old/json_ResumedTasksVO.html) |  |  |
| taskId | string |  |  |
| totalTask | number | required |  |
| type | string |  |  |
| customURL | string |  |  |
| name | string |  |  |

Example

```
{
  "state" : "...",
  "children" : [ {
    "state" : "...",
    "children" : [ { }, { } ],
    "taskId" : "...",
    "totalTask" : 12345,
    "type" : "...",
    "customURL" : "...",
    "name" : "..."
  }, {
    "state" : "...",
    "children" : [ { }, { } ],
    "taskId" : "...",
    "totalTask" : 12345,
    "type" : "...",
    "customURL" : "...",
    "name" : "..."
  } ],
  "taskId" : "...",
  "totalTask" : 12345,
  "type" : "...",
  "customURL" : "...",
  "name" : "..."
}
```
