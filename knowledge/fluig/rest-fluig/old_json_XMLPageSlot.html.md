---
content_hash: 9db3f9a20d2227cb59a2f0f85d9e11a68446146aafe240c47031a573a07dab71
fetched_at: '2026-11-03T14:34:39.244701+00:00'
page_id: json_XMLPageSlot
product: fluig
source: rest-fluig
title: Fluig REST — XMLPageSlot Data Type
type: documentation
url: https://api.fluig.com/old/json_XMLPageSlot.html
version: 1
---

# XMLPageSlot Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| name | string |  |
| widget | string |  |
| showWidgetTitle | boolean |  |
| preferences | array of [XMLWidgetPreferences](https://api.fluig.com/old/json_XMLWidgetPreferences.html) |  |
| systemWidget | boolean |  |
| enabledMobileApp | boolean |  |
| permissions | array of [XMLPermission](https://api.fluig.com/old/json_XMLPermission.html) |  |

Example

```
{
  "name" : "...",
  "widget" : "...",
  "showWidgetTitle" : true,
  "preferences" : [ {
    "value" : "...",
    "key" : "..."
  }, {
    "value" : "...",
    "key" : "..."
  } ],
  "systemWidget" : true,
  "enabledMobileApp" : true,
  "permissions" : [ {
    "code" : "...",
    "user" : "...",
    "tenantCode" : "...",
    "role" : "...",
    "description" : "...",
    "group" : "..."
  }, {
    "code" : "...",
    "user" : "...",
    "tenantCode" : "...",
    "role" : "...",
    "description" : "...",
    "group" : "..."
  } ]
}
```
