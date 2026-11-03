---
content_hash: f258f9a8c499602c77691e20a0a50b428612f44dbbda109342dd89be52282739
fetched_at: '2026-11-03T14:34:38.116281+00:00'
page_id: json_ProcessVersionVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessVersionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessVersionVO.html
version: 1
---

# ProcessVersionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| favorite | boolean |  |  |
| versionDescription | string |  |  |
| processId | string |  |  |
| children | array of [ProcessVersionVO](https://api.fluig.com/old/json_ProcessVersionVO.html) |  |  |
| companyId | number | required |  |
| selected | boolean |  |  |
| formId | number |  |  |

Example

```
{
  "favorite" : true,
  "versionDescription" : "...",
  "processId" : "...",
  "children" : [ {
    "favorite" : true,
    "versionDescription" : "...",
    "processId" : "...",
    "children" : [ { }, { } ],
    "companyId" : 12345,
    "selected" : true,
    "formId" : 12345
  }, {
    "favorite" : true,
    "versionDescription" : "...",
    "processId" : "...",
    "children" : [ { }, { } ],
    "companyId" : 12345,
    "selected" : true,
    "formId" : 12345
  } ],
  "companyId" : 12345,
  "selected" : true,
  "formId" : 12345
}
```
