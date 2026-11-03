---
content_hash: 516beadb7b62f3632e0f6db70ce31508a49fbf3306201dbc7c07cf5f480b2583
fetched_at: '2026-11-03T14:34:38.253549+00:00'
page_id: json_RequestTaskVO
product: fluig
source: rest-fluig
title: Fluig REST — RequestTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_RequestTaskVO.html
version: 1
---

# RequestTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processId | string |  |  |
| processVersion | number | required |  |
| startDate | number |  |  |
| assigneeLocal | [RequestTaskLocalVO](https://api.fluig.com/old/json_RequestTaskLocalVO.html) |  |  |
| deadlineDate | number |  |  |
| activityDescription | string |  |  |
| assigneeCode | string |  |  |
| requesterCode | string |  |  |
| warningDate | number |  |  |
| statusTask | number | required |  |
| processInstanceId | number | required |  |
| activityCode | number |  |  |
| totalRuntime | number | required |  |
| processDescription | string |  |  |
| assigneeName | string |  |  |
| requesterName | string |  |  |
| requesterLocal | [RequestTaskLocalVO](https://api.fluig.com/old/json_RequestTaskLocalVO.html) |  |  |

Example

```
{
  "processId" : "...",
  "processVersion" : 12345,
  "startDate" : 12345,
  "assigneeLocal" : {
    "id" : 12345,
    "name" : "..."
  },
  "deadlineDate" : 12345,
  "activityDescription" : "...",
  "assigneeCode" : "...",
  "requesterCode" : "...",
  "warningDate" : 12345,
  "statusTask" : 12345,
  "processInstanceId" : 12345,
  "activityCode" : 12345,
  "totalRuntime" : 12345,
  "processDescription" : "...",
  "assigneeName" : "...",
  "requesterName" : "...",
  "requesterLocal" : {
    "id" : 12345,
    "name" : "..."
  }
}
```
