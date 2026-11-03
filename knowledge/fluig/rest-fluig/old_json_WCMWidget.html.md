---
content_hash: a705e8451c1b2ee3dc72021b4237b16932d3d34ff53311a89723228a878861bb
fetched_at: '2026-11-03T14:34:38.976892+00:00'
page_id: json_WCMWidget
product: fluig
source: rest-fluig
title: Fluig REST — WCMWidget Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMWidget.html
version: 1
---

# WCMWidget Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| resourceDescription | string |  |
| uiWidget | boolean |  |
| viewFile | string |  |
| type | string |  |
| mobileAppWidget | boolean |  |
| resourceType | string |  |
| resourceLongDescription | string |  |
| editFile | string |  |
| securityCode | string |  |
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
  "resourceDescription" : "...",
  "uiWidget" : true,
  "viewFile" : "...",
  "type" : "...",
  "mobileAppWidget" : true,
  "resourceType" : "...",
  "resourceLongDescription" : "...",
  "editFile" : "...",
  "securityCode" : "...",
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
