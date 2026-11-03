---
content_hash: fe586683385f67768e30a51f88ec3061b986c672c76abd89551e18440c5c80a2
fetched_at: '2026-11-03T14:34:37.061975+00:00'
page_id: json_FormSearch
product: fluig
source: rest-fluig
title: Fluig REST — FormSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_FormSearch.html
version: 1
---

# FormSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| requestHandler | string |  |
| types | array of string |  |
| filters | array of string |  |
| fields | map of string |  |
| formToSearch | number |  |
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
  "fields" : {
    "property1" : "...",
    "property2" : "..."
  },
  "formToSearch" : 12345,
  "searchType" : "FORM",
  "offset" : 12345,
  "ordering" : "OLDEST",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_HOUR",
  "contentSearch" : true
}
```
