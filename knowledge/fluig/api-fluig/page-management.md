---
category: page-management
content_hash: e43521ab6235d080ddfb62e15c290fc9813acc39669b2a5d12a9ba49e3d418fd
endpoints: 43
fetched_at: '2026-11-03T17:04:19.592129+00:00'
module: page-management
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Page Management
type: api-reference
url: https://api.fluig.com/latest/page-management/swagger-ui/
---

# Page Management

The page management API allows managing platform pages, themes and layouts.

**Spec:** https://api.fluig.com/latest/page-management/swagger-ui/swagger.json

## GET `/v2/applications`

**Returns all available widgets**

- **operationId:** `findAll`
- **tags:** Widgets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `search` | query | string | não | Search term in the title, description, and code fields |
| `category` | query | string | não | Category of widget to be searched |
| `internal` | query | boolean | não | Internal (native to the platform) or external (customized) widgets |
| `order` | query | array | não | Sorting by field(s) |
| `expand` | query | array | não | Expandable fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/applications/categories/count`

**Returns all grouped widget categories**

- **operationId:** `findGroupedByCategories`
- **tags:** Widgets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `category` | query | string | não | Category of widget to be searched |
| `internal` | query | boolean | não | Internal (native to the platform) or external (customized) widgets |
| `order` | query | array | não | Sorting by field(s) |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/applications/{code}`

**Search a widget by the code**

- **operationId:** `findByCode`
- **tags:** Widgets

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Widget code |
| `expand` | query | array | não | Expandable fields |
| `fields` | query | array | não | Dynamic fields |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/layouts`

**Return all available layouts**

- **operationId:** `getAllLayouts`
- **tags:** Layouts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `order` | query | array | não | Sorting by field(s) |

### Respostas

- **200:** Ok
- **400:** Failed to return layout; see the response for more details
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/layouts/{code}`

**Return the layout as per its code**

- **operationId:** `getLayout`
- **tags:** Layouts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fields` | query | array | não | Dynamic fields |
| `code` | path | string | sim | Layout code |

### Respostas

- **200:** Ok
- **400:** Failed to return layout; see the response for more details
- **401:** User is not authenticated
- **404:** Layout not found
- **500:** Internal server error, see reply for more details

## GET `/v2/layouts/{code}/pages`

**Return all pages posted on a particular layout**

- **operationId:** `getPagesByLayout`
- **tags:** Layouts

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Layout code |
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Sorting by field(s) |
| `internal` | query | boolean | não | Return internal pages only |

### Respostas

- **200:** Ok
- **400:** Failed to return pages; see the response for more details
- **401:** User is not authenticated
- **404:** Layout not found
- **500:** Internal server error, see reply for more details

## GET `/v2/pages`

**Return all pages**

- **operationId:** `getPages`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `order` | query | array | não | Sorting by field(s) |
| `internal` | query | boolean | não | Return internal pages only |
| `url` | query | string | não | Returns only pages that can be accessed by the URL |
| `mobile` | query | boolean | não | Return only pages with access enabled on the mobile |

### Respostas

- **200:** Ok
- **400:** Failed to return pages; see the response for more details
- **401:** User does not have permission to perform the operation
- **500:** Internal server error, see reply for more details

## POST `/v2/pages/create`

**Page creation**

- **operationId:** `create`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | PageCreate | não |  |

### Corpo da requisição

`PageCreate`

### Respostas

- **201:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/editable/find`

**Return editable pages.**

- **operationId:** `findEditable`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `search` | query | string | não | Search filter |
| `status` | query | string | não | Page Status |
| `enabledChildren` | query | boolean | não | Filter for pages that allow children |

### Respostas

- **200:** Ok
- **400:** Failed to return pages; see the response for more details
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/pages/parent/find`

**Return parent pages.**

- **operationId:** `findParent`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `expand` | query | array | não | Expandable fields |
| `search` | query | string | não | Search filter |

### Respostas

- **200:** Ok
- **400:** Failed to return pages; see the response for more details
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## DELETE `/v2/pages/{code}`

**Delete page**

- **operationId:** `delete`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/{code}`

**Return a page as per its code**

- **operationId:** `pageByCode`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `expand` | query | array | não | Expandable fields |

### Respostas

- **200:** Ok
- **400:** Failed to return page; see the response for more details
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Page not found
- **500:** Internal server error, see reply for more details

## PATCH `/v2/pages/{code}`

**Modify page**

- **operationId:** `patchByCode`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `Page to be modified` | body | array[PageDTOPatch] | sim |  |

### Corpo da requisição

`array[PageDTOPatch]`

### Respostas

- **200:** Ok
- **400:** Failed to modify page; see the response for more details
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Page not found
- **500:** Internal server error, see reply for more details

## PUT `/v2/pages/{code}`

**Updates information on a page**

- **operationId:** `updatePage`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `body` | body | UpdatePage | sim | Page to be updated |

### Corpo da requisição

`UpdatePage`

### Respostas

- **200:** Ok
- **400:** Failed to return page; see the response for more details
- **401:** User is not authenticated
- **403:** Page not found
- **404:** Page not found
- **500:** Internal server error, see reply for more details

## GET `/v2/pages/{code}/application`

**Searches widgets on the page**

- **operationId:** `getWidgets`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `widgetCode` | query | string | não | Filter by a widget code |

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## POST `/v2/pages/{code}/application`

**Adds a Widget within the page.**

