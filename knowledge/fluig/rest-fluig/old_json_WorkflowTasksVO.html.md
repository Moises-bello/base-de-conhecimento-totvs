---
content_hash: 99b4ad1fc65ab34c3502e18639ea9479dd7c024853cbe9817cda9f6df7b9d5a1
fetched_at: '2026-11-03T14:34:39.152782+00:00'
page_id: json_WorkflowTasksVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowTasksVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowTasksVO.html
version: 1
---

# WorkflowTasksVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| fieldValue6 | string |  |  |
| slaTotalRuntimeString | string |  |  |
| fieldValue5 | string |  |  |
| movementSequence | number | required |  |
| slaDeadline | string |  |  |
| cancelable | boolean | required |  |
| fieldValue11 | string |  |  |
| slaRemaningHours | number | required |  |
| version | number | required |  |
| fieldValue12 | string |  |  |
| code | string |  |  |
| stateDescription | string |  |  |
| requesterId | string |  |  |
| fieldValue2 | string |  |  |
| threadSequence | number |  |  |
| attachDescription | string |  |  |
| requesterLogin | string |  |  |
| dateExpires | string |  |  |
| know | boolean | required |  |
| slaRemaningMinutes | number | required |  |
| colleagueName | string |  |  |
| url | string |  |  |
| processInstanceId | number | required |  |
| processId | string |  |  |
| slaRemaningDays | number | required |  |
| fieldValue13 | string |  |  |
| slaTotalRuntime | number | required |  |
| fieldValue1 | string |  |  |
| fieldValue14 | string |  |  |
| fieldValue15 | string |  |  |
| fieldValue7 | string |  |  |
| requesterName | string |  |  |
| expired | boolean | required |  |
| slaStatus | number | required |  |
| approachingExpiration | boolean | required |  |
| processDescription | string |  |  |
| fieldValue9 | string |  |  |
| fieldValue3 | string |  |  |
| processKey | string |  |  |
| fieldValue4 | string |  |  |
| startDateProcess | object |  |  |
| fieldValue8 | string |  |  |
| slaStatusString | string |  |  |
| fieldValue10 | string |  |  |
| slaRemainingTime | string |  |  |

Example

```
{
  "fieldValue6" : "...",
  "slaTotalRuntimeString" : "...",
  "fieldValue5" : "...",
  "movementSequence" : 12345,
  "slaDeadline" : "...",
  "cancelable" : true,
  "fieldValue11" : "...",
  "slaRemaningHours" : 12345,
  "version" : 12345,
  "fieldValue12" : "...",
  "code" : "...",
  "stateDescription" : "...",
  "requesterId" : "...",
  "fieldValue2" : "...",
  "threadSequence" : 12345,
  "attachDescription" : "...",
  "requesterLogin" : "...",
  "dateExpires" : "...",
  "know" : true,
  "slaRemaningMinutes" : 12345,
  "colleagueName" : "...",
  "url" : "...",
  "processInstanceId" : 12345,
  "processId" : "...",
  "slaRemaningDays" : 12345,
  "fieldValue13" : "...",
  "slaTotalRuntime" : 12345,
  "fieldValue1" : "...",
  "fieldValue14" : "...",
  "fieldValue15" : "...",
  "fieldValue7" : "...",
  "requesterName" : "...",
  "expired" : true,
  "slaStatus" : 12345,
  "approachingExpiration" : true,
  "processDescription" : "...",
  "fieldValue9" : "...",
  "fieldValue3" : "...",
  "processKey" : "...",
  "fieldValue4" : "...",
  "startDateProcess" : { },
  "fieldValue8" : "...",
  "slaStatusString" : "...",
  "fieldValue10" : "...",
  "slaRemainingTime" : "..."
}
```
