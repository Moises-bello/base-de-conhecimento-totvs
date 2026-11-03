---
content_hash: 43aef997b3a33fd3b209865db8a94b3c02fd0d169afc83079a4b969a7b5332ae
fetched_at: '2026-11-03T14:34:38.967505+00:00'
page_id: json_WCMThemeHistory
product: fluig
source: rest-fluig
title: Fluig REST — WCMThemeHistory Data Type
type: documentation
url: https://api.fluig.com/old/json_WCMThemeHistory.html
version: 1
---

# WCMThemeHistory Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| changeDate | number |  |  |
| tenantCode | string |  |  |
| tenant | [FDNTenant](https://api.fluig.com/old/json_FDNTenant.html) |  |  |
| newTheme | string |  |  |
| id | number |  |  |
| alreadyUsedResponsiveTheme | boolean | required |  |
| tenantDescription | string |  |  |
| refusedResponsive | boolean | required |  |
| oldTheme | string |  |  |

Example

```
{
  "changeDate" : 12345,
  "tenantCode" : "...",
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
  },
  "newTheme" : "...",
  "id" : 12345,
  "alreadyUsedResponsiveTheme" : true,
  "tenantDescription" : "...",
  "refusedResponsive" : true,
  "oldTheme" : "..."
}
```
