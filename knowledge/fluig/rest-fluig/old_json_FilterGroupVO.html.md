---
content_hash: 5721f3e5f970e11c6db9fee72eb398af9e39447dbea2cf4e9dcc6ba5e0180688
fetched_at: '2026-11-03T14:34:36.979287+00:00'
page_id: json_FilterGroupVO
product: fluig
source: rest-fluig
title: Fluig REST — FilterGroupVO Data Type
type: documentation
url: https://api.fluig.com/old/json_FilterGroupVO.html
version: 1
---

# FilterGroupVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| filterId | number |  |
| entityPermissions | map of number |  |
| rolesCode | array of string |  |
| tenantUserLogin | array of string |  |
| groupsCode | array of string |  |

Example

```
{
  "filterId" : 12345,
  "entityPermissions" : {
    "property1" : 12345,
    "property2" : 12345
  },
  "rolesCode" : [ "...", "..." ],
  "tenantUserLogin" : [ "...", "..." ],
  "groupsCode" : [ "...", "..." ]
}
```
