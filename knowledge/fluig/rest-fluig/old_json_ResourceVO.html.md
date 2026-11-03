---
content_hash: 7947ef6cedf6113978ded399220943380ea99e2bab70e09008b2b6a766744a82
fetched_at: '2026-11-03T14:34:38.257944+00:00'
page_id: json_ResourceVO
product: fluig
source: rest-fluig
title: Fluig REST — ResourceVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ResourceVO.html
version: 1
---

# ResourceVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| code | string |  |
| id | number |  |
| permissions | array of [PermissionVO](https://api.fluig.com/old/json_PermissionVO_vo.html) |  |
| longDescription | string |  |
| parentId | number |  |
| type | string |  |
| tenantId | number |  |
| category | string |  |
| description | string |  |
| isInternal | boolean |  |
| method | string |  |

Example

```
{
  "code" : "...",
  "id" : 12345,
  "permissions" : [ {
    "permission" : "...",
    "tenantId" : 12345,
    "role" : "...",
    "user" : "...",
    "group" : "...",
    "resource" : "...",
    "description" : "..."
  }, {
    "permission" : "...",
    "tenantId" : 12345,
    "role" : "...",
    "user" : "...",
    "group" : "...",
    "resource" : "...",
    "description" : "..."
  } ],
  "longDescription" : "...",
  "parentId" : 12345,
  "type" : "...",
  "tenantId" : 12345,
  "category" : "...",
  "description" : "...",
  "isInternal" : true,
  "method" : "..."
}
```
