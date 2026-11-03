---
content_hash: f043d1afb4028188b621fe5f920b2606cccd990104da934e045b427e9e2c1d52
fetched_at: '2026-11-03T14:34:36.184430+00:00'
page_id: json_ApplicationInstanceVO
product: fluig
source: rest-fluig
title: Fluig REST — ApplicationInstanceVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ApplicationInstanceVO.html
version: 1
---

# ApplicationInstanceVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| developerCode | string |  |  |
| systemWidget | boolean |  |  |
| locales | array of string |  |  |
| customTitle | boolean | required |  |
| localeFileBaseName | string |  |  |
| services | map of string |  |  |
| slot | string |  |  |
| renderer | string |  |  |
| icon | string |  |  |
| developerName | string |  |  |
| instanceId | number |  |  |
| permission | [AuthorizationVO](https://api.fluig.com/old/json_AuthorizationVO.html) |  |  |
| order | number |  |  |
| error | [Exception](https://api.fluig.com/old/json_Exception.html) |  |  |
| mobileAppWidget | boolean | required |  |
| data | map of string |  |  |
| description | string |  |  |
| code | string |  |  |
| version | string |  |  |
| page | [PageVO](https://api.fluig.com/old/json_PageVO.html) |  |  |
| originCode | string |  |  |
| resourcesJS | array of string |  |  |
| pageId | number |  |  |
| resourcesCSS | array of string |  |  |
| developerUrl | string |  |  |
| categories | array of string |  |  |
| context | string |  |  |
| viewFile | string |  |  |
| editFile | string |  |  |
| id | number |  |  |
| product | string |  |  |
| showTitlebar | boolean |  |  |
| applicationId | number |  |  |
| enabledMobileApp | boolean | required |  |
| title | string |  |  |
| type | string |  |  |

Example

```
{
  "developerCode" : "...",
  "systemWidget" : true,
  "locales" : [ "...", "..." ],
  "customTitle" : true,
  "localeFileBaseName" : "...",
  "services" : {
    "property1" : "...",
    "property2" : "..."
  },
  "slot" : "...",
  "renderer" : "...",
  "icon" : "...",
  "developerName" : "...",
  "instanceId" : 12345,
  "permission" : {
    "permissions" : [ "...", "..." ],
    "resource" : "..."
  },
  "order" : 12345,
  "error" : {
    "message" : "...",
    "stackTrace" : [ {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    }, {
      "methodName" : "...",
      "fileName" : "...",
      "classLoaderName" : "...",
      "moduleName" : "...",
      "lineNumber" : 12345,
      "nativeMethod" : true,
      "className" : "...",
      "moduleVersion" : "..."
    } ],
    "localizedMessage" : "...",
    "cause" : {
      "message" : "...",
      "stackTrace" : [ { }, { } ],
      "localizedMessage" : "...",
      "cause" : { },
      "suppressed" : [ { }, { } ]
    },
    "suppressed" : [ {
      "message" : "...",
      "stackTrace" : [ { }, { } ],
      "localizedMessage" : "...",
      "cause" : { },
      "suppressed" : [ { }, { } ]
    }, {
      "message" : "...",
      "stackTrace" : [ { }, { } ],
      "localizedMessage" : "...",
      "cause" : { },
      "suppressed" : [ { }, { } ]
    } ]
  },
  "mobileAppWidget" : true,
  "data" : {
    "property1" : "...",
    "property2" : "..."
  },
  "description" : "...",
  "code" : "...",
  "version" : "...",
  "page" : {
    "enabled" : true,
    "enabledMobileApp" : true,
    "searchLevel" : 12345,
    "description" : "...",
    "pageIcon" : "...",
    "disableChildLevel" : true,
    "title" : "...",
    "internal" : true,
    "displayOrder" : 12345,
    "friendlyURL" : "...",
    "children" : [ { }, { } ],
    "page" : "...",
    "iconFont" : "...",
    "hidden" : true,
    "responsiveLayout" : true,
    "lastUpdate" : 12345,
    "pageId" : 12345,
    "URI" : "...",
    "newBuilder" : true,
    "domain" : "...",
    "authType" : 12345,
    "menuGroup" : true
  },
  "originCode" : "...",
  "resourcesJS" : [ "...", "..." ],
  "pageId" : 12345,
  "resourcesCSS" : [ "...", "..." ],
  "developerUrl" : "...",
  "categories" : [ "...", "..." ],
  "context" : "...",
  "viewFile" : "...",
  "editFile" : "...",
  "id" : 12345,
  "product" : "...",
  "showTitlebar" : true,
  "applicationId" : 12345,
  "enabledMobileApp" : true,
  "title" : "...",
  "type" : "..."
}
```
