---
content_hash: 78aa1a3fbf73c3a14dac7810d82538c621511286258706b9a8847618051376d9
fetched_at: '2026-11-03T14:34:38.718847+00:00'
page_id: json_TotalKnowledgeVO
product: fluig
source: rest-fluig
title: Fluig REST — TotalKnowledgeVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TotalKnowledgeVO.html
version: 1
---

# TotalKnowledgeVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| userList | array of [KnowledgeVO](https://api.fluig.com/old/json_KnowledgeVO.html) |  |
| totalKnowledge | number |  |

Example

```
{
  "userList" : [ {
    "companyId" : 12345,
    "colleagueId" : "...",
    "documentId" : 12345,
    "version" : 12345,
    "versionDescription" : "...",
    "lastView" : 12345,
    "firstView" : 12345
  }, {
    "companyId" : 12345,
    "colleagueId" : "...",
    "documentId" : 12345,
    "version" : 12345,
    "versionDescription" : "...",
    "lastView" : 12345,
    "firstView" : 12345
  } ],
  "totalKnowledge" : 12345
}
```
