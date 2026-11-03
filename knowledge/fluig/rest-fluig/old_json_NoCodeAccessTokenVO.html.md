---
content_hash: a0c9c8b0c92e97c43837a215f83d6ca74b849c017200ce95cabafef88b211998
fetched_at: '2026-11-03T14:34:37.875138+00:00'
page_id: json_NoCodeAccessTokenVO
product: fluig
source: rest-fluig
title: Fluig REST — NoCodeAccessTokenVO Data Type
type: documentation
url: https://api.fluig.com/old/json_NoCodeAccessTokenVO.html
version: 1
---

# NoCodeAccessTokenVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| access\_token | string |  |  |
| token\_type | string |  |  |
| expires\_in | number | required |  |
| refresh\_token | string |  |  |

Example

```
{
  "access_token" : "...",
  "token_type" : "...",
  "expires_in" : 12345,
  "refresh_token" : "..."
}
```
