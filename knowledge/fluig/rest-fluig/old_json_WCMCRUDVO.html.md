---
content_hash: 1f63e498931d0bc00aa9933bd5fb7e216ccfec699d625c0f22850dbf4314ffe6
fetched_at: '2026-11-03T14:34:38.845741+00:00'
page_id: json_WCMCRUDVO
product: fluig
source: rest-fluig
title: Fluig REST — WCMCRUDVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMCRUDVO.html
version: 1
---

# WCMCRUDVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| totalRecords | number | required |  |
| records | array of object |  |  |
| pageSize | number | required |  |
| sort | string |  |  |
| startIndex | number | required |  |
| message | [FDNMessage](https://api.fluig.com/old/json_FDNMessage.html) |  |  |
| invdata | array of object |  |  |
| recordsReturned | number | required |  |
| dir | string |  |  |
| genericObject | object |  |  |
| totalpages | number | required |  |
| totalrecords | string |  |  |
| currpage | number | required |  |

Example

```
{
  "totalRecords" : 12345,
  "records" : [ { }, { } ],
  "pageSize" : 12345,
  "sort" : "...",
  "startIndex" : 12345,
  "message" : {
    "message" : "...",
    "type" : "INFO",
    "param" : { },
    "errorCode" : "...",
    "detail" : "..."
  },
  "invdata" : [ { }, { } ],
  "recordsReturned" : 12345,
  "dir" : "...",
  "genericObject" : { },
  "totalpages" : 12345,
  "totalrecords" : "...",
  "currpage" : 12345
}
```
