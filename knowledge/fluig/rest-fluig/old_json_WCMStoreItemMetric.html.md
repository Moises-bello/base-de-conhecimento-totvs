---
content_hash: 8bdd3e1c04795edd1745d31289670ba927fec81117d65e0bbe89bc214569e6d0
fetched_at: '2026-11-03T14:34:38.950102+00:00'
page_id: json_WCMStoreItemMetric
product: fluig
source: rest-fluig
title: Fluig REST — WCMStoreItemMetric Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMStoreItemMetric.html
version: 1
---

# WCMStoreItemMetric Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| views | number |  |
| developerCode | string |  |
| id | number |  |
| downloads | number |  |
| developerName | string |  |
| name | string |  |
| componentCode | string |  |

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
  "views" : 12345,
  "developerCode" : "...",
  "id" : 12345,
  "downloads" : 12345,
  "developerName" : "...",
  "name" : "...",
  "componentCode" : "..."
}
```
