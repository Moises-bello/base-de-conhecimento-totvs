---
content_hash: 2afa291979d81236270d7129df48d2de875c0a3d1af8ba93178fc2812eb55005
fetched_at: '2026-11-03T14:34:37.872037+00:00'
page_id: json_NewCookie
product: fluig
source: rest-fluig
title: Fluig REST — NewCookie Data Type
type: documentation
url: https://api.fluig.com/old/json_NewCookie.html
version: 1
---

# NewCookie Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| secure | boolean | required |  |
| comment | string |  |  |
| maxAge | number | required |  |
| httpOnly | boolean | required |  |
| expiry | number |  |  |
| Properties inherited from [Cookie](https://api.fluig.com/old/json_Cookie.html) | | | |
| name | string |  |  |
| domain | string |  |  |
| version | number | required |  |
| path | string |  |  |
| value | string |  |  |

Example

```
{
  "secure" : true,
  "comment" : "...",
  "maxAge" : 12345,
  "httpOnly" : true,
  "expiry" : 12345,
  "name" : "...",
  "domain" : "...",
  "version" : 12345,
  "path" : "...",
  "value" : "..."
}
```
