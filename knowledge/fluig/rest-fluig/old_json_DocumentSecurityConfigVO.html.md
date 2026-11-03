---
content_hash: 20b8466e27b54688ea5adf8bf78ea9c6d219a74ae5855bfe51c5197373890bc7
fetched_at: '2026-11-03T14:34:36.667943+00:00'
page_id: json_DocumentSecurityConfigVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentSecurityConfigVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentSecurityConfigVO.html
version: 1
---

# DocumentSecurityConfigVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| securityVersion | boolean |  |  |
| permission | boolean |  |  |
| companyId | number | required |  |
| showContent | boolean |  |  |
| attributionType | number |  |  |
| downloadEnabled | boolean |  |  |
| securityLevel | number |  |  |
| attributionValue | string |  |  |
| version | number | required |  |
| sequence | number | required |  |
| documentId | number | required |  |

Example

```
{
  "securityVersion" : true,
  "permission" : true,
  "companyId" : 12345,
  "showContent" : true,
  "attributionType" : 12345,
  "downloadEnabled" : true,
  "securityLevel" : 12345,
  "attributionValue" : "...",
  "version" : 12345,
  "sequence" : 12345,
  "documentId" : 12345
}
```
