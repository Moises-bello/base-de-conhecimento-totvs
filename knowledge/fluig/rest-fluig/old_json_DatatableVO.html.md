---
content_hash: 357f70ce17f675e4dd7cc13c3eeb46227acce0d901d79d7b92603a2e0570deaf
fetched_at: '2026-11-03T14:34:36.575807+00:00'
page_id: json_DatatableVO
product: fluig
source: rest-fluig
title: Fluig REST — DatatableVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DatatableVO.html
version: 1
---

# DatatableVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| invdata | array of object |  |  |
| genericObject | object |  |  |
| totalrecords | string |  |  |
| currpage | number | required |  |
| totalpages | number | required |  |

Example

```
{
  "invdata" : [ { }, { } ],
  "genericObject" : { },
  "totalrecords" : "...",
  "currpage" : 12345,
  "totalpages" : 12345
}
```
