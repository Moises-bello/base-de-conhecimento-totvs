---
content_hash: 3b909cb082ac7c190795e9f9a5b82defdd6f03cbc5402ec5c5ccc87c211c61d6
fetched_at: '2026-11-03T14:34:36.312260+00:00'
page_id: json_AuthorizeClientVO
product: fluig
source: rest-fluig
title: Fluig REST — AuthorizeClientVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AuthorizeClientVO.html
version: 1
---

# AuthorizeClientVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| serviceCode | string |  |
| method | string |  |
| endpoint | string |  |
| params | map of object |  |
| companyId | number |  |
| timeoutService | string |  |

Example

```
{
  "serviceCode" : "...",
  "method" : "...",
  "endpoint" : "...",
  "params" : {
    "property1" : { },
    "property2" : { }
  },
  "companyId" : 12345,
  "timeoutService" : "..."
}
```
