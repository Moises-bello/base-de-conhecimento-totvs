---
content_hash: 2d6a3dfa5a493e41d9e6938c73260a1b4147a0434af3dc57a9b07548551630f8
fetched_at: '2026-11-03T14:34:36.330162+00:00'
page_id: json_CancelInstanceVO
product: fluig
source: rest-fluig
title: Fluig REST — CancelInstanceVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CancelInstanceVO.html
version: 1
---

# CancelInstanceVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processInstanceId | number | required |  |
| cancelText | string |  |  |
| replacedId | string |  |  |

Example

```
{
  "processInstanceId" : 12345,
  "cancelText" : "...",
  "replacedId" : "..."
}
```
