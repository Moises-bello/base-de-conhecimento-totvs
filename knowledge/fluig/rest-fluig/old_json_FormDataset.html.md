---
content_hash: f0388a7a0f2f60fa7e3eebfec063f922f0343d1a27ed75bd9c09254226d4d513
fetched_at: '2026-11-03T14:34:37.053184+00:00'
page_id: json_FormDataset
product: fluig
source: rest-fluig
title: Fluig REST — FormDataset Data Type
type: documentation
url: https://api.fluig.com/old/json_FormDataset.html
version: 1
---

# FormDataset Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| datasetId | string |  |  |
| documentId | number |  |  |
| version | number | required |  |
| companyId | number | required |  |
| id | number |  |  |
| dataset | [Dataset](https://api.fluig.com/old/json_Dataset.html) |  |  |

Example

```
{
  "datasetId" : "...",
  "documentId" : 12345,
  "version" : 12345,
  "companyId" : 12345,
  "id" : 12345,
  "dataset" : {
    "lastRemoteSyncTimestamp" : 12345,
    "resetType" : 12345,
    "updateIntervalTimestamp" : 12345,
    "lastResetTimestamp" : 12345,
    "syncDetails" : "...",
    "type" : "...",
    "updateInterval" : 12345,
    "mobileCache" : true,
    "updateIntervalDate" : 12345,
    "journalingAdherence" : 12345,
    "lastRemoteSync" : 12345,
    "datasetDescription" : "...",
    "serverOffline" : true,
    "lastResetDate" : 12345,
    "datasetImpl" : "...",
    "active" : true,
    "syncStatus" : 12345,
    "datasetPK" : {
      "datasetId" : "...",
      "companyId" : 12345
    },
    "draft" : true,
    "lastReset" : 12345,
    "offlineMobileCache" : true,
    "lastRemoteSyncDate" : 12345,
    "datasetBuilder" : "..."
  }
}
```
