---
content_hash: 9346c192b9215da776526f4208b1baf399aae585ffdfeea9f5b0773eec4823f3
fetched_at: '2026-11-03T14:34:38.729258+00:00'
page_id: json_UserAuthTokenSessionVO
product: fluig
source: rest-fluig
title: Fluig REST — UserAuthTokenSessionVO Data Type
type: documentation
url: https://api.fluig.com/old/json_UserAuthTokenSessionVO.html
version: 1
---

# UserAuthTokenSessionVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| domain | string |  |  |
| companyId | string |  |  |
| userIdIdp | string |  |  |
| session | map of string |  |  |
| serialversionuid | number | required |  |
| accessToken | string |  |  |
| issuedTime | number |  |  |
| expiresIn | number |  |  |
| refreshToken | string |  |  |

Example

```
{
  "domain" : "...",
  "companyId" : "...",
  "userIdIdp" : "...",
  "session" : {
    "property1" : "...",
    "property2" : "..."
  },
  "serialversionuid" : 12345,
  "accessToken" : "...",
  "issuedTime" : 12345,
  "expiresIn" : 12345,
  "refreshToken" : "..."
}
```
