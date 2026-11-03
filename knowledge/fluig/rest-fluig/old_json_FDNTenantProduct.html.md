---
content_hash: 4cf85fdd74929e84abc564503a47ee147c447ca8297907381477c64f0de48c1d
fetched_at: '2026-11-03T14:34:36.889125+00:00'
page_id: json_FDNTenantProduct
product: fluig
source: rest-fluig
title: Fluig REST — FDNTenantProduct Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNTenantProduct.html
version: 1
---

# FDNTenantProduct Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| product | string |  |

Example

```
{
  "id" : 12345,
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
  "product" : "..."
}
```
