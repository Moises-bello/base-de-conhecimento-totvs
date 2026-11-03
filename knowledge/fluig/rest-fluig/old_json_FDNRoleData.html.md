---
content_hash: 5b8facd8118daaa28c520db89a275ced0f910364b21414093292b7a16b555823
fetched_at: '2026-11-03T14:34:36.873270+00:00'
page_id: json_FDNRoleData
product: fluig
source: rest-fluig
title: Fluig REST — FDNRoleData Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNRoleData.html
version: 1
---

# FDNRoleData Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| dataValue | string |  |
| dataKey | string |  |
| role | [FDNRole](https://api.fluig.com/old/json_FDNRole.html) |  |

Example

```
{
  "id" : 12345,
  "dataValue" : "...",
  "dataKey" : "...",
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
