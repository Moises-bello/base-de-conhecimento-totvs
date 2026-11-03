---
content_hash: d7ff0dc9e0255eb33ed2272069a2321132873820877d4521d907c3a1da3a3b0e
fetched_at: '2026-11-03T14:34:38.056332+00:00'
page_id: json_ProcessInstanceInfoVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessInstanceInfoVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessInstanceInfoVO.html
version: 1
---

# ProcessInstanceInfoVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| tasksInfo | array of [ProcessTaskInfoVO](https://api.fluig.com/old/json_ProcessTaskInfoVO.html) |  |  |
| formValues | map of string |  |  |
| formId | number | required |  |
| attachments | array of [ProcessAttachmentVO](https://api.fluig.com/old/json_ProcessAttachmentVO.html) |  |  |
| companyId | number | required |  |
| processVersion | number | required |  |
| startDateProcess | number |  |  |
| formVersion | number | required |  |
| taskObservations | array of [ProcessObservationVO](https://api.fluig.com/old/json_ProcessObservationVO.html) |  |  |
| processId | string |  |  |
| processInstanceId | number | required |  |

Example

```
{
  "tasksInfo" : [ {
    "state" : {
      "tenantId" : 12345,
      "sequence" : 12345,
      "stateName" : "...",
      "stateDescription" : "..."
    },
    "taskDeadline" : 12345,
    "stateSequence" : 12345,
    "transferredSequence" : 12345,
    "active" : true,
    "startDateTask" : 12345,
    "movementSequence" : 12345,
    "expired" : true,
    "colleagueName" : "...",
    "status" : 12345
  }, {
    "state" : {
      "tenantId" : 12345,
      "sequence" : 12345,
      "stateName" : "...",
      "stateDescription" : "..."
    },
    "taskDeadline" : 12345,
    "stateSequence" : 12345,
    "transferredSequence" : 12345,
    "active" : true,
    "startDateTask" : 12345,
    "movementSequence" : 12345,
    "expired" : true,
    "colleagueName" : "...",
    "status" : 12345
  } ],
  "formValues" : {
    "property1" : "...",
    "property2" : "..."
  },
  "formId" : 12345,
  "attachments" : [ {
    "colleagueId" : "...",
    "attachedDate" : 12345,
    "version" : 12345,
    "originalMovementSequence" : 12345,
    "documentId" : 12345,
    "description" : "..."
  }, {
    "colleagueId" : "...",
    "attachedDate" : 12345,
    "version" : 12345,
    "originalMovementSequence" : 12345,
    "documentId" : 12345,
    "description" : "..."
  } ],
  "companyId" : 12345,
  "processVersion" : 12345,
  "startDateProcess" : 12345,
  "formVersion" : 12345,
  "taskObservations" : [ {
    "colleagueId" : "...",
    "threadSequence" : 12345,
    "stateSequence" : 12345,
    "processInstanceId" : 12345,
    "observation" : "...",
    "movementSequence" : 12345,
    "observationDate" : 12345,
    "id" : 12345
  }, {
    "colleagueId" : "...",
    "threadSequence" : 12345,
    "stateSequence" : 12345,
    "processInstanceId" : 12345,
    "observation" : "...",
    "movementSequence" : 12345,
    "observationDate" : 12345,
    "id" : 12345
  } ],
  "processId" : "...",
  "processInstanceId" : 12345
}
```
