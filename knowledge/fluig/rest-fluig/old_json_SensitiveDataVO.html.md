---
content_hash: 11e7712438766f3b71b0d010143bc8136425b97509a7cca2e4f0cef07939afb3
fetched_at: '2026-11-03T14:34:38.357341+00:00'
page_id: json_SensitiveDataVO
product: fluig
source: rest-fluig
title: Fluig REST — SensitiveDataVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SensitiveDataVO.html
version: 1
---

# SensitiveDataVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| canAnonymizeData | boolean | required |  |
| sensitiveDataType | string |  |  |
| sensitiveData | boolean | required |  |
| reasons | array of [ReasonVO](https://api.fluig.com/old/json_ReasonVO.html) |  |  |

Example

```
{
  "canAnonymizeData" : true,
  "sensitiveDataType" : "...",
  "sensitiveData" : true,
  "reasons" : [ {
    "sensitiveDataClassification" : "...",
    "sensitiveDataClassificationJustify" : "..."
  }, {
    "sensitiveDataClassification" : "...",
    "sensitiveDataClassificationJustify" : "..."
  } ]
}
```
