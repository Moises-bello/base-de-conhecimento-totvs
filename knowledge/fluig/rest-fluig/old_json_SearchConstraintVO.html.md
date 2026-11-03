---
content_hash: dfbac2d6b8e6600526b24d5c44b44bc956f9e03956880aad0b6b84adb42eb274
fetched_at: '2026-11-03T14:34:38.317630+00:00'
page_id: json_SearchConstraintVO
product: fluig
source: rest-fluig
title: Fluig REST — SearchConstraintVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SearchConstraintVO.html
version: 1
---

# SearchConstraintVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| \_field | string |  |  |
| constraintType | [ConstraintType](https://api.fluig.com/old/json_ConstraintType.html) |  |  |
| \_finalValue | string |  |  |
| \_initialValue | string |  |  |
| \_likeSearch | boolean | required |  |
| \_type | number |  |  |

Example

```
{
  "_field" : "...",
  "constraintType" : "MUST_NOT",
  "_finalValue" : "...",
  "_initialValue" : "...",
  "_likeSearch" : true,
  "_type" : 12345
}
```
