---
content_hash: 064ea0b0af40946773a5f209273f5708a8451d7f3a2c69afeaba80c6abb1b2a8
fetched_at: '2026-11-03T14:34:37.921746+00:00'
page_id: json_OrganizationVO
product: fluig
source: rest-fluig
title: Fluig REST — OrganizationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_OrganizationVO.html
version: 1
---

# OrganizationVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| lastName | string |  |
| theme | string |  |
| password | string |  |
| federalId | string |  |
| key | [OrganizationKeyVO](https://api.fluig.com/old/json_OrganizationKeyVO.html) |  |
| firstName | string |  |
| login | string |  |
| userCode | string |  |
| description | string |  |
| skin | string |  |
| email | string |  |
| products | array of string |  |
| fullName | string |  |
| dirDefault | string |  |
| data | map of string |  |

Example

```
{
  "lastName" : "...",
  "theme" : "...",
  "password" : "...",
  "federalId" : "...",
  "key" : {
    "code" : "...",
    "id" : 12345
  },
  "firstName" : "...",
  "login" : "...",
  "userCode" : "...",
  "description" : "...",
  "skin" : "...",
  "email" : "...",
  "products" : [ "...", "..." ],
  "fullName" : "...",
  "dirDefault" : "...",
  "data" : {
    "property1" : "...",
    "property2" : "..."
  }
}
```
