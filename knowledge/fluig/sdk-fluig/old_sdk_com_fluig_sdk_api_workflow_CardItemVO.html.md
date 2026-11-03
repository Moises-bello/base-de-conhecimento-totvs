---
content_hash: 2ce42c3338fe6b8ff2d9549bad2f6ddd144a253a26946701f1185ad6a31c60b9
fetched_at: '2026-11-03T14:35:05.635755+00:00'
page_id: com/fluig/sdk/api/workflow/CardItemVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.CardItemVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/CardItemVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class CardItemVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.CardItemVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CardItemVO
  extends Object
  implements Serializable
  ```

  Value Object para CardItem

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.CardItemVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CardItemVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAdditionalComments()` | Recupera valor do additionalComments |
    | `List<AttachmentVO>` | `getAttachments()` | Recupera valor do attachments |
    | `String` | `getColleagueId()` | Recupera valor do colleagueId |
    | `String` | `getDocumentDescription()` | Recupera valor do documentDescription |
    | `Integer` | `getDocumentId()` | Recupera valor do documentId |
    | `String` | `getDocumentType()` | Recupera valor do documentType |
    | `String` | `getDocumentTypeId()` | Recupera valor do documentTypeId |
    | `Boolean` | `getDownloadEnabled()` | Recupera valor do downloadEnabled |
    | `Date` | `getExpirationDate()` | Recupera valor do expirationDate |
    | `Boolean` | `getExpires()` | Recupera valor do expires |
    | `List<Map<String,​String>>` | `getFormData()` | Recupera valor do formData |
    | `Integer` | `getIconId()` | Recupera valor do iconId |
    | `Boolean` | `getImutable()` | Recupera valor do imutable |
    | `Boolean` | `getInheritSecurity()` | Recupera valor do inheritSecurity |
    | `Boolean` | `getInternalVisualizer()` | Recupera valor do internalVisualizer |
    | `String` | `getKeyWord()` | Recupera valor do keyWord |
    | `String` | `getLanguageId()` | Recupera valor do languageId |
    | `Integer` | `getMetaListId()` | Recupera valor do metaListId |
    | `Integer` | `getNotificationDays()` | Recupera valor do notificationDays |
    | `Integer` | `getParentDocumentId()` | Recupera valor do parentDocumentId |
    | `List<DocumentPermissionVO>` | `getPermissions()` | Recupera valor do permissions |
    | `Integer` | `getPermissionType()` | Recupera valor do permissionType |
    | `Boolean` | `getPrivateDocument()` | Recupera valor do privateDocument |
    | `List<DocumentApproverVO>` | `getPublisherApprovers()` | Recupera valor do publisherApprovers |
    | `List<RelatedDocumentVO>` | `getRelatedDocuments()` | Recupera valor do relatedDocuments |
    | `List<DocumentRestrictionVO>` | `getRestrictions()` | Recupera valor do restrictions |
    | `Integer` | `getRestrictionType()` | Recupera valor do restrictionType |
    | `Long` | `getTenantId()` | Recupera valor do tenantId |
    | `Integer` | `getTopicId()` | Recupera valor do topicId |
    | `Boolean` | `getUpdateIsoProperties()` | Recupera valor do updateIsoProperties |
    | `Boolean` | `getUserNotify()` | Recupera valor do userNotify |
    | `Date` | `getValidationStartDate()` | Recupera valor do validationStartDate |
    | `Integer` | `getVersion()` | Recupera valor do version |
    | `String` | `getVersionDescription()` | Recupera valor do versionDescription |
    | `String` | `getVersionOption()` | Recupera valor do versionOption |
    | `void` | `setAdditionalComments​(String additionalComments)` | Atribui valor para additionalComments |
    | `void` | `setAttachments​(List<AttachmentVO> attachments)` | Atribui valor para attachments |
    | `void` | `setColleagueId​(String colleagueId)` | Atribui valor para colleagueId |
    | `void` | `setDocumentDescription​(String documentDescription)` | Atribui valor para documentDescription |
    | `void` | `setDocumentId​(Integer documentId)` | Atribui valor para documentId |
    | `void` | `setDocumentType​(String documentType)` | Atribui valor para documentType |
    | `void` | `setDocumentTypeId​(String documentTypeId)` | Atribui valor para documentTypeId |
    | `void` | `setDownloadEnabled​(Boolean downloadEnabled)` | Atribui valor para downloadEnabled |
    | `void` | `setExpirationDate​(Date expirationDate)` | Atribui valor para expirationDate |
    | `void` | `setExpires​(Boolean expires)` | Atribui valor para expires |
    | `void` | `setFormData​(List<Map<String,​String>> formData)` | Atribui valor para formData |
    | `void` | `setIconId​(Integer iconId)` | Atribui valor para iconId |
    | `void` | `setImutable​(Boolean imutable)` | Atribui valor para imutable |
    | `void` | `setInheritSecurity​(Boolean inheritSecurity)` | Atribui valor para inheritSecurity |
    | `void` | `setInternalVisualizer​(Boolean internalVisualizer)` | Atribui valor para internalVisualizer |
    | `void` | `setKeyWord​(String keyWord)` | Atribui valor para keyWord |
    | `void` | `setLanguageId​(String languageId)` | Atribui valor para languageId |
    | `void` | `setMetaListId​(Integer metaListId)` | Atribui valor para metaListId |
    | `void` | `setNotificationDays​(Integer notificationDays)` | Atribui valor para notificationDays |
    | `void` | `setParentDocumentId​(Integer parentDocumentId)` | Atribui valor para parentDocumentId |
    | `void` | `setPermissions​(List<DocumentPermissionVO> permissions)` | Atribui valor para permissions |
    | `void` | `setPermissionType​(Integer permissionType)` | Atribui valor para permissionType |
    | `void` | `setPrivateDocument​(Boolean privateDocument)` | Atribui valor para privateDocument |
    | `void` | `setPublisherApprovers​(List<DocumentApproverVO> publisherApprovers)` | Atribui valor para publisherApprovers |
    | `void` | `setRelatedDocuments​(List<RelatedDocumentVO> relatedDocuments)` | Atribui valor para relatedDocuments |
    | `void` | `setRestrictions​(List<DocumentRestrictionVO> restrictions)` | Atribui valor para restrictions |
    | `void` | `setRestrictionType​(Integer restrictionType)` | Atribui valor para restrictionType |
    | `void` | `setTenantId​(Long tenantId)` | Atribui valor para tenantId |
    | `void` | `setTopicId​(Integer topicId)` | Atribui valor para topicId |
    | `void` | `setUpdateIsoProperties​(Boolean updateIsoProperties)` | Atribui valor para updateIsoProperties |
    | `void` | `setUserNotify​(Boolean userNotify)` | Atribui valor para userNotify |
    | `void` | `setValidationStartDate​(Date validationStartDate)` | Atribui valor para validationStartDate |
    | `void` | `setVersion​(Integer version)` | Atribui valor para version |
    | `void` | `setVersionDescription​(String versionDescription)` | Atribui valor para versionDescription |
    | `void` | `setVersionOption​(String versionOption)` | Atribui valor para versionOption |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### CardItemVO

      ```
      public CardItemVO()
      ```

  + ### Method Detail

    - #### getDocumentId

      ```
      public Integer getDocumentId()
      ```

      Recupera valor do documentId

      Returns:
      :   the documentId
    - #### setDocumentId

      ```
      public void setDocumentId​(Integer documentId)
      ```

      Atribui valor para documentId

      Parameters:
      :   `documentId` - the documentId to set
    - #### getDocumentDescription

      ```
      public String getDocumentDescription()
      ```

      Recupera valor do documentDescription

      Returns:
      :   the documentDescription
    - #### setDocumentDescription

      ```
      public void setDocumentDescription​(String documentDescription)
      ```

      Atribui valor para documentDescription

      Parameters:
      :   `documentDescription` - the documentDescription to set
    - #### getParentDocumentId

      ```
      public Integer getParentDocumentId()
      ```

      Recupera valor do parentDocumentId

      Returns:
      :   the parentDocumentId
    - #### setParentDocumentId

      ```
      public void setParentDocumentId​(Integer parentDocumentId)
      ```

      Atribui valor para parentDocumentId

      Parameters:
      :   `parentDocumentId` - the parentDocumentId to set
    - #### getPrivateDocument

      ```
      public Boolean getPrivateDocument()
      ```

      Recupera valor do privateDocument

      Returns:
      :   the privateDocument
    - #### setPrivateDocument

      ```
      public void setPrivateDocument​(Boolean privateDocument)
      ```

      Atribui valor para privateDocument

      Parameters:
      :   `privateDocument` - the privateDocument to set
    - #### getTenantId

      ```
      public Long getTenantId()
      ```

      Recupera valor do tenantId

      Returns:
      :   the tenantId
    - #### setTenantId

      ```
      public void setTenantId​(Long tenantId)
      ```

      Atribui valor para tenantId

      Parameters:
      :   `tenantId` - the tenantId to set
    - #### getVersion

      ```
      public Integer getVersion()
      ```

      Recupera valor do version

      Returns:
      :   the version
    - #### setVersion

      ```
      public void setVersion​(Integer version)
      ```

      Atribui valor para version

      Parameters:
      :   `version` - the version to set
    - #### getMetaListId

      ```
      public Integer getMetaListId()
      ```

      Recupera valor do metaListId

      Returns:
      :   the metaListId
    - #### setMetaListId

      ```
      public void setMetaListId​(Integer metaListId)
      ```

      Atribui valor para metaListId

      Parameters:
      :   `metaListId` - the metaListId to set
    - #### getInheritSecurity

      ```
      public Boolean getInheritSecurity()
      ```

      Recupera valor do inheritSecurity

      Returns:
      :   the inheritSecurity
    - #### setInheritSecurity

      ```
      public void setInheritSecurity​(Boolean inheritSecurity)
      ```

      Atribui valor para inheritSecurity

      Parameters:
      :   `inheritSecurity` - the inheritSecurity to set
    - #### getPermissionType

      ```
      public Integer getPermissionType()
      ```

      Recupera valor do permissionType

      Returns:
      :   the permissionType
    - #### setPermissionType

      ```
      public void setPermissionType​(Integer permissionType)
      ```

      Atribui valor para permissionType

      Parameters:
      :   `permissionType` - the permissionType to set
    - #### getRestrictionType

      ```
      public Integer getRestrictionType()
      ```

      Recupera valor do restrictionType

      Returns:
      :   the restrictionType
    - #### setRestrictionType

      ```
      public void setRestrictionType​(Integer restrictionType)
      ```

      Atribui valor para restrictionType

      Parameters:
      :   `restrictionType` - the restrictionType to set
    - #### getUserNotify

      ```
      public Boolean getUserNotify()
      ```

      Recupera valor do userNotify

      Returns:
      :   the userNotify
    - #### setUserNotify

      ```
      public void setUserNotify​(Boolean userNotify)
      ```

      Atribui valor para userNotify

      Parameters:
      :   `userNotify` - the userNotify to set
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```

      Recupera valor do colleagueId

      Returns:
      :   the colleagueId
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```

      Atribui valor para colleagueId

      Parameters:
      :   `colleagueId` - the colleagueId to set
    - #### getAdditionalComments

      ```
      public String getAdditionalComments()
      ```

      Recupera valor do additionalComments

      Returns:
      :   the additionalComments
    - #### setAdditionalComments

      ```
      public void setAdditionalComments​(String additionalComments)
      ```

      Atribui valor para additionalComments

      Parameters:
      :   `additionalComments` - the additionalComments to set
    - #### getKeyWord

      ```
      public String getKeyWord()
      ```

      Recupera valor do keyWord

      Returns:
      :   the keyWord
    - #### setKeyWord

      ```
      public void setKeyWord​(String keyWord)
      ```

      Atribui valor para keyWord

      Parameters:
      :   `keyWord` - the keyWord to set
    - #### getVersionDescription

      ```
      public String getVersionDescription()
      ```

      Recupera valor do versionDescription

      Returns:
      :   the versionDescription
    - #### setVersionDescription

      ```
      public void setVersionDescription​(String versionDescription)
      ```

      Atribui valor para versionDescription

      Parameters:
      :   `versionDescription` - the versionDescription to set
    - #### getVersionOption

      ```
      public String getVersionOption()
      ```

      Recupera valor do versionOption

      Returns:
      :   the versionOption
    - #### setVersionOption

      ```
      public void setVersionOption​(String versionOption)
      ```

      Atribui valor para versionOption

      Parameters:
      :   `versionOption` - the versionOption to set
    - #### getExpires

      ```
      public Boolean getExpires()
      ```

      Recupera valor do expires

      Returns:
      :   the expires
    - #### setExpires

      ```
      public void setExpires​(Boolean expires)
      ```

      Atribui valor para expires

      Parameters:
      :   `expires` - the expires to set
    - #### getTopicId

      ```
      public Integer getTopicId()
      ```

      Recupera valor do topicId

      Returns:
      :   the topicId
    - #### setTopicId

      ```
      public void setTopicId​(Integer topicId)
      ```

      Atribui valor para topicId

      Parameters:
      :   `topicId` - the topicId to set
    - #### getIconId

      ```
      public Integer getIconId()
      ```

      Recupera valor do iconId

      Returns:
      :   the iconId
    - #### setIconId

      ```
      public void setIconId​(Integer iconId)
      ```

      Atribui valor para iconId

      Parameters:
      :   `iconId` - the iconId to set
    - #### getImutable

      ```
      public Boolean getImutable()
      ```

      Recupera valor do imutable

      Returns:
      :   the imutable
    - #### setImutable

      ```
      public void setImutable​(Boolean imutable)
      ```

      Atribui valor para imutable

      Parameters:
      :   `imutable` - the imutable to set
    - #### getLanguageId

      ```
      public String getLanguageId()
      ```

      Recupera valor do languageId

      Returns:
      :   the languageId
    - #### setLanguageId

      ```
      public void setLanguageId​(String languageId)
      ```

      Atribui valor para languageId

      Parameters:
      :   `languageId` - the languageId to set
    - #### getInternalVisualizer

      ```
      public Boolean getInternalVisualizer()
      ```

      Recupera valor do internalVisualizer

      Returns:
      :   the internalVisualizer
    - #### setInternalVisualizer

      ```
      public void setInternalVisualizer​(Boolean internalVisualizer)
      ```

      Atribui valor para internalVisualizer

      Parameters:
      :   `internalVisualizer` - the internalVisualizer to set
    - #### getDownloadEnabled

      ```
      public Boolean getDownloadEnabled()
      ```

      Recupera valor do downloadEnabled

      Returns:
      :   the downloadEnabled
    - #### setDownloadEnabled

      ```
      public void setDownloadEnabled​(Boolean downloadEnabled)
      ```

      Atribui valor para downloadEnabled

      Parameters:
      :   `downloadEnabled` - the downloadEnabled to set
    - #### getUpdateIsoProperties

      ```
      public Boolean getUpdateIsoProperties()
      ```

      Recupera valor do updateIsoProperties

      Returns:
      :   the updateIsoProperties
    - #### setUpdateIsoProperties

      ```
      public void setUpdateIsoProperties​(Boolean updateIsoProperties)
      ```

      Atribui valor para updateIsoProperties

      Parameters:
      :   `updateIsoProperties` - the updateIsoProperties to set
    - #### getDocumentTypeId

      ```
      public String getDocumentTypeId()
      ```

      Recupera valor do documentTypeId

      Returns:
      :   the documentTypeId
    - #### setDocumentTypeId

      ```
      public void setDocumentTypeId​(String documentTypeId)
      ```

      Atribui valor para documentTypeId

      Parameters:
      :   `documentTypeId` - the documentTypeId to set
    - #### getNotificationDays

      ```
      public Integer getNotificationDays()
      ```

      Recupera valor do notificationDays

      Returns:
      :   the notificationDays
    - #### setNotificationDays

      ```
      public void setNotificationDays​(Integer notificationDays)
      ```

      Atribui valor para notificationDays

      Parameters:
      :   `notificationDays` - the notificationDays to set
    - #### getValidationStartDate

      ```
      public Date getValidationStartDate()
      ```

      Recupera valor do validationStartDate

      Returns:
      :   the validationStartDate
    - #### setValidationStartDate

      ```
      public void setValidationStartDate​(Date validationStartDate)
      ```

      Atribui valor para validationStartDate

      Parameters:
      :   `validationStartDate` - the validationStartDate to set
    - #### getExpirationDate

      ```
      public Date getExpirationDate()
      ```

      Recupera valor do expirationDate

      Returns:
      :   the expirationDate
    - #### setExpirationDate

      ```
      public void setExpirationDate​(Date expirationDate)
      ```

      Atribui valor para expirationDate

      Parameters:
      :   `expirationDate` - the expirationDate to set
    - #### getDocumentType

      ```
      public String getDocumentType()
      ```

      Recupera valor do documentType

      Returns:
      :   the documentType
    - #### setDocumentType

      ```
      public void setDocumentType​(String documentType)
      ```

      Atribui valor para documentType

      Parameters:
      :   `documentType` - the documentType to set
    - #### getPermissions

      ```
      public List<DocumentPermissionVO> getPermissions()
      ```

      Recupera valor do permissions

      Returns:
      :   the permissions
    - #### setPermissions

      ```
      public void setPermissions​(List<DocumentPermissionVO> permissions)
      ```

      Atribui valor para permissions

      Parameters:
      :   `permissions` - the permissions to set
    - #### getRestrictions

      ```
      public List<DocumentRestrictionVO> getRestrictions()
      ```

      Recupera valor do restrictions

      Returns:
      :   the restrictions
    - #### setRestrictions

      ```
      public void setRestrictions​(List<DocumentRestrictionVO> restrictions)
      ```

      Atribui valor para restrictions

      Parameters:
      :   `restrictions` - the restrictions to set
    - #### getPublisherApprovers

      ```
      public List<DocumentApproverVO> getPublisherApprovers()
      ```

      Recupera valor do publisherApprovers

      Returns:
      :   the publisherApprovers
    - #### setPublisherApprovers

      ```
      public void setPublisherApprovers​(List<DocumentApproverVO> publisherApprovers)
      ```

      Atribui valor para publisherApprovers

      Parameters:
      :   `publisherApprovers` - the publisherApprovers to set
    - #### getRelatedDocuments

      ```
      public List<RelatedDocumentVO> getRelatedDocuments()
      ```

      Recupera valor do relatedDocuments

      Returns:
      :   the relatedDocuments
    - #### setRelatedDocuments

      ```
      public void setRelatedDocuments​(List<RelatedDocumentVO> relatedDocuments)
      ```

      Atribui valor para relatedDocuments

      Parameters:
      :   `relatedDocuments` - the relatedDocuments to set
    - #### getAttachments

      ```
      public List<AttachmentVO> getAttachments()
      ```

      Recupera valor do attachments

      Returns:
      :   the attachments
    - #### setAttachments

      ```
      public void setAttachments​(List<AttachmentVO> attachments)
      ```

      Atribui valor para attachments

      Parameters:
      :   `attachments` - the attachments to set
    - #### getFormData

      ```
      public List<Map<String,​String>> getFormData()
      ```

      Recupera valor do formData

      Returns:
      :   the formData
    - #### setFormData

      ```
      public void setFormData​(List<Map<String,​String>> formData)
      ```

      Atribui valor para formData

      Parameters:
      :   `formData` - the formData to set
