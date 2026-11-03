---
content_hash: abb788a0a3429568443a413da9f5bcd7a537854ad3bdc5d2ec6d69056e76b844
fetched_at: '2026-11-03T14:34:38.824969+00:00'
page_id: json_WCMApplicationDependency
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationDependency Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationDependency.html
version: 1
---

# WCMApplicationDependency Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| resourceType | string |  |
| createdAt | number |  |
| code | string |  |
| updatedAt | number |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| id | number |  |

Example

```
{
  "resourceType" : "...",
  "createdAt" : 12345,
  "code" : "...",
  "updatedAt" : 12345,
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
