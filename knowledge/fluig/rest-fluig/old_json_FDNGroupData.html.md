---
content_hash: 3abe764910c0faee4dfe7010e3558bfe10f48406eb82b14781025f7a0ce91fad
fetched_at: '2026-11-03T14:34:36.822824+00:00'
page_id: json_FDNGroupData
product: fluig
source: rest-fluig
title: Fluig REST — FDNGroupData Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNGroupData.html
version: 1
---

# FDNGroupData Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| group | [FDNGroup](https://api.fluig.com/old/json_FDNGroup.html) |  |
| dataKey | string |  |
| id | number |  |
| dataValue | string |  |

Example

```
{
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
  "dataKey" : "...",
  "id" : 12345,
  "dataValue" : "..."
}
```
