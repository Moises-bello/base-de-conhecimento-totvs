---
content_hash: d7fde44075a9f0b38dc27ad85d24a8452eda22b273d0cd54cbcc282c6aa7db0a
fetched_at: '2026-11-03T14:34:36.211247+00:00'
page_id: json_ArticleCoverVO
product: fluig
source: rest-fluig
title: Fluig REST — ArticleCoverVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleCoverVO.html
version: 1
---

# ArticleCoverVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| coordinateX | number | required |  |
| path | string |  |  |
| image | string |  |  |
| windowHeight | number | required |  |
| height | number | required |  |
| pictureId | string |  |  |
| base64media | string |  |  |
| windowWidth | number | required |  |
| coordinateY | number | required |  |
| width | number | required |  |
| pictureName | string |  |  |
| canvasData | [CropVO](https://api.fluig.com/old/json_CropVO.html) |  |  |
| boxData | [CropVO](https://api.fluig.com/old/json_CropVO.html) |  |  |

Example

```
{
  "coordinateX" : 12345,
  "path" : "...",
  "image" : "...",
  "windowHeight" : 12345,
  "height" : 12345,
  "pictureId" : "...",
  "base64media" : "...",
  "windowWidth" : 12345,
  "coordinateY" : 12345,
  "width" : 12345,
  "pictureName" : "...",
  "canvasData" : {
    "left" : 12345,
    "top" : 12345,
    "width" : 12345,
    "height" : 12345
  },
  "boxData" : {
    "left" : 12345,
    "top" : 12345,
    "width" : 12345,
    "height" : 12345
  }
}
```
