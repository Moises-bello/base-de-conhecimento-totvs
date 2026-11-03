---
content_hash: 67ed0c1ebffd7e71f36dd96f7a2738eac6fab6649bec2a17efb6019b72dd17f4
fetched_at: '2026-11-03T14:34:38.324744+00:00'
page_id: json_SearchGroupResultVO
product: fluig
source: rest-fluig
title: Fluig REST — SearchGroupResultVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SearchGroupResultVO.html
version: 1
---

# SearchGroupResultVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| groups | array of [FDNGroupVO](https://api.fluig.com/old/json_FDNGroupVO.html) |  |
| hasNext | boolean |  |

Example

```
{
  "groups" : [ {
    "data" : [ {
      "value" : "...",
      "key" : "..."
    }, {
      "value" : "...",
      "key" : "..."
    } ],
    "groupUserRoleId" : 12345,
    "login" : "...",
    "dataMap" : {
      "property1" : "...",
      "property2" : "..."
    },
    "permissions" : [ {
      "resourceId" : 12345,
      "permission" : "...",
      "permissionId" : 12345,
      "categoryId" : 12345,
      "resourceCode" : "..."
    }, {
      "resourceId" : 12345,
      "permission" : "...",
      "permissionId" : 12345,
      "categoryId" : 12345,
      "resourceCode" : "..."
    } ],
    "groupCode" : "...",
    "groupType" : "...",
    "groupParticipantsCount" : 12345,
    "description" : "...",
    "roleCode" : "...",
    "groupId" : 12345,
    "groupDescription" : "...",
    "typeCode" : "...",
    "childGroupCode" : "...",
    "tenantId" : 12345,
    "code" : "...",
    "id" : 12345,
    "isCloudDefault" : true
  }, {
    "data" : [ {
      "value" : "...",
      "key" : "..."
    }, {
      "value" : "...",
      "key" : "..."
    } ],
    "groupUserRoleId" : 12345,
    "login" : "...",
    "dataMap" : {
      "property1" : "...",
      "property2" : "..."
    },
    "permissions" : [ {
      "resourceId" : 12345,
      "permission" : "...",
      "permissionId" : 12345,
      "categoryId" : 12345,
      "resourceCode" : "..."
    }, {
      "resourceId" : 12345,
      "permission" : "...",
      "permissionId" : 12345,
      "categoryId" : 12345,
      "resourceCode" : "..."
    } ],
    "groupCode" : "...",
    "groupType" : "...",
    "groupParticipantsCount" : 12345,
    "description" : "...",
    "roleCode" : "...",
    "groupId" : 12345,
    "groupDescription" : "...",
    "typeCode" : "...",
    "childGroupCode" : "...",
    "tenantId" : 12345,
    "code" : "...",
    "id" : 12345,
    "isCloudDefault" : true
  } ],
  "hasNext" : true
}
```
