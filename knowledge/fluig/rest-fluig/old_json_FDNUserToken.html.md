---
content_hash: 26fbe79d4e096bdd9344cf4437a50148fb5efec5f79dc4edbe45d691b365f573
fetched_at: '2026-11-03T14:34:36.927114+00:00'
page_id: json_FDNUserToken
product: fluig
source: rest-fluig
title: Fluig REST — FDNUserToken Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUserToken.html
version: 1
---

# FDNUserToken Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| maxToken | number |  |
| expirationDate | number |  |
| id | number |  |
| token | string |  |
| usedToken | number |  |
| tenantId | number |  |
| status | [UserTokenStatus](https://api.fluig.com/old/json_UserTokenStatus.html) |  |
| email | string |  |
| creationDate | number |  |

Example

```
{
  "maxToken" : 12345,
  "expirationDate" : 12345,
  "id" : 12345,
  "token" : "...",
  "usedToken" : 12345,
  "tenantId" : 12345,
  "status" : "CREATED",
  "email" : "...",
  "creationDate" : 12345
}
```
