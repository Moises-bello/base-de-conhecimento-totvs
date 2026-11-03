---
content_hash: 18f16425ca3d09be42fe3fe936bf17295ba2478c51dfaed7f56b6c907df483af
fetched_at: '2026-11-03T14:34:38.676848+00:00'
page_id: json_TenantCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — TenantCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TenantCreateVO.html
version: 1
---

# TenantCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| code | string |  |
| federalId | string |  |
| idpId | string |  |
| description | string |  |
| organizationUrl | string |  |
| volumeDir | string |  |
| idpLogOff | boolean |  |
| thumbnailEnabled | boolean |  |
| removeVolume | boolean |  |
| data | map of string |  |
| adminLogin | string |  |
| adminCode | string |  |
| adminEmail | string |  |
| adminPassword | string |  |
| adminFirstName | string |  |
| adminLastName | string |  |

Example

```
{
  "id" : 12345,
  "code" : "...",
  "federalId" : "...",
  "idpId" : "...",
  "description" : "...",
  "organizationUrl" : "...",
  "volumeDir" : "...",
  "idpLogOff" : true,
  "thumbnailEnabled" : true,
  "removeVolume" : true,
  "data" : {
    "property1" : "...",
    "property2" : "..."
  },
  "adminLogin" : "...",
  "adminCode" : "...",
  "adminEmail" : "...",
  "adminPassword" : "...",
  "adminFirstName" : "...",
  "adminLastName" : "..."
}
```
