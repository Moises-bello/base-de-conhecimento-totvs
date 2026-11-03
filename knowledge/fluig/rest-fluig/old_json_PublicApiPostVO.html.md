---
content_hash: ea0e5a596c3dbefc0e7c20ced9eb9b40a81fe512d876da8358dcfbca8e3b9346
fetched_at: '2026-11-03T14:34:38.139688+00:00'
page_id: json_PublicApiPostVO
product: fluig
source: rest-fluig
title: Fluig REST — PublicApiPostVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PublicApiPostVO.html
version: 1
---

# PublicApiPostVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| postId | number |  |
| text | string |  |
| visibility | [SocialPostVisibility](https://api.fluig.com/old/json_SocialPostVisibility.html) |  |
| alias | string |  |
| customUsers | array of number |  |
| sociableObjectId | number |  |
| placesToShare | array of string |  |
| ~~mediaVO~~ | ~~[Base64MediaVO](https://api.fluig.com/old/json_Base64MediaVO.html)~~ |  |
| facts | array of string |  |
| attributes | array of string |  |
| customData | map of string |  |
| attachments | array of string |  |

Example

```
{
  "postId" : 12345,
  "text" : "...",
  "visibility" : "PRIVATE",
  "alias" : "...",
  "customUsers" : [ 12345, 12345 ],
  "sociableObjectId" : 12345,
  "placesToShare" : [ "...", "..." ],
  "facts" : [ "...", "..." ],
  "attributes" : [ "...", "..." ],
  "customData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "attachments" : [ "...", "..." ]
}
```
