---
content_hash: a9a938875f42fa4795131698aaec6a037aa6be3e007a89f933c3d30e8f85c620
fetched_at: '2026-11-03T14:34:39.192401+00:00'
page_id: json_WorkflowViewProcessHistoryVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewProcessHistoryVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewProcessHistoryVO.html
version: 1
---

# WorkflowViewProcessHistoryVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| subProcessDescription | string |  |  |
| lablelLink | string |  |  |
| labelActivity | string |  |  |
| movementHour | string |  |  |
| parentProcessId | number |  |  |
| movementTime | number | required |  |
| historyType | [ProcessHistoryTypeEnumeration](https://api.fluig.com/old/json_ProcessHistoryTypeEnumeration.html) |  |  |
| stateType | number | required |  |
| subProcessId | number | required |  |
| movementSequence | number | required |  |
| parentProcessDescription | string |  |  |
| conversion | boolean | required |  |
| mapTasks | map of [WorkflowViewProcessTaskVO](https://api.fluig.com/old/json_WorkflowViewProcessTaskVO.html) |  |  |
| isReturn | boolean | required |  |
| defaultLink | boolean | required |  |
| movementDate | number |  |  |
| replacementName | string |  |  |
| stateSequence | number | required |  |
| movementDateHour | string |  |  |

Example

```
{
  "subProcessDescription" : "...",
  "lablelLink" : "...",
  "labelActivity" : "...",
  "movementHour" : "...",
  "parentProcessId" : 12345,
  "movementTime" : 12345,
  "historyType" : "END",
  "stateType" : 12345,
  "subProcessId" : 12345,
  "movementSequence" : 12345,
  "parentProcessDescription" : "...",
  "conversion" : true,
  "mapTasks" : {
    "property1" : {
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
    },
    "property2" : {
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
  },
  "isReturn" : true,
  "defaultLink" : true,
  "movementDate" : 12345,
  "replacementName" : "...",
  "stateSequence" : 12345,
  "movementDateHour" : "..."
}
```
