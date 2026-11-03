---
content_hash: 38ec4f3529ea1517730ad5c7bad57a18df4318fcb2072b88362c9bc45082fb5c
fetched_at: '2026-11-03T14:34:38.774016+00:00'
page_id: json_UserVO_vo
product: fluig
source: rest-fluig
title: Fluig REST — UserVO Data Type
type: documentation
url: https://api.fluig.com/old/json_UserVO_vo.html
version: 1
---

# UserVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| login | string |  |
| firstName | string |  |
| lastName | string |  |
| fullName | string |  |
| password | string |  |
| email | string |  |
| idpId | string |  |
| customData | map of string |  |
| roles | array of string |  |
| groups | array of string |  |

Example

```
{
  "login" : "...",
  "firstName" : "...",
  "lastName" : "...",
  "fullName" : "...",
  "password" : "...",
  "email" : "...",
  "idpId" : "...",
  "customData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "roles" : [ "...", "..." ],
  "groups" : [ "...", "..." ]
}
```
