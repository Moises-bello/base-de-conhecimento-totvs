---
content_hash: d7f3ade4573ff89edad061cb62e83f8f9875f5f737d775df082d2f3e4710bdba
fetched_at: '2026-11-03T14:34:37.088500+00:00'
page_id: json_GlobalSearch
product: fluig
source: rest-fluig
title: Fluig REST — GlobalSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_GlobalSearch.html
version: 1
---

# GlobalSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| requestHandler | string |  |
| types | array of string |  |
| filters | array of string |  |
| Properties inherited from [AbstractSearch](https://api.fluig.com/old/json_AbstractSearch.html) | | |
| searchType | string | The JSON object type. |
| offset | number |  |
| ordering | [Ordering](https://api.fluig.com/old/json_Ordering.html) |  |
| limit | number |  |
| startPeriod | number |  |
| pattern | string |  |
| endPeriod | number |  |
| period | [DateGap](https://api.fluig.com/old/json_DateGap.html) |  |
| contentSearch | boolean |  |

Example

```
{
  "requestHandler" : "...",
  "types" : [ "...", "..." ],
  "filters" : [ "...", "..." ],
  "searchType" : "GLOBAL",
  "offset" : 12345,
  "ordering" : "NEWEST",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_YEAR",
  "contentSearch" : true
}
```
