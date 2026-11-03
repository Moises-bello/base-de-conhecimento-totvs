---
content_hash: d9a9885771105b7a659d7225d9b7189471e47c87a3addcfcdfeab6d50f68aab6
fetched_at: '2026-11-03T14:34:38.343181+00:00'
page_id: json_SearchUserParamVO
product: fluig
source: rest-fluig
title: Fluig REST — SearchUserParamVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SearchUserParamVO.html
version: 1
---

# SearchUserParamVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| id | number |  |  |
| currentUser | boolean | required |  |
| showInactive | boolean | required |  |
| pattern | string |  |  |
| order | array of string |  |  |
| role | string |  |  |
| email | string |  |  |
| pageSize | number | required |  |
| login | string |  |  |
| code | string |  |  |
| lastName | string |  |  |
| group | string |  |  |
| tenantId | number |  |  |
| firstName | string |  |  |
| expand | array of string |  |  |
| page | number | required |  |
| fullName | string |  |  |
| genericId | string |  |  |

Example

```
{
  "id" : 12345,
  "currentUser" : true,
  "showInactive" : true,
  "pattern" : "...",
  "order" : [ "...", "..." ],
  "role" : "...",
  "email" : "...",
  "pageSize" : 12345,
  "login" : "...",
  "code" : "...",
  "lastName" : "...",
  "group" : "...",
  "tenantId" : 12345,
  "firstName" : "...",
  "expand" : [ "...", "..." ],
  "page" : 12345,
  "fullName" : "...",
  "genericId" : "..."
}
```
