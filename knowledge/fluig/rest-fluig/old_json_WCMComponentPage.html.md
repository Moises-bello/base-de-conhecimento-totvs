---
content_hash: a2f6c6f822be5655d20178f76c759e0e627460e5fae0977a95600ee2cafc4f81
fetched_at: '2026-11-03T14:34:38.858507+00:00'
page_id: json_WCMComponentPage
product: fluig
source: rest-fluig
title: Fluig REST — WCMComponentPage Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMComponentPage.html
version: 1
---

# WCMComponentPage Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| pageVersion | [WCMPageVersion](https://api.fluig.com/old/json_WCMPageVersion.html) |  |
| component | [WCMComponent](https://api.fluig.com/old/json_WCMComponent.html) |  |
| id | number |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |

Example

```
{
  "pageVersion" : {
    "layout" : {
      "type" : "...",
      "securityCode" : "...",
      "uiLayout" : true,
      "resourceDescription" : "...",
      "resourceType" : "...",
      "pageVersion" : [ { }, { } ],
      "layoutFile" : "...",
      "resourceLongDescription" : "...",
      "slots" : [ { }, { } ],
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
    "lastEditUser" : {
      "data" : [ { }, { } ],
      "firstAccess" : true,
      "locationId" : 12345,
      "userCode" : "...",
      "userState" : "ACTIVE",
      "userId" : 12345,
      "anonymizationDate" : 12345,
      "id" : 12345,
      "user" : { },
      "password" : "...",
      "lastSecurityUpdateDate" : 12345,
      "tenant" : { },
      "email" : "...",
      "idpId" : "...",
      "lastUpdateDate" : 12345,
      "anonymizationUser" : { },
      "tenantId" : 12345,
      "userUUID" : "...",
      "login" : "..."
    },
    "title" : "...",
    "description" : "...",
    "icon" : "...",
    "enabledMobileApp" : true,
    "iconFont" : "...",
    "page" : {
      "defaultLocale" : "...",
      "menuGroup" : true,
      "securityCode" : "...",
      "resource" : { },
      "pageCode" : "...",
      "enabled" : true,
      "level" : 12345,
      "versions" : [ { }, { } ],
      "disableChildLevel" : true,
      "id" : 12345,
      "unpublishedPage" : { },
      "theme" : { },
      "lastPageVersion" : { },
      "importingPage" : true,
      "friendlyURL" : "...",
      "publishedPage" : { },
      "resourceDescription" : "...",
      "parentPage" : { },
      "editable" : true,
      "displayOrder" : 12345,
      "tenant" : { },
      "resourceLongDescription" : "...",
      "hidden" : true,
      "resourceType" : "..."
    },
    "enabledPathParam" : true,
    "versionDescription" : "...",
    "version" : 12345,
    "preferences" : [ {
      "id" : 12345,
      "dataValue" : "...",
      "dataKey" : "...",
      "pageVersion" : { }
    }, {
      "id" : 12345,
      "dataValue" : "...",
      "dataKey" : "...",
      "pageVersion" : { }
    } ],
    "enabledChildren" : true,
    "pageWidgets" : [ {
      "preferences" : [ { }, { } ],
      "permissions" : [ { }, { } ],
      "pageVersion" : { },
      "securityCode" : "...",
      "widgetOrder" : 12345,
      "resourceLongDescription" : "...",
      "enabledMobileApp" : true,
      "slot" : "...",
      "showTitlebar" : true,
      "systemWidget" : true,
      "resourceType" : "...",
      "resourceDescription" : "...",
      "id" : 12345,
      "widget" : { }
    }, {
      "preferences" : [ { }, { } ],
      "permissions" : [ { }, { } ],
      "pageVersion" : { },
      "securityCode" : "...",
      "widgetOrder" : 12345,
      "resourceLongDescription" : "...",
      "enabledMobileApp" : true,
      "slot" : "...",
      "showTitlebar" : true,
      "systemWidget" : true,
      "resourceType" : "...",
      "resourceDescription" : "...",
      "id" : 12345,
      "widget" : { }
    } ],
    "modifiedDate" : 12345,
    "id" : 12345,
    "published" : true,
    "authorization" : "PUBLIC"
  },
  "component" : {
    "type" : "...",
    "securityCode" : "...",
    "pageDescriptor" : "...",
    "pageFile" : "...",
    "resourceType" : "...",
    "resourceDescription" : "...",
    "resourceLongDescription" : "...",
    "dependencies" : [ {
      "resourceType" : "...",
      "file" : "...",
      "code" : "..."
    }, {
      "resourceType" : "...",
      "file" : "...",
      "code" : "..."
    } ],
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
  "id" : 12345,
  "tenant" : {
    "federalId" : "...",
    "idpId" : "...",
    "resourceType" : "...",
    "useWizard" : true,
    "code" : "...",
    "organizationUrl" : "...",
    "tenantActive" : true,
    "products" : [ {
      "id" : 12345,
      "tenant" : { },
      "product" : "..."
    }, {
      "id" : 12345,
      "tenant" : { },
      "product" : "..."
    } ],
    "idpLogOff" : true,
    "id" : 12345,
    "resourceDescription" : "...",
    "data" : [ {
      "hide" : true,
      "dataKey" : "...",
      "dataValue" : "...",
      "tenant" : { },
      "id" : 12345
    }, {
      "hide" : true,
      "dataKey" : "...",
      "dataValue" : "...",
      "tenant" : { },
      "id" : 12345
    } ],
    "securityCode" : "...",
    "thumbnailEnabled" : true,
    "UUID" : "...",
    "description" : "...",
    "removeVolume" : true
  }
}
```
