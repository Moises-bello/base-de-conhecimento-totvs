---
category: collaboration
content_hash: ad2befde2cd2b2540b889151043c41f96b30619bfb06464d769a5d0440a75c89
endpoints: 55
fetched_at: '2026-11-03T17:04:20.884988+00:00'
module: collaboration
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Social
type: api-reference
url: https://api.fluig.com/latest/collaboration/swagger-ui/
---

# Social

Work with community data using the Social API.

**Spec:** https://api.fluig.com/latest/collaboration/swagger-ui/swagger.json

## GET `/v3/communities`

**Lists information from all communities**

- **operationId:** `findAllCommunities`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `onlyFavorite` | query | boolean | não | Search for only favorite communities |
| `onlyHidden` | query | boolean | não | Search for only hidden communities |
| `userAlias` | query | string | não | User alias (Search communities in which the user is a participant) |
| `communityLikeAlias` | query | string | não | Search community by partial or full alias |
| `communityLikeName` | query | string | não | Search community by partial or full name |
| `order` | query | array | não | Ordering |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/communities/{alias}/favorites`

**Remove a community from favorites**

- **operationId:** `removeFavorite`
- **tags:** Favorites

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/communities/{alias}/favorites`

**Adds a community to favorites**

- **operationId:** `favorite`
- **tags:** Favorites

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/communities/{alias}/notify`

**Disables notification for a community**

- **operationId:** `notifyOff`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/communities/{alias}/notify`

**Enables notification for a community**

- **operationId:** `notifyOn`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/communities/{communityAlias}`

**Lists information for a specific community**

- **operationId:** `findCommunity`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `communityAlias` | path | string | sim | Community alias |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/communities/{communityAlias}/users`

**Returns the list of users participating in the community**

- **operationId:** `listMembers`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `communityAlias` | path | string | sim | Community alias |
| `order` | query | array | não | Ordering |
| `userName` | query | string | não | User name to filter in the list |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/communities/{communityAlias}/users`

**Requests permission to join the community**

- **operationId:** `requestPermission`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `communityAlias` | path | string | sim | Community alias |
| `body` | body | UserCreate | não |  |

### Corpo da requisição

`UserCreate`

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/communities/{communityAlias}/users/{userAlias}`

**Delete user from the community**

- **operationId:** `deleteMembers`
- **tags:** Communities

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `communityAlias` | path | string | sim | Community alias |
| `userAlias` | path | string | sim | User alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/medias/upload/image/{fileName}`

**Image upload**

- **operationId:** `uploadMediaImage`
- **tags:** Media

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fileName` | path | string | sim | File Name |
| `file` | formData | file | sim | Image |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/medias/upload/video/{fileName}`

**Video upload**

- **operationId:** `uploadMediaVideo`
- **tags:** Media

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fileName` | path | string | sim | File Name |
| `file` | formData | file | sim | Video |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/participation/{alias}/isMember/{userAlias}`

**Checks whether a user is a member of a community**

- **operationId:** `checkIfUserIsMember`
- **tags:** Attendance

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |
| `userAlias` | path | string | sim | User alias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/participation/{alias}/moderator/{userAlias}`

**Remove community moderator**

- **operationId:** `removeCommunityModerator`
- **tags:** Attendance

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |
| `userAlias` | path | string | sim | User alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/participation/{alias}/moderator/{userAlias}`

**Add moderator to community**

- **operationId:** `addCommunityModerator`
- **tags:** Attendance

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |
| `userAlias` | path | string | sim | User alias (Search communities in which the user is a participant) |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/participation/{alias}/moderators`

**List all moderators of a community**

- **operationId:** `listAllModerators`
- **tags:** Attendance

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | Community alias |
| `order` | query | array | não | Ordering |
| `pattern` | query | string | não |  |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts`

**List all user posts**

- **operationId:** `listPosts`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `userAlias` | query | string | sim | User alias |
| `lastPostId` | query | integer | não | ID of the last post viewed |
| `order` | query | array | não | Ordering |
| `pageSize` | query | integer | não | Number of records returned in search |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts`

