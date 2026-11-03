---
content_hash: 53c5a9cb4734afd621f36511b0c6e2168db956f493524198a6db6a00f1a113d4
fetched_at: '2026-11-03T14:34:37.729820+00:00'
page_id: json_JobRestVO
product: fluig
source: rest-fluig
title: Fluig REST — JobRestVO Data Type
type: documentation
url: https://api.fluig.com/old/json_JobRestVO.html
version: 1
---

# JobRestVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| jobId | string |  |  |
| companyId | number | required |  |
| jobType | number | required |  |
| description | string |  |  |
| interval | number | required |  |
| target | number | required |  |
| ordinalNumber | number | required |  |
| executionHour | number | required |  |
| executionMinute | number | required |  |
| startDateInMillis | number | required |  |
| data | map of string |  |  |
| lastExecution | number |  |  |
| nextExecution | number |  |  |
| started | boolean |  |  |
| recurrenceExpression | string |  |  |
| intervalType | string |  |  |

Example

```
{
  "jobId" : "...",
  "companyId" : 12345,
  "jobType" : 12345,
  "description" : "...",
  "interval" : 12345,
  "target" : 12345,
  "ordinalNumber" : 12345,
  "executionHour" : 12345,
  "executionMinute" : 12345,
  "startDateInMillis" : 12345,
  "data" : {
    "property1" : "...",
    "property2" : "..."
  },
  "lastExecution" : 12345,
  "nextExecution" : 12345,
  "started" : true,
  "recurrenceExpression" : "...",
  "intervalType" : "..."
}
```
