---
content_hash: 99d92d82279da252ec88d29f62a146af4be0a64515f48699611e06b2ad829aa9
fetched_at: '2026-11-03T14:34:36.217516+00:00'
page_id: json_ArticleCoverVO_article
product: fluig
source: rest-fluig
title: Fluig REST — ArticleCoverVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ArticleCoverVO_article.html
version: 1
---

# ArticleCoverVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| path | string |  |  |
| pictureName | string |  |  |
| image | string |  |  |
| coordinateX | number | required |  |
| coordinateY | number | required |  |
| width | number | required |  |
| height | number | required |  |
| base64media | string |  |  |
| canvasData | [CropVO](https://api.fluig.com/old/json_CropVO.html) |  |  |
| boxData | [CropVO](https://api.fluig.com/old/json_CropVO.html) |  |  |
| pictureId | string |  |  |
| windowWidth | number | required | Recupera o valor do field windowWidth |
| windowHeight | number | required | Recupera o valor do field windowHeight |

Example

```
{
  "path" : "...",
  "pictureName" : "...",
  "image" : "...",
  "coordinateX" : 12345,
  "coordinateY" : 12345,
  "width" : 12345,
  "height" : 12345,
  "base64media" : "...",
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
  },
  "pictureId" : "...",
  "windowWidth" : 12345,
  "windowHeight" : 12345
}
```
