---
content_hash: 4abe23ad4e3c0cef8165e62588a7d895e1cb311d16314b5fdf2b52d46a5910cf
fetched_at: '2026-11-03T14:34:37.174923+00:00'
page_id: json_IdentityQuickViewVO
product: fluig
source: rest-fluig
title: Fluig REST — IdentityQuickViewVO Data Type
type: documentation
url: https://api.fluig.com/old/json_IdentityQuickViewVO.html
version: 1
---

# IdentityQuickViewVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| quickViewRelayState | string |  |  |
| createdTimestamp | number | required |  |
| row | string |  |  |
| url | string |  |  |
| Properties inherited from [IdentityMenuVO](https://api.fluig.com/old/json_IdentityMenuVO.html) | | | |
| applicationId | string |  |  |
| idpLauncherUrl | string |  |  |
| erpLaunchUrl | string |  |  |
| favorite | boolean |  |  |
| hint | string |  |  |
| routineParams | string |  |  |
| sessionId | string |  |  |
| favoriteId | string |  |  |
| launchUrl | string |  |  |
| companyId | string |  |  |
| routine | string |  |  |
| moduleCode | string |  |  |
| relayState | string |  |  |
| launchType | string |  |  |
| Properties inherited from [VO](https://api.fluig.com/old/json_VO.html) | | | |
| displayName | string |  |  |
| success | boolean | required |  |
| externalId | string |  |  |
| id | string |  |  |
| selected | boolean | required |  |
| customfilter | string |  |  |

Example

```
{
  "quickViewRelayState" : "...",
  "createdTimestamp" : 12345,
  "row" : "...",
  "url" : "...",
  "applicationId" : "...",
  "idpLauncherUrl" : "...",
  "erpLaunchUrl" : "...",
  "favorite" : true,
  "hint" : "...",
  "routineParams" : "...",
  "sessionId" : "...",
  "favoriteId" : "...",
  "launchUrl" : "...",
  "companyId" : "...",
  "routine" : "...",
  "moduleCode" : "...",
  "relayState" : "...",
  "launchType" : "...",
  "displayName" : "...",
  "success" : true,
  "externalId" : "...",
  "id" : "...",
  "selected" : true,
  "customfilter" : "..."
}
```
