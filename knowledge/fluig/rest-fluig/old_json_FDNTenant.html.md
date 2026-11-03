---
content_hash: c84bd731860ad0df94a3a031480175d278df5c3a5c2e03a8cf9dab276a29e340
fetched_at: '2026-11-03T14:34:36.882442+00:00'
page_id: json_FDNTenant
product: fluig
source: rest-fluig
title: Fluig REST — FDNTenant Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNTenant.html
version: 1
---

# FDNTenant Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| federalId | string |  |
| idpId | string |  |
| resourceType | string |  |
| useWizard | boolean |  |
| code | string |  |
| organizationUrl | string |  |
| tenantActive | boolean |  |
| products | array of [FDNTenantProduct](https://api.fluig.com/old/json_FDNTenantProduct.html) |  |
| idpLogOff | boolean |  |
| id | number |  |
| resourceDescription | string |  |
| data | array of [FDNTenantData](https://api.fluig.com/old/json_FDNTenantData.html) |  |
| securityCode | string |  |
| thumbnailEnabled | boolean |  |
| UUID | string |  |
| description | string |  |
| removeVolume | boolean |  |

Example

```
{
  "federalId" : "...",
  "idpId" : "...",
  "resourceType" : "...",
  "useWizard" : true,
  "code" : "...",
  "organizationUrl" : "...",
  "tenantActive" : true,
  "products" : [ {
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
    "product" : "..."
  }, {
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
    "product" : "..."
  } ],
  "idpLogOff" : true,
  "id" : 12345,
  "resourceDescription" : "...",
  "data" : [ {
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
    "id" : 12345
  }, {
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
    "id" : 12345
  } ],
  "securityCode" : "...",
  "thumbnailEnabled" : true,
  "UUID" : "...",
  "description" : "...",
  "removeVolume" : true
}
```
