---
content_hash: 6798e81e17838cbd21aa49585e710a007527a8c9c1f71e72908606649077e879
fetched_at: '2026-11-03T14:34:36.270510+00:00'
page_id: json_AssumeProcessTasksVO
product: fluig
source: rest-fluig
title: Fluig REST — AssumeProcessTasksVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AssumeProcessTasksVO.html
version: 1
---

# AssumeProcessTasksVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| assumeProcessTaskList | array of [AssumeProcessTaskVO](https://api.fluig.com/old/json_AssumeProcessTaskVO.html) |  |

Example

```
{
  "assumeProcessTaskList" : [ {
    "processInstanceId" : 12345,
    "movementSequence" : 12345,
    "colleagueId" : "...",
    "replacementId" : "..."
  }, {
    "processInstanceId" : 12345,
    "movementSequence" : 12345,
    "colleagueId" : "...",
    "replacementId" : "..."
  } ]
}
```
