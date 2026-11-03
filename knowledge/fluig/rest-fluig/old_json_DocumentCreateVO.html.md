---
content_hash: 177eb3aa5e864eaae102e4219906dbfc4c1881be5630aac1921ac81a8e11efcf
fetched_at: '2026-11-03T14:34:36.641204+00:00'
page_id: json_DocumentCreateVO
product: fluig
source: rest-fluig
title: Fluig REST — DocumentCreateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_DocumentCreateVO.html
version: 1
---

# DocumentCreateVO Data Type

Value Object para Documento

Version
:   1.00.000

Properties

| name | data type | description |
| --- | --- | --- |
| tenantId | number | Recupera id do tenant |
| documentId | number | Recupera valor do document Id |
| version | number | Recupera valor da versão |
| documentTypeId | string | Recupera valor do id do tipo de documento |
| languageId | string | Recupera id da linguagem |
| iconId | number | Recupera id do icone |
| topicId | number | Recupera valor do id do topico |
| colleagueId | string | Recupera id do colega |
| documentDescription | string | Recupera descrição do documento |
| phisicalFile | string | Recupera arquivo fisico |
| keyWord | string | Recupera valor de palavra chave |
| createDate | number | Recupera valor para data de criação |
| approvedDate | number | Recupera valor da data de aprovação |
| lastModifiedDate | number | Recupera valor da última data de moficação |
| documentType | string | Recupera valor do tipo de documento |
| expirationDate | number | Recupera data de expiração |
| accessCount | number | Recupera número de acessso |
| atualizationId | number | Recupera id de atualização |
| parentDocumentId | number | Recupera id do pai do documento |
| visualization | string | Recupera visualização |
| relatedFiles | string | Recuprea arquivos relacionados |
| activeVersion | boolean | Recupera versão ativa |
| versionDescription | string | Recupera descrição da versão |
| approvalAndOr | boolean | Recupera condição aprovalAndOr |
| externalDocumentId | string | Recupera id documento externo |
| downloadEnabled | boolean | Recupera valor, se download é habilitado |
| approved | boolean | Recupera valor, se documento está aprovado |
| validationStartDate | number | Recupera data de inicio de validação |
| publisherId | string | Recupera id do publicador |
| cardDescription | string | Recupera descrição do card |
| allowMuiltiCardsPerUser | boolean | Recupera valor, se documento permite mult card por usuário |
| documentPropertyNumber | number | Recupera número de propriedade do documento |
| documentPropertyVersion | number | Recupera versão do documento |
| privateDocument | boolean | Recupera valor, se documento é privado |
| privateColleagueId | string | Recupera valor id privado do colega |
| indexed | boolean | Recupera valor, se documento é indexado |
| priority | number | Recupera prioridade |
| translated | boolean | Recupera valor, se documento é traduzido |
| userNotify | boolean | Recupera valor, se usuário será notificado |
| expires | boolean | Recupera valor, se documento expira |
| volumeId | string | Recupera id do volume |
| updateIsoProperties | boolean | Recupera updateIsoProperties |
| lastModifiedTime | string | Recupera última data de modificação |
| deleted | boolean | Recupera valor, se documento foi deletado |
| imutable | boolean | Recupera valor, se documento é imultavel |
| internalVisualizer | boolean | Recupera valor, se documento pode ser visualizado internamente. |
| crc | number | Recupera valor do crc |
| UUID | string | Recupera valor do UUID |
| phisicalFileSize | number | Recupera valor do tamanho do arquivo fisico |
| permissionType | number | Recupera o tipo de permissão |
| restrictionType | number | Recupera tipo de restrição |
| siteCode | string | Recupera valor do código do site |
| draft | boolean | Recupera valor de draft |
| onCheckout | boolean | Recupera valor, se documento está em checkout |
| iconPath | string | Recupera valor do path do icon |
| versionAction | string | Recupera a ação que serão realizada em relaão a versão documento |
| uploadId | string | Recupera o identificador do upload |
| additionalComments | string | Recupera o valor do comentário nas informações extras |
| inheritSecurity | boolean | Retorna se o documento herda as propriedades do parent |

Example

```
{
  "tenantId" : 12345,
  "documentId" : 12345,
  "version" : 12345,
  "documentTypeId" : "...",
  "languageId" : "...",
  "iconId" : 12345,
  "topicId" : 12345,
  "colleagueId" : "...",
  "documentDescription" : "...",
  "phisicalFile" : "...",
  "keyWord" : "...",
  "createDate" : 12345,
  "approvedDate" : 12345,
  "lastModifiedDate" : 12345,
  "documentType" : "...",
  "expirationDate" : 12345,
  "accessCount" : 12345,
  "atualizationId" : 12345,
  "parentDocumentId" : 12345,
  "visualization" : "...",
  "relatedFiles" : "...",
  "activeVersion" : true,
  "versionDescription" : "...",
  "approvalAndOr" : true,
  "externalDocumentId" : "...",
  "downloadEnabled" : true,
  "approved" : true,
  "validationStartDate" : 12345,
  "publisherId" : "...",
  "cardDescription" : "...",
  "allowMuiltiCardsPerUser" : true,
  "documentPropertyNumber" : 12345,
  "documentPropertyVersion" : 12345,
  "privateDocument" : true,
  "privateColleagueId" : "...",
  "indexed" : true,
  "priority" : 12345,
  "translated" : true,
  "userNotify" : true,
  "expires" : true,
  "volumeId" : "...",
  "updateIsoProperties" : true,
  "lastModifiedTime" : "...",
  "deleted" : true,
  "imutable" : true,
  "internalVisualizer" : true,
  "crc" : 12345,
  "UUID" : "...",
  "phisicalFileSize" : 12345.0,
  "permissionType" : 12345,
  "restrictionType" : 12345,
  "siteCode" : "...",
  "draft" : true,
  "onCheckout" : true,
  "iconPath" : "...",
  "versionAction" : "...",
  "uploadId" : "...",
  "additionalComments" : "...",
  "inheritSecurity" : true
}
```
