---
content_hash: 08cc6cf3174157d38884b7510ed422561256ea72f6a11c5da79c204a21d477b1
fetched_at: '2026-11-03T14:34:39.102273+00:00'
page_id: json_WorkflowProcessErrorLogStatusVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowProcessErrorLogStatusVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowProcessErrorLogStatusVO.html
version: 1
---

# WorkflowProcessErrorLogStatusVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| totalInstancesThatLastMovementReturnError | number | required |  |
| totalProcessVersionWithInstancesThatLastMovementReturnError | number | required |  |
| totalInstancesWithMovement | number | required |  |
| totalProcessVersionWithInstances | number | required |  |

Example

```
{
  "totalInstancesThatLastMovementReturnError" : 12345,
  "totalProcessVersionWithInstancesThatLastMovementReturnError" : 12345,
  "totalInstancesWithMovement" : 12345,
  "totalProcessVersionWithInstances" : 12345
}
```
