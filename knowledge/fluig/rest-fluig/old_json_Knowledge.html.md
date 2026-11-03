---
content_hash: fad35c68c2a876e4d27ba646b5859a5647b88ac7305e1be70428adb9f0434a42
fetched_at: '2026-11-03T14:34:37.747983+00:00'
page_id: json_Knowledge
product: fluig
source: rest-fluig
title: Fluig REST — Knowledge Data Type
type: documentation
url: https://api.fluig.com/old/json_Knowledge.html
version: 1
---

# Knowledge Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| lastView | number |  |
| knowledgePK | [KnowledgePK](https://api.fluig.com/old/json_KnowledgePK.html) |  |
| ~~lastViewed~~ | ~~number~~ |  |
| ~~lastViewedTime~~ | ~~string~~ |  |
| firstView | number |  |
| ~~knowledgeDate~~ | ~~number~~ |  |
| versionDescription | string |  |

Example

```
{
  "lastView" : 12345,
  "knowledgePK" : {
    "colleagueId" : "...",
    "documentId" : 12345,
    "version" : 12345,
    "companyId" : 12345
  },
  "firstView" : 12345,
  "versionDescription" : "..."
}
```
