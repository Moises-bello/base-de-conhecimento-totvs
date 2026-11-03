---
content_hash: d4006769525fc23a5c78263184309635eba7ae4f98baf22ac090e5799146576e
fetched_at: '2026-11-03T14:34:36.569361+00:00'
page_id: json_DatasetVO
product: fluig
source: rest-fluig
title: Fluig REST — DatasetVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DatasetVO.html
version: 1
---

# DatasetVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| constraints | array of [SearchConstraintVO](https://api.fluig.com/old/json_SearchConstraintVO.html) |  |
| name | string |  |
| fields | array of string |  |
| order | array of string |  |

Example

```
{
  "constraints" : [ {
    "_field" : "...",
    "constraintType" : "SHOULD",
    "_finalValue" : "...",
    "_initialValue" : "...",
    "_likeSearch" : true,
    "_type" : 12345
  }, {
    "_field" : "...",
    "constraintType" : "MUST",
    "_finalValue" : "...",
    "_initialValue" : "...",
    "_likeSearch" : true,
    "_type" : 12345
  } ],
  "name" : "...",
  "fields" : [ "...", "..." ],
  "order" : [ "...", "..." ]
}
```
