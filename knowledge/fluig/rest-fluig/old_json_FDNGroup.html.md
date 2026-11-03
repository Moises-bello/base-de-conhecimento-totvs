---
content_hash: 7057e6a4dd9f2eab775622dd301ddcc28d0750532cf59f16c0e3b360f588c5bb
fetched_at: '2026-11-03T14:34:36.819859+00:00'
page_id: json_FDNGroup
product: fluig
source: rest-fluig
title: Fluig REST — FDNGroup Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNGroup.html
version: 1
---

# FDNGroup Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| groupType | string |  |
| code | string |  |
| id | number |  |
| description | string |  |
| isInternal | boolean |  |
| tenantId | number |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| data | array of [FDNGroupData](https://api.fluig.com/old/json_FDNGroupData.html) |  |

Example

```
{
  "groupType" : "...",
  "code" : "...",
  "id" : 12345,
  "description" : "...",
  "isInternal" : true,
  "tenantId" : 12345,
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
  "data" : [ {
    "group" : {
      "groupType" : "...",
      "code" : "...",
      "id" : 12345,
      "description" : "...",
      "isInternal" : true,
      "tenantId" : 12345,
      "tenant" : { },
      "data" : [ { }, { } ]
    },
    "dataKey" : "...",
    "id" : 12345,
    "dataValue" : "..."
  }, {
    "group" : {
      "groupType" : "...",
      "code" : "...",
      "id" : 12345,
      "description" : "...",
      "isInternal" : true,
      "tenantId" : 12345,
      "tenant" : { },
      "data" : [ { }, { } ]
    },
    "dataKey" : "...",
    "id" : 12345,
    "dataValue" : "..."
  } ]
}
```
