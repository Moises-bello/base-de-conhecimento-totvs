---
content_hash: cb44f36a2eb8cce9995bce40cbbbc999200b6a3337fe0d6735da635aea1dbf26
fetched_at: '2026-11-03T14:34:38.440425+00:00'
page_id: json_SociableDocumentVO
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentVO.html
version: 1
---

# SociableDocumentVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| commented | boolean | required |  |
| numberComments | number |  |  |
| numberShares | number |  |  |
| denounced | boolean | required |  |
| numberLikes | number |  |  |
| numberWatch | number |  |  |
| watching | boolean | required |  |
| numberDenouncements | number |  |  |
| ~~following~~ | ~~boolean~~ | ~~required~~ |  |
| ~~numberFollows~~ | ~~number~~ |  |  |
| shared | boolean | required |  |
| documentId | number |  |  |
| sociableId | number |  |  |
| liked | boolean | required |  |
| version | number |  |  |

Example

```
{
  "commented" : true,
  "numberComments" : 12345,
  "numberShares" : 12345,
  "denounced" : true,
  "numberLikes" : 12345,
  "numberWatch" : 12345,
  "watching" : true,
  "numberDenouncements" : 12345,
  "shared" : true,
  "documentId" : 12345,
  "sociableId" : 12345,
  "liked" : true,
  "version" : 12345
}
```
