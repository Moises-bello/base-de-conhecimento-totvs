---
content_hash: d06947fa7f226f6872a3b2d6a1ae92dfd9b8ed698b9934a7fac0bcf9b1da387b
fetched_at: '2026-11-03T14:34:36.853375+00:00'
page_id: json_FDNPermission
product: fluig
source: rest-fluig
title: Fluig REST — FDNPermission Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNPermission.html
version: 1
---

# FDNPermission Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| permission | string |  |
| tenantId | number |  |
| groupCode | string |  |
| login | string |  |
| roleCode | string |  |
| resource | [FDNResource](https://api.fluig.com/old/json_FDNResource.html) |  |
| description | string |  |

Example

```
{
  "id" : 12345,
  "permission" : "...",
  "tenantId" : 12345,
  "groupCode" : "...",
  "login" : "...",
  "roleCode" : "...",
  "resource" : {
    "description" : "...",
    "categoryResources" : [ {
      "tenantId" : 12345,
      "id" : 12345,
      "category" : { },
      "resource" : { }
    }, {
      "tenantId" : 12345,
      "id" : 12345,
      "category" : { },
      "resource" : { }
    } ],
    "longDescription" : "...",
    "tenantId" : 12345,
    "method" : "...",
    "code" : "...",
    "type" : {
      "isInternal" : true,
      "code" : "...",
      "id" : 12345,
      "description" : "..."
    },
    "isInternal" : true,
    "id" : 12345,
    "parent" : { },
    "typeCode" : "..."
  },
  "description" : "..."
}
```
