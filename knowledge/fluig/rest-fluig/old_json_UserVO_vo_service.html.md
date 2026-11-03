---
content_hash: df499d3496ecfe47b6e96eca6724040ec3df9737d909be151f130559e26e8f71
fetched_at: '2026-11-03T14:34:38.782367+00:00'
page_id: json_UserVO_vo_service
product: fluig
source: rest-fluig
title: Fluig REST — UserVO Data Type
type: documentation
url: https://api.fluig.com/old/json_UserVO_vo_service.html
version: 1
---

# UserVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| locationUrl | string |  |
| tokenSecret | string |  |
| anonymizationUser | number |  |
| userCode | string |  |
| login | string |  |
| locale | string |  |
| roles | array of string |  |
| lastSecurityUpdateDate | number |  |
| birthDay | number |  |
| data | array of [NameValue](https://api.fluig.com/old/json_NameValue.html) |  |
| userUUID | string |  |
| lastUpdateDate | number |  |
| tokenAccess | string |  |
| firstName | string |  |
| tenantCode | string |  |
| email | string |  |
| tenantUUID | string |  |
| locationCode | string |  |
| groups | array of string |  |
| passwordType | string |  |
| password | string |  |
| idpId | string |  |
| tenantId | number |  |
| lastName | string |  |
| id | number |  |
| firstAccess | boolean |  |
| fullName | string |  |
| userType | number |  |
| anonymizationDate | number |  |
| locationId | number |  |

Example

```
{
  "locationUrl" : "...",
  "tokenSecret" : "...",
  "anonymizationUser" : 12345,
  "userCode" : "...",
  "login" : "...",
  "locale" : "...",
  "roles" : [ "...", "..." ],
  "lastSecurityUpdateDate" : 12345,
  "birthDay" : 12345,
  "data" : [ {
    "value" : "...",
    "name" : "..."
  }, {
    "value" : "...",
    "name" : "..."
  } ],
  "userUUID" : "...",
  "lastUpdateDate" : 12345,
  "tokenAccess" : "...",
  "firstName" : "...",
  "tenantCode" : "...",
  "email" : "...",
  "tenantUUID" : "...",
  "locationCode" : "...",
  "groups" : [ "...", "..." ],
  "passwordType" : "...",
  "password" : "...",
  "idpId" : "...",
  "tenantId" : 12345,
  "lastName" : "...",
  "id" : 12345,
  "firstAccess" : true,
  "fullName" : "...",
  "userType" : 12345,
  "anonymizationDate" : 12345,
  "locationId" : 12345
}
```
