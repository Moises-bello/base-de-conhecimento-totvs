---
content_hash: 3f4771697356b8db73d6affcbfd658ae9b5290aa13339bd8ffbc9eefebda1d7a
fetched_at: '2026-11-03T14:34:38.836748+00:00'
page_id: json_WCMApplicationService
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationService Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationService.html
version: 1
---

# WCMApplicationService Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| varName | string |  |
| jndiName | string |  |
| application | [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) |  |
| id | number |  |

Example

```
{
  "varName" : "...",
  "jndiName" : "...",
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
  "id" : 12345
}
```
