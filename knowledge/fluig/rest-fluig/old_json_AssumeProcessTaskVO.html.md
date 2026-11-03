---
content_hash: fd5b0e1bd9479a4573ca206b5997e495b759573140fdb1028d6284d31f93b75f
fetched_at: '2026-11-03T14:34:36.267493+00:00'
page_id: json_AssumeProcessTaskVO
product: fluig
source: rest-fluig
title: Fluig REST — AssumeProcessTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AssumeProcessTaskVO.html
version: 1
---

# AssumeProcessTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processInstanceId | number | required |  |
| movementSequence | number | required |  |
| colleagueId | string |  |  |
| replacementId | string |  |  |

Example

```
{
  "processInstanceId" : 12345,
  "movementSequence" : 12345,
  "colleagueId" : "...",
  "replacementId" : "..."
}
```
