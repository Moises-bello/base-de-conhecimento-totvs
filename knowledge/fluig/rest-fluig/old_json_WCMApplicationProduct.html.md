---
content_hash: 1f3fba5b6d5e6686d609f5f30be9865255f845c946597dac0d14c759e4dd291f
fetched_at: '2026-11-03T14:34:38.830447+00:00'
page_id: json_WCMApplicationProduct
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationProduct Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationProduct.html
version: 1
---

# WCMApplicationProduct Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| product | string |  |
| application | [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) |  |

Example

```
{
  "id" : 12345,
  "product" : "...",
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
  }
}
```
