---
content_hash: d4f38633c99286321bbbdca8967763613447ca4085b7674b1b039dd738e6e991
fetched_at: '2026-11-03T14:34:39.137635+00:00'
page_id: json_WorkflowProcessVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowProcessVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowProcessVO.html
version: 1
---

# WorkflowProcessVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| formHtml | string |  |  |
| adHocTask | boolean | required |  |
| formId | number | required |  |
| subProcessCreated | map of string |  |  |
| sequenceDigitalSignature | boolean | required |  |
| conditionAfterAutomatic | number | required |  |
| jobTask | boolean | required |  |
| processDescription | string |  |  |
| currentMovto | number |  |  |
| processId | string |  |  |
| keyWord | string |  |  |
| allowComplements | boolean | required |  |
| sequence | number | required |  |
| scriptVersion | number | required |  |
| deadLineText | string |  |  |
| processInstanceId | number | required |  |
| counterSign | boolean | required |  |
| avoidTransfer | boolean | required |  |
| automaticTask | boolean | required |  |
| docFileOrigName | string |  |  |
| movementDate | string |  |  |
| processLinkMessage | [ProcessLinkMessageVO](https://api.fluig.com/old/json_ProcessLinkMessageVO.html) |  |  |
| availableUsers | [WorkflowProcessAvailableUsersVO](https://api.fluig.com/old/json_WorkflowProcessAvailableUsersVO.html) |  |  |
| stateDescription | string |  |  |
| forecastedEffortType | number |  |  |
| versionDoc | number | required |  |
| expired | boolean | required |  |
| status | number | required |  |
| threadSequence | number |  |  |
| currentStates | array of [WorkflowViewProcessStateVO](https://api.fluig.com/old/json_WorkflowViewProcessStateVO.html) |  |  |
| observation | string |  |  |
| availableStates | array of [StatesVO](https://api.fluig.com/old/json_StatesVO.html) |  |  |
| version | number | required |  |
| digitalSignature | boolean | required |  |
| userPermissions | string |  |  |
| complementsLevel | number |  |  |
| formVersion | number | required |  |
| formIdV2 | number | required |  |
| signPath | string |  |  |
| initialState | boolean | required |  |
| processInstruction | string |  |  |
| taskInstruction | string |  |  |
| processDiagram | string |  |  |
| nrDoc | number | required |  |
| nameFileToBeSigned | string |  |  |
| selectedDestinyAfterAutomatic | number | required |  |
| uniqueCardVersion | boolean | required |  |
| formDescription | string |  |  |

Example

```
{
  "formHtml" : "...",
  "adHocTask" : true,
  "formId" : 12345,
  "subProcessCreated" : {
    "property1" : "...",
    "property2" : "..."
  },
  "sequenceDigitalSignature" : true,
  "conditionAfterAutomatic" : 12345,
  "jobTask" : true,
  "processDescription" : "...",
  "currentMovto" : 12345,
  "processId" : "...",
  "keyWord" : "...",
  "allowComplements" : true,
  "sequence" : 12345,
  "scriptVersion" : 12345,
  "deadLineText" : "...",
  "processInstanceId" : 12345,
  "counterSign" : true,
  "avoidTransfer" : true,
  "automaticTask" : true,
  "docFileOrigName" : "...",
  "movementDate" : "...",
  "processLinkMessage" : {
    "movementTitle" : "...",
    "movementAccessLinkDescription" : "...",
    "movementDescription" : "...",
    "tokens" : {
      "property1" : "...",
      "property2" : "..."
    }
  },
  "availableUsers" : {
    "users" : [ {
      "login" : "...",
      "colleagueName" : "...",
      "email" : "...",
      "colleagueId" : "..."
    }, {
      "login" : "...",
      "colleagueName" : "...",
      "email" : "...",
      "colleagueId" : "..."
    } ],
    "hasFormAssigment" : true,
    "willShowUsers" : true,
    "isCollectiveTask" : true
  },
  "stateDescription" : "...",
  "forecastedEffortType" : 12345,
  "versionDoc" : 12345,
  "expired" : true,
  "status" : 12345,
  "threadSequence" : 12345,
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
  "observation" : "...",
  "availableStates" : [ {
    "subProcessSequence" : 12345,
    "sequence" : 12345,
    "processId" : "...",
    "description" : "...",
    "isReturn" : true
  }, {
    "subProcessSequence" : 12345,
    "sequence" : 12345,
    "processId" : "...",
    "description" : "...",
    "isReturn" : true
  } ],
  "version" : 12345,
  "digitalSignature" : true,
  "userPermissions" : "...",
  "complementsLevel" : 12345,
  "formVersion" : 12345,
  "formIdV2" : 12345,
  "signPath" : "...",
  "initialState" : true,
  "processInstruction" : "...",
  "taskInstruction" : "...",
  "processDiagram" : "...",
  "nrDoc" : 12345,
  "nameFileToBeSigned" : "...",
  "selectedDestinyAfterAutomatic" : 12345,
  "uniqueCardVersion" : true,
  "formDescription" : "..."
}
```
