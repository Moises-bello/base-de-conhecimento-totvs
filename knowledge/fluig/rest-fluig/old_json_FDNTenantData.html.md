---
content_hash: 1d6883ec3a22f7a5247b4749071912d02371d05ee7308356e7611604bb700cdd
fetched_at: '2026-11-03T14:34:36.885501+00:00'
page_id: json_FDNTenantData
product: fluig
source: rest-fluig
title: Fluig REST — FDNTenantData Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNTenantData.html
version: 1
---

# FDNTenantData Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| hide | boolean |  |
| dataKey | string |  |
| dataValue | string |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| id | number |  |

Example

```
{
  "hide" : true,
  "dataKey" : "...",
  "dataValue" : "...",
  "tenant" : {
    "federalId" : "...",
    "idpId" : "...",
    "resourceType" : "...",
    "useWizard" : true,
    "code" : "...",
    "organizationUrl" : "...",
    "tenantActive" : true,
    "products" : [ {
      "id" : 12345,
      "tenant" : { },
      "product" : "..."
    }, {
      "id" : 12345,
      "tenant" : { },
      "product" : "..."
    } ],
    "idpLogOff" : true,
    "id" : 12345,
    "resourceDescription" : "...",
    "data" : [ {
      "hide" : true,
      "dataKey" : "...",
      "dataValue" : "...",
      "tenant" : { },
      "id" : 12345
    }, {
      "hide" : true,
      "dataKey" : "...",
      "dataValue" : "...",
      "tenant" : { },
      "id" : 12345
    } ],
    "securityCode" : "...",
    "thumbnailEnabled" : true,
    "UUID" : "...",
    "description" : "...",
    "removeVolume" : true
  },
  "id" : 12345
}
```
