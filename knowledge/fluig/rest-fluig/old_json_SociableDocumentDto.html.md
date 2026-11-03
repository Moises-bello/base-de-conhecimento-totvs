---
content_hash: d912cc61b9ba525c713b85952e7a3631a0039b391c01ddd98d04aa1a25e14706
fetched_at: '2026-11-03T14:34:38.422136+00:00'
page_id: json_SociableDocumentDto
product: fluig
source: rest-fluig
title: Fluig REST — SociableDocumentDto Data Type
type: documentation
url: https://api.fluig.com/old/json_SociableDocumentDto.html
version: 1
---

# SociableDocumentDto Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| denounced | boolean | required |  |
| version | number |  |  |
| commented | boolean | required |  |
| following | boolean | required |  |
| numberShares | number |  |  |
| documentId | number |  |  |
| numberFollows | number |  |  |
| shared | boolean | required |  |
| liked | boolean | required |  |
| sociableId | number |  |  |
| numberLikes | number |  |  |
| numberComments | number |  |  |
| numberDenouncements | number |  |  |

Example

```
{
  "denounced" : true,
  "version" : 12345,
  "commented" : true,
  "following" : true,
  "numberShares" : 12345,
  "documentId" : 12345,
  "numberFollows" : 12345,
  "shared" : true,
  "liked" : true,
  "sociableId" : 12345,
  "numberLikes" : 12345,
  "numberComments" : 12345,
  "numberDenouncements" : 12345
}
```
