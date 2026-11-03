---
content_hash: 977123780306ec65ef0d51379314a7415ade6ff8a02a504582e7f9530fcbaeb4
fetched_at: '2026-11-03T14:34:39.198972+00:00'
page_id: json_WorkflowViewProcessStateVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewProcessStateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewProcessStateVO.html
version: 1
---

# WorkflowViewProcessStateVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| stateSequence | number | required |  |
| threadSequence | number | required |  |
| deadlineText | string |  |  |
| canCurrentUserTakeTask | boolean |  |  |
| statusConsult | number |  |  |
| movementTime | number |  |  |
| joint | boolean |  |  |
| canChangeDecision | boolean |  |  |
| canceled | boolean | required |  |
| stateDescription | string |  |  |
| observation | string |  |  |
| colleagueLogin | string |  |  |
| subProcessDescription | string |  |  |
| colleagueName | string |  |  |
| subProcess | boolean |  |  |
| movementSequence | number |  |  |
| subProcessId | number |  |  |
| consensoResume | array of string |  |  |
| workflowConsensusVO | [WorkflowConsensusVO](https://api.fluig.com/old/json_WorkflowConsensusVO.html) |  |  |
| colleagueId | string |  |  |

Example

```
{
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
    "consensusDecisions" : [ {
      "colleagueLogin" : "...",
      "colleagueNameDestination" : "...",
      "decision" : 12345,
      "colleagueName" : "...",
      "taskDestination" : "...",
      "colleagueId" : "..."
    }, {
      "colleagueLogin" : "...",
      "colleagueNameDestination" : "...",
      "decision" : 12345,
      "colleagueName" : "...",
      "taskDestination" : "...",
      "colleagueId" : "..."
    } ]
  },
  "colleagueId" : "..."
}
```
