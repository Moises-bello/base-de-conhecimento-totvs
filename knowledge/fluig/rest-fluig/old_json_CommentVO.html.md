---
content_hash: beb6d6d98cd1ee35a18bac131f04f0786a6606f1128e9faba11aacd949cac8da
fetched_at: '2026-11-03T14:34:36.461803+00:00'
page_id: json_CommentVO
product: fluig
source: rest-fluig
title: Fluig REST — CommentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CommentVO.html
version: 1
---

# CommentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| sociableId | number |  |  |
| comment | string |  |  |
| creationDate | number |  |  |
| commentWithoutMention | string |  |  |
| mention | boolean | required |  |
| mentions | map of string |  |  |
| userName | string |  |  |
| userAlias | string |  |  |
| customData | map of string |  |  |

Example

```
{
  "sociableId" : 12345,
  "comment" : "...",
  "creationDate" : 12345,
  "commentWithoutMention" : "...",
  "mention" : true,
  "mentions" : {
    "property1" : "...",
    "property2" : "..."
  },
  "userName" : "...",
  "userAlias" : "...",
  "customData" : {
    "property1" : "...",
    "property2" : "..."
  }
}
```
