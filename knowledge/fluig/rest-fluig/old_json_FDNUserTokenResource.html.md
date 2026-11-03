---
content_hash: b31b2448f5cbff1662d15c04fece444644aeaf023754cdfd148e814d73e342ce
fetched_at: '2026-11-03T14:34:36.930912+00:00'
page_id: json_FDNUserTokenResource
product: fluig
source: rest-fluig
title: Fluig REST — FDNUserTokenResource Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUserTokenResource.html
version: 1
---

# FDNUserTokenResource Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| resource | string |  |
| type | [FDNTokenResourceType](https://api.fluig.com/old/json_FDNTokenResourceType.html) |  |
| id | number |  |
| userToken | [FDNUserToken](https://api.fluig.com/old/json_FDNUserToken.html) |  |

Example

```
{
  "resource" : "...",
  "type" : "URL",
  "id" : 12345,
  "userToken" : {
    "maxToken" : 12345,
    "expirationDate" : 12345,
    "id" : 12345,
    "token" : "...",
    "usedToken" : 12345,
    "tenantId" : 12345,
    "status" : "SUCCESS",
    "email" : "...",
    "creationDate" : 12345
  }
}
```
