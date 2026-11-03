---
content_hash: 7279e932adcd8fe85366859628eccca5da306dc5ae19f4a903a75cd53e762dab
fetched_at: '2026-11-03T14:34:38.799829+00:00'
page_id: json_ViewingSessionProperties
product: fluig
source: rest-fluig
title: Fluig REST — ViewingSessionProperties Data Type
type: documentation
url: https://api.fluig.com/old/json_ViewingSessionProperties.html
version: 1
---

# ViewingSessionProperties Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| watermarks | array of [WatermarkProperties](https://api.fluig.com/old/json_WatermarkProperties.html) |  |  |
| serverCaching | string |  |  |
| attachmentIndex | number | required |  |
| watermarkText | string |  |  |
| externalId | string |  |  |
| render | [RenderProperties](https://api.fluig.com/old/json_RenderProperties.html) |  |  |
| contentType | string |  |  |
| tenantId | string |  |  |
| documentSource | string |  |  |
| creationTime | string |  |  |
| documentExtension | string |  |  |
| attachmentDisplayName | string |  |  |
| origin | map of string |  |  |
| password | string |  |  |
| countOfInitialPages | number | required |  |
| startConverting | string |  |  |

Example

```
{
  "watermarks" : [ {
    "slope" : "...",
    "type" : "...",
    "verticalAlign" : "...",
    "color" : "...",
    "fontFamily" : "...",
    "horizontalAlign" : "...",
    "fontWeight" : "...",
    "fontStyle" : "...",
    "text" : "...",
    "fontSize" : "...",
    "opacity" : 12345.0
  }, {
    "slope" : "...",
    "type" : "...",
    "verticalAlign" : "...",
    "color" : "...",
    "fontFamily" : "...",
    "horizontalAlign" : "...",
    "fontWeight" : "...",
    "fontStyle" : "...",
    "text" : "...",
    "fontSize" : "...",
    "opacity" : 12345.0
  } ],
  "serverCaching" : "...",
  "attachmentIndex" : 12345,
  "watermarkText" : "...",
  "externalId" : "...",
  "render" : {
    "html5" : {
      "rasterResolution" : 12345,
      "alwaysUseRaster" : true
    },
    "flash" : {
      "optimizationLevel" : 12345
    }
  },
  "contentType" : "...",
  "tenantId" : "...",
  "documentSource" : "...",
  "creationTime" : "...",
  "documentExtension" : "...",
  "attachmentDisplayName" : "...",
  "origin" : {
    "property1" : "...",
    "property2" : "..."
  },
  "password" : "...",
  "countOfInitialPages" : 12345,
  "startConverting" : "..."
}
```
