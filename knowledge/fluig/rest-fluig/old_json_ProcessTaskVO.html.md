---
content_hash: bdbcacfee3cd64b064585220c1af837d4ba4c69a82e272df60c4fc87e32ee42d
fetched_at: '2026-11-03T14:34:38.108536+00:00'
page_id: json_ProcessTaskVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessTaskVO.html
version: 1
---

# ProcessTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| complement | boolean | required |  |
| taskObservation | string |  |  |
| canCurrentUserTakeTask | boolean | required |  |
| taskSigned | boolean | required |  |
| companyId | number | required |  |
| movementSequence | number | required |  |
| taskCompletionDateFormatted | string |  |  |
| deadlineText | string |  |  |
| taskCompletionDate | number |  |  |
| taskCompletionHour | number | required |  |
| description | string |  |  |
| colleagueId | string |  |  |
| active | boolean | required |  |
| completeType | number | required |  |
| status | number | required |  |
| processInstanceId | number | required |  |
| colleagueName | string |  |  |
| choosedSequence | number | required |  |
| completeColleagueId | string |  |  |
| transferredSequence | number | required |  |
| historTaskObservation | string |  |  |
| statusConsult | number | required |  |
| historCompleteColleague | string |  |  |
| choosedColleagueId | string |  |  |

Example

```
{
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
}
```
