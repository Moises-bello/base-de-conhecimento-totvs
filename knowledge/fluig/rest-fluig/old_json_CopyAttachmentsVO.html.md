---
content_hash: e6d5f79f8294f639358b36713d274b3b2aaa338c85a54b69fdef2daec526dd1c
fetched_at: '2026-11-03T14:34:36.529853+00:00'
page_id: json_CopyAttachmentsVO
product: fluig
source: rest-fluig
title: Fluig REST — CopyAttachmentsVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CopyAttachmentsVO.html
version: 1
---

# CopyAttachmentsVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| taskUserId | string |  |  |
| sourceProcessInstanceId | number | required |  |
| processId | string |  |  |

Example

```
{
  "taskUserId" : "...",
  "sourceProcessInstanceId" : 12345,
  "processId" : "..."
}
```
