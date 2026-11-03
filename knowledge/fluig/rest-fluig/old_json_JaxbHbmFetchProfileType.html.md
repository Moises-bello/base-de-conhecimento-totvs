---
content_hash: c8e327768950a26cecccbdc39228a9939eaf6c928fbb75e6dcf7382e718856be
fetched_at: '2026-11-03T14:34:37.394606+00:00'
page_id: json_JaxbHbmFetchProfileType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmFetchProfileType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmFetchProfileType.html
version: 1
---

# JaxbHbmFetchProfileType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| fetch | array of [JaxbHbmFetch](https://api.fluig.com/old/json_JaxbHbmFetch.html) |  |
| name | string |  |

Example

```
{
  "fetch" : [ {
    "association" : "...",
    "entity" : "...",
    "style" : "JOIN"
  }, {
    "association" : "...",
    "entity" : "...",
    "style" : "SELECT"
  } ],
  "name" : "..."
}
```
