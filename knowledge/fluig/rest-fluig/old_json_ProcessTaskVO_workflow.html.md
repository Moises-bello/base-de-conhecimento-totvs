---
content_hash: 5be613f991cc366363b13105f709049fac27511601a6e5284931442ca4991350
fetched_at: '2026-11-03T14:34:38.112351+00:00'
page_id: json_ProcessTaskVO_workflow
product: fluig
source: rest-fluig
title: Fluig REST — ProcessTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessTaskVO_workflow.html
version: 1
---

# ProcessTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| selectedColleagueId | string |  |  |
| transferredSequence | number | required |  |
| movementSequence | number | required |  |
| companyId | number | required |  |
| colleagueId | string |  |  |
| complement | string |  |  |
| processInstanceId | number | required |  |

Example

```
{
  "selectedColleagueId" : "...",
  "transferredSequence" : 12345,
  "movementSequence" : 12345,
  "companyId" : 12345,
  "colleagueId" : "...",
  "complement" : "...",
  "processInstanceId" : 12345
}
```
