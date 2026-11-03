---
content_hash: 9ca78f9f0ed315579b59f872666017209d4db5ab654c1bdd6a99c40731b086d8
fetched_at: '2026-11-03T14:34:36.662854+00:00'
page_id: json_DocumentSearch
product: fluig
source: rest-fluig
title: Fluig REST — DocumentSearch Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentSearch.html
version: 1
---

# DocumentSearch Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| types | array of string |  |
| metaDatas | map of string |  |
| requestHandler | string |  |
| documentTypes | array of [DocumentType](https://api.fluig.com/old/json_DocumentType.html) |  |
| filters | array of string |  |
| documentParentId | array of string |  |
| folderToSearch | number |  |
| documentTypesCustom | array of string |  |
| customFields | map of string |  |
| Properties inherited from [AbstractSearch](https://api.fluig.com/old/json_AbstractSearch.html) | | |
| searchType | string | The JSON object type. |
| offset | number |  |
| ordering | [Ordering](https://api.fluig.com/old/json_Ordering.html) |  |
| limit | number |  |
| startPeriod | number |  |
| pattern | string |  |
| endPeriod | number |  |
| period | [DateGap](https://api.fluig.com/old/json_DateGap.html) |  |
| contentSearch | boolean |  |

Example

```
{
  "types" : [ "...", "..." ],
  "metaDatas" : {
    "property1" : "...",
    "property2" : "..."
  },
  "requestHandler" : "...",
  "documentTypes" : [ "FOLDER", "FILEDOCUMENT" ],
  "filters" : [ "...", "..." ],
  "documentParentId" : [ "...", "..." ],
  "folderToSearch" : 12345,
  "documentTypesCustom" : [ "...", "..." ],
  "customFields" : {
    "property1" : "...",
    "property2" : "..."
  },
  "searchType" : "DOCUMENT",
  "offset" : 12345,
  "ordering" : "RELEVANT",
  "limit" : 12345,
  "startPeriod" : 12345,
  "pattern" : "...",
  "endPeriod" : 12345,
  "period" : "LAST_MONTH",
  "contentSearch" : true
}
```
