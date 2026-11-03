---
content_hash: 624c7590a2d945ec59181af7a8537c5403ee45cdbfb10a6aa39c450822b4ef06
fetched_at: '2026-11-03T14:34:37.754607+00:00'
page_id: json_KnowledgeVO
product: fluig
source: rest-fluig
title: Fluig REST — KnowledgeVO Data Type
type: documentation
url: https://api.fluig.com/old/json_KnowledgeVO.html
version: 1
---

# KnowledgeVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| companyId | number | required |  |
| colleagueId | string |  |  |
| documentId | number | required |  |
| version | number | required |  |
| versionDescription | string |  |  |
| lastView | number |  |  |
| firstView | number |  |  |

Example

```
{
  "companyId" : 12345,
  "colleagueId" : "...",
  "documentId" : 12345,
  "version" : 12345,
  "versionDescription" : "...",
  "lastView" : 12345,
  "firstView" : 12345
}
```
