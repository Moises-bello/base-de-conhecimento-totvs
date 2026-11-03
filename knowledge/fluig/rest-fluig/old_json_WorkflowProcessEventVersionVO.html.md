---
content_hash: 16f9365091190f77bd56aec3088e21d731e26b437792ec3a12e232e33c30c413
fetched_at: '2026-11-03T14:34:39.112822+00:00'
page_id: json_WorkflowProcessEventVersionVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowProcessEventVersionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowProcessEventVersionVO.html
version: 1
---

# WorkflowProcessEventVersionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| scriptVersion | number | required |  |
| author | string |  |  |
| instances | number | required |  |
| createDate | number |  |  |
| defaultVersion | boolean | required |  |

Example

```
{
  "scriptVersion" : 12345,
  "author" : "...",
  "instances" : 12345,
  "createDate" : 12345,
  "defaultVersion" : true
}
```
