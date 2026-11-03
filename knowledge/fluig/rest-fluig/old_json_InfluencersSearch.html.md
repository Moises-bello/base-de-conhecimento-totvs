---
content_hash: 68a1e83b71b87f2cb07ed60cfafaba08d0ec0e06475313eadff6f5596fa21b61
fetched_at: '2026-11-03T14:34:37.198948+00:00'
page_id: json_InfluencersSearch
product: fluig
source: rest-fluig
title: Fluig REST — InfluencersSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_InfluencersSearch.html
version: 1
---

# InfluencersSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| queryFilters | string |  |
| params | map of string |  |
| pattern | string |  |
| influencers | array of map of string |  |
| types | array of string |  |
| facetPivotField | string |  |
| requestHandler | string |  |
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
  "queryFilters" : "...",
  "params" : {
    "property1" : "...",
    "property2" : "..."
  },
  "pattern" : "...",
  "influencers" : [ {
    "property1" : "...",
    "property2" : "..."
  }, {
    "property1" : "...",
    "property2" : "..."
  } ],
  "types" : [ "...", "..." ],
  "facetPivotField" : "...",
  "requestHandler" : "...",
  "filters" : [ "...", "..." ],
  "searchType" : "INFLUENCERS",
  "offset" : 12345,
  "ordering" : "RELEVANT",
  "limit" : 12345,
  "startPeriod" : 12345,
  "endPeriod" : 12345,
  "period" : "LAST_YEAR",
  "contentSearch" : true
}
```
