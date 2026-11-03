---
content_hash: 1adbbc050a0da6a2170d1b4f4b4697458255d19b7b9b62db59ef4dab8533d37c
fetched_at: '2026-11-03T14:34:38.125090+00:00'
page_id: json_PublicApiPageVO
product: fluig
source: rest-fluig
title: Fluig REST — PublicApiPageVO Data Type
type: documentation
url: https://api.fluig.com/old/json_PublicApiPageVO.html
version: 1
---

# PublicApiPageVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| children | array of [PublicApiPageVO](https://api.fluig.com/old/json_PublicApiPageVO.html) |  |  |
| description | string |  |  |
| lastUpdate | number |  |  |
| searchLevel | number | required |  |
| title | string |  |  |
| enabledMobileApp | boolean |  |  |
| parentPageCode | string |  |  |
| iconFont | string |  |  |
| pageId | number |  |  |
| uri | string |  |  |
| pageIcon | string |  |  |
| friendlyURL | string |  |  |
| pageCode | string |  |  |

Example

```
{
  "children" : [ {
    "children" : [ { }, { } ],
    "description" : "...",
    "lastUpdate" : 12345,
    "searchLevel" : 12345,
    "title" : "...",
    "enabledMobileApp" : true,
    "parentPageCode" : "...",
    "iconFont" : "...",
    "pageId" : 12345,
    "uri" : "...",
    "pageIcon" : "...",
    "friendlyURL" : "...",
    "pageCode" : "..."
  }, {
    "children" : [ { }, { } ],
    "description" : "...",
    "lastUpdate" : 12345,
    "searchLevel" : 12345,
    "title" : "...",
    "enabledMobileApp" : true,
    "parentPageCode" : "...",
    "iconFont" : "...",
    "pageId" : 12345,
    "uri" : "...",
    "pageIcon" : "...",
    "friendlyURL" : "...",
    "pageCode" : "..."
  } ],
  "description" : "...",
  "lastUpdate" : 12345,
  "searchLevel" : 12345,
  "title" : "...",
  "enabledMobileApp" : true,
  "parentPageCode" : "...",
  "iconFont" : "...",
  "pageId" : 12345,
  "uri" : "...",
  "pageIcon" : "...",
  "friendlyURL" : "...",
  "pageCode" : "..."
}
```
