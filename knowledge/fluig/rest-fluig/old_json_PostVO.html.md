---
content_hash: ab3889be319fa655aed1fdbfe88c7ebc120f586dcfa9170cb4ce003d9c96d72b
fetched_at: '2026-11-03T14:34:37.988289+00:00'
page_id: json_PostVO
product: fluig
source: rest-fluig
title: Fluig REST — PostVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PostVO.html
version: 1
---

# PostVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| visibility | string |  |
| customUsers | array of number |  |
| text | string |  |
| sociableObjectId | number |  |
| mediaVO | [MediaVO](https://api.fluig.com/old/json_MediaVO_social.html) |  |
| id | number |  |
| alias | string |  |

Example

```
{
  "visibility" : "...",
  "customUsers" : [ 12345, 12345 ],
  "text" : "...",
  "sociableObjectId" : 12345,
  "mediaVO" : {
    "mediaName" : "...",
    "mediaVersion" : 12345,
    "mediaId" : "...",
    "mediaType" : "..."
  },
  "id" : 12345,
  "alias" : "..."
}
```
