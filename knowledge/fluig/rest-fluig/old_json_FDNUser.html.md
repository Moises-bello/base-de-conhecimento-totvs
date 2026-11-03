---
content_hash: e98c5dad75bbe93364a28d26c7e27cff5570a52b5421026849d5e6297a70a9c5
fetched_at: '2026-11-03T14:34:36.897415+00:00'
page_id: json_FDNUser
product: fluig
source: rest-fluig
title: Fluig REST — FDNUser Data Type
type: documentation
url: https://api.fluig.com/old/json_FDNUser.html
version: 1
---

# FDNUser Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| birthDate | number |  |
| anonymizationUser | [FDNUser](https://api.fluig.com/old/json_FDNUser.html) |  |
| firstName | string |  |
| userType | [FDNUserType](https://api.fluig.com/old/json_FDNUserType.html) |  |
| anonymizationDate | number |  |
| lastName | string |  |
| id | number |  |
| fullName | string |  |

Example

```
{
  "birthDate" : 12345,
  "anonymizationUser" : {
    "birthDate" : 12345,
    "anonymizationUser" : { },
    "firstName" : "...",
    "userType" : "NOLOGIN",
    "anonymizationDate" : 12345,
    "lastName" : "...",
    "id" : 12345,
    "fullName" : "..."
  },
  "firstName" : "...",
  "userType" : "NORMAL",
  "anonymizationDate" : 12345,
  "lastName" : "...",
  "id" : 12345,
  "fullName" : "..."
}
```
