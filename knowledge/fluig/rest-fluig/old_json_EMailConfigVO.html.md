---
content_hash: 55bb2500d3b02f0fe786729e737ad51a271e7c8a0edb142383a4ab780c16ac9f
fetched_at: '2026-11-03T14:34:36.753937+00:00'
page_id: json_EMailConfigVO
product: fluig
source: rest-fluig
title: Fluig REST — EMailConfigVO Data Type
type: documentation
url: https://api.fluig.com/old/json_EMailConfigVO.html
version: 1
---

# EMailConfigVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| tenantId | number | required |  |
| smtpServer | string |  |  |
| smtpPort | number | required |  |
| emailFrom | string |  |  |
| emailSecurity | string |  |  |
| user | string |  |  |
| password | string |  |  |
| connectionTimeout | number |  |  |

Example

```
{
  "tenantId" : 12345,
  "smtpServer" : "...",
  "smtpPort" : 12345,
  "emailFrom" : "...",
  "emailSecurity" : "...",
  "user" : "...",
  "password" : "...",
  "connectionTimeout" : 12345
}
```
