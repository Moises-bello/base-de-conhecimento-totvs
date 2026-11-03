---
content_hash: 7e15906ec5a225532608cfc29f5cc0cec972db53b9aa89f9a85de20c8f614c33
fetched_at: '2026-11-03T14:34:39.050379+00:00'
page_id: json_WidgetVO
product: fluig
source: rest-fluig
title: Fluig REST — WidgetVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WidgetVO.html
version: 1
---

# WidgetVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| applicationNoCodeCategory | string |  |
| uiWidget | boolean |  |
| applicationMoreInfo | string |  |
| type | string |  |
| mobileAppWidget | boolean |  |
| Properties inherited from [ApplicationVO](https://api.fluig.com/old/json_ApplicationVO.html) | | |
| internal | boolean |  |
| title | string |  |
| resources | map of string |  |
| resourcesCSS | array of string |  |
| description | string |  |
| code | string |  |
| icon | string |  |
| services | map of string |  |
| id | number |  |
| developerCode | string |  |
| renderer | string |  |
| developerUrl | string |  |
| localeFileBaseName | string |  |
| applicationContext | string |  |
| developerName | string |  |
| resourcesJS | array of string |  |
| categories | array of string |  |
| version | string |  |
| locales | array of string |  |
| extendedData | string |  |

Example

```
{
  "applicationNoCodeCategory" : "...",
  "uiWidget" : true,
  "applicationMoreInfo" : "...",
  "type" : "...",
  "mobileAppWidget" : true,
  "internal" : true,
  "title" : "...",
  "resources" : {
    "property1" : "...",
    "property2" : "..."
  },
  "resourcesCSS" : [ "...", "..." ],
  "description" : "...",
  "code" : "...",
  "icon" : "...",
  "services" : {
    "property1" : "...",
    "property2" : "..."
  },
  "id" : 12345,
  "developerCode" : "...",
  "renderer" : "...",
  "developerUrl" : "...",
  "localeFileBaseName" : "...",
  "applicationContext" : "...",
  "developerName" : "...",
  "resourcesJS" : [ "...", "..." ],
  "categories" : [ "...", "..." ],
  "version" : "...",
  "locales" : [ "...", "..." ],
  "extendedData" : "..."
}
```
