---
content_hash: 3dfceacabbd37f2665b19abbf7bfc63d46066dae59d50eb66c0380d5be8f4c74
fetched_at: '2026-11-03T14:34:38.078506+00:00'
page_id: json_ProcessSearchProcessResultVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessSearchProcessResultVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessSearchProcessResultVO.html
version: 1
---

# ProcessSearchProcessResultVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| startDateProcess | number |  |  |
| processDescription | string |  |  |
| processId | string |  |  |
| attachVersion | number | required |  |
| endDateProcess | number |  |  |
| documentDescription | string |  |  |
| deadlineText | string |  |  |
| movementSequence | number | required |  |
| attachId | number | required |  |
| requesterId | string |  |  |
| formRecordId | number |  |  |
| forecastedEffortType | number |  |  |
| stateDescription | string |  |  |
| version | number | required |  |
| requesterName | string |  |  |
| processInstanceId | number | required |  |
| statusConsult | number |  |  |
| formCode | number |  |  |
| colleagueName | string |  |  |

Example

```
{
  "startDateProcess" : 12345,
  "processDescription" : "...",
  "processId" : "...",
  "attachVersion" : 12345,
  "endDateProcess" : 12345,
  "documentDescription" : "...",
  "deadlineText" : "...",
  "movementSequence" : 12345,
  "attachId" : 12345,
  "requesterId" : "...",
  "formRecordId" : 12345,
  "forecastedEffortType" : 12345,
  "stateDescription" : "...",
  "version" : 12345,
  "requesterName" : "...",
  "processInstanceId" : 12345,
  "statusConsult" : 12345,
  "formCode" : 12345,
  "colleagueName" : "..."
}
```
