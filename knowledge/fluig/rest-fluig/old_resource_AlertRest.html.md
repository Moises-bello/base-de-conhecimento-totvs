---
content_hash: c24af041bac523cd816532433652925e8fc787db4e1330048cfb485a5c4537e2
fetched_at: '2026-11-03T14:34:39.288619+00:00'
page_id: resource_AlertRest
product: fluig
source: rest-fluig
title: Fluig REST — AlertRest Resource
type: documentation
url: https://api.fluig.com/old/resource_AlertRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# AlertRest Resource

Notification - V2

Available Since
:   1.5.12

### GET /2.0/notification/countUnreadAlerts

Counts the unread alerts.

Available Since
:   1.5.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content":"12", "message":{ "message":"OK", "detail":"OK", "type":"INFO" } }` |

Available Since
:   1.5.8

### GET /2.0/notification/getTenantTotalOfNotification

Get the number of notification in the tenant

Available Since
:   1.5.8

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method return a Long and successful message  { "content": 0, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.8

### GET /2.0/notification/listAlertsWithAction

It gets the notifications with associated action ordered by creation date

Available Since
:   1.5.8

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`[{"content": { "id" : "1", // Alert's id "senders" : [{ "id": "1", "login" : "user.login", "fullName" : "The Full User Name" }], // It represents the senders "event" : { "id" : "2", // Event's id "eventKey" : "EV-KEY", // The key if the event "description" : "KEY-GENERATED", // event description "singleDescription" : "Single Desc", // the single description "groupDescription" : "Group Desc", // the group description "icon" : "/home/icons/", // icon path "grouped" : "false", // if is grouped "canRemove" : "false", // if can be removed "onlyAdmin" : "false", // if is only for Admins "module" : { "id" : "3", // module's id "moduleKey" : "MOD-KEY", // The Module Key "description" : "Description 003", // The module description } // module object }, // event object "object" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object alert embedded in an alert "place" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object place embedded in an alert "read" : "true", // if this alert was read "canRemove" : "true", // if this alert can be removed "creationDate" : "01/01/2014", // the creation date of the alert "currentDate" : "20/01/2014", // the current date "actions" : [{ "id" : "5", // the action id "actionKey" : "ACT-KEY", // the key action "url" : "www.url.com", // the url of the action "httpMethod" : "POST", // the http method "description" : "Action 005", // The action description "descriptionAfterExec" : "Action 005e", // The action description after execution "actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT "executed" : "true", // if the action was executed "type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE. }], // the action object list }, //Response content "message": null} // Message if returns exception]` |

Available Since
:   1.5.8

### GET /2.0/notification/listAlertsWithNote

It gets the notifications with a note ordered by creation date

Available Since
:   1.5.8

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`[{"content": { "id" : "1", // Alert's id "senders" : [{ "id": "1", "login" : "user.login", "fullName" : "The Full User Name" }], // It represents the senders "event" : { "id" : "2", // Event's id "eventKey" : "EV-KEY", // The key if the event "description" : "KEY-GENERATED", // event description "singleDescription" : "Single Desc", // the single description "groupDescription" : "Group Desc", // the group description "icon" : "/home/icons/", // icon path "grouped" : "false", // if is grouped "canRemove" : "false", // if can be removed "onlyAdmin" : "false", // if is only for Admins "module" : { "id" : "3", // module's id "moduleKey" : "MOD-KEY", // The Module Key "description" : "Description 003", // The module description } // module object }, // event object "object" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object alert embedded in an alert "place" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object place embedded in an alert "read" : "true", // if this alert was read "canRemove" : "true", // if this alert can be removed "creationDate" : "01/01/2014", // the creation date of the alert "currentDate" : "20/01/2014", // the current date "actions" : [{ "id" : "5", // the action id "actionKey" : "ACT-KEY", // the key action "url" : "www.url.com", // the url of the action "httpMethod" : "POST", // the http method "description" : "Action 005", // The action description "descriptionAfterExec" : "Action 005e", // The action description after execution "actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT "executed" : "true", // if the action was executed "type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE. }], // the action object list }, //Response content "message": null} // Message if returns exception]` |

Available Since
:   1.5.8

### GET /2.0/notification/listAllAlerts

It gets all notifications ordered by creation date

Available Since
:   1.5.8

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`[{"content": { "id" : "1", // Alert's id "senders" : [{ "id": "1", "login" : "user.login", "fullName" : "The Full User Name" }], // It represents the senders "event" : { "id" : "2", // Event's id "eventKey" : "EV-KEY", // The key if the event "description" : "KEY-GENERATED", // event description "singleDescription" : "Single Desc", // the single description "groupDescription" : "Group Desc", // the group description "icon" : "/home/icons/", // icon path "grouped" : "false", // if is grouped "canRemove" : "false", // if can be removed "onlyAdmin" : "false", // if is only for Admins "module" : { "id" : "3", // module's id "moduleKey" : "MOD-KEY", // The Module Key "description" : "Description 003", // The module description } // module object }, // event object "object" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object alert embedded in an alert "place" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object place embedded in an alert "read" : "true", // if this alert was read "canRemove" : "true", // if this alert can be removed "creationDate" : "01/01/2014", // the creation date of the alert "currentDate" : "20/01/2014", // the current date "actions" : [{ "id" : "5", // the action id "actionKey" : "ACT-KEY", // the key action "url" : "www.url.com", // the url of the action "httpMethod" : "POST", // the http method "description" : "Action 005", // The action description "descriptionAfterExec" : "Action 005e", // The action description after execution "actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT "executed" : "true", // if the action was executed "type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE. }], // the action object list }, //Response content "message": null} // Message if returns exception]` |

Available Since
:   1.5.12

### GET /2.0/notification/listAllAlertsByModule

It gets all notifications by module ordered by creation date

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| module | query | module of notification |  |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):`[{"content": { "id" : "1", // Alert's id "senders" : [{ "id": "1", "login" : "user.login", "fullName" : "The Full User Name" }], // It represents the senders "event" : { "id" : "2", // Event's id "eventKey" : "EV-KEY", // The key if the event "description" : "KEY-GENERATED", // event description "singleDescription" : "Single Desc", // the single description "groupDescription" : "Group Desc", // the group description "icon" : "/home/icons/", // icon path "grouped" : "false", // if is grouped "canRemove" : "false", // if can be removed "onlyAdmin" : "false", // if is only for Admins "module" : { "id" : "3", // module's id "moduleKey" : "MOD-KEY", // The Module Key "description" : "Description 003", // The module description } // module object }, // event object "object" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object alert embedded in an alert "place" : { "id" : "4", // the alert object id "objectId" : "004", // the object identifier "objectClass" : "com.fluig.alert.Class", // the object class full name "typeDescription" : "Desc 004", // type description "description" : "Desc 004", // description "objectDetail" : "", // details "link" : "www.link.com" // object link }, // it represents an object place embedded in an alert "read" : "true", // if this alert was read "canRemove" : "true", // if this alert can be removed "creationDate" : "01/01/2014", // the creation date of the alert "currentDate" : "20/01/2014", // the current date "actions" : [{ "id" : "5", // the action id "actionKey" : "ACT-KEY", // the key action "url" : "www.url.com", // the url of the action "httpMethod" : "POST", // the http method "description" : "Action 005", // The action description "descriptionAfterExec" : "Action 005e", // The action description after execution "actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT "executed" : "true", // if the action was executed "type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE. }], // the action object list }, //Response content "message": null} // Message if returns exception]` |

