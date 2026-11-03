---
content_hash: 943d73f76fe86ba37fd9ba45cec337a444480064f18463c733bd484e18898788
fetched_at: '2026-11-03T14:34:38.666853+00:00'
page_id: json_TaskTypeVO
product: fluig
source: rest-fluig
title: Fluig REST — TaskTypeVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TaskTypeVO.html
version: 1
---

# TaskTypeVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| description | string |  |  |
| state | string |  |  |
| type | string |  |  |
| totalTask | number | required |  |
| children | array of [TaskTypeVO](https://api.fluig.com/old/json_TaskTypeVO.html) |  |  |
| totalUnknown | number | required |  |
| totalKnown | number | required |  |
| customized | boolean | required |  |
| taskId | string |  |  |
| customURL | string |  |  |

Example

```
{
  "description" : "...",
  "state" : "...",
  "type" : "...",
  "totalTask" : 12345,
  "children" : [ {
    "description" : "...",
    "state" : "...",
    "type" : "...",
    "totalTask" : 12345,
    "children" : [ { }, { } ],
    "totalUnknown" : 12345,
    "totalKnown" : 12345,
    "customized" : true,
    "taskId" : "...",
    "customURL" : "..."
  }, {
    "description" : "...",
    "state" : "...",
    "type" : "...",
    "totalTask" : 12345,
    "children" : [ { }, { } ],
    "totalUnknown" : 12345,
    "totalKnown" : 12345,
    "customized" : true,
    "taskId" : "...",
    "customURL" : "..."
  } ],
  "totalUnknown" : 12345,
  "totalKnown" : 12345,
  "customized" : true,
  "taskId" : "...",
  "customURL" : "..."
}
```
