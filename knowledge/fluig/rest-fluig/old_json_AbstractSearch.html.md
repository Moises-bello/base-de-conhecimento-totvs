---
content_hash: bc86251ab59c9d3e0d9f0099b026dffc15a07427bff6ccfd62a8b53b9ed1ee8f
fetched_at: '2026-11-03T14:34:36.040375+00:00'
page_id: json_AbstractSearch
product: fluig
source: rest-fluig
title: Fluig REST — AbstractSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_AbstractSearch.html
version: 1
---

# AbstractSearch Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| searchType | string |  | The JSON object type. |
| offset | number | required |  |
| ordering | [Ordering](https://api.fluig.com/old/json_Ordering.html) |  |  |
| limit | number | required |  |
| startPeriod | number |  |  |
| pattern | string |  |  |
| endPeriod | number |  |  |
| period | [DateGap](https://api.fluig.com/old/json_DateGap.html) |  |  |
| contentSearch | boolean | required |  |

Example

```
{
  "searchType" : "...",
  "offset" : 12345,
  "ordering" : "OLDEST",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_MONTH",
  "contentSearch" : true
}
```
