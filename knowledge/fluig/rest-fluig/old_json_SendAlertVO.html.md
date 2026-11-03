---
content_hash: 29a9afbc1b0ac443042c272c9d447c2e56359d451c129e20fcb7f1ba81be2d3a
fetched_at: '2026-11-03T14:34:38.354125+00:00'
page_id: json_SendAlertVO
product: fluig
source: rest-fluig
title: Fluig REST — SendAlertVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SendAlertVO.html
version: 1
---

# SendAlertVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| eventKey | string |  |
| loginReceiver | string |  |
| object | [GenericAlertObject](https://api.fluig.com/old/json_GenericAlertObject.html) |  |
| place | [GenericAlertObject](https://api.fluig.com/old/json_GenericAlertObject.html) |  |
| actions | array of [AlertActionVO](https://api.fluig.com/old/json_AlertActionVO.html) |  |
| metadata | map of string |  |
| priority | string |  |

Example

```
{
  "eventKey" : "...",
  "loginReceiver" : "...",
  "object" : {
    "alertObjectTypeDescriptionKey" : "...",
    "alertObjectClass" : "...",
    "alertObjectDetailKey" : "...",
    "alertObjectId" : 12345,
    "alertObjectDescription" : "...",
    "alertObjectLink" : "...",
    "alertObjectNote" : "..."
  },
  "place" : {
    "alertObjectTypeDescriptionKey" : "...",
    "alertObjectClass" : "...",
    "alertObjectDetailKey" : "...",
    "alertObjectId" : 12345,
    "alertObjectDescription" : "...",
    "alertObjectLink" : "...",
    "alertObjectNote" : "..."
  },
  "actions" : [ {
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
  }, {
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
  } ],
  "metadata" : {
    "property1" : "...",
    "property2" : "..."
  },
  "priority" : "..."
}
```
