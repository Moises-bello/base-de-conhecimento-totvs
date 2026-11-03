---
content_hash: ce37cc68b1c582c8240f6ed1761c30ed30f2088defffde3f31e6604b29800911
fetched_at: '2026-11-03T14:34:38.321731+00:00'
page_id: json_SearchConstraintVO_vo
product: fluig
source: rest-fluig
title: Fluig REST — SearchConstraintVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SearchConstraintVO_vo.html
version: 1
---

# SearchConstraintVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| \_field | string |  |  |
| \_finalValue | string |  |  |
| \_initialValue | string |  |  |
| \_type | number |  |  |
| \_likeSearch | boolean | required |  |
| constraintType | [ConstraintType](https://api.fluig.com/old/json_ConstraintType.html) |  |  |

Example

```
{
  "_field" : "...",
  "_finalValue" : "...",
  "_initialValue" : "...",
  "_type" : 12345,
  "_likeSearch" : true,
  "constraintType" : "MUST_NOT"
}
```
