---
content_hash: 6ed7f0549727c0ea806e85ca7908b595e8ec6cc68c967e507f5b379301df3b34
fetched_at: '2026-11-03T14:34:38.051206+00:00'
page_id: json_ProcessHistoryVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessHistoryVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessHistoryVO.html
version: 1
---

# ProcessHistoryVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| labelActivity | string |  |  |
| active | boolean |  |  |
| isReturn | boolean |  |  |
| movementDate | number |  |  |
| tasks | array of [ProcessTaskVO](https://api.fluig.com/old/json_ProcessTaskVO.html) |  |  |
| stateSequence | number |  |  |
| previousMovementSequence | number |  |  |
| subProcessId | number |  |  |
| threadSequence | number |  |  |
| movementHour | string |  |  |
| movementSequence | number | required |  |
| companyId | number | required |  |
| conversionSequence | number |  |  |
| labelLink | string |  |  |
| processInstanceId | number | required |  |

Example

```
{
  "labelActivity" : "...",
  "active" : true,
  "isReturn" : true,
  "movementDate" : 12345,
  "tasks" : [ {
    "complement" : true,
    "taskObservation" : "...",
    "canCurrentUserTakeTask" : true,
    "taskSigned" : true,
    "companyId" : 12345,
    "movementSequence" : 12345,
    "taskCompletionDateFormatted" : "...",
    "deadlineText" : "...",
    "taskCompletionDate" : 12345,
    "taskCompletionHour" : 12345,
    "description" : "...",
    "colleagueId" : "...",
    "active" : true,
    "completeType" : 12345,
    "status" : 12345,
    "processInstanceId" : 12345,
    "colleagueName" : "...",
    "choosedSequence" : 12345,
    "completeColleagueId" : "...",
    "transferredSequence" : 12345,
    "historTaskObservation" : "...",
    "statusConsult" : 12345,
    "historCompleteColleague" : "...",
    "choosedColleagueId" : "..."
  }, {
    "complement" : true,
    "taskObservation" : "...",
    "canCurrentUserTakeTask" : true,
    "taskSigned" : true,
    "companyId" : 12345,
    "movementSequence" : 12345,
    "taskCompletionDateFormatted" : "...",
    "deadlineText" : "...",
    "taskCompletionDate" : 12345,
    "taskCompletionHour" : 12345,
    "description" : "...",
    "colleagueId" : "...",
    "active" : true,
    "completeType" : 12345,
    "status" : 12345,
    "processInstanceId" : 12345,
    "colleagueName" : "...",
    "choosedSequence" : 12345,
    "completeColleagueId" : "...",
    "transferredSequence" : 12345,
    "historTaskObservation" : "...",
    "statusConsult" : 12345,
    "historCompleteColleague" : "...",
    "choosedColleagueId" : "..."
  } ],
  "stateSequence" : 12345,
  "previousMovementSequence" : 12345,
  "subProcessId" : 12345,
  "threadSequence" : 12345,
  "movementHour" : "...",
  "movementSequence" : 12345,
  "companyId" : 12345,
  "conversionSequence" : 12345,
  "labelLink" : "...",
  "processInstanceId" : 12345
}
```
