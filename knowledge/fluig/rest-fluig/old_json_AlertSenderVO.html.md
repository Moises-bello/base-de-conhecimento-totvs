---
content_hash: 29ae2bd8e2000dcec12329e5695d7336a2c3c85db78a1cd49d2b2d974ac94762
fetched_at: '2026-11-03T14:34:36.119174+00:00'
page_id: json_AlertSenderVO
product: fluig
source: rest-fluig
title: Fluig REST — AlertSenderVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertSenderVO.html
version: 1
---

# AlertSenderVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| user | [AlertUserVO](https://api.fluig.com/old/json_AlertUserVO_vo.html) |  |
| via | string |  |
| id | number |  |
| creationDate | number |  |

Example

```
{
  "user" : {
    "tenantId" : 12345,
    "lastUpdateDate" : 12345,
    "login" : "...",
    "id" : 12345,
    "lastName" : "...",
    "fisrtName" : "...",
    "fullName" : "..."
  },
  "via" : "...",
  "id" : 12345,
  "creationDate" : 12345
}
```
