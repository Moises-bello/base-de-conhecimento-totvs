---
content_hash: d832bb4c7a50a740ce9e5285f50385a4283fbe866b7fead09d62d477f82d4871
fetched_at: '2026-11-03T14:34:38.071838+00:00'
page_id: json_ProcessSearchProcessListResultVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessSearchProcessListResultVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessSearchProcessListResultVO.html
version: 1
---

# ProcessSearchProcessListResultVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| resultFinalizedVo | array of [ProcessSearchProcessResultVO](https://api.fluig.com/old/json_ProcessSearchProcessResultVO.html) |  |  |
| limit | number | required |  |
| resultCanceledVo | array of [ProcessSearchProcessResultVO](https://api.fluig.com/old/json_ProcessSearchProcessResultVO.html) |  |  |
| resultOpenedVo | array of [ProcessSearchProcessResultVO](https://api.fluig.com/old/json_ProcessSearchProcessResultVO.html) |  |  |

Example

```
{
  "resultFinalizedVo" : [ {
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
  }, {
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
  } ],
  "limit" : 12345,
  "resultCanceledVo" : [ {
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
  }, {
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
  } ],
  "resultOpenedVo" : [ {
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
  }, {
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
  } ]
}
```
