---
content_hash: 939a47c3f1870d25e1c9b6691a351388cfb755dd891149a129bd5a8fa7773c81
fetched_at: '2026-11-03T14:34:38.770182+00:00'
page_id: json_UserVO_user
product: fluig
source: rest-fluig
title: Fluig REST — UserVO Data Type
type: documentation
url: https://api.fluig.com/old/json_UserVO_user.html
version: 1
---

# UserVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| isActive | boolean |  |
| password | string |  |
| fullName | string |  |
| code | string |  |
| tokenAccess | string |  |
| tokenSecret | string |  |
| login | string |  |
| id | number |  |
| extData | map of object |  |
| lastName | string |  |
| userUUID | string |  |
| email | string |  |
| groups | array of string |  |
| timezone | string |  |
| firstName | string |  |
| roles | array of string |  |

Example

```
{
  "isActive" : true,
  "password" : "...",
  "fullName" : "...",
  "code" : "...",
  "tokenAccess" : "...",
  "tokenSecret" : "...",
  "login" : "...",
  "id" : 12345,
  "extData" : {
    "property1" : { },
    "property2" : { }
  },
  "lastName" : "...",
  "userUUID" : "...",
  "email" : "...",
  "groups" : [ "...", "..." ],
  "timezone" : "...",
  "firstName" : "...",
  "roles" : [ "...", "..." ]
}
```
