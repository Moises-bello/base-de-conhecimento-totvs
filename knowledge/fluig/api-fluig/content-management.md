---
category: content-management
content_hash: 188c1db8da99b68b81cf1d5c3659606907c2dce66ba93a50227456d0d3ad65da
endpoints: 29
fetched_at: '2026-11-03T17:04:19.193695+00:00'
module: content-management
openapi_version: '2.0'
product: fluig
source: api-fluig
title: API Fluig — Content Management
type: api-reference
url: https://api.fluig.com/latest/content-management/swagger-ui/
---

# Content Management

Find and retrieve information on content related to documents and favourites

**Spec:** https://api.fluig.com/latest/content-management/swagger-ui/swagger.json

## GET `/v2/documents/allDocumentHits/{documentId}`

**Busca hit dos documentos**

- **operationId:** `getAllDocumentHits`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/documents/comment`

**Criar comentário de um documento**

- **operationId:** `createDocumentComment`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | CreateComment | sim | Comentário |

### Corpo da requisição

`CreateComment`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/documents/maxUploadSize`

**Busca tamanho máximo de upload de documentos em Bytes**

- **operationId:** `getMaxUploadSize`
- **tags:** Documents

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/documents/publish`

**Publicar arquivos que foram feitos upload no ECM**

- **operationId:** `publish`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | CreateDocument | sim | Documento a publicar |

### Corpo da requisição

`CreateDocument`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/documents/upload/{fileName}`

**Remover Upload de Arquivos**

- **operationId:** `deleteDocumentUpload`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fileName` | path | string | sim | Nome do documento |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/documents/upload/{fileName}`

**Realiza o upload de documentos**

- **operationId:** `documentUpload`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `fileName` | path | string | sim | Nome do documento |
| `file` | formData | file | sim | Arquivo de Upload |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/documents/upload/{fileName}/{parentId}/publish`

**Realiza upload de documentos e publica com propriedades default**

- **operationId:** `documentUploadAndPublish`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `parentId` | path | integer | sim | Diretório de destino |
| `fileName` | path | string | sim | Nome do documento |
| `file` | formData | file | sim | Arquivo de Upload |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/documents/uploads`

**Limpa a área de upload de documentos do usuário**

- **operationId:** `removeAllFiles`
- **tags:** Documents

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/documents/{documentId}`

**Realiza a exclusão de documentos**

- **operationId:** `deleteDocument`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |

### Respostas

- **204:** Successful request without body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/documents/{documentId}/comments`

**Lista comentários de um documento**

- **operationId:** `listComments`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `documentId` | path | integer | sim | Id do documento |
| `documentVersion` | query | integer | não | Versão do documento |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PATCH `/v2/documents/{documentId}/description`

**Altera descrição de documento**

- **operationId:** `changeDescription`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |
| `body` | body | DocumentDescription | sim | Nova descrição |

### Corpo da requisição

`DocumentDescription`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/documents/{documentId}/favorite`

**Remove um documento dos favoritos**

- **operationId:** `deleteFavorite`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |

### Respostas

- **204:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/documents/{documentId}/favorite`

**Adiciona um documento aos favoritos**

- **operationId:** `favoriteDocument`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |

### Respostas

- **204:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **409:** Conflict between resources. An accompanying error message will explain further
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/documents/{documentId}/thumbnail`

**Busca o thumbnail do documento**

- **operationId:** `getThumbnail`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |
| `size` | query | string | não | Buscar por tamanho |
| `scale` | query | integer | não | Buscar por escala em porcentagem do tamanho original |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/documents/{documentId}/thumbnail/article`

**Busca o thumbnail de um artigo cropado**

- **operationId:** `getThumbnailArticle`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `documentId` | path | integer | sim | Id do documento |
| `scale` | query | integer | não | Buscar por escala em porcentagem do tamanho original |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/documents/{id}`

**Retrieve the document**

- **operationId:** `retrieve`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | The document identifier id |
| `expand` | query | array | não | Campos expansíveis |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will

## PATCH `/v2/documents/{id}`

**Update document properties**

- **operationId:** `update`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | The document identifier id |
| `body` | body | array[DocumentPatchDTOPatch] | sim | The properties to be updated |
| `expand` | query | array | não | Campos expansíveis |

### Corpo da requisição

`array[DocumentPatchDTOPatch]`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will

## GET `/v2/documents/{id}/stream`

**Retorna uma mídia através do identificador do documento**

- **operationId:** `media`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | The document identifier id |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PATCH `/v2/documents/{id}/users/{userCode}/hits`

**Adiciona visualizações na última versão do documento**

- **operationId:** `updateHitsActiveVersion`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Id do documento |
| `userCode` | path | string | sim | Código do usuário |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## PATCH `/v2/documents/{id}/users/{userCode}/version/{version}/hits`

**Adiciona visualizações ao documento na versão informada**

- **operationId:** `updateHitsWithVersion`
- **tags:** Documents

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Id do documento |
| `userCode` | path | string | sim | Código do usuário |
| `version` | path | integer | sim | Versão do documento |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/folders/{documentRootId}/{currentDocumentId}`

