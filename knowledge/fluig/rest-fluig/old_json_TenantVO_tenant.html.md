---
content_hash: 03932c669408d152dd8502abe937e4e5037816175427d3856dee0b52cc5a638a
fetched_at: '2026-11-03T14:34:38.691516+00:00'
page_id: json_TenantVO_tenant
product: fluig
source: rest-fluig
title: Fluig REST — TenantVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TenantVO_tenant.html
version: 1
---

# TenantVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| federalId | string |  |
| description | string |  |
| organizationUrl | string |  |
| data | map of string |  |
| thumbnailEnabled | boolean |  |
| id | number |  |
| idpId | string |  |
| volumeDir | string |  |
| idpLogOff | boolean |  |
| removeVolume | boolean |  |
| adminUser | [AdminUserVO](https://api.fluig.com/old/json_AdminUserVO.html) |  |
| tenantActive | boolean |  |
| code | string |  |

Example

```
{
  "federalId" : "...",
  "description" : "...",
  "organizationUrl" : "...",
  "data" : {
    "property1" : "...",
    "property2" : "..."
  },
  "thumbnailEnabled" : true,
  "id" : 12345,
  "idpId" : "...",
  "volumeDir" : "...",
  "idpLogOff" : true,
  "removeVolume" : true,
  "adminUser" : {
    "email" : "...",
    "lastName" : "...",
    "code" : "...",
    "login" : "...",
    "firstName" : "..."
  },
  "tenantActive" : true,
  "code" : "..."
}
```