**Create new post**

- **operationId:** `createPost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | PostCreate | sim | v3.postsRest.postCreate |

### Corpo da requisição

`PostCreate`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/posts/comments/{commentId}/likes`

**Delete a comment support**

- **operationId:** `removeCommentLike`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `commentId` | path | integer | sim | Comment ID |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/comments/{commentId}/likes`

**Search list of users who liked a comment**

- **operationId:** `commentLikes`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `commentId` | path | integer | sim | Comment ID |
| `alias` | query | string | não | User alias to filter in the list |
| `name` | query | string | não | User name to filter in the list |
| `order` | query | array | não | v3.posts.comments.order |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/comments/{commentId}/likes`

**Support a comment**

- **operationId:** `commentLike`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `commentId` | path | integer | sim | Comment ID |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/denounce/comments/{commentId}`

**Report a comment**

- **operationId:** `denounceComment`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `commentId` | path | integer | sim | Comment ID |
| `text` | query | string | sim | Report justification |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/denounce/post/{postId}`

**Report a Post**

- **operationId:** `denouncePost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `text` | query | string | sim | Report justification |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/multiplesPlaces`

**Create new post**

- **operationId:** `createPostInMultiplesPlaces`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | PostCreateInMultiplesPlaces | sim | v3.postsRest.postCreate |

### Corpo da requisição

`PostCreateInMultiplesPlaces`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/shareContent`

**Share posts**

- **operationId:** `shareContent`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | Share | não |  |

### Corpo da requisição

`Share`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{id}/likes`

**List users who supported a post**

- **operationId:** `postLikes`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Post ID to be searched |
| `alias` | query | string | não | User alias to filter in the list |
| `name` | query | string | não | User name to filter in the list |
| `order` | query | array | não | Ordering |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{id}/shared`

**Search users who shared the post**

- **operationId:** `shared`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Post ID to be searched |
| `name` | query | string | não | User name to filter in the list |
| `order` | query | string | não | Ordering |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{id}/watchers`

**Search users following the post**

- **operationId:** `postWatchers`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Post ID to be searched |
| `name` | query | string | não | User name to filter in the list |
| `order` | query | array | não | Ordering |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/posts/{postId}`

**Delete a post**

- **operationId:** `removePost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{postId}`

**Search a post**

- **operationId:** `findPost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v3/posts/{postId}`

**Edit a post**

- **operationId:** `editPost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `body` | body | PostEdit | não |  |

### Corpo da requisição

`PostEdit`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{postId}/comments`

**Lists comments from a specific post**

- **operationId:** `listComments`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `publisherAlias` | query | string | não | Filter by publisher alias |
| `hasLikes` | query | boolean | não | Filter by likes |
| `hasMentions` | query | boolean | não | Filter by mentions |
| `order` | query | array | não | Ordering |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/{postId}/comments`

**Comment on a POST published in the community**

- **operationId:** `commentPost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `body` | body | CommentPost | não |  |
| `expand` | query | array | não | Expandable fields |

### Corpo da requisição

`CommentPost`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/posts/{postId}/comments/{commentId}`

**Deletes a comment from a post**

- **operationId:** `removeComment`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `commentId` | path | integer | sim | Comment ID |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{postId}/comments/{commentId}`

**Search for a comment from a post**

- **operationId:** `findComment`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `commentId` | path | integer | sim | Comment ID |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v3/posts/{postId}/comments/{commentId}`

**Enter a comment**

- **operationId:** `editComment`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `commentId` | path | integer | sim | Comment ID |
| `body` | body | CommentPost | não |  |
| `expand` | query | array | não | Expandable fields |

### Corpo da requisição

`CommentPost`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/posts/{postId}/likes/{userAlias}`

**Delete support from a post**

- **operationId:** `removePostLikeByAlias`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `userAlias` | path | string | sim | User alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/posts/{postId}/likes/{userAlias}`

**Search for user who supported the POST**

- **operationId:** `findUserThatLikedPost`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `userAlias` | path | string | sim | User alias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/{postId}/likes/{userAlias}`

**Support a post**

- **operationId:** `postLike`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |
| `userAlias` | path | string | sim | User alias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/posts/{postId}/notify`

