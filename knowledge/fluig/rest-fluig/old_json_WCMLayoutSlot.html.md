---
content_hash: 62966aa1f86e31ac721fb29b4af46f685f990a9129915aa9aaff895890e042ff
fetched_at: '2026-11-03T14:34:38.882787+00:00'
page_id: json_WCMLayoutSlot
product: fluig
source: rest-fluig
title: Fluig REST — WCMLayoutSlot Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMLayoutSlot.html
version: 1
---

# WCMLayoutSlot Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| layout | [WCMLayout](https://api.fluig.com/old/json_WCMLayout.html) |  |
| slot | string |  |
| editableSlot | boolean |  |
| decorator | boolean |  |
| id | number |  |

Example

```
{
  "layout" : {
    "type" : "...",
    "securityCode" : "...",
    "uiLayout" : true,
    "resourceDescription" : "...",
    "resourceType" : "...",
    "pageVersion" : [ {
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
    }, {
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
    } ],
    "layoutFile" : "...",
    "resourceLongDescription" : "...",
    "slots" : [ {
      "layout" : { },
      "slot" : "...",
      "editableSlot" : true,
      "decorator" : true,
      "id" : 12345
    }, {
      "layout" : { },
      "slot" : "...",
      "editableSlot" : true,
      "decorator" : true,
      "id" : 12345
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
  "slot" : "...",
  "editableSlot" : true,
  "decorator" : true,
  "id" : 12345
}
```
