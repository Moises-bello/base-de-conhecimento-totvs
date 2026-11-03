---
content_hash: 63862b7be8877f9707d0bc0d35687bf51f2c5044bc4d1157347b355900337e23
fetched_at: '2026-11-03T14:34:39.810804+00:00'
page_id: resource_FilterRest
product: fluig
source: rest-fluig
title: Fluig REST — FilterRest Resource
type: documentation
url: https://api.fluig.com/old/resource_FilterRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# FilterRest Resource

Filters - V2

Available Since
:   1.6.1

### POST /2.0/filter/create

Creates a new filter base on the user.

Available Since
:   1.6.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [FilterVO](https://api.fluig.com/old/json_FilterVO.html) (JSON) | Request JSON (example):  ```                {                   	"id" : 0, // Process filter id, must be 0 to create                   	"name" : "Name", // Process filter name                   	"type" : "1", // Process filter type (0 - Document, 1 - Process)                   	"isPublic" : true, // If the process is public or not                   	"processId" : "", // The main process of the filter, if does not have one don't fill this field                  	"fields" : [ // Fields of the filter                  { 		"id" : 0, // Process filter field id, must be 0 to create, 		"key" : "processId", // Key of the value to be filtered, 			//  It can be visible or not and the values depends on it. 			//  Not Visibles (main filters to search for): 			//  "initialRange" - Initial value of the solicitationId range 			//  "finalRange" - Final value of the solicitationId range 			//  "startDate" - Parameter that defines the start date to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialStartDate" - Initial start date to search, only applies if "startDate" is "period" 			//  "finalStartDate" - Final start date to search, only applies if "startDate" is "period" 			//  "requesterId" - Requester's user code to search, only appliable to filters that work outside the "My requests" tab 			//  "termDate" - Parameter that defines the deadline date of the tasks to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialTermDate" - Initial deadline date to search, only applies if "termDate" is "period" 			//  "finalTermDate" - Final deadline date to search, only applies if "termDate" is "period" 			//  "attachmentDescription" - Solicitation form identifier value 			//  "responsibleId" - Responsible's user code to search, only appliable to filters that work outside the "Due tasks" and "Tasks in pool" tabs 			//  "processId" - Main process id to search the tasks 			//  "stateDescription" - State description of the location of the tasks to search 			//  Visibles (select the columns that will appear on the result): 			//  "processInstanceId" - Process instance id 			//  "processDescription" - Process description 			//  "requesterName" - Requester name 			//  "stateDescription" - Locate state description 			//  "colleagueName" - Responsible name 			//  "attachDescription" - Form identifier 			//  "dateExpires" - Deadline date 			//  "requesterId" - Requester user code 			//  "processId" - Process id 			//  "version" - Process version 			//  "movementSequence" - Movement sequence 			//  "stateSequence" - Activity code 			//  "startDateProcess" - Start date process 			//  "formFieldName" - It can be any form field name that is a descriptor field in the process definition (up to ten to select), in this case the "type" value must be "FORM" 		"value" : "", // Value to search (if not visible) 		"type" : "REQUEST", // type of the field, "REQUEST" for default, "FORM" if the key is a form field name 		"label" : "", // Field descriptor, not needed 		"slotId" : 1, // Slot Id from the form field, must be correlated to the selected field 		"visible" : false // If the field belongs to the Visible group or not                  }                  ],                  	"filterOrder" : { 		"id" : 0, // Process filter order id, must be 0 to create, 		"field":  { 		"id" : 0, // Process filter field id, must be 0 to create, 		"key" : "processId", // Key of the value to be filtered, 			//  It can be visible or not and the values depends on it. 			//  Not Visibles (main filters to search for): 			//  "initialRange" - Initial value of the solicitationId range 			//  "finalRange" - Final value of the solicitationId range 			//  "startDate" - Parameter that defines the start date to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialStartDate" - Initial start date to search, only applies if "startDate" is "period" 			//  "finalStartDate" - Final start date to search, only applies if "startDate" is "period" 			//  "requesterId" - Requester's user code to search, only appliable to filters that work outside the "My requests" tab 			//  "termDate" - Parameter that defines the deadline date of the tasks to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialTermDate" - Initial deadline date to search, only applies if "termDate" is "period" 			//  "finalTermDate" - Final deadline date to search, only applies if "termDate" is "period" 			//  "attachmentDescription" - Solicitation form identifier value 			//  "responsibleId" - Responsible's user code to search, only appliable to filters that work outside the "Due tasks" and "Tasks in pool" tabs 			//  "processId" - Main process id to search the tasks 			//  "stateDescription" - State description of the location of the tasks to search 			//  Visibles (select the columns that will appear on the result): 			//  "processInstanceId" - Process instance id 			//  "processDescription" - Process description 			//  "requesterName" - Requester name 			//  "stateDescription" - Locate state description 			//  "colleagueName" - Responsible name 			//  "attachDescription" - Form identifier 			//  "dateExpires" - Deadline date 			//  "requesterId" - Requester user code 			//  "processId" - Process id 			//  "version" - Process version 			//  "movementSequence" - Movement sequence 			//  "stateSequence" - Activity code 			//  "startDateProcess" - Start date process 			//  "formFieldName" - It can be any form field name that is a descriptor field in the process definition (up to ten to select), in this case the "type" value must be "FORM" 		"value" : "", // Value to search (if not visible) 		"type" : "REQUEST", // type of the field, "REQUEST" for default, "FORM" if the key is a form field name 		"label" : "", // Field descriptor, not needed 		"slotId" : 1, // Slot on the datatable (if visible) 		"visible" : false // If the field belongs to the Visible group or not                  },                  	"order" : "asc" // If the order by is asc or desc                  }                } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterResultVO            {            	"content": {            		"filterId" : 1, //Filter Id            		"userId" : 1, // User tenant id            		"filterName" : "Name", //Filter name            		"userName" : "Name", //User name            		"processId" : "ABC", //Process Id            		"isPublic" : true // If filter is public            	},            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.6.1

### GET /2.0/filter/listProcessFilters

Get process filters considering logged user.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| findPublicFilters | query | **(optional - default = false)** Returns filters that are public along with the search, it is ignored if "onlyMyFilters" is true | false | required |
| limit | query | **(optional - default = 30)**  Search results limit | 20 | required |
| offset | query | **(optional - default = 0)**  Start search result | 0 | required |
| onlyMyFilters | query | **(optional - default = false)** Only returns filters that the user created | false | required |
| orderby | query | **(optional - default = "")**  Search ordenation, it can be FILTER\_ASC, FILTER\_DESC, USER\_ASC, USER\_DESC | FILTER\_DESC |  |
| pattern | query | **(optional - default = "")**  Pattern to search (applies on the filter name) |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterResultVO            {            	"content": [{            		"filterId" : 1, //Filter Id            		"userId" : 1, // User tenant id            		"filterName" : "Name", //Filter name            		"userName" : "Name", //User name            		"processId" : "ABC", //Process Id            		"isPublic" : true // If filter is public            	}],            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.6.1

### POST /2.0/filter/removeFilters

Remove process filter by id.

Available Since
:   1.6.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of number (JSON) | - Filters Id on an array |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.6.1

### POST /2.0/filter/saveFiltersGroup

Remove process filter by id.

Available Since
:   1.6.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [FilterGroupVO](https://api.fluig.com/old/json_FilterGroupVO.html) (JSON) | Request JSON (example):  ```                {                   	"filterId" : 1, // Process filter id                   	"groupsCode": [ "ABC", "CDE" ] // Group codes to relate                } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterGroupResultVO            {            	"content": [{            		"id" : 1, //Filter Group Id            		"filterId" : 1, // Filter Id            		"filterName" : "Name", //Filter name            		"groupId" : 1, //Group Id            		"groupCode" : "ABC", //Group Code            		"groupDescription" : "Description" //Group Description            	}],            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.6.1

### POST /2.0/filter/update

Updates a filter base on the user.

Available Since
:   1.6.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [FilterVO](https://api.fluig.com/old/json_FilterVO.html) (JSON) | Request JSON (example):  ```                {                   	"id" : 0, // Process filter id, must be 0 to create                   	"name" : "Name", // Process filter name                   	"type" : "1", // Process filter type (0 - Document, 1 - Process)                   	"isPublic" : true, // If the process is public or not                   	"processId" : "", // The main process of the filter, if does not have one don't fill this field                  	"fields" : [ // Fields of the filter                  { 		"id" : 0, // Process filter field id, must be 0 to create, 		"key" : "processId", // Key of the value to be filtered, 			//  It can be visible or not and the values depends on it. 			//  Not Visibles (main filters to search for): 			//  "initialRange" - Initial value of the solicitationId range 			//  "finalRange" - Final value of the solicitationId range 			//  "startDate" - Parameter that defines the start date to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialStartDate" - Initial start date to search, only applies if "startDate" is "period" 			//  "finalStartDate" - Final start date to search, only applies if "startDate" is "period" 			//  "requesterId" - Requester's user code to search, only appliable to filters that work outside the "My requests" tab 			//  "termDate" - Parameter that defines the deadline date of the tasks to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialTermDate" - Initial deadline date to search, only applies if "termDate" is "period" 			//  "finalTermDate" - Final deadline date to search, only applies if "termDate" is "period" 			//  "attachmentDescription" - Solicitation form identifier value 			//  "responsibleId" - Responsible's user code to search, only appliable to filters that work outside the "Due tasks" and "Tasks in pool" tabs 			//  "processId" - Main process id to search the tasks 			//  "stateDescription" - State description of the location of the tasks to search 			//  Visibles (select the columns that will appear on the result): 			//  "processInstanceId" - Process instance id 			//  "processDescription" - Process description 			//  "requesterName" - Requester name 			//  "stateDescription" - Locate state description 			//  "colleagueName" - Responsible name 			//  "attachDescription" - Form identifier 			//  "dateExpires" - Deadline date 			//  "requesterId" - Requester user code 			//  "processId" - Process id 			//  "version" - Process version 			//  "movementSequence" - Movement sequence 			//  "stateSequence" - Activity code 			//  "startDateProcess" - Start date process 			//  "formFieldName" - It can be any form field name that is a descriptor field in the process definition (up to ten to select), in this case the "type" value must be "FORM" 		"value" : "", // Value to search (if not visible) 		"type" : "REQUEST", // type of the field, "REQUEST" for default, "FORM" if the key is a form field name 		"label" : "", // Field descriptor, not needed 		"slotId" : 1, // Slot Id from the form field, must be correlated to the selected field 		"visible" : false // If the field belongs to the Visible group or not                  }                  ],                  	"filterOrder" : { 		"id" : 0, // Process filter order id, must be 0 to create, 		"field":  { 		"id" : 0, // Process filter field id, must be 0 to create, 		"key" : "processId", // Key of the value to be filtered, 			//  It can be visible or not and the values depends on it. 			//  Not Visibles (main filters to search for): 			//  "initialRange" - Initial value of the solicitationId range 			//  "finalRange" - Final value of the solicitationId range 			//  "startDate" - Parameter that defines the start date to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialStartDate" - Initial start date to search, only applies if "startDate" is "period" 			//  "finalStartDate" - Final start date to search, only applies if "startDate" is "period" 			//  "requesterId" - Requester's user code to search, only appliable to filters that work outside the "My requests" tab 			//  "termDate" - Parameter that defines the deadline date of the tasks to search, it can be LITERALLY: ("today", "yesterday", "thisweek", "lastweek", "thismonth", "lastmonth", "thisyear", "lastyear", "period") 			//  "initialTermDate" - Initial deadline date to search, only applies if "termDate" is "period" 			//  "finalTermDate" - Final deadline date to search, only applies if "termDate" is "period" 			//  "attachmentDescription" - Solicitation form identifier value 			//  "responsibleId" - Responsible's user code to search, only appliable to filters that work outside the "Due tasks" and "Tasks in pool" tabs 			//  "processId" - Main process id to search the tasks 			//  "stateDescription" - State description of the location of the tasks to search 			//  Visibles (select the columns that will appear on the result): 			//  "processInstanceId" - Process instance id 			//  "processDescription" - Process description 			//  "requesterName" - Requester name 			//  "stateDescription" - Locate state description 			//  "colleagueName" - Responsible name 			//  "attachDescription" - Form identifier 			//  "dateExpires" - Deadline date 			//  "requesterId" - Requester user code 			//  "processId" - Process id 			//  "version" - Process version 			//  "movementSequence" - Movement sequence 			//  "stateSequence" - Activity code 			//  "startDateProcess" - Start date process 			//  "formFieldName" - It can be any form field name that is a descriptor field in the process definition (up to ten to select), in this case the "type" value must be "FORM" 		"value" : "", // Value to search (if not visible) 		"type" : "REQUEST", // type of the field, "REQUEST" for default, "FORM" if the key is a form field name 		"label" : "", // Field descriptor, not needed 		"slotId" : 1, // Slot on the datatable (if visible) 		"visible" : false // If the field belongs to the Visible group or not                  },                  	"order" : "asc" // If the order by is asc or desc                  }                } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterResultVO            {            	"content": {            		"filterId" : 1, //Filter Id            		"userId" : 1, // User tenant id            		"filterName" : "Name", //Filter name            		"userName" : "Name", //User name            		"processId" : "ABC", //Process Id            		"isPublic" : true // If filter is public            	},            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.6.1

### GET /2.0/filter/getFiltersGroup/{filterId}

Get process filter group relations by id.

Available Since
:   1.6.1

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| filterId | path | Filter Id |  | required |
| limit | query |  | 20 | required |
| offset | query |  | 0 | required |
| orderby | query |  | CODE\_DESC |  |
| pattern | query |  |  |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterGroupResultVO            {            	"content": [{            		"id" : 1, //Filter Group Id            		"filterId" : 1, // Filter Id            		"filterName" : "Name", //Filter name            		"groupId" : 1, //Group Id            		"groupCode" : "ABC", //Group Code            		"groupDescription" : "Description" //Group Description            	}],            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.6.1

### GET /2.0/filter/getProcessFilterById/{filterId}

Get process filter by id.

Available Since
:   1.6.1

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| filterId | path | Filter Id | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterResultVO            {            	"content": {            		"filterId" : 1, //Filter Id            		"userId" : 1, // User tenant id            		"filterName" : "Name", //Filter name            		"userName" : "Name", //User name            		"processId" : "ABC", //Process Id            		"isPublic" : true // If filter is public            	},            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |

Available Since
:   1.6.0

### PATCH /2.0/filter/{filterId}/name

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| filterId | path |  | required |

Request Body

| media type | data type |
| --- | --- |
| application/json | [FilterUpdateNameVO](https://api.fluig.com/old/json_FilterUpdateNameVO.html) (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.0

### POST /2.0/filter/{instanceId}/sequence

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| instanceId | path |  | long |

Request Body

| media type | data type |
| --- | --- |
| application/json | map of string (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.6.1

### POST /2.0/filter/updatePublicProcessFilter/{filterId}/{isPublic}

Update isPublic flag of the filter.

Available Since
:   1.6.1

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| filterId | path | Filter Id | required |
| isPublic | path | If the filter will be public or not | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method return a list of FilterResultVO            {            	"content": {            		"filterId" : 1, //Filter Id            		"userId" : 1, // User tenant id            		"filterName" : "Name", //Filter name            		"userName" : "Name", //User name            		"processId" : "ABC", //Process Id            		"isPublic" : true // If filter is public            	},            	"message": {            		"message": "OK",            		"detail": "OK",            		"type": "INFO"            	}            } ``` |
