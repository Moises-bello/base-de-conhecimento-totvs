---
content_hash: a3816ff6cfe15b69e968422bd684f04d016e121e4a6ba9cbc74bf684e1eb149f
fetched_at: '2026-11-03T14:34:38.815612+00:00'
page_id: json_WCMApplicationAppDependency
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationAppDependency Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationAppDependency.html
version: 1
---

# WCMApplicationAppDependency Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| applicationDependency | [WCMApplicationDependency](https://api.fluig.com/old/json_WCMApplicationDependency.html) |  |
| active | boolean |  |
| updatedAt | number |  |
| createdAt | number |  |
| component | [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) |  |
| id | number |  |

Example

```
{
  "applicationDependency" : {
    "resourceType" : "...",
    "createdAt" : 12345,
    "code" : "...",
    "updatedAt" : 12345,
    "tenant" : {
      "federalId" : "...",
      "idpId" : "...",
      "resourceType" : "...",
      "useWizard" : true,
      "code" : "...",
      "organizationUrl" : "...",
      "tenantActive" : true,
      "products" : [ { }, { } ],
      "idpLogOff" : true,
      "id" : 12345,
      "resourceDescription" : "...",
      "data" : [ { }, { } ],
      "securityCode" : "...",
      "thumbnailEnabled" : true,
      "UUID" : "...",
      "description" : "...",
      "removeVolume" : true
    },
    "id" : 12345
  },
  "active" : true,
  "updatedAt" : 12345,
  "createdAt" : 12345,
  "component" : {
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
