---
content_hash: b461cb913b926a4e06d8b651078e907a8211d6d6ebb1e6d1ef6aa71ffd43a242
fetched_at: '2026-11-03T14:34:38.582280+00:00'
page_id: json_StatesVO
product: fluig
source: rest-fluig
title: Fluig REST — StatesVO Data Type
type: documentation
url: https://api.fluig.com/old/json_StatesVO.html
version: 1
---

# StatesVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| subProcessSequence | number | required |  |
| sequence | number |  |  |
| processId | string |  |  |
| description | string |  |  |
| isReturn | boolean |  |  |

Example

```
{
  "subProcessSequence" : 12345,
  "sequence" : 12345,
  "processId" : "...",
  "description" : "...",
  "isReturn" : true
}
```
