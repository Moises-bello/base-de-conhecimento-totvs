---
content_hash: a46e60bc0ae59ac04a29e11af090ebbacbd0551850532e32ee0508fddaa20327
fetched_at: '2026-11-03T14:34:38.482295+00:00'
page_id: json_SocialBreadcrumbVO_social
product: fluig
source: rest-fluig
title: Fluig REST — SocialBreadcrumbVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialBreadcrumbVO_social.html
version: 1
---

# SocialBreadcrumbVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| items | array of [SocialBreadcrumbItemVO](https://api.fluig.com/old/json_SocialBreadcrumbItemVO.html) |  |
| map | map of string |  |

Example

```
{
  "items" : [ {
    "description" : "...",
    "url" : "..."
  }, {
    "description" : "...",
    "url" : "..."
  } ],
  "map" : {
    "property1" : "...",
    "property2" : "..."
  }
}
```
