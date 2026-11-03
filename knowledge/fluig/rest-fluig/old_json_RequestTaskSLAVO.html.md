---
content_hash: 06191275148fa4a3773836e1d73c9e299e786164c0e4a0cc6d578dc2a5727a3b
fetched_at: '2026-11-03T14:34:38.247089+00:00'
page_id: json_RequestTaskSLAVO
product: fluig
source: rest-fluig
title: Fluig REST — RequestTaskSLAVO Data Type
type: documentation
url: https://api.fluig.com/old/json_RequestTaskSLAVO.html
version: 1
---

# RequestTaskSLAVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| assigneeName | string |  |  |
| activityCode | number | required |  |
| assigneeLocal | [LocalVO](https://api.fluig.com/old/json_LocalVO.html) |  |  |
| activityDescription | string |  |  |
| assigneeCode | string |  |  |

Example

```
{
  "assigneeName" : "...",
  "activityCode" : 12345,
  "assigneeLocal" : {
    "timezone" : "...",
    "localUsers" : [ {
      "userName" : "...",
      "localId" : 12345,
      "id" : 12345,
      "userCode" : "..."
    }, {
      "userName" : "...",
      "localId" : 12345,
      "id" : 12345,
      "userCode" : "..."
    } ],
    "defaultLocale" : true,
    "radius" : 12345.0,
    "name" : "...",
    "holidays" : [ {
      "locals" : [ { }, { } ],
      "description" : "...",
      "date" : "...",
      "companyId" : 12345,
      "id" : 12345,
      "_expandables" : [ "...", "..." ],
      "recurrent" : true
    }, {
      "locals" : [ { }, { } ],
      "description" : "...",
      "date" : "...",
      "companyId" : 12345,
      "id" : 12345,
      "_expandables" : [ "...", "..." ],
      "recurrent" : true
    } ],
    "longitude" : 12345.0,
    "id" : 12345,
    "_expandables" : [ "...", "..." ],
    "latitude" : 12345.0
  },
  "activityDescription" : "...",
  "assigneeCode" : "..."
}
```
