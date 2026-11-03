---
content_hash: 45d7eafc14fcec2d0d6567f3c55aa8419e0af08314e83c44c389cad1d776a5f6
fetched_at: '2026-11-03T14:34:38.100863+00:00'
page_id: json_ProcessTaskInfoVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessTaskInfoVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessTaskInfoVO.html
version: 1
---

# ProcessTaskInfoVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| state | [ProcessStateVO](https://api.fluig.com/old/json_ProcessStateVO.html) |  |  |
| taskDeadline | number |  |  |
| stateSequence | number | required |  |
| transferredSequence | number | required |  |
| active | boolean | required |  |
| startDateTask | number |  |  |
| movementSequence | number | required |  |
| expired | boolean | required |  |
| colleagueName | string |  |  |
| status | number | required |  |

Example

```
{
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
}
```
