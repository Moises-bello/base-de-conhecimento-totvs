---
content_hash: 409fa90090eba6b7b7a556ae0e6e2ea8cbf4795c2707c98becbaabd4afc2e248
fetched_at: '2026-11-03T14:34:36.326291+00:00'
page_id: json_CancelInstanceParameterVO
product: fluig
source: rest-fluig
title: Fluig REST — CancelInstanceParameterVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CancelInstanceParameterVO.html
version: 1
---

# CancelInstanceParameterVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| service | boolean | required |  |
| companyId | number | required |  |
| cancelText | string |  |  |
| validateRequester | boolean | required |  |
| userId | string |  |  |
| reactivate | boolean | required |  |
| replacementId | string |  |  |
| processInstanceId | number | required |  |

Example

```
{
  "service" : true,
  "companyId" : 12345,
  "cancelText" : "...",
  "validateRequester" : true,
  "userId" : "...",
  "reactivate" : true,
  "replacementId" : "...",
  "processInstanceId" : 12345
}
```
