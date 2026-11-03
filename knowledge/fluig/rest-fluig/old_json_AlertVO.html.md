---
content_hash: f8014d1b05c8f6b6cef17bfae6d5e2a2c6de09796a3b82de04eaa5b58e68b8e0
fetched_at: '2026-11-03T14:34:36.138917+00:00'
page_id: json_AlertVO
product: fluig
source: rest-fluig
title: Fluig REST — AlertVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertVO.html
version: 1
---

# AlertVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| priority | string |  |
| senders | array of [AlertSenderVO](https://api.fluig.com/old/json_AlertSenderVO.html) |  |
| actions | array of [AlertActionVO](https://api.fluig.com/old/json_AlertActionVO.html) |  |
| read | boolean |  |
| canRemove | boolean |  |
| creationDate | number |  |
| event | [AlertEventVO](https://api.fluig.com/old/json_AlertEventVO.html) |  |
| currentDate | number |  |
| object | [AlertObjectVO](https://api.fluig.com/old/json_AlertObjectVO.html) |  |
| receiver | [AlertUserVO](https://api.fluig.com/old/json_AlertUserVO_vo.html) |  |
| place | [AlertObjectVO](https://api.fluig.com/old/json_AlertObjectVO.html) |  |
| id | number |  |

Example

```
{
  "priority" : "...",
  "senders" : [ {
    "user" : {
      "tenantId" : 12345,
      "lastUpdateDate" : 12345,
      "login" : "...",
      "id" : 12345,
      "lastName" : "...",
      "fisrtName" : "...",
      "fullName" : "..."
    },
    "via" : "...",
    "id" : 12345,
    "creationDate" : 12345
  }, {
    "user" : {
      "tenantId" : 12345,
      "lastUpdateDate" : 12345,
      "login" : "...",
      "id" : 12345,
      "lastName" : "...",
      "fisrtName" : "...",
      "fullName" : "..."
    },
    "via" : "...",
    "id" : 12345,
    "creationDate" : 12345
  } ],
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
  "read" : true,
  "canRemove" : true,
  "creationDate" : 12345,
  "event" : {
    "groupDescription" : "...",
    "active" : true,
    "descriptionKey" : "...",
    "id" : 12345,
    "singleDescriptionKey" : "...",
    "description" : "...",
    "required" : true,
    "grouped" : true,
    "groupDescriptionKey" : "...",
    "canRemove" : true,
    "singleDescription" : "...",
    "icon" : "...",
    "module" : {
      "id" : 12345,
      "moduleKey" : "...",
      "tenantId" : 12345,
      "description" : "..."
    },
    "onlyAdmin" : true,
    "eventKey" : "..."
  },
  "currentDate" : 12345,
  "object" : {
    "alertObjectDetailKey" : "...",
    "objectDetailKey" : "...",
    "alertObjectTypeDescriptionKey" : "...",
    "typeDescriptionKey" : "...",
    "link" : "...",
    "alertObjectDescription" : "...",
    "objectDetail" : "...",
    "objectClass" : "...",
    "description" : "...",
    "id" : 12345,
    "alertObjectId" : 12345,
    "objectId" : 12345,
    "note" : "...",
    "alertObjectNote" : "...",
    "alertObjectClass" : "...",
    "alertObjectLink" : "...",
    "typeDescription" : "..."
  },
  "receiver" : {
    "tenantId" : 12345,
    "lastUpdateDate" : 12345,
    "login" : "...",
    "id" : 12345,
    "lastName" : "...",
    "fisrtName" : "...",
    "fullName" : "..."
  },
  "place" : {
    "alertObjectDetailKey" : "...",
    "objectDetailKey" : "...",
    "alertObjectTypeDescriptionKey" : "...",
    "typeDescriptionKey" : "...",
    "link" : "...",
    "alertObjectDescription" : "...",
    "objectDetail" : "...",
    "objectClass" : "...",
    "description" : "...",
    "id" : 12345,
    "alertObjectId" : 12345,
    "objectId" : 12345,
    "note" : "...",
    "alertObjectNote" : "...",
    "alertObjectClass" : "...",
    "alertObjectLink" : "...",
    "typeDescription" : "..."
  },
  "id" : 12345
}
```
