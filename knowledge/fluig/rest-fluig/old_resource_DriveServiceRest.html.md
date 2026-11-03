---
content_hash: 2b598b01fa5d1bdd6af222c569a031a8423611f9bb0d5ff53765d6b7323ecc8b
fetched_at: '2026-11-03T14:34:39.765304+00:00'
page_id: resource_DriveServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — DriveServiceRest Resource
type: documentation
url: https://api.fluig.com/old/resource_DriveServiceRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# DriveServiceRest Resource

Fluig Connect

### GET /ecm/connect/config

Get fluig connect startup configuration

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | Response JSON (example):  ```  {  	"content": {  	"tenantId" : "1",//Tenant's id  	"tenantCode" : "demo",	//Tenant's code  	"enabled" : "true",	//Whether or not fluig connect is enabled  	"hasPermissionDrive" : "true",	//Whether or not the user has permission to use fluig connect  	"hasPermissionEndpoints" : "true",	//Whether or not the user receives notifications on fluig connect  	"hasSyncPermission" : "true",	//Whether or not the user has sync feature enabled  	"endpointAddress" : "www.demo.com",	//Address for receiving endpoint notifications  },  message: "" } ``` |
