---
content_hash: 193f5a48d5fcf229e19ca489e27695e73aba3ae4535c5082055eb41c3b19e5f4
fetched_at: '2026-11-03T14:34:36.812098+00:00'
page_id: json_FDNCategoryResource
product: fluig
source: rest-fluig
title: Fluig REST — FDNCategoryResource Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNCategoryResource.html
version: 1
---

# FDNCategoryResource Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| tenantId | number |  |
| id | number |  |
| category | [FDNCategory](https://api.fluig.com/old/json_FDNCategory.html) |  |
| resource | [FDNResource](https://api.fluig.com/old/json_FDNResource.html) |  |

Example

```
{
  "tenantId" : 12345,
  "id" : 12345,
  "category" : {
    "parentId" : 12345,
    "iconUrl" : "...",
    "id" : 12345,
    "internal" : true,
    "description" : "...",
    "hidden" : true,
    "name" : "...",
    "tenantId" : 12345,
    "code" : "..."
  },
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
  }
}
```
