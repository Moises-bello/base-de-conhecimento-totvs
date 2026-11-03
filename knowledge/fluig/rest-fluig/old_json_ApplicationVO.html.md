---
content_hash: 243f96eafd71bf2490545d66741b2b774aefe30bd7f67bfd4a56fdce85c2592c
fetched_at: '2026-11-03T14:34:36.197656+00:00'
page_id: json_ApplicationVO
product: fluig
source: rest-fluig
title: Fluig REST — ApplicationVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ApplicationVO.html
version: 1
---

# ApplicationVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
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
