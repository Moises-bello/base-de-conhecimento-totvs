---
content_hash: 0d064484a61d7a55d4c65d9b05a06f44bf8ee3c90c9488df500107304cf0b7da
fetched_at: '2026-11-03T14:34:36.466814+00:00'
page_id: json_CommunityCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — CommunityCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CommunityCreateVO.html
version: 1
---

# CommunityCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| alias | string |  |
| name | string |  |
| description | string |  |
| adminAlias | string |  |
| hidden | boolean |  |
| privateContent | boolean |  |
| approvalRequired | boolean |  |
| ecmInfo | map of object |  |
| createForum | boolean |  |

Example

```
{
  "alias" : "...",
  "name" : "...",
  "description" : "...",
  "adminAlias" : "...",
  "hidden" : true,
  "privateContent" : true,
  "approvalRequired" : true,
  "ecmInfo" : {
    "property1" : { },
    "property2" : { }
  },
  "createForum" : true
}
```
