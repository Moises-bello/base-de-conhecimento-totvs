---
content_hash: 427a08f7decfe638b2273f7f06412b07e3bee9b2ef6dbdd0590f52d96f3248b8
fetched_at: '2026-11-03T14:34:38.704369+00:00'
page_id: json_TimelineSearch
product: fluig
source: rest-fluig
title: Fluig REST — TimelineSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_TimelineSearch.html
version: 1
---

# TimelineSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| filters | array of string |  |
| author | number |  |
| requestHandler | string |  |
| types | array of string |  |
| communityToSearch | number |  |
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
  "author" : 12345,
  "requestHandler" : "...",
  "types" : [ "...", "..." ],
  "communityToSearch" : 12345,
  "searchType" : "POST",
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
