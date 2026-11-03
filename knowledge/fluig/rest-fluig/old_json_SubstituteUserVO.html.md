---
content_hash: 613e046103dccd914b038260d6403a1d6e69ab5023a01758ec7f23dd8eea13fc
fetched_at: '2026-11-03T14:34:38.619137+00:00'
page_id: json_SubstituteUserVO
product: fluig
source: rest-fluig
title: Fluig REST — SubstituteUserVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SubstituteUserVO.html
version: 1
---

# SubstituteUserVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| id | number | required |  |
| companyId | number | required |  |
| userId | string |  |  |
| substituteId | string |  |  |
| validationStartDate | string |  |  |
| validationFinalDate | string |  |  |
| viewWorkflowTasks | boolean |  |  |
| viewGEDTasks | boolean |  |  |
| processes | array of [SubstituteUserProcessVO](https://api.fluig.com/old/json_SubstituteUserProcessVO.html) |  |  |
| userLastUpdateDate | number |  |  |
| userName | string |  |  |
| userAlias | string |  |  |
| substituteLastUpdateDate | number |  |  |
| substituteAlias | string |  |  |
| substituteName | string |  |  |

Example

```
{
  "id" : 12345,
  "companyId" : 12345,
  "userId" : "...",
  "substituteId" : "...",
  "validationStartDate" : "...",
  "validationFinalDate" : "...",
  "viewWorkflowTasks" : true,
  "viewGEDTasks" : true,
  "processes" : [ {
    "companyId" : 12345,
    "userId" : "...",
    "substituteId" : "...",
    "process" : "..."
  }, {
    "companyId" : 12345,
    "userId" : "...",
    "substituteId" : "...",
    "process" : "..."
  } ],
  "userLastUpdateDate" : 12345,
  "userName" : "...",
  "userAlias" : "...",
  "substituteLastUpdateDate" : 12345,
  "substituteAlias" : "...",
  "substituteName" : "..."
}
```
