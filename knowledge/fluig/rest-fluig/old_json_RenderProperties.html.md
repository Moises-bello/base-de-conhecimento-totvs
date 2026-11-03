---
content_hash: 4584e0a77b4d6d3c23f18ace0da28dba6585894bc36238e26e0512a7edb93c9d
fetched_at: '2026-11-03T14:34:38.224477+00:00'
page_id: json_RenderProperties
product: fluig
source: rest-fluig
title: Fluig REST — RenderProperties Data Type
type: documentation
url: https://api.fluig.com/old/json_RenderProperties.html
version: 1
---

# RenderProperties Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| html5 | [Html5RenderProperties](https://api.fluig.com/old/json_Html5RenderProperties.html) |  |
| flash | [FlashRenderProperties](https://api.fluig.com/old/json_FlashRenderProperties.html) |  |

Example

```
{
  "html5" : {
    "rasterResolution" : 12345,
    "alwaysUseRaster" : true
  },
  "flash" : {
    "optimizationLevel" : 12345
  }
}
```
