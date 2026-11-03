---
content_hash: 28eda0f752fe67958aa3d1cba24c87dc20cebe1f1375c2f472aafe697e87a8f5
fetched_at: '2026-11-03T14:34:36.946345+00:00'
page_id: json_FavoriteServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — FavoriteServiceRest Data Type
type: documentation
url: https://api.fluig.com/old/json_FavoriteServiceRest.html
version: 1
---

# FavoriteServiceRest Data Type

Favorites

Properties

| name | data type | description |
| --- | --- | --- |
| favorites | array of [FavoriteVO](https://api.fluig.com/old/json_FavoriteVO.html) | Returns all socials marked as favorites. The socials can be users or communities. |
| Properties inherited from [GenericBean](https://api.fluig.com/old/json_GenericBean.html) | | |
| errorHandler | [ErrorHandler](https://api.fluig.com/old/json_ErrorHandler.html) |  |

Example

```
{
  "favorites" : [ {
    "id" : 12345,
    "alias" : "...",
    "name" : "...",
    "socialType" : "...",
    "lastUpdate" : 12345
  }, {
    "id" : 12345,
    "alias" : "...",
    "name" : "...",
    "socialType" : "...",
    "lastUpdate" : 12345
  } ]
}
```
