---
content_hash: a2e72427964732fd61b30e3fc5fc43eda1978d344c01ed51e9c12c0ab633a0cb
fetched_at: '2026-11-03T14:34:38.887998+00:00'
page_id: json_WCMMenuItem
product: fluig
source: rest-fluig
title: Fluig REST — WCMMenuItem Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMMenuItem.html
version: 1
---

# WCMMenuItem Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| type | number |  |
| openTarget | string |  |
| hidden | boolean |  |
| icon | string |  |
| securityCode | string |  |
| resourceType | string |  |
| resourceDescription | string |  |
| level | number |  |
| parentMenuItem | [WCMMenuItem](https://api.fluig.com/old/json_WCMMenuItem.html) |  |
| openURL | string |  |
| authorization | [MenuAuth](https://api.fluig.com/old/json_MenuAuth.html) |  |
| description | string |  |
| title | string |  |
| displayOrder | number |  |
| id | number |  |
| resource | [FDNResource](https://api.fluig.com/old/json_FDNResource.html) |  |

Example

```
{
  "type" : 12345,
  "openTarget" : "...",
  "hidden" : true,
  "icon" : "...",
  "securityCode" : "...",
  "resourceType" : "...",
  "resourceDescription" : "...",
  "level" : 12345,
  "parentMenuItem" : {
    "type" : 12345,
    "openTarget" : "...",
    "hidden" : true,
    "icon" : "...",
    "securityCode" : "...",
    "resourceType" : "...",
    "resourceDescription" : "...",
    "level" : 12345,
    "parentMenuItem" : { },
    "openURL" : "...",
    "authorization" : "AUTHENTICATED",
    "description" : "...",
    "title" : "...",
    "displayOrder" : 12345,
    "id" : 12345,
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
    }
  },
  "openURL" : "...",
  "authorization" : "AUTHENTICATED",
  "description" : "...",
  "title" : "...",
  "displayOrder" : 12345,
  "id" : 12345,
  "resource" : {
    "description" : "...",
    "categoryResources" : [ {
      "tenantId" : 12345,
      "id" : 12345,
      "category" : { },
      "resource" : { }
    }, {
      "tenantId" : 12345,
      "id" : 12345,
      "category" : { },
      "resource" : { }
    } ],
    "longDescription" : "...",
    "tenantId" : 12345,
    "method" : "...",
    "code" : "...",
    "type" : {
      "isInternal" : true,
      "code" : "...",
      "id" : 12345,
      "description" : "..."
    },
    "isInternal" : true,
    "id" : 12345,
    "parent" : { },
    "typeCode" : "..."
  }
}
```
