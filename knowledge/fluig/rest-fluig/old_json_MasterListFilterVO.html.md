---
content_hash: ccec5c645c67e299669b618b2a74d189d9331a56e229c0662d5716ebbb8cccd5
fetched_at: '2026-11-03T14:34:37.800751+00:00'
page_id: json_MasterListFilterVO
product: fluig
source: rest-fluig
title: Fluig REST — MasterListFilterVO Data Type
type: documentation
url: https://api.fluig.com/old/json_MasterListFilterVO.html
version: 1
---

# MasterListFilterVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| publisherId | string |  |  |
| expired | boolean | required |  |
| approvalStatus | array of string |  |  |
| updateDateFromAsDate | number |  |  |
| updateDateToAsDate | number |  |  |
| documentTypeId | string |  |  |
| authorId | string |  |  |
| subFolders | boolean | required |  |
| controlledCopyLog | boolean | required |  |
| approvalHistory | boolean | required |  |
| updateDateFrom | string |  |  |
| notReleased | boolean | required |  |
| consumedQuota | boolean | required |  |
| folders | array of string |  |  |
| updateDateTo | string |  |  |
| hideApprovedHistory | boolean | required |  |
| printFormat | [MasterListPrintFormat](https://api.fluig.com/old/json_MasterListPrintFormat.html) |  |  |

Example

```
{
  "publisherId" : "...",
  "expired" : true,
  "approvalStatus" : [ "...", "..." ],
  "updateDateFromAsDate" : 12345,
  "updateDateToAsDate" : 12345,
  "documentTypeId" : "...",
  "authorId" : "...",
  "subFolders" : true,
  "controlledCopyLog" : true,
  "approvalHistory" : true,
  "updateDateFrom" : "...",
  "notReleased" : true,
  "consumedQuota" : true,
  "folders" : [ "...", "..." ],
  "updateDateTo" : "...",
  "hideApprovedHistory" : true,
  "printFormat" : "HTML"
}
```
