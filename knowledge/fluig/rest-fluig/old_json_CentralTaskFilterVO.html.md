---
content_hash: ddedfc24474f3d9435f6b62a78236401bc0f59441f1552463c98f1d1a245dab0
fetched_at: '2026-11-03T14:34:36.408351+00:00'
page_id: json_CentralTaskFilterVO
product: fluig
source: rest-fluig
title: Fluig REST — CentralTaskFilterVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CentralTaskFilterVO.html
version: 1
---

# CentralTaskFilterVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| name | string |  |
| type | string |  |
| processFields | array of [CentralTaskFilterFieldVO](https://api.fluig.com/old/json_CentralTaskFilterFieldVO.html) |  |
| formFields | array of [CentralTaskFilterFieldVO](https://api.fluig.com/old/json_CentralTaskFilterFieldVO.html) |  |
| documentFields | array of [CentralTaskFilterFieldVO](https://api.fluig.com/old/json_CentralTaskFilterFieldVO.html) |  |
| orderKey | string |  |
| orderType | string |  |
| processId | string |  |

Example

```
{
  "id" : 12345,
  "name" : "...",
  "type" : "...",
  "processFields" : [ {
    "key" : "...",
    "value" : "...",
    "visible" : true
  }, {
    "key" : "...",
    "value" : "...",
    "visible" : true
  } ],
  "formFields" : [ {
    "key" : "...",
    "value" : "...",
    "visible" : true
  }, {
    "key" : "...",
    "value" : "...",
    "visible" : true
  } ],
  "documentFields" : [ {
    "key" : "...",
    "value" : "...",
    "visible" : true
  }, {
    "key" : "...",
    "value" : "...",
    "visible" : true
  } ],
  "orderKey" : "...",
  "orderType" : "...",
  "processId" : "..."
}
```
