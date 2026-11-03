---
content_hash: 89201612813f114eac263bcef11ff23c2b6d9384712a2350772e7ea1744bbfed
fetched_at: '2026-11-03T14:34:36.551182+00:00'
page_id: json_Dataset
product: fluig
source: rest-fluig
title: Fluig REST — Dataset Data Type
type: documentation
url: https://api.fluig.com/old/json_Dataset.html
version: 1
---

# Dataset Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| lastRemoteSyncTimestamp | number |  |  |
| resetType | number |  |  |
| updateIntervalTimestamp | number |  |  |
| lastResetTimestamp | number |  |  |
| syncDetails | string |  |  |
| type | string |  |  |
| updateInterval | number |  |  |
| mobileCache | boolean |  |  |
| updateIntervalDate | number |  |  |
| journalingAdherence | number |  |  |
| lastRemoteSync | number |  |  |
| datasetDescription | string |  |  |
| serverOffline | boolean |  |  |
| lastResetDate | number |  |  |
| datasetImpl | string |  |  |
| active | boolean | required |  |
| syncStatus | number |  |  |
| datasetPK | [DatasetPK](https://api.fluig.com/old/json_DatasetPK.html) |  |  |
| draft | boolean |  |  |
| lastReset | number |  |  |
| offlineMobileCache | boolean |  |  |
| lastRemoteSyncDate | number |  |  |
| datasetBuilder | string |  |  |

Example

```
{
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
```
