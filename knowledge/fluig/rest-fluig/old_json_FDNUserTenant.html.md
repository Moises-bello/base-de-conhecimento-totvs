---
content_hash: 6003e2f41e4dea2166cf1c9bbde6b6a61facea82ca144a9f099cded6a7de3a9b
fetched_at: '2026-11-03T14:34:36.923345+00:00'
page_id: json_FDNUserTenant
product: fluig
source: rest-fluig
title: Fluig REST — FDNUserTenant Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUserTenant.html
version: 1
---

# FDNUserTenant Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| data | array of [FDNUserData](https://api.fluig.com/old/json_FDNUserData.html) |  |
| firstAccess | boolean |  |
| locationId | number |  |
| userCode | string |  |
| userState | [UserState](https://api.fluig.com/old/json_UserState.html) |  |
| userId | number |  |
| anonymizationDate | number |  |
| id | number |  |
| user | [FDNUser](https://api.fluig.com/old/json_FDNUser.html) |  |
| password | string |  |
| lastSecurityUpdateDate | number |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |
| email | string |  |
| idpId | string |  |
| lastUpdateDate | number |  |
| anonymizationUser | [FDNUserTenant](https://api.fluig.com/old/json_FDNUserTenant.html) |  |
| tenantId | number |  |
| userUUID | string |  |
| login | string |  |

Example

```
{
  "data" : [ {
    "dataKey" : "...",
    "id" : 12345,
    "anonymizationUser" : {
      "data" : [ { }, { } ],
      "firstAccess" : true,
      "locationId" : 12345,
      "userCode" : "...",
      "userState" : "UNCONFIRMED",
      "userId" : 12345,
      "anonymizationDate" : 12345,
      "id" : 12345,
      "user" : { },
      "password" : "...",
      "lastSecurityUpdateDate" : 12345,
      "tenant" : { },
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
      "data" : [ { }, { } ],
      "firstAccess" : true,
      "locationId" : 12345,
      "userCode" : "...",
      "userState" : "UNCONFIRMED",
      "userId" : 12345,
      "anonymizationDate" : 12345,
      "id" : 12345,
      "user" : { },
      "password" : "...",
      "lastSecurityUpdateDate" : 12345,
      "tenant" : { },
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
  }, {
    "dataKey" : "...",
    "id" : 12345,
    "anonymizationUser" : {
      "data" : [ { }, { } ],
      "firstAccess" : true,
      "locationId" : 12345,
      "userCode" : "...",
      "userState" : "ACTIVE",
      "userId" : 12345,
      "anonymizationDate" : 12345,
      "id" : 12345,
      "user" : { },
      "password" : "...",
      "lastSecurityUpdateDate" : 12345,
      "tenant" : { },
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
      "data" : [ { }, { } ],
      "firstAccess" : true,
      "locationId" : 12345,
      "userCode" : "...",
      "userState" : "ACTIVE",
      "userId" : 12345,
      "anonymizationDate" : 12345,
      "id" : 12345,
      "user" : { },
      "password" : "...",
      "lastSecurityUpdateDate" : 12345,
      "tenant" : { },
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
    "userType" : "INTERNAL",
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
  "email" : "...",
  "idpId" : "...",
  "lastUpdateDate" : 12345,
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
    "userState" : "ACTIVE",
    "userId" : 12345,
    "anonymizationDate" : 12345,
    "id" : 12345,
    "user" : {
      "birthDate" : 12345,
      "anonymizationUser" : { },
      "firstName" : "...",
      "userType" : "NOLOGIN",
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
  "tenantId" : 12345,
  "userUUID" : "...",
  "login" : "..."
}
```
