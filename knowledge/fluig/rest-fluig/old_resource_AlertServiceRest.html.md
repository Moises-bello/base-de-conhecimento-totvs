---
content_hash: 3f7f5284dd4b6db6f7270f8b1134a2d9a6e67b626004c3c812f2c094ce824626
fetched_at: '2026-11-03T14:34:39.339425+00:00'
page_id: resource_AlertServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — AlertServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_AlertServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# AlertServiceRest Resource

Notifications

### POST /alert/customEmailSender

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | Request JSON (example):  ```  {  	"to" : "user1@empresa.com;user2@empresa.com", //emails of recipients separated by ";"  	"from" : "admin@empresa.com", // sender  	"subject" : "teste", //   subject  	 "templateId" : "teste", // Email template Id previously registered  	 "dialectId"  : "pt_BR", //Email dialect , if not informed receives pt_BR , email dialect ("pt_BR", "en_US", "es")  	 "param" : {} //  Map with variables to be replaced in the template  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/action/execute

This method has been deprecated. Use /action/execute/v2 instead.

Execute an action of an alert.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AlertActionVO](https://api.fluig.com/old/json_AlertActionVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10" // the action id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` A plain boolean value that indicates if the action has been executed successfully ``` |

Available Since
:   1.3.0

### GET /alert/alerts/countUnread

This method has been deprecated. Use /alerts/countUnread/v2 instead.

Counts the unread alerts.

Available Since
:   1.3.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` A plain numeric value ``` |

### GET /alert/appSender/findVoList

List the applications that send alerts.

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [AlertAppSenderVO](https://api.fluig.com/old/json_AlertAppSenderVO.html) (JSON) | Response List of JSON (example):  ```  {  	"id" : "7", // application sender id  	"applicationKey" : "PROCESSOS", // application unique key  	"description" : "Processos", // application description  	"tenantId" : "1" // the tenant id  } ``` |

### POST /alert/appSender/registerApp

This method has been deprecated. on 1.3.6

Register an application to send alerts.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RegisterApplicationVO](https://api.fluig.com/old/json_RegisterApplicationVO.html) (JSON) | Request JSON (example):  ```  {  	"applicationKey" : "SampleApp", // Application logic name. Unique key for system identification.  	"descriptionKey" : "SampleApp", // key for search a description in I18n  	"jndiName" : "java:global/system/module/submodule/Class" // JNDI to do the lookup to EJB that implements AlertSenderApp interface.  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.6

### POST /alert/appSender/registerApplication

Register an application to send alerts.

Available Since
:   1.3.6

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RegisterApplicationVO](https://api.fluig.com/old/json_RegisterApplicationVO.html) (JSON) | Request JSON (example):  ```  {  	"applicationKey" : "SampleApp", // Application logic name. Unique key for system identification.  	"descriptionKey" : "SampleApp", // key for search a description in I18n  	"jndiName" : "java:global/system/module/submodule/Class" // JNDI to do the lookup to EJB that implements AlertSenderApp interface.  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.3

### GET /alert/application/actives

Return all actives sender applications.

Available Since
:   1.4.3

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {  	"content":[{"id":4044,"applicationKey":"FLUIG_ALERT_CENTRAL","description":"Fluig","tenantId":1}], // Sender application  	"message": "OK" // Messsage  }] ``` |

### POST /alert/application/enable

Activate or disable an application.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ActivateApplicationVO](https://api.fluig.com/old/json_ActivateApplicationVO.html) (JSON) | Request JSON (example):  ```  {  	"appKey" : "EVT-KEY", // Unique key that represents the application  	"active" : "true" // Indicates if this application will be enable or disable  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.6

### POST /alert/event/changeStatus

Activate or disable an event.

Available Since
:   1.3.6

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ActivateEventVO](https://api.fluig.com/old/json_ActivateEventVO.html) (JSON) | Request JSON (example):  ```  {  	"eventKey" : "EVT-KEY", // Unique key that represents the event  	"active" : "true" // Indicates if this event will be enable or disable  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/event/createEvent

It creates a new event to generate alerts and also creates default configuration for all users who matter use this event
  
**OBS:** Only tenant administrator user is allowed to call this procedure.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CreateEventVO](https://api.fluig.com/old/json_CreateEventVO.html) (JSON) | Request JSON (example):  ```  {  	"eventKey" : "EVT-KEY", // Unique key that represents the event  	"required" : "false", // It indicates if this event is required. If true, the user cannot configure to do not receive alerts about this event  	"descriptionKey" : "EVT-KEY-DESC", // Key used to obtain the description in I18n  	"singleDescriptionKey" : "EVT-KEY-SINGLE-DESC", // Key used to obtain the description of the user's action in I18n  	"groupDescriptionKey" : "EVT-KEY-GROUP-DESC", // Key used to obtain the description of the multi user's action in I18n  	"eventIcon" : "", // the event icon  	"moduleId" : "Processos", // Module of this event belongs  	"grouped" : "false", // It indicates if the alert can be grouped by action and object  	"canRemove" : "false", // It indicates if the alert can be removed  	"removeAfterExecAction" : "true", // It indicates if the alert will be removed after execute the action  	"onlyAdmin" : "false", // It indicates if this event is valid only for admin users  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/event/enable

This method has been deprecated. on 1.3.6

Activate or disable an event.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [ActivateEventVO](https://api.fluig.com/old/json_ActivateEventVO.html) (JSON) | Request JSON (example):  ```  {  	"eventKey" : "EVT-KEY", // Unique key that represents the event  	"active" : "true" // Indicates if this event will be enable or disable  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### GET /alert/event/eventsByModule

Returns the alert events of a given module.

Request Parameters

| name | type | description |
| --- | --- | --- |
| moduleKey | query | REQUIRED module's key |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [AlertEventVO](https://api.fluig.com/old/json_AlertEventVO.html) (JSON) | Response List of JSON (example):  ```  {  	"id" : "8", // Event id  	"eventKey" : "EVT-KEY", // Unique key that represents the event  	"descriptionKey" : "EVT-KEY-DESC", // Key used to obtain the description in I18n  	"singleDescriptionKey" : "EVT-KEY-SINGLE-DESC", // Key used to obtain the description of the user's action in I18n  	"groupDescriptionKey" : "EVT-KEY-GROUP-DESC", // Key used to obtain the description of the multi user's action in I18n  	"icon" : "", // the event icon  	"grouped" : "false", // It indicates if the alert can be grouped by action and object  	"canRemove" : "false", // It indicates if the alert can be removed  	"onlyAdmin" : "false", // It indicates if this event is valid only for admin users  	"module" : {  		"id" : "1", // the module id  		"moduleKey" : "MOD-KEY", // unique key of the module  		"description" : "description Module", // the module description  		"tenantId" : "1" // the tenant id  	} // Module of this event belongs  } ``` |

### POST /alert/module/create

It creates a new module to group alert events.
Note: Only an user with admin privileges can execute this method.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CreateModuleVO](https://api.fluig.com/old/json_CreateModuleVO.html) (JSON) | Request JSON (example):  ```  {  	"moduleKey" : "MOD-KEY", // Unique key that represents the module.  	"descriptionKey" : "module.custom.description" //The description key. If a key is given, it should be registered in the i18n service to be translated according to user's language. This attribute can be a plain text. In this case, the module's name will not be translated.  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### GET /alert/module/findVoList

Lists the alert modules.

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [AlertModuleVO](https://api.fluig.com/old/json_AlertModuleVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1", // Module's id  	"moduleKey" : "PROCESSOS", // module's key  	"description" : "Processos", // module's description  	"tenantId" : "1" // the tenant id  }] ``` |

Available Since
:   1.3.0

### GET /alert/service/countGroupedUnreadAlerts

This method has been deprecated. Use /service/countGroupedUnreadAlerts/v2 instead.

Counts the unread alerts grouped by modules for the logged user.

Available Since
:   1.3.0

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {  	"name" : "COLABORATION",       // Name of the group  	"description" : "COLABORATION",            // Description of the group  	"quantity" : "12"  // Quantity of alerts of the group  } ``` |

### GET /alert/service/countUnreadAlerts

This method has been deprecated. on 1.3.0

Counts the unread alerts.

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | number (JSON) | ``` A plain numeric value ``` |

### GET /alert/service/findAll

This method has been deprecated. Use /service/findAll/v2 instead.

It gets all the alerts ordered by creation date

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [AlertVO](https://api.fluig.com/old/json_AlertVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1", // Alert's id  	"senders" : [{  		"id": "1",  		"login" : "user.login",  		"fullName" : "The Full User Name"  	}], // It represents the senders  	"event" : {  		"id" : "2", // Event's id  		"eventKey" : "EV-KEY", // The key if the event  		"description" : "KEY-GENERATED", // event description  		"singleDescription" : "Single Desc", // the single description  		"groupDescription" : "Group Desc", // the group description  		"icon" : "/home/icons/", // icon path  		"grouped" : "false", // if is grouped  		"canRemove" : "false", // if can be removed  		"onlyAdmin" : "false", // if is only for Admins  		"module" : {  			"id" : "3", // module's id  			"moduleKey" : "MOD-KEY", // The Module Key  			"description" : "Description 003", // The module description  		} // module object  	}, // event object  	"object" : {  		"id" : "4", // the alert object id  		"objectId" : "004", // the object identifier  		"objectClass" : "com.fluig.alert.Class", // the object class full name  		"typeDescription" : "Desc 004", // type description  		"description" : "Desc 004", // description  		"objectDetail" : "", // details  		"link" : "www.link.com" // object link  		"note" : "" // the alert note  	}, // it represents an object alert embedded in an alert  	"place" : {  		"id" : "4", // the alert object id  		"objectId" : "004", // the object identifier  		"objectClass" : "com.fluig.alert.Class", // the object class full name  		"typeDescription" : "Desc 004", // type description  		"description" : "Desc 004", // description  		"objectDetail" : "", // details  		"link" : "www.link.com" // object link  		"note" : "" // the alert note  	}, // it represents an object place embedded in an alert  	"read" : "true", // if this alert was read  	"canRemove" : "true", // if this alert can be removed  	"creationDate" : "01/01/2014", // the creation date of the alert  	"currentDate" : "20/01/2014", // the current date  	"actions" : [{  		"id" : "5", // the action id  		"actionKey" : "ACT-KEY", // the key action  		"url" : "www.url.com", // the url of the action  		"httpMethod" : "POST", // the http method  		"description" : "Action 005", // The action description  		"descriptionAfterExec" : "Action 005e", // The action description after execution  		"actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT  		"executed" : "true", // if the action was executed  		"type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE.  	}],	// the action object list  }] ``` |

### POST /alert/service/markAllAsRead

This method has been deprecated. Use /service/markAllAsRead/v2 instead.

Marks all logged user's alerts as read.

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/service/markAsRead

This method has been deprecated. Use /service/markAsRead/v2 instead.

Marks the given alerts as read.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MarkAlertAsReadVO](https://api.fluig.com/old/json_MarkAlertAsReadVO.html) (JSON) | Request JSON (example):  ```  {  	"alertsId" : ["1","2"], //REQUIRED the id alerts list  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/service/removeAlert

Removes the given alert.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RemoveAlertVO](https://api.fluig.com/old/json_RemoveAlertVO.html) (JSON) | Request JSON (example):  ```  {  	"alertId" : "1", //REQUIRED the id alert  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/service/removeAlerts

This method has been deprecated. Use /service/removeAlerts/v2 instead.

Removes the given alerts.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RemoveAlertsVO](https://api.fluig.com/old/json_RemoveAlertsVO.html) (JSON) | Request JSON (example):  ```  {  	"alertsId" : ["1","2"], // REQUIRED the id alerts list  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

### POST /alert/service/sendAlert

This method has been deprecated. 1.3.6

Sends an alert.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SendAlertVO](https://api.fluig.com/old/json_SendAlertVO.html) (JSON) | Request JSON (example):  ```  {  	"eventKey" : "EVT-KEY", //REQUIRED String that represents the event who generates the alert  	"loginReceiver" : "placido.domingos", //REQUIRED User login (alias, idpId or userCode) who will receive the alert  	"object" : {  		"alertObjectId" : "1", // the object id  		"alertObjectClass" : "com.fluig.Class", // the object class full name  		"alertObjectTypeDescriptionKey" : "com.fluig.Class.descKey", // the key for search the object description in I18n  		"alertObjectDescription" : "description 001", // the object description showed in the alert  		"alertObjectLink" : "www.fluig.com", // the link to access the object  		"alertObjectDetailKey" : "" //  		"alertObjectNote" : "" // the alert note  	}, // object used for alert  	"place" : {  		"alertObjectId" : "1", // the object id  		"alertObjectClass" : "com.fluig.Class", // the object class full name  		"alertObjectTypeDescriptionKey" : "com.fluig.Class.descKey", // the key for search the object description in I18n  		"alertObjectDescription" : "description 001", // the object description showed in the alert  		"alertObjectLink" : "www.fluig.com", // the link to access the object  		"alertObjectDetailKey" : "" //  		"alertObjectNote" : "" // the alert note  	}, // object used for place  	"actions" : [{  		"id" : "5", // the action id  		"actionKey" : "ACT-KEY", // the key action  		"url" : "www.url.com", // the url of the action  		"httpMethod" : "POST", // the http method  		"description" : "Action 005", // The action description  		"descriptionAfterExec" : "Action 005e", // The action description after execution  		"actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT  		"executed" : "true", // if the action was executed  		"type" : "HTTP" // the type of the action. it can be JMS, HTTP or NONE.  	}],	// the action object list  	"metadata" : {"KEY" : "VALUE"} // is a key-value map-list for metadata  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.3.6

### POST /alert/service/sendNotification

Sends a notification.

Available Since
:   1.3.6

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [SendAlertVO](https://api.fluig.com/old/json_SendAlertVO.html) (JSON) | Request JSON (example):`{ "eventKey" : "LIKE", //REQUIRED String that represents the event who generates the alert "loginReceiver" : "placido.domingos", //REQUIRED User login (alias, idpId or userCode) who will receive the alert "priority" : "NORMAL", // Options: NONE (Doesn't send notification), LOW, NORMAL and HIGH "object" : { // the object of the alert, such as document, post, image or process "alertObjectId" : "1", // the unique id number of the object "alertObjectTypeDescriptionKey" : "Contract", // description of the object type "alertObjectDescription" : "Agreement document", // the object description showed in the alert "alertObjectLink" : "/ecmnavigation?app_ecm_navigation_doc=7", // the link to access the object "alertObjectDetailKey" : "from last Monday", // (OPTIONAL) details of the key "alertObjectNote" : "Approved by the board members" // (OPTIONAL) the object note for extra information, it allows up to 600 characters }, "place" : { // (OPTIONAL) where the alert took action, such as communities, timeline, and so on... "alertObjectId" : "1", // the unique id number of the object "alertObjectDescription" : "ECM", // where the notification took place "alertObjectLink" : "/ecmnavigation", // the link to access the place where the notification took place "alertObjectDetailKey" : "In the folder 'contracts'" }, "metadata" : {"FIRST-NAME" : "JOHNNY", "SURNAME" : "DEEP"} // (OPTIONAL) is a key-value map-list for metadata. Such metadata are used for the Central Alert, like SMS' and E-mails }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

### POST /alert/action/execute/v2

Execute an action of an alert.

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AlertActionVO](https://api.fluig.com/old/json_AlertActionVO.html) (JSON) | Request JSON (example):  ```  {  	"id" : "10" // the action id  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` A plain boolean value that indicates if the action has been executed successfully ``` |

Available Since
:   1.4.11

### GET /alert/alerts/countUnread/v2

Counts the unread alerts.

Available Since
:   1.4.11

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  {"content": {  "1" //Count  }, "message": null // Message if returns exception  } ``` |

Available Since
:   1.4.3

### GET /alert/application/isActive/{appKey}

Return if the application sender is active.

Available Since
:   1.4.3

Request Parameters

| name | type | description |
| --- | --- | --- |
| appKey | path | Application key |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  [{  	"content" : "true", // The opitions are true and false  	"message" : "OK" // Messsage  }] ``` |

### GET /alert/sender/findSenders/{alertId}

Lists the users who have sent an alert

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alertId | path | REQUIRED alert's id | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | array of [AlertSenderVO](https://api.fluig.com/old/json_AlertSenderVO.html) (JSON) | Response List of JSON (example):  ```  [{  	"id" : "1", // Send Alert's id  	"user" : {  		"id" : "4", // user id  		"login" : "placido.domingos", // user login  		"fullName" : "Placido Domingos" // user full name  	}, // user object  	"creationDate" : "01/01/2014", // alert creation date  	"via" : "" // TODO  }] ``` |

Available Since
:   1.4.11

### GET /alert/service/countGroupedUnreadAlerts/v2

Counts the unread alerts grouped by modules for the logged user.

Available Since
:   1.4.11

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {"content": {  	"name" : "COLABORATION",       // Name of the group  	"description" : "COLABORATION",            // Description of the group  	"quantity" : "12"  // Quantity of alerts of the group  }, //Response content  "message": null} ``` |

Available Since
:   1.4.11

### GET /alert/service/findAll/v2

It gets all the alerts ordered by creation date

Available Since
:   1.4.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| limit | query | limit of records returned | required |
| offset | query | the offset | required |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response List of JSON (example):  ```  [{"content": {  	"id" : "1", // Alert's id  	"senders" : [{  		"id": "1",  		"login" : "user.login",  		"fullName" : "The Full User Name"  	}], // It represents the senders  	"event" : {  		"id" : "2", // Event's id  		"eventKey" : "EV-KEY", // The key if the event  		"description" : "KEY-GENERATED", // event description  		"singleDescription" : "Single Desc", // the single description  		"groupDescription" : "Group Desc", // the group description  		"icon" : "/home/icons/", // icon path  		"grouped" : "false", // if is grouped  		"canRemove" : "false", // if can be removed  		"onlyAdmin" : "false", // if is only for Admins  		"module" : {  			"id" : "3", // module's id  			"moduleKey" : "MOD-KEY", // The Module Key  			"description" : "Description 003", // The module description  		} // module object  	}, // event object  	"object" : {  		"id" : "4", // the alert object id  		"objectId" : "004", // the object identifier  		"objectClass" : "com.fluig.alert.Class", // the object class full name  		"typeDescription" : "Desc 004", // type description  		"description" : "Desc 004", // description  		"objectDetail" : "", // details  		"link" : "www.link.com" // object link  	}, // it represents an object alert embedded in an alert  	"place" : {  		"id" : "4", // the alert object id  		"objectId" : "004", // the object identifier  		"objectClass" : "com.fluig.alert.Class", // the object class full name  		"typeDescription" : "Desc 004", // type description  		"description" : "Desc 004", // description  		"objectDetail" : "", // details  		"link" : "www.link.com" // object link  	}, // it represents an object place embedded in an alert  	"read" : "true", // if this alert was read  	"canRemove" : "true", // if this alert can be removed  	"creationDate" : "01/01/2014", // the creation date of the alert  	"currentDate" : "20/01/2014", // the current date  	"actions" : [{  		"id" : "5", // the action id  		"actionKey" : "ACT-KEY", // the key action  		"url" : "www.url.com", // the url of the action  		"httpMethod" : "POST", // the http method  		"description" : "Action 005", // The action description  		"descriptionAfterExec" : "Action 005e", // The action description after execution  		"actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT  		"executed" : "true", // if the action was executed  		"type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE.  	}], // the action object list  }, //Response content  "message": null} // Message if returns exception] ``` |

### GET /alert/service/findById/{alertId}

/\*\*
Finds an alert by its id.

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| alertId | path | - id do alerta | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AlertVO](https://api.fluig.com/old/json_AlertVO.html) (JSON) | Alert Object of JSON (example):  ```  {  	"id" : "1", // Alert's id  	"senders" : [{  		"id": "1",  		"login" : "user.login",  		"fullName" : "The Full User Name"  	}], // It represents the senders  	"event" : {  		"id" : "2", // Event's id  		"eventKey" : "EV-KEY", // The key if the event  		"description" : "KEY-GENERATED", // event description  		"singleDescription" : "Single Desc", // the single description  		"groupDescription" : "Group Desc", // the group description  		"icon" : "/home/icons/", // icon path  		"grouped" : "false", // if is grouped  		"canRemove" : "false", // if can be removed  		"onlyAdmin" : "false", // if is only for Admins  		"module" : {  			"id" : "3", // module's id  			"moduleKey" : "MOD-KEY", // The Module Key  			"description" : "Description 003", // The module description  			"tenantId" : "1" // The Tenant Id  		} // module object  	}, // event object  	"object" : {  		"id" : "4", // the alert object id  		"objectId" : "004", // the object identifier  		"objectClass" : "com.fluig.alert.Class", // the object class full name  		"typeDescription" : "Desc 004", // type description  		"description" : "Desc 004", // description  		"objectDetail" : "", // details  		"link" : "www.link.com" // object link  		"note" : "", // the alert note  	}, // it represents an object alert embedded in an alert  	"place" : {  		"id" : "4", // the alert object id  		"objectId" : "004", // the object identifier  		"objectClass" : "com.fluig.alert.Class", // the object class full name  		"typeDescription" : "Desc 004", // type description  		"description" : "Desc 004", // description  		"objectDetail" : "", // details  		"link" : "www.link.com" // object link  		"note" : "", // the alert note  	}, // it represents an object place embedded in an alert  	"read" : "true", // if this alert was read  	"canRemove" : "", // if this alert can be removed  	"creationDate" : "", // the creation date of the alert  	"currentDate" : "", // the current date  	"actions" : [{  		"id" : "5", // the action id  		"actionKey" : "ACT-KEY", // the key action  		"url" : "www.url.com", // the url of the action  		"httpMethod" : "POST", // the http method  		"description" : "Action 005", // The action description  		"descriptionAfterExec" : "Action 005e", // The action description after execution  		"actionType" : "MAIN", // the type of the action. it can be MAIN or DEFAULT  		"executed" : "true", // if the action was executed  		"type" : "HTTP", // the type of the action. it can be JMS, HTTP or NONE.  	}],	// the action object list  } ``` |

Available Since
:   1.4.11

### POST /alert/service/markAllAsRead/v2

Marks all logged user's alerts as read.

Available Since
:   1.4.11

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ```  This method just return HTTP 200 status ``` |

Available Since
:   1.4.11

### POST /alert/service/markAsRead/v2

Marks the given alerts as read.

Available Since
:   1.4.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MarkAlertAsReadVO](https://api.fluig.com/old/json_MarkAlertAsReadVO.html) (JSON) | Request JSON (example):  ```  {  	"alertsId" : ["1","2"], //REQUIRED the id alerts list  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.11

### POST /alert/service/removeAlerts/v2

Removes the given alerts.

Available Since
:   1.4.11

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [RemoveAlertsVO](https://api.fluig.com/old/json_RemoveAlertsVO.html) (JSON) | Request JSON (example):  ```  {  	"alertsId" : ["1","2"], // REQUIRED the id alerts list  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |
