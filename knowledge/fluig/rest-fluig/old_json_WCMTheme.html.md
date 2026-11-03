---
content_hash: 1f03d9da528e8e3f2506192e9eccfa2e5f9df681f130972527dbc9a7395b436b
fetched_at: '2026-11-03T14:34:38.963159+00:00'
page_id: json_WCMTheme
product: fluig
source: rest-fluig
title: Fluig REST — WCMTheme Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMTheme.html
version: 1
---

# WCMTheme Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| themeFile | string |  |
| type | string |  |
| securityCode | string |  |
| resourceLongDescription | string |  |
| resourceType | string |  |
| resourceDescription | string |  |
| Properties inherited from [WCMApplication](https://api.fluig.com/old/json_WCMApplication.html) | | |
| earFileName | string |  |
| title | string |  |
| maxHeight | number |  |
| locales | array of [WCMApplicationLocale](https://api.fluig.com/old/json_WCMApplicationLocale.html) |  |
| minHeight | number |  |
| product | string |  |
| internal | boolean |  |
| fileName | string |  |
| originCode | string |  |
| description | string |  |
| icon | string |  |
| developerUrl | string |  |
| id | number |  |
| extendedData | string |  |
| localeFileBaseName | string |  |
| appTenantCode | string |  |
| developerName | string |  |
| applicationExtensible | boolean |  |
| categories | array of [WCMApplicationCategory](https://api.fluig.com/old/json_WCMApplicationCategory.html) |  |
| maxWidth | number |  |
| services | array of [WCMApplicationService](https://api.fluig.com/old/json_WCMApplicationService.html) |  |
| renderer | string |  |
| developerCode | string |  |
| resources | array of [WCMApplicationResource](https://api.fluig.com/old/json_WCMApplicationResource.html) |  |
| context | string |  |
| applicationVersion | string |  |
| applicationPublic | boolean |  |
| isExtension | boolean |  |
| minWidth | number |  |
| code | string |  |
| activationClass | string |  |

Example

```
{
  "themeFile" : "...",
  "type" : "...",
  "securityCode" : "...",
  "resourceLongDescription" : "...",
  "resourceType" : "...",
  "resourceDescription" : "...",
  "earFileName" : "...",
  "title" : "...",
  "maxHeight" : 12345,
  "locales" : [ {
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
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
  }, {
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
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
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
      "context" : "...",
      "applicationVersion" : "...",
      "applicationPublic" : true,
      "isExtension" : true,
      "minWidth" : 12345,
      "code" : "...",
      "activationClass" : "..."
    },
    "id" : 12345
  }, {
    "category" : "...",
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
      "context" : "...",
      "applicationVersion" : "...",
      "applicationPublic" : true,
      "isExtension" : true,
      "minWidth" : 12345,
      "code" : "...",
      "activationClass" : "..."
    },
    "id" : 12345
  } ],
  "maxWidth" : 12345,
  "services" : [ {
    "varName" : "...",
    "jndiName" : "...",
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
      "context" : "...",
      "applicationVersion" : "...",
      "applicationPublic" : true,
      "isExtension" : true,
      "minWidth" : 12345,
      "code" : "...",
      "activationClass" : "..."
    },
    "id" : 12345
  }, {
    "varName" : "...",
    "jndiName" : "...",
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
      "context" : "...",
      "applicationVersion" : "...",
      "applicationPublic" : true,
      "isExtension" : true,
      "minWidth" : 12345,
      "code" : "...",
      "activationClass" : "..."
    },
    "id" : 12345
  } ],
  "renderer" : "...",
  "developerCode" : "...",
  "resources" : [ {
    "order" : 12345,
    "type" : "...",
    "id" : 12345,
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
      "context" : "...",
      "applicationVersion" : "...",
      "applicationPublic" : true,
      "isExtension" : true,
      "minWidth" : 12345,
      "code" : "...",
      "activationClass" : "..."
    },
    "resource" : "..."
  }, {
    "order" : 12345,
    "type" : "...",
    "id" : 12345,
    "application" : {
      "earFileName" : "...",
      "title" : "...",
      "maxHeight" : 12345,
      "locales" : [ { }, { } ],
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
      "categories" : [ { }, { } ],
      "maxWidth" : 12345,
      "services" : [ { }, { } ],
      "renderer" : "...",
      "developerCode" : "...",
      "resources" : [ { }, { } ],
      "context" : "...",
      "applicationVersion" : "...",
      "applicationPublic" : true,
      "isExtension" : true,
      "minWidth" : 12345,
      "code" : "...",
      "activationClass" : "..."
    },
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
```
