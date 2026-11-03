---
content_hash: 4faead05e33a5a9ef4b5ad716417211f7551ca03530ad5823e4b5bdfc766daf3
fetched_at: '2026-11-03T14:34:40.025631+00:00'
page_id: resource_PermissionRest
product: fluig
source: rest-fluig
title: Fluig REST — PermissionRest Resource
type: documentation
url: https://api.fluig.com/old/resource_PermissionRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# PermissionRest Resource

Permission

Available Since
:   1.5.13

### GET /2.0/permission/listall/widgets

List permission of all widgets.

Available Since
:   1.5.13

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content": [ { "Permissions": { "widgetEdit": { "Permission": "permission.widget.edit", "Role": "user", "User": "", "Group": "" }, "widgetPageAdd": { "Permission": "permission.widget.pageadd", "Role": "user", "User": "", "Group": "" }, "widgetView": { "Permission": "permission.widget.view", "Role": "user", "User": "", "Group": "" } }, "Title": "Mural", "Visible?": false, "Code": "ecm_shareplace", "Description": "Mural", "Mobile?": false }, ... { "Permissions": { "widgetEdit": { "Permission": "permission.widget.edit", "Role": "user", "User": "", "Group": "" }, "widgetPageAdd": { "Permission": "permission.widget.pageadd", "Role": "user", "User": "", "Group": "" }, "widgetView": { "Permission": "permission.widget.view", "Role": "user", "User": "", "Group": "" } }, "Title": "Ajuda", "Visible?": false, "Code": "ecm_help", "Description": "Ajuda fluig", "Mobile?": false } ], "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5.13

### GET /2.0/permission/find/widget/{widgetCode}

Finds all current widget permission.

Available Since
:   1.5.13

Request Parameters

| name | type | description |
| --- | --- | --- |
| widgetCode | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `{ "content": { "widgetEdit": { "Permission": "permission.widget.edit", "Role": "user", "User": "", "Group": "" }, "widgetPageAdd": { "Permission": "permission.widget.pageadd", "Role": "user", "User": "", "Group": "" }, "widgetView": { "Permission": "permission.widget.view", "Role": "user", "User": "", "Group": "" } }, "message": { "message": "OK", "detail": "OK", "type": "INFO", "errorCode": null } }` |

Available Since
:   1.5.13

### POST /2.0/permission/grantdefault/widget/{widgetCode}

Grants all widget permission to default.
Requires the tenant admin role.

Available Since
:   1.5.13

Request Parameters

| name | type | description |
| --- | --- | --- |
| widgetCode | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |
| application/xml | anyType (XML) |

Available Since
:   1.5.13

### POST /2.0/permission/revoke/widget/{widgetCode}

Revoke all widget permission.
Requires the tenant admin role.

Available Since
:   1.5.13

Request Parameters

| name | type | description |
| --- | --- | --- |
| widgetCode | path |  |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) |  |
| application/xml | anyType (XML) |
