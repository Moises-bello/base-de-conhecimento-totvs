---
content_hash: 277c60030caa7d3a614a4ad789d898860093eaf934eb1aa949760735d031b7f0
fetched_at: '2026-11-03T14:34:36.900995+00:00'
page_id: json_FDNUserData
product: fluig
source: rest-fluig
title: Fluig REST — FDNUserData Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUserData.html
version: 1
---

# FDNUserData Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| dataKey | string |  |
| id | number |  |
| anonymizationUser | [FDNUserTenant](https://api.fluig.com/old/json_FDNUserTenant.html) |  |
| dataValue | string |  |
| user | [FDNUserTenant](https://api.fluig.com/old/json_FDNUserTenant.html) |  |
| hide | boolean |  |
| anonymizationDate | number |  |

Example

```
{
  "dataKey" : "...",
  "id" : 12345,
  "anonymizationUser" : {
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
    "userState" : "REMOVED",
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
  "dataValue" : "...",
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
    "userState" : "BLOCKED",
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
  "hide" : true,
  "anonymizationDate" : 12345
}
```
