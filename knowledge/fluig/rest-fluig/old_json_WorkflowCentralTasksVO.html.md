---
content_hash: 38904f7708d788ff4a14df6625ac8c16ca60a9b7a1a058c1acc020c978d146d8
fetched_at: '2026-11-03T14:34:39.075778+00:00'
page_id: json_WorkflowCentralTasksVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowCentralTasksVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowCentralTasksVO.html
version: 1
---

# WorkflowCentralTasksVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| workflowProcessStatus | number | required |  |
| counterSign | boolean |  |  |
| colleaguesManager | array of string |  |  |
| complementsLevel | number |  |  |
| closureDateTime | number |  |  |
| statusConsult | number |  |  |
| hasParallel | boolean |  |  |
| allowComplements | boolean |  |  |
| formDescription | string |  |  |
| startDateProcess | number |  |  |
| processInstruction | string |  |  |
| attachVersion | number |  |  |
| loggedFirstName | string |  |  |
| requesterEmail | string |  |  |
| stateSequence | number |  |  |
| consensusReached | boolean |  |  |
| companyId | number | required |  |
| formVersion | number | required |  |
| processDiagram | string |  |  |
| active | boolean |  |  |
| currentStates | array of [WorkflowViewProcessStateVO](https://api.fluig.com/old/json_WorkflowViewProcessStateVO.html) |  |  |
| timeZoneUser | string |  |  |
| forecastedEffortType | number |  |  |
| formHtml | string |  |  |
| formIdV2 | number | required |  |
| attachments | number | required |  |
| attachId | number |  |  |
| formId | number | required |  |
| Properties inherited from [WorkflowTasksVO](https://api.fluig.com/old/json_WorkflowTasksVO.html) | | | |
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
  "workflowProcessStatus" : 12345,
  "counterSign" : true,
  "colleaguesManager" : [ "...", "..." ],
  "complementsLevel" : 12345,
  "closureDateTime" : 12345,
  "statusConsult" : 12345,
  "hasParallel" : true,
  "allowComplements" : true,
  "formDescription" : "...",
  "startDateProcess" : 12345,
  "processInstruction" : "...",
  "attachVersion" : 12345,
  "loggedFirstName" : "...",
  "requesterEmail" : "...",
  "stateSequence" : 12345,
  "consensusReached" : true,
  "companyId" : 12345,
  "formVersion" : 12345,
  "processDiagram" : "...",
  "active" : true,
  "currentStates" : [ {
    "stateSequence" : 12345,
    "threadSequence" : 12345,
    "deadlineText" : "...",
    "canCurrentUserTakeTask" : true,
    "statusConsult" : 12345,
    "movementTime" : 12345,
    "joint" : true,
    "canChangeDecision" : true,
    "canceled" : true,
    "stateDescription" : "...",
    "observation" : "...",
    "colleagueLogin" : "...",
    "subProcessDescription" : "...",
    "colleagueName" : "...",
    "subProcess" : true,
    "movementSequence" : 12345,
    "subProcessId" : 12345,
    "consensoResume" : [ "...", "..." ],
    "workflowConsensusVO" : {
      "validPercentage" : true,
      "reachedPercentage" : 12345,
      "agreementPercentage" : 12345,
      "consensusDecisions" : [ { }, { } ]
    },
    "colleagueId" : "..."
  }, {
    "stateSequence" : 12345,
    "threadSequence" : 12345,
    "deadlineText" : "...",
    "canCurrentUserTakeTask" : true,
    "statusConsult" : 12345,
    "movementTime" : 12345,
    "joint" : true,
    "canChangeDecision" : true,
    "canceled" : true,
    "stateDescription" : "...",
    "observation" : "...",
    "colleagueLogin" : "...",
    "subProcessDescription" : "...",
    "colleagueName" : "...",
    "subProcess" : true,
    "movementSequence" : 12345,
    "subProcessId" : 12345,
    "consensoResume" : [ "...", "..." ],
    "workflowConsensusVO" : {
      "validPercentage" : true,
      "reachedPercentage" : 12345,
      "agreementPercentage" : 12345,
      "consensusDecisions" : [ { }, { } ]
    },
    "colleagueId" : "..."
  } ],
  "timeZoneUser" : "...",
  "forecastedEffortType" : 12345,
  "formHtml" : "...",
  "formIdV2" : 12345,
  "attachments" : 12345,
  "attachId" : 12345,
  "formId" : 12345,
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
  "fieldValue8" : "...",
  "slaStatusString" : "...",
  "fieldValue10" : "...",
  "slaRemainingTime" : "..."
}
```
