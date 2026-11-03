---
content_hash: 51bab25d20b72a02556375f395d3df8391f8095a0f7c3a5d212796b318c6ba47
fetched_at: '2026-11-03T14:34:37.736419+00:00'
page_id: json_JobVO
product: fluig
source: rest-fluig
title: Fluig REST — JobVO Data Type
type: documentation
url: https://api.fluig.com/old/json_JobVO.html
version: 1
---

# JobVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| companyId | number | required |  |
| description | string |  |  |
| intervalDescriptions | string |  |  |
| lastExecution | number |  |  |
| interval | number | required |  |
| jobId | string |  |  |
| recurrenceExpression | string |  |  |
| intervalType | [IntervalType](https://api.fluig.com/old/json_IntervalType.html) |  |  |
| nextExecution | number |  |  |
| started | boolean |  |  |
| data | map of string |  |  |
| startDateInMillis | number | required |  |
| executionMinute | number | required |  |
| target | number | required |  |
| jobType | number | required |  |
| ordinalNumber | number | required |  |
| executionHour | number | required |  |

Example

```
{
  "companyId" : 12345,
  "description" : "...",
  "intervalDescriptions" : "...",
  "lastExecution" : 12345,
  "interval" : 12345,
  "jobId" : "...",
  "recurrenceExpression" : "...",
  "intervalType" : "WEEKLY",
  "nextExecution" : 12345,
  "started" : true,
  "data" : {
    "property1" : "...",
    "property2" : "..."
  },
  "startDateInMillis" : 12345,
  "executionMinute" : 12345,
  "target" : 12345,
  "jobType" : 12345,
  "ordinalNumber" : 12345,
  "executionHour" : 12345
}
```
