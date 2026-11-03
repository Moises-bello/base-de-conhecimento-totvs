---
content_hash: a2bdb28f4a677d67d09c7193e456a781fe35563ca25cf3870931d044aeeb49ff
fetched_at: '2026-11-03T14:34:38.624316+00:00'
page_id: json_SuggestTagSearch
product: fluig
source: rest-fluig
title: Fluig REST — SuggestTagSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_SuggestTagSearch.html
version: 1
---

# SuggestTagSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| requestHandler | string |  |
| filters | array of string |  |
| types | array of string |  |
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
  "filters" : [ "...", "..." ],
  "types" : [ "...", "..." ],
  "searchType" : "TAG",
  "offset" : 12345,
  "ordering" : "NEWEST",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_DAY",
  "contentSearch" : true
}
```
