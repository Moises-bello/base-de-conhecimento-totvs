---
content_hash: 184909864e08fdc27b92bb5d8b3db6015244ccd93befdd9e61eb8f00bca995f1
fetched_at: '2026-11-03T14:34:37.161521+00:00'
page_id: json_IdentityQuickViewDataVO
product: fluig
source: rest-fluig
title: Fluig REST — IdentityQuickViewDataVO Data Type
type: documentation
url: https://api.fluig.com/old/json_IdentityQuickViewDataVO.html
version: 1
---

# IdentityQuickViewDataVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| currpage | number |  |
| data | array of map of string |  |
| totalpages | number |  |
| totalrecords | number |  |
| Properties inherited from [VO](https://api.fluig.com/old/json_VO.html) | | |
| displayName | string |  |
| success | boolean |  |
| externalId | string |  |
| id | string |  |
| selected | boolean |  |
| customfilter | string |  |

Example

```
{
  "currpage" : 12345,
  "data" : [ {
    "property1" : "...",
    "property2" : "..."
  }, {
    "property1" : "...",
    "property2" : "..."
  } ],
  "totalpages" : 12345,
  "totalrecords" : 12345,
  "displayName" : "...",
  "success" : true,
  "externalId" : "...",
  "id" : "...",
  "selected" : true,
  "customfilter" : "..."
}
```
