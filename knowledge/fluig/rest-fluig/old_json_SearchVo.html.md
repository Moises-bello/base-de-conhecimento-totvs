---
content_hash: f01fbbc4571e8082728c51986db1d30261905860f7c3f140297978325d29843d
fetched_at: '2026-11-03T14:34:38.347049+00:00'
page_id: json_SearchVo
product: fluig
source: rest-fluig
title: Fluig REST — SearchVo Data Type
type: documentation
url: https://api.fluig.com/old/json_SearchVo.html
version: 1
---

# SearchVo Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| searchType | string |  |  |
| pattern | string |  |  |
| startPeriod | number |  |  |
| endPeriod | number |  |  |
| period | [DateGap](https://api.fluig.com/old/json_DateGap.html) |  |  |
| ordering | [Ordering](https://api.fluig.com/old/json_Ordering.html) |  |  |
| limit | number | required |  |
| offset | number | required |  |

Example

```
{
  "searchType" : "...",
  "pattern" : "...",
  "startPeriod" : 12345,
  "endPeriod" : 12345,
  "period" : "LAST_HOUR",
  "ordering" : "OLDEST",
  "limit" : 12345,
  "offset" : 12345
}
```
