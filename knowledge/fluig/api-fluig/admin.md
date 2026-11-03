---
category: admin
content_hash: 8abfcc33813acfecd7fe9120286ebc334dd950d43ed59f4ff736d946630f7572
endpoints: 35
fetched_at: '2026-11-03T17:04:21.388742+00:00'
module: admin
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Administrator
type: api-reference
url: https://api.fluig.com/latest/admin/swagger-ui/
---

# Administrator

This API manages groups, roles and users

**Spec:** https://api.fluig.com/latest/admin/swagger-ui/swagger.json

## GET `/v1/groups`

**Returns list of groups**

- **operationId:** `findGroups`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `description` | query | string | não | Group description |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list groups
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v1/groups`

**Add new group**

- **operationId:** `create`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `Group data` | body | GroupCreate | sim |  |

### Corpo da requisição

`GroupCreate`

### Respostas

- **201:** Ok
- **400:** Failed to create group, see response for more details
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## DELETE `/v1/groups/{code}`

**Delete group with the entered code**

- **operationId:** `delete`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to delete the group
- **401:** User is not authenticated
- **404:** Group not found
- **500:** Internal server error, see reply for more details

## GET `/v1/groups/{code}`

**Returns list of users associated to the group**

- **operationId:** `findGroupByCode`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `fields` | query | array | não | Dynamic fields |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to filter group by code
- **401:** User is not authenticated
- **404:** Company not found
- **500:** Internal server error, see reply for more details

## PUT `/v1/groups/{code}`

**Update group information**

- **operationId:** `update`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `body` | body | GroupUpdate | sim | Group data |

### Corpo da requisição

`GroupUpdate`

### Respostas

- **200:** Ok
- **400:** An error occurred trying to update the group
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v1/groups/{code}/groups`

**Returns list of subgroups**

- **operationId:** `findChildGroupsByParentCode`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list subgroups
- **401:** User is not authenticated
- **404:** Sub-groups list not found
- **500:** Internal server error, see reply for more details

## GET `/v1/groups/{code}/roles`

**Returns list of roles related to the group**

- **operationId:** `findRolesOfGroup`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `description` | query | string | não | Group description |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list roles
- **401:** User is not authenticated
- **404:** Group not found
- **500:** Internal server error, see reply for more details

## POST `/v1/groups/{code}/roles`

**Relate role to group**

- **operationId:** `createUserRole`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `body` | body | AddRole | sim | Role data |

### Corpo da requisição

`AddRole`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to relate role to the group
- **401:** User is not authenticated
- **404:** Group not found
- **500:** Internal server error, see reply for more details

## DELETE `/v1/groups/{code}/roles/{role}`

**Delete role from the group**

- **operationId:** `removeRoleFromGroup`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `role` | path | string | sim | Role code |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to delete role from the group
- **401:** User is not authenticated
- **404:** admin.api.group.notfound
- **500:** Internal server error, see reply for more details

## GET `/v1/groups/{code}/users`

**Returns list of users associated to the group**

- **operationId:** `findUsersByGroup`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `userCode` | query | string | não | User code |
| `login` | query | string | não | Login |
| `email` | query | string | não | Email |
| `firstName` | query | string | não | First name |
| `lastName` | query | string | não | Last name |
| `fullName` | query | string | não | Full Name |
| `showInactive` | query | boolean | não | Show inactive users |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list users associated to the group
- **401:** User is not authenticated
- **404:** List of associated users not found
- **500:** Internal server error, see reply for more details

## POST `/v1/groups/{code}/users`

**Add user to group**

- **operationId:** `addUserToGroup`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `body` | body | AddUser | sim | User data |

### Corpo da requisição

`AddUser`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to add the user to the group
- **401:** User is not authenticated
- **404:** Group not found
- **500:** Internal server error, see reply for more details

## DELETE `/v1/groups/{code}/users/{login}`

**Remove the user from the group**

- **operationId:** `removeUserFromGroup`
- **tags:** Groups

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Group code |
| `login` | path | string | sim | Login |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to remove the user from the group
- **401:** User is not authenticated
- **404:** Group not found
- **500:** Internal server error, see reply for more details

## GET `/v1/roles`

**List roles**

- **operationId:** `findRoles`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `description` | query | string | não | Role description |
| `pattern` | query | string | não | Role description or code |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** admin.api.role.find.failed
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v1/roles`

**Add new role**

- **operationId:** `create`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | RoleCreate | sim | Role data |

### Corpo da requisição

`RoleCreate`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to add a new role
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## DELETE `/v1/roles/{code}`

**Delete role**

- **operationId:** `deleteRole`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | The role identifier code |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to delete the role
- **401:** User is not authenticated
- **404:** Role not found
- **500:** Internal server error, see reply for more details

## GET `/v1/roles/{code}`

**List roles by code**

- **operationId:** `findByRoleCode`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Role code |
| `fields` | query | array | não | Dynamic fields |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** admin.api.role.find.by.code.failed
- **401:** User is not authenticated
- **404:** Role not found
- **500:** Internal server error, see reply for more details

## PUT `/v1/roles/{code}`

**Update role information**

- **operationId:** `update`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Role code |
| `body` | body | RoleUpdate | sim | Role data |

### Corpo da requisição

`RoleUpdate`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to update the role
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v1/roles/{code}/users`