Available Since
:   1.5.12

### POST /2.0/notification/markAlertAsRead

Marks the given alerts as read.

Available Since
:   1.5.12

Request Body

| media type | data type |
| --- | --- |
| application/json | [MarkAlertAsReadVO](https://api.fluig.com/old/json_MarkAlertAsReadVO.html) (JSON) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### POST /2.0/notification/markAllAlertsAsRead

Marks all the given alerts as read.

Available Since
:   1.5.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content":"OK", "message":{ "message":"OK", "detail":"OK", "type":"INFO" } }` |

Available Since
:   1.5.12

### POST /2.0/notification/removeAlerts

Removes the given alerts.

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RemoveAlertsVO](https://api.fluig.com/old/json_RemoveAlertsVO.html) (JSON) | Request JSON (example):`{ "alertsId" : ["1","2"], // REQUIRED the id alerts list }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### POST /2.0/notification/saveConfiguration

Save notifications config.

Available Since
:   1.5.12

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AlertConfigVO](https://api.fluig.com/old/json_AlertConfigVO.html) (JSON) | Request JSON (example):`{ "eventKey" : "DOCUMENT_APPROVAL_PENDING", "applicationKey" : "MailSender", // Options: MailSender, PushSender and FLUIG_ALERT_CENTRAL "wantReceive" : 0 // 0 - Disable, 1 - Enable }` |
| application/xml | [alertConfigVO](https://api.fluig.com/old/xml_ns0_alertConfigVO.html) (XML) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content":"OK", "message":{ "message":"OK", "detail":"OK", "type":"INFO" } }` |
