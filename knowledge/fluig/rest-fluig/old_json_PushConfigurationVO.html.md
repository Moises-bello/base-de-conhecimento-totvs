---
content_hash: 8b72962e540575b6848addc9f1f5d68f58b8e679c59c0ef09d152e7b177d7b2c
fetched_at: '2026-11-03T14:34:38.183372+00:00'
page_id: json_PushConfigurationVO
product: fluig
source: rest-fluig
title: Fluig REST — PushConfigurationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PushConfigurationVO.html
version: 1
---

# PushConfigurationVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| token | string |  |
| channel | string |  |
| language | string |  |
| deviceToken | string |  |
| imei | string |  |
| pushService | [PushServiceEnum](https://api.fluig.com/old/json_PushServiceEnum.html) |  |
| pushApp | [PushAppEnum](https://api.fluig.com/old/json_PushAppEnum.html) |  |

Example

```
{
  "token" : "...",
  "channel" : "...",
  "language" : "...",
  "deviceToken" : "...",
  "imei" : "...",
  "pushService" : "URBAN_AIRSHIP",
  "pushApp" : "MY_APPROVAL"
}
```
