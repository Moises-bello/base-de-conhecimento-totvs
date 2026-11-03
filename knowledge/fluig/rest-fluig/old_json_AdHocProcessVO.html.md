---
content_hash: 4b7825955f0d9577d69583f133932a3694a4fa5fc98906ed7f5651f6a6a43b5d
fetched_at: '2026-11-03T14:34:36.055644+00:00'
page_id: json_AdHocProcessVO
product: fluig
source: rest-fluig
title: Fluig REST — AdHocProcessVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AdHocProcessVO.html
version: 1
---

# AdHocProcessVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processInstanceId | number | required |  |
| stateSequence | number | required |  |
| name | string |  |  |
| description | string |  |  |
| adHocTasks | array of [WorkflowAdHocProcessVO](https://api.fluig.com/old/json_WorkflowAdHocProcessVO.html) |  |  |

Example

```
{
  "processInstanceId" : 12345,
  "stateSequence" : 12345,
  "name" : "...",
  "description" : "...",
  "adHocTasks" : [ {
    "name" : "...",
    "dueDate" : "...",
    "responsible" : "...",
    "taskState" : 12345,
    "observation" : "..."
  }, {
    "name" : "...",
    "dueDate" : "...",
    "responsible" : "...",
    "taskState" : 12345,
    "observation" : "..."
  } ]
}
```
