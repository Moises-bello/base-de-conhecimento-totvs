---
content_hash: c2295e2a61877f540604c0e99fa3204d82cbd45f86a553787d3b8853d9cc47de
fetched_at: '2026-11-03T14:34:37.821152+00:00'
page_id: json_MediaVO
product: fluig
source: rest-fluig
title: Fluig REST — MediaVO Data Type
type: documentation
url: https://api.fluig.com/old/json_MediaVO.html
version: 1
---

# MediaVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| documentId | number |  |  |
| url | string |  |  |
| socialObjectId | number |  |  |
| id | number |  |  |
| file | string |  |  |
| name | string |  |  |
| previousMediaId | number |  |  |
| type | [SocialMediaType](https://api.fluig.com/old/json_SocialMediaType.html) |  |  |
| gallery | [MediaVO](https://api.fluig.com/old/json_MediaVO.html) |  |  |
| canWrite | boolean | required |  |
| creationDate | number |  |  |
| canEdit | boolean | required |  |
| nextMediaId | number |  |  |
| alias | string |  |  |
| numberMedias | number |  |  |
| viewUrl | string |  |  |
| version | number |  |  |
| description | string |  |  |

Example

```
{
  "documentId" : 12345,
  "url" : "...",
  "socialObjectId" : 12345,
  "id" : 12345,
  "file" : "...",
  "name" : "...",
  "previousMediaId" : 12345,
  "type" : "VIDEO",
  "gallery" : {
    "documentId" : 12345,
    "url" : "...",
    "socialObjectId" : 12345,
    "id" : 12345,
    "file" : "...",
    "name" : "...",
    "previousMediaId" : 12345,
    "type" : "GALLERY_PHOTO",
    "gallery" : { },
    "canWrite" : true,
    "creationDate" : 12345,
    "canEdit" : true,
    "nextMediaId" : 12345,
    "alias" : "...",
    "numberMedias" : 12345,
    "viewUrl" : "...",
    "version" : 12345,
    "description" : "..."
  },
  "canWrite" : true,
  "creationDate" : 12345,
  "canEdit" : true,
  "nextMediaId" : 12345,
  "alias" : "...",
  "numberMedias" : 12345,
  "viewUrl" : "...",
  "version" : 12345,
  "description" : "..."
}
```
