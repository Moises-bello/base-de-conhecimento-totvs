---
content_hash: bc0debe32016954b95d2fcec85e8785981858b82b3571724d9797703ed51278d
fetched_at: '2026-11-03T14:34:36.122466+00:00'
page_id: json_AlertSenderVO_alert
product: fluig
source: rest-fluig
title: Fluig REST — AlertSenderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertSenderVO_alert.html
version: 1
---

# AlertSenderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| via | string |  |
| user | [AlertUserVO](https://api.fluig.com/old/json_AlertUserVO.html) |  |
| creationDate | number |  |
| id | number |  |

Example

```
{
  "via" : "...",
  "user" : {
    "fullName" : "...",
    "lastUpdateDate" : 12345,
    "login" : "...",
    "fisrtName" : "...",
    "lastName" : "...",
    "tenantId" : 12345,
    "id" : 12345
  },
  "creationDate" : 12345,
  "id" : 12345
}
```
