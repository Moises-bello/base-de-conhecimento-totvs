---
content_hash: e1e0d89241ead746bae2ef383102073787e218e6d014b53f731f31a8ae0c8f20
fetched_at: '2026-11-03T14:34:36.940799+00:00'
page_id: json_FDNVolumeSite
product: fluig
source: rest-fluig
title: Fluig REST — FDNVolumeSite Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNVolumeSite.html
version: 1
---

# FDNVolumeSite Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| volumeId | number |  |
| storage | string |  |
| site | [FDNSite](https://api.fluig.com/old/json_FDNSite.html) |  |
| siteId | number |  |
| volume | [FDNVolume](https://api.fluig.com/old/json_FDNVolume.html) |  |
| id | number |  |

Example

```
{
  "volumeId" : 12345,
  "storage" : "...",
  "site" : {
    "siteCode" : "...",
    "tenant" : {
      "federalId" : "...",
      "idpId" : "...",
      "resourceType" : "...",
      "useWizard" : true,
      "code" : "...",
      "organizationUrl" : "...",
      "tenantActive" : true,
      "products" : [ { }, { } ],
      "idpLogOff" : true,
      "id" : 12345,
      "resourceDescription" : "...",
      "data" : [ { }, { } ],
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
  },
  "siteId" : 12345,
  "volume" : {
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
      "products" : [ { }, { } ],
      "idpLogOff" : true,
      "id" : 12345,
      "resourceDescription" : "...",
      "data" : [ { }, { } ],
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
  },
  "id" : 12345
}
```
