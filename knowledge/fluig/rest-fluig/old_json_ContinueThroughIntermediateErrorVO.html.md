---
content_hash: 1ad2216a0703f038f93a28dae21a1405132292748a4ed055df6527734777db00
fetched_at: '2026-11-03T14:34:36.523516+00:00'
page_id: json_ContinueThroughIntermediateErrorVO
product: fluig
source: rest-fluig
title: Fluig REST — ContinueThroughIntermediateErrorVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ContinueThroughIntermediateErrorVO.html
version: 1
---

# ContinueThroughIntermediateErrorVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processInstanceId | number | required |  |
| sequence | number | required |  |
| version | number | required |  |
| login | string |  |  |
| userId | string |  |  |
| processId | string |  |  |
| threadSequence | number | required |  |
| companyId | number | required |  |
| obs | string |  |  |

Example

```
{
  "processInstanceId" : 12345,
  "sequence" : 12345,
  "version" : 12345,
  "login" : "...",
  "userId" : "...",
  "processId" : "...",
  "threadSequence" : 12345,
  "companyId" : 12345,
  "obs" : "..."
}
```
