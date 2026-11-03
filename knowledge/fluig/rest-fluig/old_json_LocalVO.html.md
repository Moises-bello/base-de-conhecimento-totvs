---
content_hash: 662cba9a60d376d71beffca1f642e072b5b91291628b1fdd29860008590818db
fetched_at: '2026-11-03T14:34:37.779762+00:00'
page_id: json_LocalVO
product: fluig
source: rest-fluig
title: Fluig REST — LocalVO Data Type
type: documentation
url: https://api.fluig.com/old/json_LocalVO.html
version: 1
---

# LocalVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| timezone | string |  |  |
| localUsers | array of [LocalUserVO](https://api.fluig.com/old/json_LocalUserVO.html) |  |  |
| defaultLocale | boolean | required |  |
| radius | number | required |  |
| name | string |  |  |
| holidays | array of [HolidayVO](https://api.fluig.com/old/json_HolidayVO.html) |  |  |
| longitude | number | required |  |
| id | number |  |  |
| \_expandables | array of string |  |  |
| latitude | number | required |  |

Example

```
{
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
    "locals" : [ {
      "timezone" : "...",
      "localUsers" : [ { }, { } ],
      "defaultLocale" : true,
      "radius" : 12345.0,
      "name" : "...",
      "holidays" : [ { }, { } ],
      "longitude" : 12345.0,
      "id" : 12345,
      "_expandables" : [ "...", "..." ],
      "latitude" : 12345.0
    }, {
      "timezone" : "...",
      "localUsers" : [ { }, { } ],
      "defaultLocale" : true,
      "radius" : 12345.0,
      "name" : "...",
      "holidays" : [ { }, { } ],
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
  }, {
    "locals" : [ {
      "timezone" : "...",
      "localUsers" : [ { }, { } ],
      "defaultLocale" : true,
      "radius" : 12345.0,
      "name" : "...",
      "holidays" : [ { }, { } ],
      "longitude" : 12345.0,
      "id" : 12345,
      "_expandables" : [ "...", "..." ],
      "latitude" : 12345.0
    }, {
      "timezone" : "...",
      "localUsers" : [ { }, { } ],
      "defaultLocale" : true,
      "radius" : 12345.0,
      "name" : "...",
      "holidays" : [ { }, { } ],
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
  } ],
  "longitude" : 12345.0,
  "id" : 12345,
  "_expandables" : [ "...", "..." ],
  "latitude" : 12345.0
}
```
