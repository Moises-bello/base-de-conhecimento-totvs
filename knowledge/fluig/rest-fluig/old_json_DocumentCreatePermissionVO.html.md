---
content_hash: 18173c0d6f79c8dfc23d6629522d0b2903934bc125ccc590165c46023eb03bef
fetched_at: '2026-11-03T14:34:36.627978+00:00'
page_id: json_DocumentCreatePermissionVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentCreatePermissionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentCreatePermissionVO.html
version: 1
---

# DocumentCreatePermissionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| documentId | number | required | the documentId |
| documentPermissionVO | array of [DocumentPermissionVO](https://api.fluig.com/old/json_DocumentPermissionVO.html) |  | the documentPermissionVO |

Example

```
{
  "documentId" : 12345,
  "documentPermissionVO" : [ {
    "inheritSecurity" : true,
    "securityLevel" : 12345,
    "downloadEnabled" : true,
    "securityVersion" : true,
    "showContent" : true,
    "attributionDescription" : "...",
    "attributionType" : 12345,
    "attributionValue" : "..."
  }, {
    "inheritSecurity" : true,
    "securityLevel" : 12345,
    "downloadEnabled" : true,
    "securityVersion" : true,
    "showContent" : true,
    "attributionDescription" : "...",
    "attributionType" : 12345,
    "attributionValue" : "..."
  } ]
}
```
