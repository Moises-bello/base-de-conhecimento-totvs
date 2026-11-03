---
content_hash: 443acf88f16004ec7408ef4b125880627cc647413851f259480e5db54c9ea391
fetched_at: '2026-11-03T14:34:37.940879+00:00'
page_id: json_PageVO
product: fluig
source: rest-fluig
title: Fluig REST — PageVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PageVO.html
version: 1
---

# PageVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| enabled | boolean | required |  |
| enabledMobileApp | boolean |  |  |
| searchLevel | number |  |  |
| description | string |  |  |
| pageIcon | string |  |  |
| disableChildLevel | boolean | required |  |
| title | string |  |  |
| internal | boolean | required |  |
| displayOrder | number |  |  |
| friendlyURL | string |  |  |
| children | array of [PageVO](https://api.fluig.com/old/json_PageVO.html) |  |  |
| page | string |  |  |
| iconFont | string |  |  |
| hidden | boolean |  |  |
| responsiveLayout | boolean | required |  |
| lastUpdate | number |  |  |
| pageId | number |  |  |
| URI | string |  |  |
| newBuilder | boolean | required |  |
| domain | string |  |  |
| authType | number | required |  |
| menuGroup | boolean | required |  |

Example

```
{
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
  "children" : [ {
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
  }, {
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
  } ],
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
}
```
