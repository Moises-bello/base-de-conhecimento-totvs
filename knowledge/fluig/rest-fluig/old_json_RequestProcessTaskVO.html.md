---
content_hash: de9593cf91996d411a10c80ca2056ed8639e9731939c0c328d9293b54e721763
fetched_at: '2026-11-03T14:34:38.233612+00:00'
page_id: json_RequestProcessTaskVO
product: fluig
source: rest-fluig
title: Fluig REST — RequestProcessTaskVO Data Type
type: documentation
url: https://api.fluig.com/old/json_RequestProcessTaskVO.html
version: 1
---

# RequestProcessTaskVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| remainingTime | number |  |  |
| statusTask | number | required |  |
| processInstanceId | number | required |  |
| processId | string |  |  |
| stateName | string |  |  |
| percentageConcluded | number |  |  |
| spentTime | number |  |  |
| deadlineDate | number |  |  |
| warningDate | number |  |  |
| requesterName | string |  |  |
| fullTime | number |  |  |
| endDate | number |  |  |
| startDate | number |  |  |
| periodId | string |  |  |
| processVersion | number | required |  |
| requesterCode | string |  |  |
| processDescription | string |  |  |
| cardFields | map of string |  |  |

Example

```
{
  "remainingTime" : 12345,
  "statusTask" : 12345,
  "processInstanceId" : 12345,
  "processId" : "...",
  "stateName" : "...",
  "percentageConcluded" : 12345,
  "spentTime" : 12345,
  "deadlineDate" : 12345,
  "warningDate" : 12345,
  "requesterName" : "...",
  "fullTime" : 12345,
  "endDate" : 12345,
  "startDate" : 12345,
  "periodId" : "...",
  "processVersion" : 12345,
  "requesterCode" : "...",
  "processDescription" : "...",
  "cardFields" : {
    "property1" : "...",
    "property2" : "..."
  }
}
```
