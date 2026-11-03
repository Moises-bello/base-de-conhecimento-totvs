---
content_hash: d3808138f088294fa4484b7d8ab646f4ed1529b405ca8e776cf4a90f1be8df9d
fetched_at: '2026-11-03T14:34:37.095876+00:00'
page_id: json_GlobalSearchVO
product: fluig
source: rest-fluig
title: Fluig REST — GlobalSearchVO Data Type
type: documentation
url: https://api.fluig.com/old/json_GlobalSearchVO.html
version: 1
---

# GlobalSearchVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| searchType | string |  | the searchType |
| pattern | string |  | the pattern |
| startPeriod | number |  | the startPeriod |
| types | array of string |  | the types |
| endPeriod | number |  | the endPeriod |
| period | [DateGap](https://api.fluig.com/old/json_DateGap.html) |  | the period |
| ordering | [Ordering](https://api.fluig.com/old/json_Ordering.html) |  | the ordering |
| limit | number | required | the limit |
| offset | number | required | the offset |
| documentTypes | array of [DocumentType](https://api.fluig.com/old/json_DocumentType.html) |  | the documentTypes |
| documentTypesCustom | array of string |  | the documentTypesCustom |
| documentParentId | array of string |  |  |
| metaDatas | map of string |  | the metaDatas |
| customFields | map of string |  | the customFields |
| author | number |  | the author |
| communityToSearch | number |  | the communityToSearch |
| formToSearch | number |  | the formToSearch |
| fields | map of string |  | the fields |
| folderToSearch | number |  | the folderToSearch |
| contentSearch | boolean | required |  |

Example

```
{
  "searchType" : "...",
  "pattern" : "...",
  "startPeriod" : 12345,
  "types" : [ "...", "..." ],
  "endPeriod" : 12345,
  "period" : "LAST_HOUR",
  "ordering" : "NEWEST",
  "limit" : 12345,
  "offset" : 12345,
  "documentTypes" : [ "FILEREPORT", "EXTERNALLINK" ],
  "documentTypesCustom" : [ "...", "..." ],
  "documentParentId" : [ "...", "..." ],
  "metaDatas" : {
    "property1" : "...",
    "property2" : "..."
  },
  "customFields" : {
    "property1" : "...",
    "property2" : "..."
  },
  "author" : 12345,
  "communityToSearch" : 12345,
  "formToSearch" : 12345,
  "fields" : {
    "property1" : "...",
    "property2" : "..."
  },
  "folderToSearch" : 12345,
  "contentSearch" : true
}
```