- **operationId:** `addWidget`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `body` | body | PageWidgetCreate | não |  |

### Corpo da requisição

`PageWidgetCreate`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/pages/{code}/application`

**Moves a Widget within the page.**

- **operationId:** `moveWidget`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `body` | body | MoveWidget | não |  |

### Corpo da requisição

`MoveWidget`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/pages/{code}/application/{instanceId}`

**Remove widget from the page**

- **operationId:** `removeWidget`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `instanceId` | path | integer | sim | InstanceId of the widget to be deleted. |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/pages/{code}/archive`

**Archive pages**

- **operationId:** `archived`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/{code}/breadcrumb`

**Search breadcrumb of a page**

- **operationId:** `getBreadcrumbPage`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/pages/{code}/change-edit-user`

**Changes draft user page**

- **operationId:** `changeEditUser`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/pages/{code}/draft`

**Discard draft of one page**

- **operationId:** `deleteDraft`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/pages/{code}/draft`

**Create a page draft**

- **operationId:** `createDraft`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/pages/{code}/duplicate`

**Duplicates a page**

- **operationId:** `duplicate`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `body` | body | PageDuplicate | não |  |

### Corpo da requisição

`PageDuplicate`

### Respostas

- **201:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/pages/{code}/friendlyUrl`

**Update friendly url**

- **operationId:** `changeFriendlyUrl`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `value` | query | string | sim | Friendly URL |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/{code}/last-edit-user`

**Returns if the logged-in user is the last editor of the page**

- **operationId:** `isLastEditUser`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/pages/{code}/layouts/{layoutCode}`

**Changes the page layout.**

- **operationId:** `changePageLayout`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `layoutCode` | path | string | sim | Layout code |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/{code}/menu`

**Search pages of the logged in user’s menu**

- **operationId:** `getMenu`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `isParent` | query | boolean | sim | Return the child pages of the page code entered |
| `isMobile` | query | boolean | sim | Mobile menu |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/{code}/permission`

**Return page permissions or default permissions.**

- **operationId:** `findPermissionByPageCode`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **200:** Ok
- **400:** Failed to return page permissions, see the response for more details
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Page not found
- **500:** Internal server error, see reply for more details

## POST `/v2/pages/{code}/publish`

**Publishes page in draft**

- **operationId:** `publish`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `body` | body | PagePublish | não |  |

### Corpo da requisição

`PagePublish`

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/pages/{code}/reset`

**Reset internal page to the initial state**

- **operationId:** `reset`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |

### Respostas

- **202:** Page will be reset
- **400:** Failed to reset internal page to its initial state
- **401:** User is not authenticated
- **403:** User does not have permission to perform the operation
- **404:** Page not found
- **500:** Internal server error, see reply for more details

## PUT `/v2/pages/{code}/unarchive`

**Unarchiving pages**

- **operationId:** `unarchived`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `unlinkParent` | query | boolean | sim | Unlink from root page |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/pages/{code}/versions`

**Return page versions**

- **operationId:** `getPageVersions`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `search` | query | string | não | Filter by description |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PUT `/v2/pages/{code}/versions/restore`

**Restores the page to a version**

- **operationId:** `restorePageVersion`
- **tags:** Pages

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Page code |
| `body` | body | PageVersionRestore | não |  |

### Corpo da requisição

`PageVersionRestore`

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/themes`

**Return all themes**

- **operationId:** `findThemes`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fields` | query | array | não | Dynamic fields |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page. |
| `status` | query | array | não | Status |

### Respostas

- **200:** Ok
- **400:** Failed to restore themes, see the response for more details
- **401:** User is not authenticated
- **500:** Internal server error, see reply for more details

## GET `/v2/themes/responsive-theme/enabled`

**Returns if only Responsive Theme is enabled**

- **operationId:** `responsiveThemeEnable`
- **tags:** Themes

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## GET `/v2/themes/theme-change/blocked`

**Returns if the theme change is blocked**

- **operationId:** `isBlockThemeChange`
- **tags:** Themes

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## GET `/v2/themes/{code}`

**Return the theme as per the entered code**

- **operationId:** `getTheme`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Theme code |

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## GET `/v2/themes/{code}/preferences`

**Returns all preferences for the entered theme **

- **operationId:** `getPreferences`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Theme code |

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## POST `/v2/themes/{code}/preferences`

**Saves all preferences for the entered theme**

- **operationId:** `savePreferences`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Theme code |
| `body` | body | ThemePreferences | sim | Object with the preferences of a theme |

### Corpo da requisição

`ThemePreferences`

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## POST `/v2/themes/{code}/restore`

**Restore the preferences for the entered theme**

- **operationId:** `restore`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `code` | path | string | sim | Theme code |

### Respostas

- **200:** Ok
- **204:** Successful request without body content
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## GET `/v2/themes/{tenantCode}/dark-logo`

**api.themes.get.image.dark.logo**

- **operationId:** `getImageDarkLogo`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `tenantCode` | path | string | sim | Company code |

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details

## GET `/v2/themes/{tenantCode}/logo`

**Search for the company logo**

- **operationId:** `getImageLogo`
- **tags:** Themes

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `tenantCode` | path | string | sim | Company code |

### Respostas

- **200:** Ok
- **400:** Failed to restore theme, see the response for more details
- **401:** User is not authenticated
- **404:** Theme not found
- **500:** Internal server error, see reply for more details
