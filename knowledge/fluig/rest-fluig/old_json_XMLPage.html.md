---
content_hash: ca6711fe62d7fd8e1802ce3607ff9b5e3a700eb1d6642ff26c6260498a5dc28b
fetched_at: '2026-11-03T14:34:39.238523+00:00'
page_id: json_XMLPage
product: fluig
source: rest-fluig
title: Fluig REST — XMLPage Data Type
type: documentation
url: https://api.fluig.com/old/json_XMLPage.html
version: 1
---

# XMLPage Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| slots | array of [XMLPageSlot](https://api.fluig.com/old/json_XMLPageSlot.html) |  |
| enabledPathParam | boolean |  |
| dependsOn | string |  |
| title | string |  |
| editable | boolean |  |
| dependsOnApp | string |  |
| importingPage | boolean |  |
| tenantCode | string |  |
| defaultLocale | string |  |
| pages | array of [XMLPages](https://api.fluig.com/old/json_XMLPages.html) |  |
| category | string |  |
| disableChildLevel | boolean |  |
| description | string |  |
| permissionMappings | array of [XMLPermissionMapping](https://api.fluig.com/old/json_XMLPermissionMapping.html) |  |
| parentCode | string |  |
| enabledChildren | boolean |  |
| layout | string |  |
| iconFont | string |  |
| hidden | boolean |  |
| enabled | boolean |  |
| code | string |  |
| theme | string |  |
| data | array of [XMLPageData](https://api.fluig.com/old/json_XMLPageData.html) |  |
| displayOrder | number |  |
| enabledMobileApp | boolean |  |
| menuGroup | boolean |  |
| internalPage | boolean |  |
| permissions | array of [XMLPermission](https://api.fluig.com/old/json_XMLPermission.html) |  |
| authorization | number |  |
| template | boolean |  |
| icon | string |  |

Example

```
{
  "slots" : [ {
    "name" : "...",
    "widget" : "...",
    "showWidgetTitle" : true,
    "preferences" : [ {
      "value" : "...",
      "key" : "..."
    }, {
      "value" : "...",
      "key" : "..."
    } ],
    "systemWidget" : true,
    "enabledMobileApp" : true,
    "permissions" : [ {
      "code" : "...",
      "user" : "...",
      "tenantCode" : "...",
      "role" : "...",
      "description" : "...",
      "group" : "..."
    }, {
      "code" : "...",
      "user" : "...",
      "tenantCode" : "...",
      "role" : "...",
      "description" : "...",
      "group" : "..."
    } ]
  }, {
    "name" : "...",
    "widget" : "...",
    "showWidgetTitle" : true,
    "preferences" : [ {
      "value" : "...",
      "key" : "..."
    }, {
      "value" : "...",
      "key" : "..."
    } ],
    "systemWidget" : true,
    "enabledMobileApp" : true,
    "permissions" : [ {
      "code" : "...",
      "user" : "...",
      "tenantCode" : "...",
      "role" : "...",
      "description" : "...",
      "group" : "..."
    }, {
      "code" : "...",
      "user" : "...",
      "tenantCode" : "...",
      "role" : "...",
      "description" : "...",
      "group" : "..."
    } ]
  } ],
  "enabledPathParam" : true,
  "dependsOn" : "...",
  "title" : "...",
  "editable" : true,
  "dependsOnApp" : "...",
  "importingPage" : true,
  "tenantCode" : "...",
  "defaultLocale" : "...",
  "pages" : [ {
    "pages" : [ {
      "slots" : [ { }, { } ],
      "enabledPathParam" : true,
      "dependsOn" : "...",
      "title" : "...",
      "editable" : true,
      "dependsOnApp" : "...",
      "importingPage" : true,
      "tenantCode" : "...",
      "defaultLocale" : "...",
      "pages" : [ { }, { } ],
      "category" : "...",
      "disableChildLevel" : true,
      "description" : "...",
      "permissionMappings" : [ { }, { } ],
      "parentCode" : "...",
      "enabledChildren" : true,
      "layout" : "...",
      "iconFont" : "...",
      "hidden" : true,
      "enabled" : true,
      "code" : "...",
      "theme" : "...",
      "data" : [ { }, { } ],
      "displayOrder" : 12345,
      "enabledMobileApp" : true,
      "menuGroup" : true,
      "internalPage" : true,
      "permissions" : [ { }, { } ],
      "authorization" : 12345,
      "template" : true,
      "icon" : "..."
    }, {
      "slots" : [ { }, { } ],
      "enabledPathParam" : true,
      "dependsOn" : "...",
      "title" : "...",
      "editable" : true,
      "dependsOnApp" : "...",
      "importingPage" : true,
      "tenantCode" : "...",
      "defaultLocale" : "...",
      "pages" : [ { }, { } ],
      "category" : "...",
      "disableChildLevel" : true,
      "description" : "...",
      "permissionMappings" : [ { }, { } ],
      "parentCode" : "...",
      "enabledChildren" : true,
      "layout" : "...",
      "iconFont" : "...",
      "hidden" : true,
      "enabled" : true,
      "code" : "...",
      "theme" : "...",
      "data" : [ { }, { } ],
      "displayOrder" : 12345,
      "enabledMobileApp" : true,
      "menuGroup" : true,
      "internalPage" : true,
      "permissions" : [ { }, { } ],
      "authorization" : 12345,
      "template" : true,
      "icon" : "..."
    } ],
    "version" : "..."
  }, {
    "pages" : [ {
      "slots" : [ { }, { } ],
      "enabledPathParam" : true,
      "dependsOn" : "...",
      "title" : "...",
      "editable" : true,
      "dependsOnApp" : "...",
      "importingPage" : true,
      "tenantCode" : "...",
      "defaultLocale" : "...",
      "pages" : [ { }, { } ],
      "category" : "...",
      "disableChildLevel" : true,
      "description" : "...",
      "permissionMappings" : [ { }, { } ],
      "parentCode" : "...",
      "enabledChildren" : true,
      "layout" : "...",
      "iconFont" : "...",
      "hidden" : true,
      "enabled" : true,
      "code" : "...",
      "theme" : "...",
      "data" : [ { }, { } ],
      "displayOrder" : 12345,
      "enabledMobileApp" : true,
      "menuGroup" : true,
      "internalPage" : true,
      "permissions" : [ { }, { } ],
      "authorization" : 12345,
      "template" : true,
      "icon" : "..."
    }, {
      "slots" : [ { }, { } ],
      "enabledPathParam" : true,
      "dependsOn" : "...",
      "title" : "...",
      "editable" : true,
      "dependsOnApp" : "...",
      "importingPage" : true,
      "tenantCode" : "...",
      "defaultLocale" : "...",
      "pages" : [ { }, { } ],
      "category" : "...",
      "disableChildLevel" : true,
      "description" : "...",
      "permissionMappings" : [ { }, { } ],
      "parentCode" : "...",
      "enabledChildren" : true,
      "layout" : "...",
      "iconFont" : "...",
      "hidden" : true,
      "enabled" : true,
      "code" : "...",
      "theme" : "...",
      "data" : [ { }, { } ],
      "displayOrder" : 12345,
      "enabledMobileApp" : true,
      "menuGroup" : true,
      "internalPage" : true,
      "permissions" : [ { }, { } ],
      "authorization" : 12345,
      "template" : true,
      "icon" : "..."
    } ],
    "version" : "..."
  } ],
  "category" : "...",
  "disableChildLevel" : true,
  "description" : "...",
  "permissionMappings" : [ {
    "toPermission" : "...",
    "resource" : "...",
    "permission" : "...",
    "description" : "..."
  }, {
    "toPermission" : "...",
    "resource" : "...",
    "permission" : "...",
    "description" : "..."
  } ],
  "parentCode" : "...",
  "enabledChildren" : true,
  "layout" : "...",
  "iconFont" : "...",
  "hidden" : true,
  "enabled" : true,
  "code" : "...",
  "theme" : "...",
  "data" : [ {
    "value" : "...",
    "key" : "..."
  }, {
    "value" : "...",
    "key" : "..."
  } ],
  "displayOrder" : 12345,
  "enabledMobileApp" : true,
  "menuGroup" : true,
  "internalPage" : true,
  "permissions" : [ {
    "code" : "...",
    "user" : "...",
    "tenantCode" : "...",
    "role" : "...",
    "description" : "...",
    "group" : "..."
  }, {
    "code" : "...",
    "user" : "...",
    "tenantCode" : "...",
    "role" : "...",
    "description" : "...",
    "group" : "..."
  } ],
  "authorization" : 12345,
  "template" : true,
  "icon" : "..."
}
```
