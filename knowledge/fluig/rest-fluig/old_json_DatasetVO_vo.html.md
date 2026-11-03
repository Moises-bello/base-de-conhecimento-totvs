---
content_hash: 23bf654de5b67fd8472ac3cfcc7d97943f30ec58458584da1fc43aeb1c18de2f
fetched_at: '2026-11-03T14:34:36.572331+00:00'
page_id: json_DatasetVO_vo
product: fluig
source: rest-fluig
title: Fluig REST — DatasetVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DatasetVO_vo.html
version: 1
---

# DatasetVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| name | string |  |
| fields | array of string |  |
| constraints | array of [SearchConstraintVO](https://api.fluig.com/old/json_SearchConstraintVO_vo.html) |  |
| order | array of string |  |

Example

```
{
  "name" : "...",
  "fields" : [ "...", "..." ],
  "constraints" : [ {
    "_field" : "...",
    "_finalValue" : "...",
    "_initialValue" : "...",
    "_type" : 12345,
    "_likeSearch" : true,
    "constraintType" : "MUST"
  }, {
    "_field" : "...",
    "_finalValue" : "...",
    "_initialValue" : "...",
    "_type" : 12345,
    "_likeSearch" : true,
    "constraintType" : "MUST"
  } ],
  "order" : [ "...", "..." ]
}
```
