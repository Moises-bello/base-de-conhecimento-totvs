---
content_hash: 4c7e52b24bd345994cf2353a248fa4d0615efe72fc1e2946e9c50a338bdf7dd2
fetched_at: '2026-11-03T14:34:37.166327+00:00'
page_id: json_IdentityQuickViewModelVO
product: fluig
source: rest-fluig
title: Fluig REST — IdentityQuickViewModelVO Data Type
type: documentation
url: https://api.fluig.com/old/json_IdentityQuickViewModelVO.html
version: 1
---

# IdentityQuickViewModelVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| colModel | array of [Header](https://api.fluig.com/old/json_Header.html) |  |
| relatedActions | array of [RelatedAction](https://api.fluig.com/old/json_RelatedAction.html) |  |
| dataURL | string |  |
| selectionValues | array of [Filter](https://api.fluig.com/old/json_Filter.html) |  |
| filters | array of [Filter](https://api.fluig.com/old/json_Filter.html) |  |
| autoComplete | boolean |  |
| Properties inherited from [VO](https://api.fluig.com/old/json_VO.html) | | |
| displayName | string |  |
| success | boolean |  |
| externalId | string |  |
| id | string |  |
| selected | boolean |  |
| customfilter | string |  |

Example

```
{
  "colModel" : [ {
    "index" : "...",
    "name" : "...",
    "sortable" : true,
    "align" : "...",
    "hidden" : true,
    "width" : "...",
    "label" : "..."
  }, {
    "index" : "...",
    "name" : "...",
    "sortable" : true,
    "align" : "...",
    "hidden" : true,
    "width" : "...",
    "label" : "..."
  } ],
  "relatedActions" : [ {
    "label" : "...",
    "relayState" : "..."
  }, {
    "label" : "...",
    "relayState" : "..."
  } ],
  "dataURL" : "...",
  "selectionValues" : [ {
    "code" : "...",
    "label" : "..."
  }, {
    "code" : "...",
    "label" : "..."
  } ],
  "filters" : [ {
    "code" : "...",
    "label" : "..."
  }, {
    "code" : "...",
    "label" : "..."
  } ],
  "autoComplete" : true,
  "displayName" : "...",
  "success" : true,
  "externalId" : "...",
  "id" : "...",
  "selected" : true,
  "customfilter" : "..."
}
```
