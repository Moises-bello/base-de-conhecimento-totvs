---
content_hash: 4814e29f2532d301b0da2f624a041fed09bc7925972bd903d0122d0f2d617628
fetched_at: '2026-11-03T14:34:36.877253+00:00'
page_id: json_FDNSite
product: fluig
source: rest-fluig
title: Fluig REST — FDNSite Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNSite.html
version: 1
---

# FDNSite Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| siteCode | string |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| active | boolean |  |
| local | [FDNLocal](https://api.fluig.com/old/json_FDNLocal.html) |  |
| id | number |  |
| tenantId | number |  |
| siteURL | string |  |
| maximumRetries | number |  |
| streamLimit | number |  |
| copyLimit | number |  |

Example

```
{
  "siteCode" : "...",
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
  "active" : true,
  "local" : { },
  "id" : 12345,
  "tenantId" : 12345,
  "siteURL" : "...",
  "maximumRetries" : 12345,
  "streamLimit" : 12345,
  "copyLimit" : 12345
}
```
