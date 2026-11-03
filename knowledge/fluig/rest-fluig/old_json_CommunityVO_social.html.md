---
content_hash: 34801fe20233018a8e52be99282da53d3d3f2a05a58be7ebc088b72d0b5ae084
fetched_at: '2026-11-03T14:34:36.492410+00:00'
page_id: json_CommunityVO_social
product: fluig
source: rest-fluig
title: Fluig REST — CommunityVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CommunityVO_social.html
version: 1
---

# CommunityVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| createForum | boolean |  |
| name | string |  |
| adminAlias | string |  |
| ecmInfo | map of object |  |
| privateContent | boolean |  |
| description | string |  |
| alias | string |  |
| id | number |  |
| approvalRequired | boolean |  |
| hidden | boolean |  |

Example

```
{
  "createForum" : true,
  "name" : "...",
  "adminAlias" : "...",
  "ecmInfo" : {
    "property1" : { },
    "property2" : { }
  },
  "privateContent" : true,
  "description" : "...",
  "alias" : "...",
  "id" : 12345,
  "approvalRequired" : true,
  "hidden" : true
}
```
