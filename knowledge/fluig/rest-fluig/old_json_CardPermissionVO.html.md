---
content_hash: 57a40836f6eed84622aaebb257e1b26e3ee373bdab531d5829f1c85a6f2c87fd
fetched_at: '2026-11-03T14:34:36.388666+00:00'
page_id: json_CardPermissionVO
product: fluig
source: rest-fluig
title: Fluig REST — CardPermissionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CardPermissionVO.html
version: 1
---

# CardPermissionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| serialVersionUID | number | required |  |
| securityLevel | number |  |  |
| securityVersion | boolean |  |  |
| inheritSecurity | boolean |  |  |
| downloadEnabled | boolean |  |  |
| showContent | boolean |  |  |
| attributionDescription | string |  |  |
| attributionType | number |  |  |
| attributionValue | string |  |  |

Example

```
{
  "serialVersionUID" : 12345,
  "securityLevel" : 12345,
  "securityVersion" : true,
  "inheritSecurity" : true,
  "downloadEnabled" : true,
  "showContent" : true,
  "attributionDescription" : "...",
  "attributionType" : 12345,
  "attributionValue" : "..."
}
```
