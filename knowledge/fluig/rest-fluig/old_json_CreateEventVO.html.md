---
content_hash: f1ea1599c929cfc46990984664576ba4f9577f0c1161417ac8d50d22bf5b6bda
fetched_at: '2026-11-03T14:34:36.533826+00:00'
page_id: json_CreateEventVO
product: fluig
source: rest-fluig
title: Fluig REST — CreateEventVO Data Type
type: documentation
url: https://api.fluig.com/old/json_CreateEventVO.html
version: 1
---

# CreateEventVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| eventKey | string |  |
| descriptionKey | string |  |
| singleDescriptionKey | string |  |
| groupDescriptionKey | string |  |
| eventIcon | string |  |
| moduleId | number |  |
| grouped | boolean |  |
| canRemove | boolean |  |
| removeAfterExecAction | boolean |  |
| onlyAdmin | boolean |  |
| required | boolean |  |

Example

```
{
  "eventKey" : "...",
  "descriptionKey" : "...",
  "singleDescriptionKey" : "...",
  "groupDescriptionKey" : "...",
  "eventIcon" : "...",
  "moduleId" : 12345,
  "grouped" : true,
  "canRemove" : true,
  "removeAfterExecAction" : true,
  "onlyAdmin" : true,
  "required" : true
}
```