**Busca o breadcrumb abaixo do documento enviado como raiz**

- **operationId:** `getBreadCrumb`
- **tags:** Pastas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `currentDocumentId` | path | integer | sim | Id da pasta atual |
| `documentRootId` | path | integer | sim | Id da pasta raiz |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## POST `/v2/folders/{parentId}`

**Realiza a criação de pasta**

- **operationId:** `createNewFolder`
- **tags:** Pastas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `parentId` | path | integer | sim | Id da pasta |
| `body` | body | DocumentDescription | sim | Descrição da pasta |

### Corpo da requisição

`DocumentDescription`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/folders/{parentId}/documents`

**Busca documentos de uma pasta**

- **operationId:** `getDocuments`
- **tags:** Pastas

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `parentId` | path | integer | sim | Id da pasta |
| `authorId` | query | string | não | Filtra pelo autor documento |
| `documentDescription` | query | string | não | Filtra pela descrição do documento |
| `documentTypeId` | query | string | não | Filtra pelo tipo de documento |
| `topicId` | query | string | não | Filtra pelo assunto do documento |
| `publisherAlias` | query | string | não | Filtra pelo publicador do documento |
| `dtstartModify` | query | string | não | Filtra pela data de modificação - Data inicial |
| `dtendModify` | query | string | não | Filtra pela data de modificação - Data final |
| `idDocumentStart` | query | string | não | Filtra a partir do ID inicial |
| `idDocumentEnd` | query | string | não | Filtra até o ID final |
| `customFieldId` | query | string | não | Filtra por metadados customizados |
| `customDescription` | query | string | não | FIltra por descrição customizada |
| `order` | query | array | sim | Ordenação |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not allowed
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/watermarks`

**Buscar por marcas d'água**

- **operationId:** `findWatermarks`
- **tags:** Marca d'água

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `order` | query | array | não | Campos Ordenados |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |
| `id` | query | array | não | Buscar pelo id da marca d'água |
| `name` | query | string | não | Buscar pelo nome da marca d'água |
| `value` | query | string | não | Buscar pelo valor da marca d'água |

### Respostas

- **200:** response.status.ok
- **400:** response.status.bad.request
- **401:** response.status.unauthorized
- **403:** response.status.forbidden
- **500:** response.status.server.error

## POST `/v2/watermarks`

**Adiciona uma marca d'água**

- **operationId:** `createWatermark`
- **tags:** Marca d'água

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `body` | body | WatermarkUpdate | sim | Marca d'água |

### Corpo da requisição

`WatermarkUpdate`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## DELETE `/v2/watermarks/{id}`

**Remove uma marca d'água**

- **operationId:** `removeWatermark`
- **tags:** Marca d'água

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Identificador da marca d'água |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will

## GET `/v2/watermarks/{id}`

**Busca a marca d'água**

- **operationId:** `retrieveWatermark`
- **tags:** Marca d'água

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Identificador da marca d'água |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will

## PUT `/v2/watermarks/{id}`

**Edita uma marca d'água**

- **operationId:** `editWatermark`
- **tags:** Marca d'água

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Identificador da marca d'água |
| `body` | body | WatermarkUpdate | sim | Marca d'água |

### Corpo da requisição

`WatermarkUpdate`

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error message will explain further
- **401:** Authentication credentials were missing or incorrect
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will explain further

## GET `/v2/watermarks/{id}/listDocuments`

**Lista os documentos que utilizam uma marca d'água**

- **operationId:** `listDocumentsAssociatedWithWatermark`
- **tags:** Marca d'água

### Parâmetros

| Nome | Em | Tipo | Obrigatório | Descrição |
|------|-----|------|-------------|-----------|
| `id` | path | integer | sim | Identificador da marca d'água |
| `page` | query | integer | não | Page Number |
| `pageSize` | query | integer | não | Number of records per page |

### Respostas

- **200:** Successful request with body content
- **400:** The request was invalid or could not be served. An accompanying error
- **401:** Authentication credentials were missing or incorrect
- **403:** The request is understood, but it has been refused or access is not
- **404:** The requested resource could not be found
- **500:** Something went wrong on the server. An accompanying error message will
