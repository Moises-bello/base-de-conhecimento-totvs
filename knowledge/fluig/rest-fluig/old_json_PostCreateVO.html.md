---
content_hash: 0b25e6037afc260af68900248a747367466eea695d35ac8798d5800675ed3fb6
fetched_at: '2026-11-03T14:34:37.979207+00:00'
page_id: json_PostCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — PostCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PostCreateVO.html
version: 1
---

# PostCreateVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| text | string |  |
| visibility | string |  |
| alias | string |  |
| customUsers | array of number |  |
| sociableObjectId | number |  |
| mediaVO | [MediaVO](https://api.fluig.com/old/json_MediaVO_social.html) |  |

Example

```
{
  "text" : "...",
  "visibility" : "...",
  "alias" : "...",
  "customUsers" : [ 12345, 12345 ],
  "sociableObjectId" : 12345,
  "mediaVO" : {
    "mediaName" : "...",
    "mediaVersion" : 12345,
    "mediaId" : "...",
    "mediaType" : "..."
  }
}
```
