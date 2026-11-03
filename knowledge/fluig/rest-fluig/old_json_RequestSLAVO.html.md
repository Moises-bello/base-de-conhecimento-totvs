---
content_hash: 196c5fa4a6fc29ce3e0c621953f5b24d7043f3c89f317f4b42ebedc2d29406df
fetched_at: '2026-11-03T14:34:38.240338+00:00'
page_id: json_RequestSLAVO
product: fluig
source: rest-fluig
title: Fluig REST — RequestSLAVO Data Type
type: documentation
url: https://api.fluig.com/old/json_RequestSLAVO.html
version: 1
---

# RequestSLAVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| cardFields | map of string |  |  |
| processId | string |  |  |
| endDate | number |  |  |
| requesterName | string |  |  |
| fullTime | number |  |  |
| percentageConcluded | number |  |  |
| warningDate | number |  |  |
| statusRequest | string |  |  |
| actualTasks | array of [RequestTaskSLAVO](https://api.fluig.com/old/json_RequestTaskSLAVO.html) |  |  |
| \_expandables | array of string |  |  |
| spentTime | number |  |  |
| requesterLocal | [LocalVO](https://api.fluig.com/old/json_LocalVO.html) |  |  |
| remainingTime | number |  |  |
| requesterCode | string |  |  |
| deadlineDate | number |  |  |
| processDescription | string |  |  |
| statusSla | string |  |  |
| processInstanceId | number | required |  |
| processVersion | number | required |  |
| startDate | number |  |  |

Example

```
{
  "cardFields" : {
    "property1" : "...",
    "property2" : "..."
  },
  "processId" : "...",
  "endDate" : 12345,
  "requesterName" : "...",
  "fullTime" : 12345,
  "percentageConcluded" : 12345,
  "warningDate" : 12345,
  "statusRequest" : "...",
  "actualTasks" : [ {
    "assigneeName" : "...",
    "activityCode" : 12345,
    "assigneeLocal" : {
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
    },
    "activityDescription" : "...",
    "assigneeCode" : "..."
  }, {
    "assigneeName" : "...",
    "activityCode" : 12345,
    "assigneeLocal" : {
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
    },
    "activityDescription" : "...",
    "assigneeCode" : "..."
  } ],
  "_expandables" : [ "...", "..." ],
  "spentTime" : 12345,
  "requesterLocal" : {
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
  "remainingTime" : 12345,
  "requesterCode" : "...",
  "deadlineDate" : 12345,
  "processDescription" : "...",
  "statusSla" : "...",
  "processInstanceId" : 12345,
  "processVersion" : 12345,
  "startDate" : 12345
}
```
