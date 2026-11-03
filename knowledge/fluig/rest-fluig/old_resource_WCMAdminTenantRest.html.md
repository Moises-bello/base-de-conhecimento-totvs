---
content_hash: 5ba2aa8e028712cfd129d5da0e235ae4fedf74c52e1b6d602b2e4738ed738934
fetched_at: '2026-11-03T14:34:40.465745+00:00'
page_id: resource_WCMAdminTenantRest
product: fluig
source: rest-fluig
title: Fluig REST — WCMAdminTenantRest Resource
type: documentation
url: https://api.fluig.com/old/resource_WCMAdminTenantRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# WCMAdminTenantRest Resource

Tenants

Available Since
:   1.4.8

### GET /admin/tenant

Get tenant info

Available Since
:   1.4.8

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content":{  		"id":56987,  		"code":"company",  		"federalId":"company",  			"UUID":"xxxx-xxxxx-xxxx-xxxx",  		"idpId":null,  		"description":"company",  		"organizationUrl":"http://totvs.com",  		"data":{  			"key":"value" // Teant Data  		},  		"adminUser":null,  		"products":[  			"ECM",  			"social_application"  		],  		"idpLogOff":false,  		"thumbnailEnabled":false,  		"removeVolume":false  	},  	"message":null  } ``` |

Available Since
:   1.4.1

### POST /admin/tenant

Create a new tenant

