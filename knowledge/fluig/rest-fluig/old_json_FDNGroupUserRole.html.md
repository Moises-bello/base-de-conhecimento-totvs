---
content_hash: 72e238b2e1fd36f138d365cffb7428d3784e0f2b90ef4b7021a0af0434089180
fetched_at: '2026-11-03T14:34:36.829599+00:00'
page_id: json_FDNGroupUserRole
product: fluig
source: rest-fluig
title: Fluig REST — FDNGroupUserRole Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNGroupUserRole.html
version: 1
---

# FDNGroupUserRole Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| groupCode | string |  |
| childGroupCode | string |  |
| user | [FDNUserTenant](https://api.fluig.com/old/json_FDNUserTenant.html) |  |
| role | [FDNRole](https://api.fluig.com/old/json_FDNRole.html) |  |
| id | number |  |
| login | string |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| group | [FDNGroup](https://api.fluig.com/old/json_FDNGroup.html) |  |
| roleCode | string |  |
| tenantId | number |  |
| childGroup | [FDNGroup](https://api.fluig.com/old/json_FDNGroup.html) |  |

Example

```
{
  "groupCode" : "...",
  "childGroupCode" : "...",
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
    "userState" : "UNCONFIRMED",
    "userId" : 12345,
    "anonymizationDate" : 12345,
    "id" : 12345,
    "user" : {
      "birthDate" : 12345,
      "anonymizationUser" : { },
      "firstName" : "...",
      "userType" : "APPLICATION",
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
  },
  "id" : 12345,
  "login" : "...",
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
  "group" : {
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
    "data" : [ {
      "group" : { },
      "dataKey" : "...",
      "id" : 12345,
      "dataValue" : "..."
    }, {
      "group" : { },
      "dataKey" : "...",
      "id" : 12345,
      "dataValue" : "..."
    } ]
  },
  "roleCode" : "...",
  "tenantId" : 12345,
  "childGroup" : {
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
    "data" : [ {
      "group" : { },
      "dataKey" : "...",
      "id" : 12345,
      "dataValue" : "..."
    }, {
      "group" : { },
      "dataKey" : "...",
      "id" : 12345,
      "dataValue" : "..."
    } ]
  }
}
```
