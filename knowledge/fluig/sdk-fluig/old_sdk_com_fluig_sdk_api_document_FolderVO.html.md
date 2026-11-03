---
content_hash: de9644ecc4f0ad5adfd7e6dd1fe0899014e6a67d62f2406486161418b49ed943
fetched_at: '2026-11-03T14:35:04.259211+00:00'
page_id: com/fluig/sdk/api/document/FolderVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.document.FolderVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/FolderVO.html
version: 1
---

Package [com.fluig.sdk.api.document](https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/package-summary.html)

## Class FolderVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.document.FolderVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class FolderVO
  extends Object
  implements Serializable
  ```

  Value Object para Folder

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.document.FolderVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `FolderVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAdditionalComments()` | Recupera comentário adicional |
    | `Boolean` | `getApprovalAndOr()` | Recupera valor de approvalAndOr |
    | `String` | `getColleagueId()` | Recupera valor do colleagueId |
    | `Date` | `getCreateDate()` | Recupera valor da data de criação |
    | `String` | `getDocumentDescription()` | Recupera valor de descrição do documento |
    | `Integer` | `getDocumentId()` | Recupera valor do documentoId |
    | `String` | `getDocumentTypeId()` | Recupera id do tipo de documento |
    | `List<String>` | `getDocumentTypes()` | Recupera os tipos de documento |
    | `Boolean` | `getDownloadEnabled()` | Recupera informação se download da pasta está disponível |
    | `Boolean` | `getExpires()` | Informa se a pasta pode expirar |
    | `Map<String,​Object>` | `getFilters()` | Recupera os filtros |
    | `Integer` | `getIconId()` | Recupera valor do iconId |
    | `Boolean` | `getImutable()` | Recupera boolean se pasta é imutavel |
    | `Boolean` | `getInheritSecurity()` | Recupera segurança herdada |
    | `Boolean` | `getInternalVisualizer()` | Recupera valor de visualizador interno |
    | `String` | `getKeyWord()` | Recupera valor da palavra chave |
    | `Boolean` | `getNotifyUser()` | Recupera boolean se usuário será notificado |
    | `Integer` | `getParentFolderId()` | Recupera valor do id da pasta pai |
    | `List<DocumentPermissionVO>` | `getPermissions()` | Recupera lista de permissões |
    | `Integer` | `getPermissionType()` | Recupera tipo de permissão |
    | `Boolean` | `getPrivateDocument()` | Recupera boolean se documento é privado |
    | `List<DocumentApproverVO>` | `getPublisherApprovers()` | Recupera lista de publicadores aprovadores |
    | `String` | `getPublisherId()` | Recupera id do publicador |
    | `List<DocumentRestrictionVO>` | `getRestrictions()` | Recupera lista de restrições de documentos |
    | `Integer` | `getRestrictionType()` | Recupera tipo de restrição |
    | `Long` | `getTenantId()` | Recupera valor do tenantId |
    | `Integer` | `getTopicId()` | Recupera id do topico |
    | `Boolean` | `getUpdateIsoProperties()` | Recupera informação se update de iso properties é permitido |
    | `Integer` | `getVersion()` | Recupera valor da versão |
    | `String` | `getVersionDescription()` | Recupera valor da descrição da versão |
    | `String` | `getVolumeId()` | Recupera id do volume |
    | `void` | `setAdditionalComments​(String additionalComments)` | Atribui valor para comentário adicional |
    | `void` | `setApprovalAndOr​(Boolean approvalAndOr)` | Atribui valor para approvalAndOr |
    | `void` | `setColleagueId​(String colleagueId)` | Atribui valor para colleagueId |
    | `void` | `setCreateDate​(Date createDate)` | Atribui valor a data de criação |
    | `void` | `setDocumentDescription​(String documentDescription)` | Atribui valor para descrição do documento |
    | `void` | `setDocumentId​(Integer documentId)` | Atribui valor para documentId |
    | `void` | `setDocumentTypeId​(String documentTypeId)` | Atribui valor para documentTypeId |
    | `void` | `setDocumentTypes​(List<String> documentTypes)` | Atribui tipo de documentos |
    | `void` | `setDownloadEnabled​(Boolean downloadEnabled)` | Atribui valor para informação se download de pasta está disponível |
    | `void` | `setExpires​(Boolean expires)` | Atribui valor para informar se a pasta pode expirar |
    | `void` | `setFilters​(Map<String,​Object> filters)` | Atribui filtros |
    | `void` | `setIconId​(Integer iconId)` | Atribui valor para iconId |
    | `void` | `setImutable​(Boolean imutable)` | Atribui boolean se pasta será imutavel |
    | `void` | `setInheritSecurity​(Boolean inheritSecurity)` | Atribui valor para segurança herdada |
    | `void` | `setInternalVisualizer​(Boolean internalVisualizer)` | Atribui boolean se pasta possui visualizador interno |
    | `void` | `setKeyWord​(String keyWord)` | Configura valor da palavra chave |
    | `void` | `setNotifyUser​(Boolean notifyUser)` | Atribui boolean se usuário será notificado |
    | `void` | `setParentFolderId​(Integer parentFolderId)` | Atribui valor para id da pasta pai |
    | `void` | `setPermissions​(List<DocumentPermissionVO> permissions)` | Atribui valor para lista de permissões |
    | `void` | `setPermissionType​(Integer permissionType)` | Atribui valor ao tipo de permissão |
    | `void` | `setPrivateDocument​(Boolean privateDocument)` | Atribui boolean se documento é privado |
    | `void` | `setPublisherApprovers​(List<DocumentApproverVO> publisherApprovers)` | Atribui valor para publicadores aprovadores |
    | `void` | `setPublisherId​(String publisherId)` | Atribui valor para id do publicador |
    | `void` | `setRestrictions​(List<DocumentRestrictionVO> restrictions)` | Atribui valor para lista de restrições de documentos |
    | `void` | `setRestrictionType​(Integer restrictionType)` | Atribui valor para tipo de restrição |
    | `void` | `setTenantId​(Long tenantId)` | Atribui valor para tenantId |
    | `void` | `setTopicId​(Integer topicId)` | Atribui valor para topicId |
    | `void` | `setUpdateIsoProperties​(Boolean updateIsoProperties)` | Atribui permitir atualização de iso properties |
    | `void` | `setVersion​(Integer version)` | Atribui valor para versão |
    | `void` | `setVersionDescription​(String versionDescription)` | Atribui valor para descrição da versão |
    | `void` | `setVolumeId​(String volumeId)` | Atribui valor do id do volume |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### FolderVO

      ```
      public FolderVO()
      ```

  + ### Method Detail

    - #### getTenantId

      ```
      public Long getTenantId()
      ```

      Recupera valor do tenantId

      Returns:
      :   Long
    - #### setTenantId

      ```
      public void setTenantId​(Long tenantId)
      ```

      Atribui valor para tenantId

      Parameters:
      :   `tenantId` -
    - #### getDocumentId

      ```
      public Integer getDocumentId()
      ```

      Recupera valor do documentoId

      Returns:
      :   Integer
    - #### setDocumentId

      ```
      public void setDocumentId​(Integer documentId)
      ```

      Atribui valor para documentId

      Parameters:
      :   `documentId` -
    - #### getVersion

      ```
      public Integer getVersion()
      ```

      Recupera valor da versão

      Returns:
      :   Integer
    - #### setVersion

      ```
      public void setVersion​(Integer version)
      ```

      Atribui valor para versão

      Parameters:
      :   `version` -
    - #### getIconId

      ```
      public Integer getIconId()
      ```

      Recupera valor do iconId

      Returns:
      :   Integer
    - #### setIconId

      ```
      public void setIconId​(Integer iconId)
      ```

      Atribui valor para iconId

      Parameters:
      :   `iconId` -
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```

      Recupera valor do colleagueId

      Returns:
      :   Strubg
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```

      Atribui valor para colleagueId

      Parameters:
      :   `colleagueId` -
    - #### getDocumentDescription

      ```
      public String getDocumentDescription()
      ```

      Recupera valor de descrição do documento

      Returns:
      :   String
    - #### setDocumentDescription

      ```
      public void setDocumentDescription​(String documentDescription)
      ```

      Atribui valor para descrição do documento

      Parameters:
      :   `documentDescription` -
    - #### getKeyWord

      ```
      public String getKeyWord()
      ```

      Recupera valor da palavra chave

      Returns:
      :   String
    - #### setKeyWord

      ```
      public void setKeyWord​(String keyWord)
      ```

      Configura valor da palavra chave

      Parameters:
      :   `keyWord` -
    - #### getCreateDate

      ```
      public Date getCreateDate()
      ```

      Recupera valor da data de criação

      Returns:
      :   Date
    - #### setCreateDate

      ```
      public void setCreateDate​(Date createDate)
      ```

      Atribui valor a data de criação

      Parameters:
      :   `createDate` -
    - #### getParentFolderId

      ```
      public Integer getParentFolderId()
      ```

      Recupera valor do id da pasta pai

      Returns:
      :   Integer
    - #### setParentFolderId

      ```
      public void setParentFolderId​(Integer parentFolderId)
      ```

      Atribui valor para id da pasta pai

      Parameters:
      :   `parentFolderId` -
    - #### getPublisherId

      ```
      public String getPublisherId()
      ```

      Recupera id do publicador

      Returns:
      :   String
    - #### setPublisherId

      ```
      public void setPublisherId​(String publisherId)
      ```

      Atribui valor para id do publicador

      Parameters:
      :   `publisherId` -
    - #### getVolumeId

      ```
      public String getVolumeId()
      ```

      Recupera id do volume

      Returns:
      :   String
    - #### setVolumeId

      ```
      public void setVolumeId​(String volumeId)
      ```

      Atribui valor do id do volume

      Parameters:
      :   `volumeId` -
    - #### getPermissionType

      ```
      public Integer getPermissionType()
      ```

      Recupera tipo de permissão

      Returns:
      :   Integer
    - #### setPermissionType

      ```
      public void setPermissionType​(Integer permissionType)
      ```

      Atribui valor ao tipo de permissão

      Parameters:
      :   `permissionType` -
    - #### getRestrictionType

      ```
      public Integer getRestrictionType()
      ```

      Recupera tipo de restrição

      Returns:
      :   Integer
    - #### setRestrictionType

      ```
      public void setRestrictionType​(Integer restrictionType)
      ```

      Atribui valor para tipo de restrição

      Parameters:
      :   `restrictionType` -
    - #### getInheritSecurity

      ```
      public Boolean getInheritSecurity()
      ```

      Recupera segurança herdada

      Returns:
      :   Boolean
    - #### setInheritSecurity

      ```
      public void setInheritSecurity​(Boolean inheritSecurity)
      ```

      Atribui valor para segurança herdada

      Parameters:
      :   `inheritSecurity` -
    - #### getPermissions

      ```
      public List<DocumentPermissionVO> getPermissions()
      ```

      Recupera lista de permissões

      Returns:
      :   List
    - #### setPermissions

      ```
      public void setPermissions​(List<DocumentPermissionVO> permissions)
      ```

      Atribui valor para lista de permissões

      Parameters:
      :   `permissions` -
    - #### getRestrictions

      ```
      public List<DocumentRestrictionVO> getRestrictions()
      ```

      Recupera lista de restrições de documentos

      Returns:
      :   List
    - #### setRestrictions

      ```
      public void setRestrictions​(List<DocumentRestrictionVO> restrictions)
      ```

      Atribui valor para lista de restrições de documentos

      Parameters:
      :   `restrictions` -
    - #### getPublisherApprovers

      ```
      public List<DocumentApproverVO> getPublisherApprovers()
      ```

      Recupera lista de publicadores aprovadores

      Returns:
      :   List
    - #### setPublisherApprovers

      ```
      public void setPublisherApprovers​(List<DocumentApproverVO> publisherApprovers)
      ```

      Atribui valor para publicadores aprovadores

      Parameters:
      :   `publisherApprovers` -
    - #### getAdditionalComments

      ```
      public String getAdditionalComments()
      ```

      Recupera comentário adicional

      Returns:
      :   String
    - #### setAdditionalComments

      ```
      public void setAdditionalComments​(String additionalComments)
      ```

      Atribui valor para comentário adicional

      Parameters:
      :   `additionalComments` -
    - #### getVersionDescription

      ```
      public String getVersionDescription()
      ```

      Recupera valor da descrição da versão

      Returns:
      :   String
    - #### setVersionDescription

      ```
      public void setVersionDescription​(String versionDescription)
      ```

      Atribui valor para descrição da versão

      Parameters:
      :   `versionDescription` -
    - #### getExpires

      ```
      public Boolean getExpires()
      ```

      Informa se a pasta pode expirar

      Returns:
      :   Boolean
    - #### setExpires

      ```
      public void setExpires​(Boolean expires)
      ```

      Atribui valor para informar se a pasta pode expirar

      Parameters:
      :   `expires` -
    - #### getTopicId

      ```
      public Integer getTopicId()
      ```

      Recupera id do topico

      Returns:
      :   Integer
    - #### setTopicId

      ```
      public void setTopicId​(Integer topicId)
      ```

      Atribui valor para topicId

      Parameters:
      :   `topicId` -
    - #### getApprovalAndOr

      ```
      public Boolean getApprovalAndOr()
      ```

      Recupera valor de approvalAndOr

      Returns:
      :   Boolean
    - #### setApprovalAndOr

      ```
      public void setApprovalAndOr​(Boolean approvalAndOr)
      ```

      Atribui valor para approvalAndOr

      Parameters:
      :   `approvalAndOr` -
    - #### getDownloadEnabled

      ```
      public Boolean getDownloadEnabled()
      ```

      Recupera informação se download da pasta está disponível

      Returns:
      :   Boolean
    - #### setDownloadEnabled

      ```
      public void setDownloadEnabled​(Boolean downloadEnabled)
      ```

      Atribui valor para informação se download de pasta está disponível

      Parameters:
      :   `downloadEnabled` -
    - #### getUpdateIsoProperties

      ```
      public Boolean getUpdateIsoProperties()
      ```

      Recupera informação se update de iso properties é permitido

      Returns:
      :   Boolean updateIsoProperties
    - #### setUpdateIsoProperties

      ```
      public void setUpdateIsoProperties​(Boolean updateIsoProperties)
      ```

      Atribui permitir atualização de iso properties

      Parameters:
      :   `updateIsoProperties` -
    - #### getDocumentTypeId

      ```
      public String getDocumentTypeId()
      ```

      Recupera id do tipo de documento

      Returns:
      :   String
    - #### setDocumentTypeId

      ```
      public void setDocumentTypeId​(String documentTypeId)
      ```

      Atribui valor para documentTypeId

      Parameters:
      :   `documentTypeId` -
    - #### getNotifyUser

      ```
      public Boolean getNotifyUser()
      ```

      Recupera boolean se usuário será notificado

      Returns:
      :   Boolean
    - #### setNotifyUser

      ```
      public void setNotifyUser​(Boolean notifyUser)
      ```

      Atribui boolean se usuário será notificado

      Parameters:
      :   `notifyUser` -
    - #### getImutable

      ```
      public Boolean getImutable()
      ```

      Recupera boolean se pasta é imutavel

      Returns:
      :   Boolean
    - #### setImutable

      ```
      public void setImutable​(Boolean imutable)
      ```

      Atribui boolean se pasta será imutavel

      Parameters:
      :   `imutable` -
    - #### getInternalVisualizer

      ```
      public Boolean getInternalVisualizer()
      ```

      Recupera valor de visualizador interno

      Returns:
      :   Boolean
    - #### setInternalVisualizer

      ```
      public void setInternalVisualizer​(Boolean internalVisualizer)
      ```

      Atribui boolean se pasta possui visualizador interno

      Parameters:
      :   `internalVisualizer` -
    - #### getPrivateDocument

      ```
      public Boolean getPrivateDocument()
      ```

      Recupera boolean se documento é privado

      Returns:
      :   Boolean
    - #### setPrivateDocument

      ```
      public void setPrivateDocument​(Boolean privateDocument)
      ```

      Atribui boolean se documento é privado

      Parameters:
      :   `privateDocument` -
    - #### getDocumentTypes

      ```
      public List<String> getDocumentTypes()
      ```

      Recupera os tipos de documento

      Returns:
      :   List
    - #### setDocumentTypes

      ```
      public void setDocumentTypes​(List<String> documentTypes)
      ```

      Atribui tipo de documentos

      Parameters:
      :   `documentTypes` -
    - #### getFilters

      ```
      public Map<String,​Object> getFilters()
      ```

      Recupera os filtros

      Returns:
      :   Map
    - #### setFilters

      ```
      public void setFilters​(Map<String,​Object> filters)
      ```

      Atribui filtros

      Parameters:
      :   `filters` -
