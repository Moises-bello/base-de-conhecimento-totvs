---
content_hash: 237c75894a1fb8dfc92eda2f4bd30271a500a5eb720ea27e39f4027c7595a1c3
fetched_at: '2026-11-03T14:34:36.909954+00:00'
page_id: json_FDNUserPicture
product: fluig
source: rest-fluig
title: Fluig REST — FDNUserPicture Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUserPicture.html
version: 1
---

# FDNUserPicture Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| picture | string |  |
| user | [FDNUserTenant](https://api.fluig.com/old/json_FDNUserTenant.html) |  |

Example

```
{
  "id" : 12345,
  "picture" : "...",
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
  }
}
```
