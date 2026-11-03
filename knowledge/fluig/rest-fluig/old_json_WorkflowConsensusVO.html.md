---
content_hash: c4c302d3cd45259fbfaa1687c8e39d044c03478f16f7cce8f29cfea6de8ec796
fetched_at: '2026-11-03T14:34:39.083399+00:00'
page_id: json_WorkflowConsensusVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowConsensusVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowConsensusVO.html
version: 1
---

# WorkflowConsensusVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| validPercentage | boolean |  |
| reachedPercentage | number |  |
| agreementPercentage | number |  |
| consensusDecisions | array of [WorkflowConsensusDecisionVO](https://api.fluig.com/old/json_WorkflowConsensusDecisionVO.html) |  |

Example

```
{
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
}
```
