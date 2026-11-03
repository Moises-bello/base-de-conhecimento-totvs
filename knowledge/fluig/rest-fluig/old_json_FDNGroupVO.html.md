---
content_hash: 487a1b9870935fa9cb42e262cc1a9e0277f8980d68323ef670f38d584030ee13
fetched_at: '2026-11-03T14:34:36.835805+00:00'
page_id: json_FDNGroupVO
product: fluig
source: rest-fluig
title: Fluig REST — FDNGroupVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNGroupVO.html
version: 1
---

# FDNGroupVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| data | array of [FDNGroupDataVO](https://api.fluig.com/old/json_FDNGroupDataVO.html) |  |  |
| groupUserRoleId | number |  |  |
| login | string |  |  |
| dataMap | map of string |  |  |
| permissions | array of [PermissionResourceVO](https://api.fluig.com/old/json_PermissionResourceVO.html) |  |  |
| groupCode | string |  |  |
| groupType | string |  |  |
| groupParticipantsCount | number | required |  |
| description | string |  |  |
| roleCode | string |  |  |
| groupId | number |  |  |
| groupDescription | string |  |  |
| typeCode | string |  |  |
| childGroupCode | string |  |  |
| tenantId | number |  |  |
| code | string |  |  |
| id | number |  |  |
| isCloudDefault | boolean |  |  |

Example

```
{
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
}
```
