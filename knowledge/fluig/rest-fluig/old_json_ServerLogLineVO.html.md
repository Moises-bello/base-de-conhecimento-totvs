---
content_hash: 5f51ba880203be9e832270078a8bd303677bc020c706c6eba35eb394323abed5
fetched_at: '2026-11-03T14:34:38.366074+00:00'
page_id: json_ServerLogLineVO
product: fluig
source: rest-fluig
title: Fluig REST — ServerLogLineVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ServerLogLineVO.html
version: 1
---

# ServerLogLineVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| type | string |  |  |
| thread | string |  |  |
| line | number | required |  |
| content | string |  |  |
| stackTrace | array of string |  |  |
| date | string |  |  |
| clazz | string |  |  |

Example

```
{
  "type" : "...",
  "thread" : "...",
  "line" : 12345,
  "content" : "...",
  "stackTrace" : [ "...", "..." ],
  "date" : "...",
  "clazz" : "..."
}
```
