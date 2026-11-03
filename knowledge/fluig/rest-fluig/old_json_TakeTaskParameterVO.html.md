---
content_hash: f85fbf8de99e7292f3c7117ad153f8bc616172323ddf29cecc7103e1cc556d99
fetched_at: '2026-11-03T14:34:38.656098+00:00'
page_id: json_TakeTaskParameterVO
product: fluig
source: rest-fluig
title: Fluig REST — TakeTaskParameterVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TakeTaskParameterVO.html
version: 1
---

# TakeTaskParameterVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| validateUser | boolean | required |  |
| replacementId | string |  |  |
| taskOwner | string |  |  |
| fromPool | boolean | required |  |
| processInstanceId | number | required |  |
| userId | string |  |  |
| tenantId | number | required |  |
| movementSequence | number | required |  |

Example

```
{
  "validateUser" : true,
  "replacementId" : "...",
  "taskOwner" : "...",
  "fromPool" : true,
  "processInstanceId" : 12345,
  "userId" : "...",
  "tenantId" : 12345,
  "movementSequence" : 12345
}
```