**Stop receiving post notifications**

- **operationId:** `removeNotify`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/posts/{postId}/notify`

**Receive post notification**

- **operationId:** `notify`
- **tags:** Posts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `postId` | path | integer | sim | Post ID |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/socials`

**Users and communities list**

- **operationId:** `list`
- **tags:** Socials

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `pattern` | query | string | não |  |
| `order` | query | array | não | Ordering |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/socials/{alias}`

**v3.socials.get.apiOperation**

- **operationId:** `get`
- **tags:** Socials

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | v3.socialUser.socialAlias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/timeline/{socialAlias}`

**List all timeline posts**

- **operationId:** `getTimeline`
- **tags:** Timeline

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `socialAlias` | path | string | sim | Alias of a logged-in user/community |
| `lastPostId` | query | integer | não | ID of the last post viewed |
| `order` | query | array | não | Ordering |
| `pageSize` | query | integer | não | Number of records returned in search |
| `fields` | query | array | não | Dynamic fields |
| `loggedUserPublications` | query | boolean | não | List only the logged-in user’s posts |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/users`

**Lists information from all users**

- **operationId:** `findAll`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | query | string | não | Search user by partial or full alias |
| `isFavorite` | query | boolean | não | List favorite users relative to the logged-in user |
| `name` | query | string | não | Search user by partial or full name |
| `order` | query | array | não | Ordering |
| `relationStatus` | query | string | não | Relationship status |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/users/current/favorites`

**List favorite users relative to the logged-in user**

- **operationId:** `listCurrentFavorites`
- **tags:** Favorites

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/users/{alias}`

**Lists information for a user**

- **operationId:** `find`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | User alias |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/users/{alias}/favorites`

**Adds a user to favorites**

- **operationId:** `favoriteAlias`
- **tags:** Favorites

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | User alias |
| `body` | body | FavoriteCreate | não |  |

### Corpo da requisição

`FavoriteCreate`

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/users/{alias}/favorites/{favoriteAlias}`

**Deletes a user from favorites**

- **operationId:** `deleteAlias`
- **tags:** Favorites

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | User alias |
| `favoriteAlias` | path | string | sim | User alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/users/{alias}/following`

**List of users who are followed by a specific user**

- **operationId:** `listFollowings`
- **tags:** Users

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | User alias |
| `order` | query | array | não | Ordering |
| `name` | query | string | não | Lists users who are followed by partial or full name |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/users/{alias}/picture`

**Returns an image of a specific user**

- **operationId:** `getProfilePicture`
- **tags:** Profile picture

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | User alias |
| `type` | query | string | não | Image type |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/users/{alias}/picture`

**Adds or Changes an image for a specific user**

- **operationId:** `updateFile`
- **tags:** Profile picture

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `alias` | path | string | sim | User alias |
| `file` | formData | file | sim | Upload file |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v3/users/{userAlias}/followers`

**Search for all followers of a user**

- **operationId:** `findAllFollowers`
- **tags:** Followers

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `userAlias` | path | string | sim | User alias |
| `order` | query | array | não | Ordering |
| `name` | query | string | não | Search followers by partial or full name |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v3/users/{userAlias}/followers`

**Requests to follow a specific user**

- **operationId:** `followRequest`
- **tags:** Followers

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `userAlias` | path | string | sim | User alias |
| `body` | body | UserCreate | sim | Related user alias |

### Corpo da requisição

`UserCreate`

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/users/{userAlias}/followers/{followerAlias}`

**Deletes a user from another user's follower list**

- **operationId:** `unfollowByAlias`
- **tags:** Followers

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `userAlias` | path | string | sim | User alias |
| `followerAlias` | path | string | sim | Related user alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v3/users/{userAlias}/followers/{followerAlias}/cancelRequest`

**Remove pending requests  **

- **operationId:** `cancelRequest`
- **tags:** Followers

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `userAlias` | path | string | sim | User alias |
| `followerAlias` | path | string | sim | Related user alias |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further
