---
content_hash: 210e860a49876e2814e8f29ce4730acafd5b36d64066f1219d08521beb545ca8
fetched_at: '2026-11-03T14:34:36.728654+00:00'
page_id: json_DocumentWatchVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentWatchVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentWatchVO.html
version: 1
---

# DocumentWatchVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| version | number |  |
| Properties inherited from [UserVO](https://api.fluig.com/old/json_UserVO.html) | | |
| id | number |  |
| name | string |  |
| description | string |  |
| alias | string |  |
| lastUpdate | number |  |
| data | map of string |  |

Example

```
{
  "version" : 12345,
  "id" : 12345,
  "name" : "...",
  "description" : "...",
  "alias" : "...",
  "lastUpdate" : 12345,
  "data" : {
    "property1" : "...",
    "property2" : "..."
  }
}
```
