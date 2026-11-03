---
content_hash: bd5d3a5173d5fc57027bcc46ab9a5e3a4e01863881d78743257c2e4b4c60d050
fetched_at: '2026-11-03T14:34:38.925450+00:00'
page_id: json_WCMPageWidget
product: fluig
source: rest-fluig
title: Fluig REST — WCMPageWidget Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMPageWidget.html
version: 1
---

# WCMPageWidget Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| preferences | array of [WCMApplicationData](https://api.fluig.com/old/json_WCMApplicationData.html) |  |
| permissions | array of [FDNPermission](https://api.fluig.com/old/json_FDNPermission.html) |  |
| pageVersion | [WCMPageVersion](https://api.fluig.com/old/json_WCMPageVersion.html) |  |
| securityCode | string |  |
| widgetOrder | number |  |
| resourceLongDescription | string |  |
| enabledMobileApp | boolean |  |
| slot | string |  |
| showTitlebar | boolean |  |
| systemWidget | boolean |  |
| resourceType | string |  |
| resourceDescription | string |  |
| id | number |  |
| widget | [WCMWidget](https://api.fluig.com/old/json_WCMWidget.html) |  |

Example

```
{
  "preferences" : [ {
    "instance" : {
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
    },
    "dataValue" : "...",
    "id" : 12345,
    "dataKey" : "..."
  }, {
    "instance" : {
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
    },
    "dataValue" : "...",
    "id" : 12345,
    "dataKey" : "..."
  } ],
  "permissions" : [ {
    "id" : 12345,
    "permission" : "...",
    "tenantId" : 12345,
    "groupCode" : "...",
    "login" : "...",
    "roleCode" : "...",
    "resource" : {
      "description" : "...",
      "categoryResources" : [ { }, { } ],
      "longDescription" : "...",
      "tenantId" : 12345,
      "method" : "...",
      "code" : "...",
      "type" : { },
      "isInternal" : true,
      "id" : 12345,
      "parent" : { },
      "typeCode" : "..."
    },
    "description" : "..."
  }, {
    "id" : 12345,
    "permission" : "...",
    "tenantId" : 12345,
    "groupCode" : "...",
    "login" : "...",
    "roleCode" : "...",
    "resource" : {
      "description" : "...",
      "categoryResources" : [ { }, { } ],
      "longDescription" : "...",
      "tenantId" : 12345,
      "method" : "...",
      "code" : "...",
      "type" : { },
      "isInternal" : true,
      "id" : 12345,
      "parent" : { },
      "typeCode" : "..."
    },
    "description" : "..."
  } ],
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
      "userState" : "BLOCKED",
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
    "authorization" : "AUTHENTICATED"
  },
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
  "widget" : {
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
