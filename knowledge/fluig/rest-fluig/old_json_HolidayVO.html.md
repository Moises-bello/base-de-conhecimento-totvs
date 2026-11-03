---
content_hash: 16fe304083c5248071eb8bdbebdb4cafc20e579bb0a2869573f896d2ec590451
fetched_at: '2026-11-03T14:34:37.126072+00:00'
page_id: json_HolidayVO
product: fluig
source: rest-fluig
title: Fluig REST — HolidayVO Data Type
type: documentation
url: https://api.fluig.com/old/json_HolidayVO.html
version: 1
---

# HolidayVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| locals | array of [LocalVO](https://api.fluig.com/old/json_LocalVO.html) |  |  |
| description | string |  |  |
| date | string |  |  |
| companyId | number | required |  |
| id | number |  |  |
| \_expandables | array of string |  |  |
| recurrent | boolean | required |  |

Example

```
{
  "locals" : [ {
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
  }, {
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
  } ],
  "description" : "...",
  "date" : "...",
  "companyId" : 12345,
  "id" : 12345,
  "_expandables" : [ "...", "..." ],
  "recurrent" : true
}
```
