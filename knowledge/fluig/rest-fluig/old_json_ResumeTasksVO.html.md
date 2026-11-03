---
content_hash: 8ea3d2ad78c0ec969a6ca890a4a8bbe5757bdf53501ec64e59d45b7a8a36a013
fetched_at: '2026-11-03T14:34:38.275494+00:00'
page_id: json_ResumeTasksVO
product: fluig
source: rest-fluig
title: Fluig REST — ResumeTasksVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ResumeTasksVO.html
version: 1
---

# ResumeTasksVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| myDocuments | number | required |  |
| toApprover | number | required |  |
| learningTasks | number | required |  |
| expiredTasks | number | required |  |
| openTasks | number | required |  |
| myRequests | number | required |  |
| checkout | number | required |  |
| replacement | boolean | required |  |

Example

```
{
  "myDocuments" : 12345,
  "toApprover" : 12345,
  "learningTasks" : 12345,
  "expiredTasks" : 12345,
  "openTasks" : 12345,
  "myRequests" : 12345,
  "checkout" : 12345,
  "replacement" : true
}
```
