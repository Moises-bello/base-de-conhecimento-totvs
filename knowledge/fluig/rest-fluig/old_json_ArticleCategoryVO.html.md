---
content_hash: bd3209d7a03949ab6e19309563d5063e17db0e37b48c76b5dd92df846c93476c
fetched_at: '2026-11-03T14:34:36.205749+00:00'
page_id: json_ArticleCategoryVO
product: fluig
source: rest-fluig
title: Fluig REST — ArticleCategoryVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleCategoryVO.html
version: 1
---

# ArticleCategoryVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| name | string |  |  |
| alias | string |  |  |
| description | string |  |  |
| securityLevel | [SECURITY\_LEVEL](https://api.fluig.com/old/json_SECURITY_LEVEL.html) |  |  |
| type | [SocialDocumentType](https://api.fluig.com/old/json_SocialDocumentType.html) |  |  |
| url | string |  |  |
| parentId | number |  |  |
| listable | boolean | required |  |
| totalDocs | number |  |  |
| id | number |  |  |

Example

```
{
  "name" : "...",
  "alias" : "...",
  "description" : "...",
  "securityLevel" : "SECURITY_DENIED",
  "type" : "ARTICLE",
  "url" : "...",
  "parentId" : 12345,
  "listable" : true,
  "totalDocs" : 12345,
  "id" : 12345
}
```
