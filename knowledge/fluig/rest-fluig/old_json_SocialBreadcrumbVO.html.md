---
content_hash: 651320da3a09a0226d54afd7f81c93b406a53abe2b3b50dea88e3fccb0aea06b
fetched_at: '2026-11-03T14:34:38.477540+00:00'
page_id: json_SocialBreadcrumbVO
product: fluig
source: rest-fluig
title: Fluig REST — SocialBreadcrumbVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialBreadcrumbVO.html
version: 1
---

# SocialBreadcrumbVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| map | map of string |  |
| items | array of [SocialBreadcrumbItemVO](https://api.fluig.com/old/json_SocialBreadcrumbItemVO_vo.html) |  |

Example

```
{
  "map" : {
    "property1" : "...",
    "property2" : "..."
  },
  "items" : [ {
    "description" : "...",
    "url" : "..."
  }, {
    "description" : "...",
    "url" : "..."
  } ]
}
```
