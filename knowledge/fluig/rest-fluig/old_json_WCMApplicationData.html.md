---
content_hash: 27d850c513ee61103da19d247d0cd57f5f9b355d1317bc1525cc6bf56dc88df5
fetched_at: '2026-11-03T14:34:38.821759+00:00'
page_id: json_WCMApplicationData
product: fluig
source: rest-fluig
title: Fluig REST — WCMApplicationData Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMApplicationData.html
version: 1
---

# WCMApplicationData Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| instance | [WCMPageWidget](https://api.fluig.com/old/json_WCMPageWidget.html) |  |
| dataValue | string |  |
| id | number |  |
| dataKey | string |  |

Example

```
{
  "instance" : {
    "preferences" : [ {
      "instance" : { },
      "dataValue" : "...",
      "id" : 12345,
      "dataKey" : "..."
    }, {
      "instance" : { },
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
      "resource" : { },
      "description" : "..."
    }, {
      "id" : 12345,
      "permission" : "...",
      "tenantId" : 12345,
      "groupCode" : "...",
      "login" : "...",
      "roleCode" : "...",
      "resource" : { },
      "description" : "..."
    } ],
    "pageVersion" : {
      "layout" : { },
      "lastEditUser" : { },
      "title" : "...",
      "description" : "...",
      "icon" : "...",
      "enabledMobileApp" : true,
      "iconFont" : "...",
      "page" : { },
      "enabledPathParam" : true,
      "versionDescription" : "...",
      "version" : 12345,
      "preferences" : [ { }, { } ],
      "enabledChildren" : true,
      "pageWidgets" : [ { }, { } ],
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
    }
  },
  "dataValue" : "...",
  "id" : 12345,
  "dataKey" : "..."
}
```