Available Since
:   1.4.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [TenantVO](https://api.fluig.com/old/json_TenantVO.html) (JSON) | REQUIRED Request JSON (example):  ```  {  	 "id" ; 100, // tenant's id  	 "code" : "community01", //tenant's code  	 "federalId" : "123", // tenant's federal id  	 "idpId" : "5zi7mbx6hw8a60h61412167955790", // fluig identity id  	 "description" : "My Company", // tenant's description  	 "organizationUrl" : "http://www.mycompany.com", // tenant's website  	 "defaultDir" : "/mnt01/myvolume", // tenant's repository  	 "idpLogOff" : false, // do fluig identiy logoff during fluig client logoff?  	 "thumbnailEnabled" : false, // to generate thumbnais for images and videos  	 "adminUser" : {  		 "login" : "john", // administrator's login  		 "password" : "doe", // administrator's password  		 "firstName" : "John", // administrator's firstName  		 "lastName" : "Doe", // administrator's lastName  		 "email" : "john@mycompany.com", // administrator's email  	}  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.4.1

### POST /admin/tenant/analytics

Configures analytics for a tenant

Available Since
:   1.4.1

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AnalyticsVO](https://api.fluig.com/old/json_AnalyticsVO.html) (JSON) | REQUIRED Request JSON (example):  ```  {  	 "tenantId" : 100, // tenant's id  	 "projectId" : "123456", //tenant's projectId at GoodData  	 "user" : "johndoe", // GoodData user  	 "password" : "1412167955790", // GoodData password  	 "active" : "true" // Is analytics active?  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.5.12

### POST /admin/tenant/disableFluigViewerCloud

Disable fluig viewer cloud

Available Since
:   1.5.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.4.5

### POST /admin/tenant/emailConfig

This method has been deprecated.

Configures the SMTP Server for a tenant

Available Since
:   1.4.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [EMailConfigVO](https://api.fluig.com/old/json_EMailConfigVO.html) (JSON) | REQUIRED Request JSON (example):  ```  {  	 "tenantId" : 100, // tenant's id  	 "smtpServer" : "smtp.mycompany.com", // tenant's smtp server  	 "smtpPort" : 25, // tenant's smtp port  	 "emailFrom" : "fluig@mycompany.com", //Default email from  	 "emailSecurity" : "none"/"tls"/"ssl", // Security type used by smtp server  	 "user" : "john", // SMTP Server user  	 "password" : "doe" // SMTP Server password  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.5.7

### POST /admin/tenant/enableFluigViewerCloud

Enable fluig viewer cloud

Available Since
:   1.5.7

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### GET /admin/tenant/fluigViewerCloudEnabled

Returns true or false whether fluig viewer cloud is enabled/disabled

Available Since
:   1.5.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content":{ "tenantId":"123", "key":"internalVisualizerService", "fluigViewerCloudEnabled":"true", } }` |

Available Since
:   1.4.1

### GET /admin/tenant/getEmailConfig

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| tenantId | query |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |

Available Since
:   1.5.0

### GET /admin/tenant/identityConfig

Configures Fluig Identity for a tenant

Available Since
:   1.5.0

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| tenantid | query |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Request JSON (example):  ```  {  	 "tenantId" : 100, // tenant's id  	 "enabled" : true, // is identity enabled?  	 "justInTimeProvisioning" : "true", // to provisioning users  	 "ignoreSSLValidation" : "true", // to ignore ssl validations  	 "clockSkew" : "10800", // variation of servers clock  	 "spIssuerName" : "TotvsLabs", // service provider issuer name  	 "providerName" : "TotvsLabs", // provider's name  	 "spProtocolBinding" : "HttpPost", // service provider protocol bindind  	 "idpProtocolBinding" : "HttpPost", // identity protocol binding  	 "acsURL" : "http://127.0.0.1:8080/portal/idp/ACS", // ACS url  	 "idpDestination" : "https://mycompany.thecloudpass.com/cloudpass/SPInitPost/receiveSSORequest/n3m111nv0y25wyra1412341234937/42", // identity URL destination  	 "idpDomain" : "mycompany.thecloudpass.com", // identity tenant's domain  	 "certificateFile" : "/fluig/certs/mycompany.thecloudpass.com.crt", // certificate file  	 "nameIdFormat" : "transient", // name id format  	 "idpIssuerName" : "TotvsLabs", // identity Issuer Name  	 "idpCertIssuerName" : "TotvsLabs", // identity certificate issuer name  	 "homePageURL" : "https://mycompany.thecloudpass.com/cloudpass/", // cloudpass home page  	 "logoutURL" : "https://mycompany.thecloudpass.com/cloudpass/login/logout", // logout URL  	 "apiURL" : "https://mycompany.thecloudpass.com", // cloudpass home  	 "authorization" : "IDM_URL", // authorization type  	 "apiClientKey" : "0f621b6c-1d22-465b-aa1c-b829bd912222", // tenant's client key  	 "configurationToken" : "NDI6Om4zbTQxMG52MHkyNXd5cmExNDE2OTQ1MjE0OTM3" // identity application configuration token  } ``` |

Available Since
:   1.5.0

### POST /admin/tenant/identityConfig

Configures Fluig Identity for a tenant

Available Since
:   1.5.0

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [IdentityVO](https://api.fluig.com/old/json_IdentityVO.html) (JSON) | REQUIRED Request JSON (example):  ```  {  	 "tenantId" : 100, // tenant's id  	 "enabled" : true, // is identity enabled?  	 "justInTimeProvisioning" : "true", // to provisioning users  	 "ignoreSSLValidation" : "true", // to ignore ssl validations  	 "clockSkew" : "10800", // variation of servers clock  	 "spIssuerName" : "TotvsLabs", // service provider issuer name  	 "providerName" : "TotvsLabs", // provider's name  	 "spProtocolBinding" : "HttpPost", // service provider protocol bindind  	 "idpProtocolBinding" : "HttpPost", // identity protocol binding  	 "acsURL" : "http://127.0.0.1:8080/portal/idp/ACS", // ACS URL  	 "idpDestination" : "https://mycompany.thecloudpass.com/cloudpass/SPInitPost/receiveSSORequest/n3m111nv0y25wyra1412341234937/42", // identity URL destination  	 "idpDomain" : "mycompany.thecloudpass.com", // identity tenant's domain  	 "certificateFile" : "/fluig/certs/mycompany.thecloudpass.com.crt", // certificate file  	 "nameIdFormat" : "transient", // name id format  	 "idpIssuerName" : "TotvsLabs", // identity Issuer Name  	 "idpCertIssuerName" : "TotvsLabs", // identity certificate issuer name  	 "homePageURL" : "https://mycompany.thecloudpass.com/cloudpass/", // cloudpass home page  	 "logoutURL" : "https://mycompany.thecloudpass.com/cloudpass/login/logout", // logout URL  	 "apiURL" : "https://mycompany.thecloudpass.com", // cloudpass home  	 "authorization" : "IDM_URL", // authorization type  	 "apiClientKey" : "0f621b6c-1d22-465b-aa1c-b829bd912222", // tenant's client key  	 "configurationToken" : "NDI6Om4zbTQxMG52MHkyNXd5cmExNDE2OTQ1MjE0OTM3" // identity application configuration token  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.5.6

### POST /admin/tenant/updateMailConfig

Configures the SMTP Server for a tenant

Available Since
:   1.5.6

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [MailConfigurationVO](https://api.fluig.com/old/json_MailConfigurationVO.html) (JSON) | REQUIRED Request JSON (example):  ```  {  	 "tenantId" : 100, // tenant's id  	 "enabled" : 100, // tenant's id  	 "host" : "smtp.mycompany.com", // tenant's smtp server  	 "port" : 25, // tenant's smtp port  	 "from" : "fluig@mycompany.com", //Default email from  	 "security" : "true", // if use tls  	 "authentication" : "true", // if smtp server has security and requires user and password  	 "user" : "john", // SMTP Server user  	 "password" : "doe" // SMTP Server password  } ``` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | ``` This method just return HTTP 200 status ``` |

Available Since
:   1.5.12

### POST /admin/tenant/disableFluigViewerCloud/{tenantId}

Disable fluig viewer cloud by tenant id

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| tenantId | path |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### POST /admin/tenant/enableFluigViewerCloud/{tenantId}

Enable fluig viewer cloud by tenant id

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| tenantId | path |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.12

### GET /admin/tenant/fluigViewerCloudEnabled/{tenantId}

Returns true or false whether fluig viewer cloud is enabled/disabled

Available Since
:   1.5.12

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| tenantId | path |  | long |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):`{ "content":{ "tenantId":"123", "key":"internalVisualizerService", "fLuigViewerCloudEnabled":"true", } }` |

Available Since
:   1.5.11

### POST /admin/tenant/identityConfig/v2

Available Since
:   1.5.11

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| configurationToken | query | identity application configuration token (Ex: "NDI6Om4zbTQxMG52MHkyNXd5cmExNDE2OTQ1MjE0OTM3"). |  |
| enableIdentity | query | ('true' to enable / 'false' to disable). Default: false. | boolean |
| identityUrl | query | Itentity Base URL |  |
| tenantCode | query |  |  |
| tenantId | query |  | long |
| useJustInTimeProvisioning | query | to provisioning users (true / false). Default: false. | boolean |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |
