---
content_hash: da64df0590927012d464941f67344a2432ede907f9424e9e266867a92b79b301
fetched_at: '2026-11-03T14:34:38.392830+00:00'
page_id: json_ShareVO_service
product: fluig
source: rest-fluig
title: Fluig REST — ShareVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ShareVO_service.html
version: 1
---

# ShareVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| contentId | number |  |
| shareType | [SourceShareType](https://api.fluig.com/old/json_SourceShareType.html) |  |
| contentType | string |  |
| type | [SociableShareType](https://api.fluig.com/old/json_SociableShareType.html) |  |
| text | string |  |
| originUrl | string |  |
| linkUrl | string |  |
| socialTargets | array of number |  |
| aliasTargets | array of string |  |

Example

```
{
  "contentId" : 12345,
  "shareType" : "SOCIAL",
  "contentType" : "...",
  "type" : "FOLLOWERS",
  "text" : "...",
  "originUrl" : "...",
  "linkUrl" : "...",
  "socialTargets" : [ 12345, 12345 ],
  "aliasTargets" : [ "...", "..." ]
}
```
