---
content_hash: 8832966922f93f82454c875e8a0e79c1d40e9800b5173e960ce37a150ae4123e
fetched_at: '2026-11-03T14:34:40.129156+00:00'
page_id: resource_SearchServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — SearchServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_SearchServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# SearchServiceRest Resource

Searches

### POST /search/advanced

to obtain precision in the search, use as quotation marks, for example: "parameter"

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [GlobalSearchVO](https://api.fluig.com/old/json_GlobalSearchVO.html) (JSON) | Request JSON (example):`{ // General filters "searchType" : "GLOBAL", //Types: GLOBAL, USER, COMMUNITY, DOCUMENT, PROCESS, POST, FORM, TAG, WORD "pattern" : "#worldCup Brazil", //Supports hash tags searches "startPeriod" : "2014-01-30", //Search start date (optional parameter) "endPeriod" : "2014-01-30", //Search end date (optional parameter) "period" : "LAST_HOUR", //Gaps: LAST_HOUR, LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR (optional parameter) //the parameter period override the startPeriod and endPeriod parameters "ordering" : "RELEVANT", //Orderings: RELEVANT, NEWEST, OLDEST "limit" : "2", //Limit of results "offset" : "2", //Result offset (optional parameter) "contentSearch" : "true" //search in the file content // Filters for GLOBAL search "types" : ["DOCUMENT"], //Types: USER, COMMUNITY, DOCUMENT, PROCESS // Filters for DOCUMENT search "documentTypes" : ["FILEDOCUMENT"], //Types: FILEDOCUMENT, FOLDER, EDITABLEDOCUMENT, FILEREPORT, EXTERNALLINK "documentTypesCustom" : ["Contrato"], //Documents types created in Fluig "documentParentId" : ["94"], //Search in a document parent folder "metaDatas" : {"author" : "Paulo Coelho", "age" : "18"}, //Meta data filters "folderToSearch" : "5" //ID folder to search "customFields" : {"author" : "Paulo Coelho", "age" : "18"}, //Custom fields filters // Filters for POST search "author" : "adm", //Alias of author of the post "communityToSearch" : "com1", //Alias of community where the post was published // Filters for FORM search "formToSearch" : "2", //Parent folder "fields" : {"author" : "Paulo Coelho", "age" : "18"} //Fields of form }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {  	"timeElapsed" : "132ms",		//Time to recovery the data  	"totalHits" : "2",				//Number of results  	"offset" : "5",					//Offset  	"items" : [						//Result list  		"fields" : [  			 "DocumentName" : "Portal",  			 "DocumentCreateDate" : "30/01/2014",  			 "DocumentDescription" : "Description"  		]  	],  	"groups" : [					//Groups  		"name" : "DocumentType",  		"totalHits" : "20",  		"categories" : [  			 "COMMUNITY": "15",  			 "DOCUMENT": "3",  			 "PROCESS": "1",  			 "USER": "1"  		]  	]  } ``` |
