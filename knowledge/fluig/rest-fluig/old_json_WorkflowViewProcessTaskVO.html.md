---
content_hash: c882c52280227f7188a9c487e401939d86a3412ef80125dae7238d490c714c87
fetched_at: '2026-11-03T14:34:39.211038+00:00'
page_id: json_WorkflowViewProcessTaskVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewProcessTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewProcessTaskVO.html
version: 1
---

# WorkflowViewProcessTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processTaskCompleteDetailVO | [WorkflowViewProcessTaskCompleteDetailVO](https://api.fluig.com/old/json_WorkflowViewProcessTaskCompleteDetailVO.html) |  |  |
| movementTime | number |  |  |
| completeColleagueName | string |  |  |
| choosedActivityLabel | string |  |  |
| movementDateHour | string |  |  |
| observation | string |  |  |
| history | string |  |  |
| login | string |  |  |
| hasPassword | boolean | required |  |
| processStateExecutionType | number |  |  |
| replacementName | string |  |  |
| description | string |  |  |
| choosedColleagueLogin | string |  |  |
| documentId | number |  |  |
| movementSequence | number |  |  |
| transferredSequence | number |  |  |
| choosedStateSequence | number |  |  |
| status | number |  |  |
| choosedColleagueName | string |  |  |
| taskSigned | boolean |  |  |
| completeTaskManager | boolean | required |  |
| version | number |  |  |
| userId | string |  |  |

Example

```
{
  "processTaskCompleteDetailVO" : {
    "taskCompletedType" : 12345,
    "taskCompleterUsername" : "...",
    "taskCompletedDescType" : "...",
    "taskCompletedBy" : "...",
    "taskAssignedLogin" : "...",
    "taskAssignedUsername" : "...",
    "taskCompleterLogin" : "..."
  },
  "movementTime" : 12345,
  "completeColleagueName" : "...",
  "choosedActivityLabel" : "...",
  "movementDateHour" : "...",
  "observation" : "...",
  "history" : "...",
  "login" : "...",
  "hasPassword" : true,
  "processStateExecutionType" : 12345,
  "replacementName" : "...",
  "description" : "...",
  "choosedColleagueLogin" : "...",
  "documentId" : 12345,
  "movementSequence" : 12345,
  "transferredSequence" : 12345,
  "choosedStateSequence" : 12345,
  "status" : 12345,
  "choosedColleagueName" : "...",
  "taskSigned" : true,
  "completeTaskManager" : true,
  "version" : 12345,
  "userId" : "..."
}
```
