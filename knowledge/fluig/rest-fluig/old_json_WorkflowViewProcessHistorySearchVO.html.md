---
content_hash: 100cd87bb31ad17bffa43bfb46733f76811ed57cf18e32c689e4896fede0ac4e
fetched_at: '2026-11-03T14:34:39.185689+00:00'
page_id: json_WorkflowViewProcessHistorySearchVO
product: fluig
source: rest-fluig
title: Fluig REST — WorkflowViewProcessHistorySearchVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WorkflowViewProcessHistorySearchVO.html
version: 1
---

# WorkflowViewProcessHistorySearchVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| taskUserId | string |  |  |
| dateFrom | string |  |  |
| historyTypes | array of string |  |  |
| processVersion | number |  |  |
| page | number | required |  |
| pageSize | number | required |  |
| dateTo | string |  |  |
| searchUser | string |  |  |
| searchTask | string |  |  |
| sortBy | string |  |  |
| movementSequence | number |  |  |
| processInstanceId | number | required |  |
| searchComment | string |  |  |
| processId | string |  |  |
| tenantId | number | required |  |

Example

```
{
  "taskUserId" : "...",
  "dateFrom" : "...",
  "historyTypes" : [ "...", "..." ],
  "processVersion" : 12345,
  "page" : 12345,
  "pageSize" : 12345,
  "dateTo" : "...",
  "searchUser" : "...",
  "searchTask" : "...",
  "sortBy" : "...",
  "movementSequence" : 12345,
  "processInstanceId" : 12345,
  "searchComment" : "...",
  "processId" : "...",
  "tenantId" : 12345
}
```
