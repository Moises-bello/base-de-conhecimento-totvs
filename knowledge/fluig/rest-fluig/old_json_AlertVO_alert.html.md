---
content_hash: e1cad5ba21109b6db51c6e050802d512bbc4a67cb5e1afe8de13022484141e37
fetched_at: '2026-11-03T14:34:36.143973+00:00'
page_id: json_AlertVO_alert
product: fluig
source: rest-fluig
title: Fluig REST — AlertVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertVO_alert.html
version: 1
---

# AlertVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| event | [AlertEventVO](https://api.fluig.com/old/json_AlertEventVO_alert.html) |  |
| place | [AlertObjectVO](https://api.fluig.com/old/json_AlertObjectVO_alert.html) |  |
| senders | array of [AlertSenderVO](https://api.fluig.com/old/json_AlertSenderVO_alert.html) |  |
| read | boolean |  |
| creationDateTime | number |  |
| priority | string |  |
| object | [AlertObjectVO](https://api.fluig.com/old/json_AlertObjectVO_alert.html) |  |
| actions | array of [AlertActionVO](https://api.fluig.com/old/json_AlertActionVO_alert.html) |  |
| canRemove | boolean |  |
| creationDate | number |  |
| id | number |  |
| currentDate | number |  |
| receiver | [AlertUserVO](https://api.fluig.com/old/json_AlertUserVO.html) |  |

Example

```
{
  "event" : {
    "canRemove" : true,
    "groupDescription" : "...",
    "eventKey" : "...",
    "icon" : "...",
    "groupDescriptionKey" : "...",
    "id" : 12345,
    "onlyAdmin" : true,
    "description" : "...",
    "descriptionKey" : "...",
    "singleDescriptionKey" : "...",
    "active" : true,
    "grouped" : true,
    "module" : {
      "description" : "...",
      "id" : 12345,
      "moduleKey" : "...",
      "tenantId" : 12345
    },
    "singleDescription" : "...",
    "required" : true
  },
  "place" : {
    "typeDescriptionKey" : "...",
    "objectDetail" : "...",
    "note" : "...",
    "objectId" : 12345,
    "objectClass" : "...",
    "objectDetailKey" : "...",
    "typeDescription" : "...",
    "link" : "...",
    "description" : "...",
    "id" : 12345
  },
  "senders" : [ {
    "via" : "...",
    "user" : {
      "fullName" : "...",
      "lastUpdateDate" : 12345,
      "login" : "...",
      "fisrtName" : "...",
      "lastName" : "...",
      "tenantId" : 12345,
      "id" : 12345
    },
    "creationDate" : 12345,
    "id" : 12345
  }, {
    "via" : "...",
    "user" : {
      "fullName" : "...",
      "lastUpdateDate" : 12345,
      "login" : "...",
      "fisrtName" : "...",
      "lastName" : "...",
      "tenantId" : 12345,
      "id" : 12345
    },
    "creationDate" : 12345,
    "id" : 12345
  } ],
  "read" : true,
  "creationDateTime" : 12345,
  "priority" : "...",
  "object" : {
    "typeDescriptionKey" : "...",
    "objectDetail" : "...",
    "note" : "...",
    "objectId" : 12345,
    "objectClass" : "...",
    "objectDetailKey" : "...",
    "typeDescription" : "...",
    "link" : "...",
    "description" : "...",
    "id" : 12345
  },
  "actions" : [ {
    "type" : "...",
    "description" : "...",
    "url" : "...",
    "descriptionAfterExec" : "...",
    "actionKey" : "...",
    "descriptionKey" : "...",
    "executed" : true,
    "integrationType" : "...",
    "descriptionAfterExecKey" : "...",
    "id" : 12345,
    "actionType" : "...",
    "httpMethod" : "..."
  }, {
    "type" : "...",
    "description" : "...",
    "url" : "...",
    "descriptionAfterExec" : "...",
    "actionKey" : "...",
    "descriptionKey" : "...",
    "executed" : true,
    "integrationType" : "...",
    "descriptionAfterExecKey" : "...",
    "id" : 12345,
    "actionType" : "...",
    "httpMethod" : "..."
  } ],
  "canRemove" : true,
  "creationDate" : 12345,
  "id" : 12345,
  "currentDate" : 12345,
  "receiver" : {
    "fullName" : "...",
    "lastUpdateDate" : 12345,
    "login" : "...",
    "fisrtName" : "...",
    "lastName" : "...",
    "tenantId" : 12345,
    "id" : 12345
  }
}
```