**Returns list of users related to the role**

- **operationId:** `findUsersByRole`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Role code |
| `userCode` | query | string | não | User code |
| `login` | query | string | não | Login |
| `email` | query | string | não | Email |
| `firstName` | query | string | não | First name |
| `lastName` | query | string | não | Last name |
| `fullName` | query | string | não | Full Name |
| `showInactive` | query | boolean | não | Show inactive users |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred listing users related to the role
- **401:** User is not authenticated
- **404:** Role not found
- **500:** Internal server error, see reply for more details

## POST `/v1/roles/{code}/users`

**Relate user to role**

- **operationId:** `addUserToRole`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Role code |
| `body` | body | AddUser | sim | User data |

### Corpo da requisição

`AddUser`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to add a user to the role
- **401:** User is not authenticated
- **404:** Role not found
- **500:** Internal server error, see reply for more details

## DELETE `/v1/roles/{code}/users/{login}`

**Remove the user from the rule**

- **operationId:** `removeUserFromRole`
- **tags:** Roles

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Role code |
| `login` | path | string | sim | Login |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to remove the user from the role
- **401:** User is not authenticated
- **404:** Role not found
- **500:** Internal server error, see reply for more details

## GET `/v1/users`

**Returns list of users**

- **operationId:** `findUsers`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | query | string | não | User code |
| `email` | query | string | não | Email |
| `firstName` | query | string | não | First name |
| `lastName` | query | string | não | Last name |
| `fullName` | query | string | não | Full Name |
| `pattern` | query | string | não | User name or code |
| `role` | query | string | não | Role code |
| `genericId` | query | string | não | Generic Identifier |
| `showInactive` | query | boolean | não | Show inactive users |
| `currentUser` | query | boolean | não | Use current user data? |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list users
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v1/users`

**Add new user**

- **operationId:** `createUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `User data` | body | UserCreate | sim |  |

### Corpo da requisição

`UserCreate`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to add a new user
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v1/users/updateUserData`

**Update user data properties**

- **operationId:** `updateUserData`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `User data` | body | UserDataUpdate | sim |  |

### Corpo da requisição

`UserDataUpdate`

### Respostas

- **201:** Ok
- **401:** User is not authenticated
- **403:** The user is authenticated but is not authorized to perform the operation
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## GET `/v1/users/{login}`

**Filter users by login**

- **operationId:** `findUserByLogin`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `fields` | query | array | não | Dynamic fields |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to filter users by login
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## PATCH `/v1/users/{login}`

**Update a user property**

- **operationId:** `patchUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | The user identifier login |
| `The user to be updated` | body | array[UserUpdateDTOPatch] | sim |  |

### Corpo da requisição

`array[UserUpdateDTOPatch]`

### Respostas

- **200:** Success
- **400:** Failed to edit user, see response for more details
- **401:** Access denied
- **403:** The user is authenticated but is not authorized to perform the operation
- **404:** Users not found
- **500:** Internal error, see response for more details

## PUT `/v1/users/{login}`

**Edit user**

- **operationId:** `updateUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `User data` | body | UserUpdate | sim |  |

### Corpo da requisição

`UserUpdate`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to edit user
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## POST `/v1/users/{login}/activate`

**Enable user**

- **operationId:** `activateUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |

### Respostas

- **200:** Ok
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## POST `/v1/users/{login}/deactivate`

**Deactivate user**

- **operationId:** `deactivateUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |

### Respostas

- **200:** Ok
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## GET `/v1/users/{login}/groups`

**Returns list of user groups**

- **operationId:** `findGroupsOfUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `returnAll` | query | boolean | não | Returns all groups, discarding paging |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list user groups
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## POST `/v1/users/{login}/groups`

**Add user to a group**

- **operationId:** `createUserGroup`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `body` | body | AddToUser | sim | Group data |

### Corpo da requisição

`AddToUser`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to add user to a group
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## DELETE `/v1/users/{login}/groups/{code}`

**Remove the user from the group**

- **operationId:** `removeUserFromGroup`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `code` | path | string | sim | Group code |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to remove the user from the entered group
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## GET `/v1/users/{login}/picture`

**Returns user image by login**

- **operationId:** `getPictureUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `width` | query | integer | não | Image width |

### Respostas

- **200:** Ok
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v1/users/{login}/roles`

**Returns list of roles related to the user**

- **operationId:** `findRolesOfUser`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | The number of items to be returned in each page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Order by field |

### Respostas

- **200:** Ok
- **400:** An error occurred trying to list user roles
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## POST `/v1/users/{login}/roles`

**Add role to user**

- **operationId:** `createUserRole`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `body` | body | AddToUser | sim | Role data |

### Corpo da requisição

`AddToUser`

### Respostas

- **201:** Ok
- **400:** An error occurred trying to add a new role to the user
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details

## DELETE `/v1/users/{login}/roles/{code}`

**Remove the user from the rule**

- **operationId:** `removeUserFromRole`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `login` | path | string | sim | Login |
| `code` | path | string | sim | Role code |

### Respostas

- **204:** Ok
- **400:** An error occurred trying to remove the user from the entered role
- **401:** User is not authenticated
- **404:** User not found!
- **500:** Internal server error, see reply for more details
