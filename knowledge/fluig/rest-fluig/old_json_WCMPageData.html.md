---
content_hash: 16955230511752f0c4a644bab264585badf3d6d7c6e29012d503967b87b3e857
fetched_at: '2026-11-03T14:34:38.898891+00:00'
page_id: json_WCMPageData
product: fluig
source: rest-fluig
title: Fluig REST — WCMPageData Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMPageData.html
version: 1
---

# WCMPageData Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| id | number |  |
| dataValue | string |  |
| dataKey | string |  |
| pageVersion | [WCMPageVersion](https://api.fluig.com/old/json_WCMPageVersion.html) |  |

Example

```
{
  "id" : 12345,
  "dataValue" : "...",
  "dataKey" : "...",
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
      "userState" : "UNCONFIRMED",
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
  }
}
```
