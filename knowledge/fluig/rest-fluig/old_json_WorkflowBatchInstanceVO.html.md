---
content_hash: 921c2066818b9853b77a1bf5d6f84b2c6d00223b1905c9ea36b61462d49dd22c
fetched_at: '2026-11-03T14:34:39.057575+00:00'
page_id: json_WorkflowBatchInstanceVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowBatchInstanceVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowBatchInstanceVO.html
version: 1
---

# WorkflowBatchInstanceVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| observation | string |  |  |
| managerMode | boolean | required |  |
| selectedColleagues | array of string |  |  |
| movementSequence | number |  |  |
| tenantId | number | required |  |
| userId | string |  |  |
| replacementId | string |  |  |
| instanceId | number |  |  |
| selectedState | number | required |  |

Example

```
{
  "observation" : "...",
  "managerMode" : true,
  "selectedColleagues" : [ "...", "..." ],
  "movementSequence" : 12345,
  "tenantId" : 12345,
  "userId" : "...",
  "replacementId" : "...",
  "instanceId" : 12345,
  "selectedState" : 12345
}
```
