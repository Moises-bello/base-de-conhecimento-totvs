---
content_hash: a49be13349aa616ed2bd423ac4ab56eb67be19a1d92cf18ab4c2e57c2e467ffc
fetched_at: '2026-11-03T14:34:38.911405+00:00'
page_id: json_WCMPageVO
product: fluig
source: rest-fluig
title: Fluig REST — WCMPageVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMPageVO.html
version: 1
---

# WCMPageVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| parent | number |  |  |
| layout | number |  |  |
| preferences | map of string |  |  |
| title | string |  |  |
| parentCode | string |  |  |
| clazz | string |  |  |
| iconUploaded | boolean | required |  |
| resourceDescription | string |  |  |
| uri | string |  |  |
| securityCode | string |  |  |
| pageIcon | string |  |  |
| editable | boolean |  |  |
| layoutDescription | string |  |  |
| opened | boolean |  |  |
| depthLevel | number |  |  |
| description | string |  |  |
| parentVO | [WCMPageVO](https://api.fluig.com/old/json_WCMPageVO.html) |  |  |
| iconFont | string |  |  |
| enabled | boolean | required |  |
| themeCode | string |  |  |
| friendlyURL | string |  |  |
| menuGroup | boolean | required |  |
| resourceType | string |  |  |
| enabledPathParam | boolean | required |  |
| pageKey | [WCMPageKeyVO](https://api.fluig.com/old/json_WCMPageKeyVO.html) |  |  |
| permissions | array of [PermissionVO](https://api.fluig.com/old/json_PermissionVO_vo.html) |  |  |
| enabledMobileApp | boolean | required |  |
| authorization | number |  |  |
| disableChildLevel | boolean | required |  |
| layoutCode | string |  |  |
| enabledChildren | boolean | required |  |
| themeId | number |  |  |
| childrens | array of [WCMPageVO](https://api.fluig.com/old/json_WCMPageVO.html) |  |  |
| displayOrder | number |  |  |
| hidden | boolean |  |  |
| layoutTitle | string |  |  |

Example

```
{
  "parent" : 12345,
  "layout" : 12345,
  "preferences" : {
    "property1" : "...",
    "property2" : "..."
  },
  "title" : "...",
  "parentCode" : "...",
  "clazz" : "...",
  "iconUploaded" : true,
  "resourceDescription" : "...",
  "uri" : "...",
  "securityCode" : "...",
  "pageIcon" : "...",
  "editable" : true,
  "layoutDescription" : "...",
  "opened" : true,
  "depthLevel" : 12345,
  "description" : "...",
  "parentVO" : {
    "parent" : 12345,
    "layout" : 12345,
    "preferences" : {
      "property1" : "...",
      "property2" : "..."
    },
    "title" : "...",
    "parentCode" : "...",
    "clazz" : "...",
    "iconUploaded" : true,
    "resourceDescription" : "...",
    "uri" : "...",
    "securityCode" : "...",
    "pageIcon" : "...",
    "editable" : true,
    "layoutDescription" : "...",
    "opened" : true,
    "depthLevel" : 12345,
    "description" : "...",
    "parentVO" : { },
    "iconFont" : "...",
    "enabled" : true,
    "themeCode" : "...",
    "friendlyURL" : "...",
    "menuGroup" : true,
    "resourceType" : "...",
    "enabledPathParam" : true,
    "pageKey" : {
      "code" : "...",
      "id" : 12345
    },
    "permissions" : [ {
      "permission" : "...",
      "tenantId" : 12345,
      "role" : "...",
      "user" : "...",
      "group" : "...",
      "resource" : "...",
      "description" : "..."
    }, {
      "permission" : "...",
      "tenantId" : 12345,
      "role" : "...",
      "user" : "...",
      "group" : "...",
      "resource" : "...",
      "description" : "..."
    } ],
    "enabledMobileApp" : true,
    "authorization" : 12345,
    "disableChildLevel" : true,
    "layoutCode" : "...",
    "enabledChildren" : true,
    "themeId" : 12345,
    "childrens" : [ { }, { } ],
    "displayOrder" : 12345,
    "hidden" : true,
    "layoutTitle" : "..."
  },
  "iconFont" : "...",
  "enabled" : true,
  "themeCode" : "...",
  "friendlyURL" : "...",
  "menuGroup" : true,
  "resourceType" : "...",
  "enabledPathParam" : true,
  "pageKey" : {
    "code" : "...",
    "id" : 12345
  },
  "permissions" : [ {
    "permission" : "...",
    "tenantId" : 12345,
    "role" : "...",
    "user" : "...",
    "group" : "...",
    "resource" : "...",
    "description" : "..."
  }, {
    "permission" : "...",
    "tenantId" : 12345,
    "role" : "...",
    "user" : "...",
    "group" : "...",
    "resource" : "...",
    "description" : "..."
  } ],
  "enabledMobileApp" : true,
  "authorization" : 12345,
  "disableChildLevel" : true,
  "layoutCode" : "...",
  "enabledChildren" : true,
  "themeId" : 12345,
  "childrens" : [ {
    "parent" : 12345,
    "layout" : 12345,
    "preferences" : {
      "property1" : "...",
      "property2" : "..."
    },
    "title" : "...",
    "parentCode" : "...",
    "clazz" : "...",
    "iconUploaded" : true,
    "resourceDescription" : "...",
    "uri" : "...",
    "securityCode" : "...",
    "pageIcon" : "...",
    "editable" : true,
    "layoutDescription" : "...",
    "opened" : true,
    "depthLevel" : 12345,
    "description" : "...",
    "parentVO" : { },
    "iconFont" : "...",
    "enabled" : true,
    "themeCode" : "...",
    "friendlyURL" : "...",
    "menuGroup" : true,
    "resourceType" : "...",
    "enabledPathParam" : true,
    "pageKey" : {
      "code" : "...",
      "id" : 12345
    },
    "permissions" : [ {
      "permission" : "...",
      "tenantId" : 12345,
      "role" : "...",
      "user" : "...",
      "group" : "...",
      "resource" : "...",
      "description" : "..."
    }, {
      "permission" : "...",
      "tenantId" : 12345,
      "role" : "...",
      "user" : "...",
      "group" : "...",
      "resource" : "...",
      "description" : "..."
    } ],
    "enabledMobileApp" : true,
    "authorization" : 12345,
    "disableChildLevel" : true,
    "layoutCode" : "...",
    "enabledChildren" : true,
    "themeId" : 12345,
    "childrens" : [ { }, { } ],
    "displayOrder" : 12345,
    "hidden" : true,
    "layoutTitle" : "..."
  }, {
    "parent" : 12345,
    "layout" : 12345,
    "preferences" : {
      "property1" : "...",
      "property2" : "..."
    },
    "title" : "...",
    "parentCode" : "...",
    "clazz" : "...",
    "iconUploaded" : true,
    "resourceDescription" : "...",
    "uri" : "...",
    "securityCode" : "...",
    "pageIcon" : "...",
    "editable" : true,
    "layoutDescription" : "...",
    "opened" : true,
    "depthLevel" : 12345,
    "description" : "...",
    "parentVO" : { },
    "iconFont" : "...",
    "enabled" : true,
    "themeCode" : "...",
    "friendlyURL" : "...",
    "menuGroup" : true,
    "resourceType" : "...",
    "enabledPathParam" : true,
    "pageKey" : {
      "code" : "...",
      "id" : 12345
    },
    "permissions" : [ {
      "permission" : "...",
      "tenantId" : 12345,
      "role" : "...",
      "user" : "...",
      "group" : "...",
      "resource" : "...",
      "description" : "..."
    }, {
      "permission" : "...",
      "tenantId" : 12345,
      "role" : "...",
      "user" : "...",
      "group" : "...",
      "resource" : "...",
      "description" : "..."
    } ],
    "enabledMobileApp" : true,
    "authorization" : 12345,
    "disableChildLevel" : true,
    "layoutCode" : "...",
    "enabledChildren" : true,
    "themeId" : 12345,
    "childrens" : [ { }, { } ],
    "displayOrder" : 12345,
    "hidden" : true,
    "layoutTitle" : "..."
  } ],
  "displayOrder" : 12345,
  "hidden" : true,
  "layoutTitle" : "..."
}
```
