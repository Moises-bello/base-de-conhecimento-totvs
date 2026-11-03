---
content_hash: 0635440416d92a4a81f4cfe0ade39ae80317a03e85b7d4cb1eedba7bf4654a38
fetched_at: '2026-11-03T14:34:38.751136+00:00'
page_id: json_UserSearch
product: fluig
source: rest-fluig
title: Fluig REST — UserSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_UserSearch.html
version: 1
---

# UserSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| requestHandler | string |  |
| types | array of string |  |
| communityToSearch | number |  |
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
  "communityToSearch" : 12345,
  "filters" : [ "...", "..." ],
  "searchType" : "USER",
  "offset" : 12345,
  "ordering" : "RELEVANT",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_WEEK",
  "contentSearch" : true
}
```
