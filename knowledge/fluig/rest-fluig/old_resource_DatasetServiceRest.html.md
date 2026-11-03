---
content_hash: d0146da9ea2b0f001598528a3ed68527c84a38e930bd40b20f8a3dd0d93dbdf0
fetched_at: '2026-11-03T14:34:39.639744+00:00'
page_id: resource_DatasetServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — DatasetServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_DatasetServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# DatasetServiceRest Resource

Datasets

### GET /ecm/dataset/availableDatasets

Returns the avaibles datasets

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	"workflowColleagueRole",  //avaible dataset name  	"FactActivityVolume",     //avaible dataset name  	"FactFlowVolume",         //avaible dataset name  	"colleagueGroup",         //avaible dataset name  } ``` |

### GET /ecm/dataset/cardDatasetValues

Request Parameters

| name | type | description |
| --- | --- | --- |
| data | query |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### POST /ecm/dataset/cardDatasetValues

Returns a card dataset

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Request JSON (example):  ```  {  	"datasetId" : "99",      //dataset's id (number)  	"filter" : {"field1": "value1", "field2":"value2"},      //dataset filter values  	"likeField" : "likeField" //field used to the like expression  	"likeValue" : "likeValue" //value used to fill the like expression  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	"chave" : "codcoligada=1&idmov=143900",                                  //dataset's card id  	"commarea" : "codcoligada=1&idmov=143900&codtmv=1.2.01&user=josue.gomes",//commarea  	"Situacao" : "cancelado",                                                //situation  	"Usuario_do_Cadastramento" : "josue.gomes",                              //registration user  	"Valor" : "10000000.00",                                                 //value  } ``` |

### GET /ecm/dataset/datasetJournaling

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| datasetId | query |  |  |
| lastSync | query |  | required |
| numberOfRows | query |  | required |
| startRecord | query |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| text/json | object (JSON) | ```  {  "content": {      "lastRetrievedRecordId": 0,      "addedRecords": [           {               "mail": "adm",               "volumeId": null,               "extensionNr": null,               "especializationArea": null,               "colleaguePK.colleagueId": "adm",               "colleaguePK.companyId": "1",               "defaultLanguage": null,               "currentProject": null,               "groupId": null,               "maxPrivateSize": null,               "adminUser": "true",               "emailHtml": null,               "active": "true",               "login": "adm",               "colleagueName": "adm adm"           },           {               "mail": "aaa@asdsa.com",               "volumeId": null,               "extensionNr": null,               "especializationArea": null,               "colleaguePK.colleagueId": "4872394823",               "colleaguePK.companyId": "1",               "defaultLanguage": "pt_BR",               "currentProject": null,               "groupId": null,               "maxPrivateSize": null,               "adminUser": "false",               "emailHtml": "true",               "active": "true",               "login": "adm1",               "colleagueName": "ADM 2 ADMADM"           }      ],      "updatedRecords": [               mesmo formato do array addedRecords      ],      "removedRecords": [               mesmo formato do array addedRecords      ]      },      "message": null  } ``` |

### POST /ecm/dataset/datasets

Returns a dataset

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Request JSON (example):`{ "name" : "topic", //dataset's id "fields" : ["field1", "field2"], //fields to return "constraints" : [{ //constraints to filter the search, all fields specified inside are required "_field" : "value1", //name of the field used in the constraint "_initialValue": "value2", //value to be filtered "_finalValue" : "value3", //final value to be filtered "_type": 0, //type of the constraint (1 - MUST, 2 - SHOULD, 3 - MUST_NOT) "_likeSearch": false //if it is a LIKE search }], "order" : ["field1"] // Array specifying the order by parameter }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` {   content: {       values: [1] //the properties of dataset (changes by sending the "fields" parameter)           0:  {               topicPK.topicId: 1               topicPK.companyId: 1               description: "Diversos"               mandatory: false               updateEmail: null               removeEmail: null           }       columns: [6] //the returned columns of dataset (changes by sending the "fields" parameter)           0:  "topicPK.topicId"           1:  "topicPK.companyId"           2:  "description"           3:  "mandatory"           4:  "updateEmail"           5:  "removeEmail"   }   message: null  } ``` |

### GET /ecm/dataset/editable

Request Parameters

| name | type | description |
| --- | --- | --- |
| datasetIds | query |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### GET /ecm/dataset/previewJournaling

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| datasetId | query |  |  |
| lastSync | query |  | required |
| numberOfRows | query |  | required |
| startRecord | query |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### GET /ecm/dataset/search

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| datasetId | query | Dataset Id for search |  |
| filterFields | query | Prefilter fields for the dataset to load, divided by comma |  |
| likeField | query | The like field, if it is a metadata field have to change the # for \_ |  |
| likeValue | query | The like value, for relative searchs |  |
| limit | query | The limit of results returned by the dataset | required |
| orderBy | query | The ordering field and the direction |  |
| resultFields | query | The result columns, divided by comma |  |
| searchField | query | Field by that the dataset will be filtered on demand |  |
| searchValue | query | The dynamic value for the searchField |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### POST /ecm/dataset/search

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Request JSON (example):  ``` {  	"datasetId" : "datasetId",  	"searchField" : "searchField",  	"searchValue" : "searchValue",  	"filterFields" : ["field1", "field2"],  	"resultFields" : ["value1", "value2"],  	"likeField" : "likeField",  	"likeValue" : "likeValue",  	"limit" : "50",  #9;"orderBy" : "orderField"  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### GET /ecm/dataset/standardDatasetValues

Request Parameters

| name | type | description |
| --- | --- | --- |
| data | query |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

### POST /ecm/dataset/standardDatasetValues

Returns a list of standard datasets

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Request JSON (example):  ```  {  	"datasetId" : "topic",      //dataset's id  	"filter" : {"field1": "value1", "field2":"value2"}      //dataset filter values  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  	"description" : "Diversos",      //dataset's description  	"topicId" : "1",      //dataset's id  } ``` |

Available Since
:   1.5.5

### POST /ecm/dataset/synchronizeDataset

This method has been deprecated. Use /{datasetId}/synchronize
Synchronize Dataset.

Available Since
:   1.5.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | REQUIRED dataset id |
| application/xml | string (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"content" : true  } ``` |

### GET /ecm/dataset/datasetStructure/{datasetId}

Request Parameters

| name | type | description |
| --- | --- | --- |
| datasetId | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  "content": {      "datasetId": "colleague",      "fields": [          {              "fieldName": "colleaguePK.companyId",              "dataType": "string"          },          {              "fieldName": "colleaguePK.colleagueId",              "dataType": "string"          },          ...          {              "fieldName": "groupId",              "dataType": "string"          }      ],      "lastReset": 0,      "lastUpdate": 0  },  "message": null  } ``` |

### POST /ecm/dataset/{componentId}/update

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| componentId | path |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.5

### POST /ecm/dataset/{datasetId}/synchronize

Synchronize Dataset .

Available Since
:   1.6.5

Request Parameters

| name | type | description |
| --- | --- | --- |
| datasetId | path | REQUIRED dataset id |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"content" : true  } ``` |

### GET /ecm/dataset/{componentId}/check/dependency

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| componentId | path |  | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |
