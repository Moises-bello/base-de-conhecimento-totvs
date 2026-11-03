---
content_hash: 158faf294a1d78a16a1614333c96cc7681fc7dcbcab0723e1e48848cb82f4d2c
fetched_at: '2026-11-03T14:34:39.180232+00:00'
page_id: json_WorkflowViewObservationVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewObservationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewObservationVO.html
version: 1
---

# WorkflowViewObservationVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| stateSequence | number | required |  |
| movementSequence | number | required |  |
| processInstanceId | number | required |  |
| threadSequence | number | required |  |
| observation | string |  |  |
| managerMode | boolean | required |  |

Example

```
{
  "stateSequence" : 12345,
  "movementSequence" : 12345,
  "processInstanceId" : 12345,
  "threadSequence" : 12345,
  "observation" : "...",
  "managerMode" : true
}
```
