---
content_hash: 6a2ca69206dad337841979bd7ebec97de5c20d4714b7ac97fe6ad645b76bce5a
fetched_at: '2026-11-03T14:34:37.106638+00:00'
page_id: json_GroupVO
product: fluig
source: rest-fluig
title: Fluig REST — GroupVO Data Type
type: documentation
url: https://api.fluig.com/old/json_GroupVO.html
version: 1
---

# GroupVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| groupType | string |  |
| code | string |  |
| extData | map of string |  |
| id | number |  |
| description | string |  |
| isInternal | boolean |  |

Example

```
{
  "groupType" : "...",
  "code" : "...",
  "extData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "id" : 12345,
  "description" : "...",
  "isInternal" : true
}
```
