---
content_hash: 7160ecf6f80419af8f08fab83aa29d863484e701837571449fc93eb298dbad85
fetched_at: '2026-11-03T14:34:39.044032+00:00'
page_id: json_WidgetPartSecurityConfigVO
product: fluig
source: rest-fluig
title: Fluig REST — WidgetPartSecurityConfigVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WidgetPartSecurityConfigVO.html
version: 1
---

# WidgetPartSecurityConfigVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| securityVersion | boolean |  |  |
| attributionDescription | string |  |  |
| attributionValue | string |  |  |
| inheritOriginSecurity | boolean | required |  |
| tableId | string |  |  |
| attributionType | number |  |  |
| permission | boolean |  |  |
| securityLevel | number |  |  |
| inheritSecurity | boolean | required |  |
| downloadEnabled | boolean |  |  |
| showContent | boolean |  |  |

Example

```
{
  "securityVersion" : true,
  "attributionDescription" : "...",
  "attributionValue" : "...",
  "inheritOriginSecurity" : true,
  "tableId" : "...",
  "attributionType" : 12345,
  "permission" : true,
  "securityLevel" : 12345,
  "inheritSecurity" : true,
  "downloadEnabled" : true,
  "showContent" : true
}
```
