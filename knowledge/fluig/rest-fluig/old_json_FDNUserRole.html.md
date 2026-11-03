---
content_hash: c2a263cc935812b37bf522adc497c467f257dec6d71db0a286cd8b4b211a0342
fetched_at: '2026-11-03T14:34:36.917465+00:00'
page_id: json_FDNUserRole
product: fluig
source: rest-fluig
title: Fluig REST — FDNUserRole Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUserRole.html
version: 1
---

# FDNUserRole Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| roleCode | string |  |
| user | [FDNUserTenant](https://api.fluig.com/old/json_FDNUserTenant.html) |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| tenantId | number |  |
| login | string |  |
| id | number |  |
| role | [FDNRole](https://api.fluig.com/old/json_FDNRole.html) |  |

Example

```
{
  "roleCode" : "...",
  "user" : {
    "data" : [ {
      "dataKey" : "...",
      "id" : 12345,
      "anonymizationUser" : { },
      "dataValue" : "...",
      "user" : { },
      "hide" : true,
      "anonymizationDate" : 12345
    }, {
      "dataKey" : "...",
      "id" : 12345,
      "anonymizationUser" : { },
      "dataValue" : "...",
      "user" : { },
      "hide" : true,
      "anonymizationDate" : 12345
    } ],
    "firstAccess" : true,
    "locationId" : 12345,
    "userCode" : "...",
    "userState" : "ACTIVE",
    "userId" : 12345,
    "anonymizationDate" : 12345,
    "id" : 12345,
    "user" : {
      "birthDate" : 12345,
      "anonymizationUser" : { },
      "firstName" : "...",
      "userType" : "NORMAL",
      "anonymizationDate" : 12345,
      "lastName" : "...",
      "id" : 12345,
      "fullName" : "..."
    },
    "password" : "...",
    "lastSecurityUpdateDate" : 12345,
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
    "email" : "...",
    "idpId" : "...",
    "lastUpdateDate" : 12345,
    "anonymizationUser" : { },
    "tenantId" : 12345,
    "userUUID" : "...",
    "login" : "..."
  },
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
  "tenantId" : 12345,
  "login" : "...",
  "id" : 12345,
  "role" : {
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
    "description" : "...",
    "code" : "...",
    "data" : [ {
      "id" : 12345,
      "dataValue" : "...",
      "dataKey" : "...",
      "role" : { }
    }, {
      "id" : 12345,
      "dataValue" : "...",
      "dataKey" : "...",
      "role" : { }
    } ],
    "tenantId" : 12345,
    "internal" : true
  }
}
```
