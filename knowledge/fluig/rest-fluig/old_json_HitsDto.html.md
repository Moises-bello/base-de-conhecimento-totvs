---
content_hash: 4db69e6158f1c15308f59c20aa03f0b886fa4d8adb5366ed6a8367cb9146e172
fetched_at: '2026-11-03T14:34:37.118905+00:00'
page_id: json_HitsDto
product: fluig
source: rest-fluig
title: Fluig REST — HitsDto Data Type
type: documentation
url: https://api.fluig.com/old/json_HitsDto.html
version: 1
---

# HitsDto Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| totalHits | number |  |
| knowledge | array of [Knowledge](https://api.fluig.com/old/json_Knowledge.html) |  |

Example

```
{
  "totalHits" : 12345,
  "knowledge" : [ {
    "lastView" : 12345,
    "knowledgePK" : {
      "colleagueId" : "...",
      "documentId" : 12345,
      "version" : 12345,
      "companyId" : 12345
    },
    "firstView" : 12345,
    "versionDescription" : "..."
  }, {
    "lastView" : 12345,
    "knowledgePK" : {
      "colleagueId" : "...",
      "documentId" : 12345,
      "version" : 12345,
      "companyId" : 12345
    },
    "firstView" : 12345,
    "versionDescription" : "..."
  } ]
}
```
