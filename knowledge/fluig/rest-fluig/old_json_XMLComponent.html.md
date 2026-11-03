---
content_hash: 1eb0594433ffb87165f034c680db2b53ab782000e49c289bb7937b59bb6fa7fa
fetched_at: '2026-11-03T14:34:39.227920+00:00'
page_id: json_XMLComponent
product: fluig
source: rest-fluig
title: Fluig REST — XMLComponent Data Type
type: documentation
url: https://api.fluig.com/old/json_XMLComponent.html
version: 1
---

# XMLComponent Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| developerName | string |  |
| code | string |  |
| dependencies | array of [XMLComponentDependency](https://api.fluig.com/old/json_XMLComponentDependency.html) |  |
| developerCode | string |  |
| developerURL | string |  |
| activationClass | string |  |
| icon | string |  |
| version | string |  |
| category | string |  |
| title | string |  |
| description | string |  |

Example

```
{
  "developerName" : "...",
  "code" : "...",
  "dependencies" : [ {
    "resourceType" : "...",
    "file" : "...",
    "code" : "..."
  }, {
    "resourceType" : "...",
    "file" : "...",
    "code" : "..."
  } ],
  "developerCode" : "...",
  "developerURL" : "...",
  "activationClass" : "...",
  "icon" : "...",
  "version" : "...",
  "category" : "...",
  "title" : "...",
  "description" : "..."
}
```
