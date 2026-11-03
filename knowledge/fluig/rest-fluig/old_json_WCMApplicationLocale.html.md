---
content_hash: 66ac5c4492cb95c0db692cba6acbd5988b8f0a7b3d22da00737b7302548285dd
fetched_at: '2026-11-03T14:34:38.827694+00:00'
page_id: json_WCMApplicationLocale
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationLocale Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationLocale.html
version: 1
---

# WCMApplicationLocale Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| application | [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) |  |
| code | string |  |
| id | number |  |

Example

```
{
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
  "code" : "...",
  "id" : 12345
}
```
