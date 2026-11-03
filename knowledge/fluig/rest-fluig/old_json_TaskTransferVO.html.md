---
content_hash: cbed5a15aadb8bf517e57b330257f1d06fb7220b94de623001abd0c237bb6c78
fetched_at: '2026-11-03T14:34:38.660733+00:00'
page_id: json_TaskTransferVO
product: fluig
source: rest-fluig
title: Fluig REST — TaskTransferVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TaskTransferVO.html
version: 1
---

# TaskTransferVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| transferApprovers | boolean |  |
| transferActiveDocuments | boolean |  |
| instanceIdFinal | number |  |
| transferMyDocumentsInApproval | boolean |  |
| transferApprovals | boolean |  |
| transferPendingWorkflow | boolean |  |
| userTo | string |  |
| transferDocumentSecurity | boolean |  |
| transferOpenWorkflow | boolean |  |
| documentIdInitial | number |  |
| instanceIdInitial | number |  |
| documentIdFinal | number |  |
| userFrom | string |  |

Example

```
{
  "transferApprovers" : true,
  "transferActiveDocuments" : true,
  "instanceIdFinal" : 12345,
  "transferMyDocumentsInApproval" : true,
  "transferApprovals" : true,
  "transferPendingWorkflow" : true,
  "userTo" : "...",
  "transferDocumentSecurity" : true,
  "transferOpenWorkflow" : true,
  "documentIdInitial" : 12345,
  "instanceIdInitial" : 12345,
  "documentIdFinal" : 12345,
  "userFrom" : "..."
}
```
