---
content_hash: 09528e5fc50a31229b05b9ec0a69695f372bed5df1a5b91f48c07de889f3a7ac
fetched_at: '2026-11-03T14:34:36.075166+00:00'
page_id: json_AlertActionVO
product: fluig
source: rest-fluig
title: Fluig REST — AlertActionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertActionVO.html
version: 1
---

# AlertActionVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| url | string |  |
| descriptionAfterExec | string |  |
| integrationType | [FDNAlertIntegrationType](https://api.fluig.com/old/json_FDNAlertIntegrationType.html) |  |
| id | number |  |
| executed | boolean |  |
| actionKey | string |  |
| type | [FDNAlertIntegrationType](https://api.fluig.com/old/json_FDNAlertIntegrationType.html) |  |
| actionType | [FDNAlertActionType](https://api.fluig.com/old/json_FDNAlertActionType.html) |  |
| description | string |  |
| httpMethod | string |  |
| descriptionKey | string |  |
| descriptionAfterExecKey | string |  |

Example

```
{
  "url" : "...",
  "descriptionAfterExec" : "...",
  "integrationType" : { },
  "id" : 12345,
  "executed" : true,
  "actionKey" : "...",
  "type" : { },
  "actionType" : { },
  "description" : "...",
  "httpMethod" : "...",
  "descriptionKey" : "...",
  "descriptionAfterExecKey" : "..."
}
```
