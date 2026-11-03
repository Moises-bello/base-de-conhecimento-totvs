---
content_hash: 1e83c4e68d0632388a1b6590d9b247ab6b53d26f4e62b112def8b1890ebd6b9c
fetched_at: '2026-11-03T14:34:38.068007+00:00'
page_id: json_ProcessSearch
product: fluig
source: rest-fluig
title: Fluig REST — ProcessSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessSearch.html
version: 1
---

# ProcessSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| filters | array of string |  |
| requestHandler | string |  |
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
  "filters" : [ "...", "..." ],
  "requestHandler" : "...",
  "types" : [ "...", "..." ],
  "searchType" : "PROCESS",
  "offset" : 12345,
  "ordering" : "OLDEST",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_YEAR",
  "contentSearch" : true
}
```
