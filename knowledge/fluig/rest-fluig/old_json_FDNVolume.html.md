---
content_hash: bd002338bcdc682fd7988a95e8aa0dc8d6624e2dcea29e92abf27aebcf943e1d
fetched_at: '2026-11-03T14:34:36.937322+00:00'
page_id: json_FDNVolume
product: fluig
source: rest-fluig
title: Fluig REST — FDNVolume Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNVolume.html
version: 1
---

# FDNVolume Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| volumeCode | string |  |  |
| volumeType | number | required |  |
| id | number |  |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |  |
| maxSize | number | required |  |
| tenantId | number |  |  |
| usedSpace | number | required |  |
| documentId | number |  |  |

Example

```
{
  "volumeCode" : "...",
  "volumeType" : 12345,
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
  "maxSize" : 12345.0,
  "tenantId" : 12345,
  "usedSpace" : 12345.0,
  "documentId" : 12345
}
```
