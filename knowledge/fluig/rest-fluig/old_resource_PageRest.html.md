---
content_hash: 9759338be568ae1bf62284503422d9c5fa27cd35e35bdbc4e78ab78347479a31
fetched_at: '2026-11-03T14:34:40.017045+00:00'
page_id: resource_PageRest
product: fluig
source: rest-fluig
title: Fluig REST — PageRest Resource
type: documentation
url: https://api.fluig.com/old/resource_PageRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# PageRest Resource

Page

Available Since
:   1.5.12

### POST /2.0/pages/createPageDraftFromVersion

Create a page draft from an especific page version

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| pageCode | query | Page Code |  |
| pageVersion | query | Page Version | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.8

### GET /2.0/pages/findMenuFromPage

Find menu from page

Available Since
:   1.5.8

Request Parameters

| name | type | description | default |
| --- | --- | --- | --- |
| pageCode | query | Code of requested page **(REQUIRED - default = 'home')** | home |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, Object User  { "content": [{ "pageId": 29, "pageIcon": "portal/api/servlet/image/1/page/pagefavorites.png", "title": "Documentos favoritos", "description": "Documentos favoritos", "searchLevel": 0, "pageCode": "pagefavorites", "children": [], "parentPageCode": "principalfavorites", "uri": "portal/p/1/pagefavorites", "friendlyURL": null }, { "pageId": 31, "pageIcon": "portal/api/servlet/image/1/page/pageprocessfavorites.png", "title": "Processos favoritos", "description": "Processos favoritos", "searchLevel": 0, "pageCode": "pageprocessfavorites", "children": [], "parentPageCode": "principalfavorites", "uri": "portal/p/1/pageprocessfavorites", "friendlyURL": null }, { "pageId": 33, "pageIcon": "portal/api/servlet/image/1/page/pagecontactfavorites.png", "title": "Contatos Favoritos", "description": "Contatos Favoritos", "searchLevel": 0, "pageCode": "pagecontactfavorites", "children": [], "parentPageCode": "principalfavorites", "uri": "portal/p/1/pagecontactfavorites", "friendlyURL": null }], "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5

### GET /2.0/pages/findPages

Find fluig pages  
  
Find fluig pages: send data query param

Available Since
:   1.5

Request Parameters

| name | type | description | default | constraints |
| --- | --- | --- | --- | --- |
| codePage | query |  |  |  |
| filter | query |  |  |  |
| internalPages | query |  | false | boolean |
| isMobile | query |  | false | boolean |
| pageIndex | query |  | 0 | required |
| pageSize | query |  | 20 | required |
| parentPageCode | query |  |  |  |
| searchLevel | query |  | 0 | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status, Object User   {  	"content": [{  		"pageId": 29,  		"pageIcon": "portal/api/servlet/image/1/page/pagefavorites.png",  		"title": "Documentos favoritos",  		"description": "Documentos favoritos",  		"searchLevel": 0,  		"pageCode": "pagefavorites",  		"children": [],  		"parentPageCode": "principalfavorites",  		"uri": "portal/p/1/pagefavorites",  		"friendlyURL": null  	}, {  		"pageId": 31,  		"pageIcon": "portal/api/servlet/image/1/page/pageprocessfavorites.png",  		"title": "Processos favoritos",  		"description": "Processos favoritos",  		"searchLevel": 0,  		"pageCode": "pageprocessfavorites",  		"children": [],  		"parentPageCode": "principalfavorites",  		"uri": "portal/p/1/pageprocessfavorites",  		"friendlyURL": null  	}, {  		"pageId": 33,  		"pageIcon": "portal/api/servlet/image/1/page/pagecontactfavorites.png",  		"title": "Contatos Favoritos",  		"description": "Contatos Favoritos",  		"searchLevel": 0,  		"pageCode": "pagecontactfavorites",  		"children": [],  		"parentPageCode": "principalfavorites",  		"uri": "portal/p/1/pagecontactfavorites",  		"friendlyURL": null  	}],  	"message": {  		"message": "OK",  		"detail": "OK",  		"type": "INFO"  	}  } ``` |

Available Since
:   1.5.12

### POST /2.0/pages/publishPageDraft

Publish a page draft as is.

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | query | Page Code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.12

### POST /2.0/pages/reloadPageLayout

Reload page layout. In order to work it properly, de page must have a current draft.
Call 'publishPageDraft' if you got and an error.

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | query | Page Code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### PUT /2.0/pages/disable/{pageCode}

Disable a page: it's impossible to access that page, but it still exists.  
You can use the enable method to make it available again.  
Important: You need to have permission to DELETE PAGES to disable a page.

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | path | Page Code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### PUT /2.0/pages/enable/{pageCode}

Enable a previous disabled page, to make it available again.  
Important: You need to have permission to DELETE PAGES to enable a page.

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | path | Page Code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.8

### GET /2.0/pages/getWidgetPreferences/{instanceId}

Retrieve a map with preferences of a widget instance

Available Since
:   1.5.8

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| instanceId | path | The widget instance id to get preferences | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method returns a map with preferences of a widget instance  { "content": { "dataKey1": "widget-preference-1", "dataKey2": "widget-preference-2" }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5

### PUT /2.0/pages/hide/{pageCode}

Set a page visibility status to HIDDEN

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | path | Page Code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### GET /2.0/pages/mobileMapping/{pageCode}

Returns mobile rendering capabilities of a page and their respective widgets

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content": { "code": "home", "title": "Home", "widgets": [{ "id": 1297, "slot": "SlotA", "order": 1, "code": "html_editor", "mobileEnabled": true }, { "id": 1298, "slot": "SlotB", "order": 1, "code": "html_editor", "mobileEnabled": false }], "mobileEnabled": true }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5.12

### GET /2.0/pages/pageHistory/{pageCode}

Available Since
:   1.5.12

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### PUT /2.0/pages/show/{pageCode}

Set a page visibility status to SHOW

Request Parameters

| name | type | description |
| --- | --- | --- |
| pageCode | path | Page Code |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5

### POST /2.0/pages/updateWidgetMobileStatus/{instanceId}

Update mobile rendering status of a page widget instance

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| instanceId | path | Widget Instance | long |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | boolean (JSON) | New status for mobile rendering |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |
