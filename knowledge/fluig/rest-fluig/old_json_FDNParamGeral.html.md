---
content_hash: a6be00d1ed6b66d2b1507d549835ff57b6ddd627f3fe28fa74bc56473cc2e43b
fetched_at: '2026-11-03T14:34:36.849820+00:00'
page_id: json_FDNParamGeral
product: fluig
source: rest-fluig
title: Fluig REST — FDNParamGeral Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNParamGeral.html
version: 1
---

# FDNParamGeral Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| id | number |  |
| dataKey | string |  |
| tenantId | number |  |
| dataValue | string |  |

Example

```
{
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
  "id" : 12345,
  "dataKey" : "...",
  "tenantId" : 12345,
  "dataValue" : "..."
}
```
