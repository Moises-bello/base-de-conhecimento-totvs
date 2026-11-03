---
content_hash: d1421d536391b4fd1bf0b958723a812ce9e51fde698802a19d76c42be9f23b5e
fetched_at: '2026-11-03T14:34:39.494707+00:00'
page_id: resource_CommunityRest
product: fluig
source: rest-fluig
title: Fluig REST — CommunityRest Resource
type: documentation
url: https://api.fluig.com/old/resource_CommunityRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# CommunityRest Resource

Community

Available Since
:   1.5.9

### POST /2.0/communities/addUsers

Add an user to a community  
  
Create a new community: fill object AddUserToCommunityVO

Available Since
:   1.5.9

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [AddUserToCommunityVO](https://api.fluig.com/old/json_AddUserToCommunityVO.html) (JSON) | Request JSON (example):`{ "communityAlias" : "community.alias", // community alias "userAliases" : ["user1","user2"] // user aliases }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "message": { "message": "User successfully added", "detail": "User successfully added", "type": "INFO" } }` |

Available Since
:   1.5

### POST /2.0/communities/create

Create a community  
  
Create a new community: fill object CommunityCreateVO

Available Since
:   1.5

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommunityCreateVO](https://api.fluig.com/old/json_CommunityCreateVO.html) (JSON) | Request JSON (example):`{ "alias" : "alias.community", // Alias Communit "name" : "Name Community Example", // Name Community "description" : "Description of community", // Community description "adminAlias" : "user.community.admin.login", // User Admin Alias "hidden" : "false", // Community must be hidden "privateContent" : "false", // The community has private content "approvalRequired" : "false", // If is necessary to approve actions "createForum" : "false", // If is necessary to create forum in the community }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "id": 162, "alias": "alias.community1436203427286", "name": "Community Name", "description": "Community Description", "adminAlias": "fluig.user", "hidden": false, "privateContent": false, "approvalRequired": false, "ecmInfo": null }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5.12

### POST /2.0/communities/disablePostEditionAllCommunities

Disbale edition post in all communities

Available Since
:   1.5.12

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status` |

Available Since
:   1.5.7

### POST /2.0/communities/update

update a community  
  
Create a new community: fill object CommunityCreateVO

Available Since
:   1.5.7

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | [CommunityCreateVO](https://api.fluig.com/old/json_CommunityCreateVO.html) (JSON) | Request JSON (example):`{ "alias" : "alias.community", // Alias Communit "name" : "Name Community Example", // Name Community "description" : "Description of community", // Community description "adminAlias" : "user.community.admin.login", // User Admin Alias "hidden" : "false", // Community must be hidden "privateContent" : "false", // The community has private content "approvalRequired" : "false", // If is necessary to approve actions, "createForum" : "false", // If is necessary to create forum in the community }` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "id": 162, "alias": "alias.community1436203427286", "name": "Community Name", "description": "Community Description", "adminAlias": "fluig.user", "hidden": false, "privateContent": false, "approvalRequired": false, "ecmInfo": null }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |

Available Since
:   1.5

### POST /2.0/communities/addUser/{communityId}

This method has been deprecated. As of release 1.5.9, replaced by [addUsers](https://api.fluig.com/old/json_CommunityRest.html)

Add User  
  
Add an user to a community

Available Since
:   1.5

Request Parameters

| name | type | description | constraints |
| --- | --- | --- | --- |
| communityId | path | REQUIRED Community Id | long |

Request Body

| media type | data type | description |
| --- | --- | --- |
| application/json | string (JSON) | REQUIRED Alias Community `community_alias_name` |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | `This method just return HTTP 200 status, successful message  { "content": { "id": 126, "alias": "alias.community1435934217949", "name": "Community Name", "description": "Community Description", "adminAlias": "fluig.user", "hidden": false, "privateContent": false, "approvalRequired": false, "ecmInfo": null }, "message": { "message": "OK", "detail": "OK", "type": "INFO" } }` |
