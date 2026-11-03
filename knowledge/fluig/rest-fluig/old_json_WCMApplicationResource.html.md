---
content_hash: 809c44eeeeb9e5bd7c1919e504ea18d2d7e39823597b81bc1904c536d5840e96
fetched_at: '2026-11-03T14:34:38.833704+00:00'
page_id: json_WCMApplicationResource
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationResource Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationResource.html
version: 1
---

# WCMApplicationResource Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| order | number |  |
| type | string |  |
| id | number |  |
| application | [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) |  |
| resource | string |  |

Example

```
{
  "order" : 12345,
  "type" : "...",
  "id" : 12345,
  "application" : {
    "earFileName" : "...",
    "title" : "...",
    "maxHeight" : 12345,
    "locales" : [ {
      "application" : { },
      "code" : "...",
      "id" : 12345
    }, {
      "application" : { },
      "code" : "...",
      "id" : 12345
    } ],
    "minHeight" : 12345,
    "product" : "...",
    "internal" : true,
    "fileName" : "...",
    "originCode" : "...",
    "description" : "...",
    "icon" : "...",
    "developerUrl" : "...",
    "id" : 12345,
    "extendedData" : "...",
    "localeFileBaseName" : "...",
    "appTenantCode" : "...",
    "developerName" : "...",
    "applicationExtensible" : true,
    "categories" : [ {
      "category" : "...",
      "application" : { },
      "id" : 12345
    }, {
      "category" : "...",
      "application" : { },
      "id" : 12345
    } ],
    "maxWidth" : 12345,
    "services" : [ {
      "varName" : "...",
      "jndiName" : "...",
      "application" : { },
      "id" : 12345
    }, {
      "varName" : "...",
      "jndiName" : "...",
      "application" : { },
      "id" : 12345
    } ],
    "renderer" : "...",
    "developerCode" : "...",
    "resources" : [ {
      "order" : 12345,
      "type" : "...",
      "id" : 12345,
      "application" : { },
      "resource" : "..."
    }, {
      "order" : 12345,
      "type" : "...",
      "id" : 12345,
      "application" : { },
      "resource" : "..."
    } ],
    "context" : "...",
    "applicationVersion" : "...",
    "applicationPublic" : true,
    "isExtension" : true,
    "minWidth" : 12345,
    "code" : "...",
    "activationClass" : "..."
  },
  "resource" : "..."
}
```
