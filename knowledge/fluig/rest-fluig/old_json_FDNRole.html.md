---
content_hash: d80c63352db95e5a56fd0f6508314bbff64389db8dcaea90ec16284530e7425f
fetched_at: '2026-11-03T14:34:36.869581+00:00'
page_id: json_FDNRole
product: fluig
source: rest-fluig
title: Fluig REST — FDNRole Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNRole.html
version: 1
---

# FDNRole Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| description | string |  |
| code | string |  |
| data | array of [FDNRoleData](https://api.fluig.com/old/json_FDNRoleData.html) |  |
| tenantId | number |  |
| internal | boolean |  |

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
  "description" : "...",
  "code" : "...",
  "data" : [ {
    "id" : 12345,
    "dataValue" : "...",
    "dataKey" : "...",
    "role" : {
      "id" : 12345,
      "tenant" : { },
      "description" : "...",
      "code" : "...",
      "data" : [ { }, { } ],
      "tenantId" : 12345,
      "internal" : true
    }
  }, {
    "id" : 12345,
    "dataValue" : "...",
    "dataKey" : "...",
    "role" : {
      "id" : 12345,
      "tenant" : { },
      "description" : "...",
      "code" : "...",
      "data" : [ { }, { } ],
      "tenantId" : 12345,
      "internal" : true
    }
  } ],
  "tenantId" : 12345,
  "internal" : true
}
```
