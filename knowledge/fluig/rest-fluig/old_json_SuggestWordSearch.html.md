---
content_hash: 31c126f0e02dc8b9e4e9c0693c57e29194a6e9debef76484d41114d46e6efd74
fetched_at: '2026-11-03T14:34:38.629681+00:00'
page_id: json_SuggestWordSearch
product: fluig
source: rest-fluig
title: Fluig REST — SuggestWordSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_SuggestWordSearch.html
version: 1
---

# SuggestWordSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| types | array of string |  |
| filters | array of string |  |
| requestHandler | string |  |
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
  "types" : [ "...", "..." ],
  "filters" : [ "...", "..." ],
  "requestHandler" : "...",
  "searchType" : "WORD",
  "offset" : 12345,
  "ordering" : "RELEVANT",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_DAY",
  "contentSearch" : true
}
```
