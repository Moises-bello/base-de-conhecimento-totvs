---
content_hash: cfd05cc3cf27d08b431226c9452eb3a1b0c27cf3ef94fc6471c3fbba8a538d05
fetched_at: '2026-11-03T14:34:38.089020+00:00'
page_id: json_ProcessSearchVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessSearchVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessSearchVO.html
version: 1
---

# ProcessSearchVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| groupTableData | boolean | required |  |
| stateData | boolean | required |  |
| requestSLA | boolean | required |  |
| opened | boolean | required |  |
| userLoggedAdmin | boolean |  |  |
| dataIni | string |  |  |
| processId | string |  |  |
| userId | string |  |  |
| formData | boolean | required |  |
| canceled | boolean | required |  |
| finished | boolean | required |  |
| companyId | number | required |  |
| filter | number | required |  |
| instanceFim | number | required |  |
| dataFim | string |  |  |
| listPsProcessVo | array of [ProcessSearchProcessVO](https://api.fluig.com/old/json_ProcessSearchProcessVO.html) |  |  |
| sequence | number | required |  |
| includeTables | boolean | required |  |
| tenantId | number |  |  |
| version | number | required |  |
| multiNumProcess | string |  |  |
| instanceIni | number | required |  |

Example

```
{
  "groupTableData" : true,
  "stateData" : true,
  "requestSLA" : true,
  "opened" : true,
  "userLoggedAdmin" : true,
  "dataIni" : "...",
  "processId" : "...",
  "userId" : "...",
  "formData" : true,
  "canceled" : true,
  "finished" : true,
  "companyId" : 12345,
  "filter" : 12345,
  "instanceFim" : 12345,
  "dataFim" : "...",
  "listPsProcessVo" : [ {
    "processId" : "...",
    "managerCustomAssignment" : true,
    "processDescription" : "..."
  }, {
    "processId" : "...",
    "managerCustomAssignment" : true,
    "processDescription" : "..."
  } ],
  "sequence" : 12345,
  "includeTables" : true,
  "tenantId" : 12345,
  "version" : 12345,
  "multiNumProcess" : "...",
  "instanceIni" : 12345
}
```
