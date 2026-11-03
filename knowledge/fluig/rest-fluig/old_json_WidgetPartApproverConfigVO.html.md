---
content_hash: 20eb7c5794a70c403e557b096e73f4298f23c16a2ec0ced673ad453e6553c97c
fetched_at: '2026-11-03T14:34:38.988954+00:00'
page_id: json_WidgetPartApproverConfigVO
product: fluig
source: rest-fluig
title: Fluig REST — WidgetPartApproverConfigVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WidgetPartApproverConfigVO.html
version: 1
---

# WidgetPartApproverConfigVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| approvalMode | number | required |  |
| levelDescription | string |  |  |
| digitalSignature | boolean | required |  |
| colleagueLogin | string |  |  |
| levelId | number | required |  |
| tableId | number | required |  |
| colleagueName | string |  |  |
| colleagueId | string |  |  |
| approverType | number | required |  |

Example

```
{
  "approvalMode" : 12345,
  "levelDescription" : "...",
  "digitalSignature" : true,
  "colleagueLogin" : "...",
  "levelId" : 12345,
  "tableId" : 12345,
  "colleagueName" : "...",
  "colleagueId" : "...",
  "approverType" : 12345
}
```
