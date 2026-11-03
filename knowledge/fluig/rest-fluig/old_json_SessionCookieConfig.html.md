---
content_hash: b20fca65fcfe777767dd22b4f9de548d67344883a5ece22118d2de43b16c0d9d
fetched_at: '2026-11-03T14:34:38.380108+00:00'
page_id: json_SessionCookieConfig
product: fluig
source: rest-fluig
title: Fluig REST — SessionCookieConfig Data Type
type: documentation
url: https://api.fluig.com/old/json_SessionCookieConfig.html
version: 1
---

# SessionCookieConfig Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| maxAge | number | required |  |
| comment | string |  |  |
| name | string |  |  |
| path | string |  |  |
| httpOnly | boolean | required |  |
| domain | string |  |  |
| secure | boolean | required |  |

Example

```
{
  "maxAge" : 12345,
  "comment" : "...",
  "name" : "...",
  "path" : "...",
  "httpOnly" : true,
  "domain" : "...",
  "secure" : true
}
```
