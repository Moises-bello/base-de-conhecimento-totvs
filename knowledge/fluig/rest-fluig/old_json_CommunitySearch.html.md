---
content_hash: cfaaa2e63627e1d62b3fb1c01ad5da022ceaa8d6ba782821dd61a94eef4c915b
fetched_at: '2026-11-03T14:34:36.478701+00:00'
page_id: json_CommunitySearch
product: fluig
source: rest-fluig
title: Fluig REST — CommunitySearch Data Type
type: documentation
url: https://api.fluig.com/old/json_CommunitySearch.html
version: 1
---

# CommunitySearch Data Type

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
  "searchType" : "COMMUNITY",
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
