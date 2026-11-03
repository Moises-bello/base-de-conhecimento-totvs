---
content_hash: ce9b7af1f05d5d4104d9cc049dcd7d05724c7955ed469bd2da6c05adcbc11ca7
fetched_at: '2026-11-03T14:34:38.489469+00:00'
page_id: json_SocialDocDto
product: fluig
source: rest-fluig
title: Fluig REST — SocialDocDto Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialDocDto.html
version: 1
---

# SocialDocDto Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| documentId | number |  |  |
| parentDocumentId | number |  |  |
| createDate | number |  |  |
| sociableObjectId | number |  |  |
| phisicalFilePath | string |  |  |
| documentType | string |  |  |
| version | number | required |  |
| userPermission | number |  |  |
| documentDescription | string |  |  |

Example

```
{
  "documentId" : 12345,
  "parentDocumentId" : 12345,
  "createDate" : 12345,
  "sociableObjectId" : 12345,
  "phisicalFilePath" : "...",
  "documentType" : "...",
  "version" : 12345,
  "userPermission" : 12345,
  "documentDescription" : "..."
}
```
