---
content_hash: e4c3ee5eb34269e4cf571a924620b1d648bb5f0e7ec7f8b66640289ab9e7b60c
fetched_at: '2026-11-03T14:34:39.087141+00:00'
page_id: json_WorkflowProcessAvailableUsersVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowProcessAvailableUsersVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowProcessAvailableUsersVO.html
version: 1
---

# WorkflowProcessAvailableUsersVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| users | array of [ColleagueVO](https://api.fluig.com/old/json_ColleagueVO.html) |  |  |
| hasFormAssigment | boolean | required |  |
| willShowUsers | boolean |  |  |
| isCollectiveTask | boolean |  |  |

Example

```
{
  "users" : [ {
    "login" : "...",
    "colleagueName" : "...",
    "email" : "...",
    "colleagueId" : "..."
  }, {
    "login" : "...",
    "colleagueName" : "...",
    "email" : "...",
    "colleagueId" : "..."
  } ],
  "hasFormAssigment" : true,
  "willShowUsers" : true,
  "isCollectiveTask" : true
}
```
