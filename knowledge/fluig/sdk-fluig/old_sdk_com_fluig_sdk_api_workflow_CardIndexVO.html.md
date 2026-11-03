---
content_hash: e21c89b6514cd0d8d07c64d1f1cc7208c13c91d9609c3a03104479f049931baf
fetched_at: '2026-11-03T14:35:05.563199+00:00'
page_id: com/fluig/sdk/api/workflow/CardIndexVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.CardIndexVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/CardIndexVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class CardIndexVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.CardIndexVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CardIndexVO
  extends Object
  implements Serializable
  ```

  Value Object para CardIndex

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.CardIndexVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CardIndexVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<CardIndexAttachmentVO>` | `getAttachments()` | Recupera valor do attachments |
    | `String` | `getCardDescription()` | Recupera valor do cardDescription |
    | `String` | `getDatasetName()` | Recupera valor do datasetName |
    | `String` | `getDocumentDescription()` | Recupera valor do documentDescription |
    | `Integer` | `getDocumentId()` | Recupera valor do documentId |
    | `Integer` | `getParentDocumentId()` | Recupera valor do parentDocumentId |
    | `Integer` | `getPersistenceType()` | Recupera valor do persistenceType |
    | `String` | `getPublisherId()` | Recupera valor do publisherId |
    | `Long` | `getTenantId()` | Recupera valor do tenantId |
    | `void` | `setAttachments​(List<CardIndexAttachmentVO> attachments)` | Atribui valor para attachments |
    | `void` | `setCardDescription​(String cardDescription)` | Atribui valor para cardDescription |
    | `void` | `setDatasetName​(String datasetName)` | Atribui valor para datasetName |
    | `void` | `setDocumentDescription​(String documentDescription)` | Atribui valor para documentDescription |
    | `void` | `setDocumentId​(Integer documentId)` | Atribui valor para documentId |
    | `void` | `setParentDocumentId​(Integer parentDocumentId)` | Atribui valor para parentDocumentId |
    | `void` | `setPersistenceType​(Integer persistenceType)` | Atribui valor para persistenceType |
    | `void` | `setPublisherId​(String publisherId)` | Atribui valor para publisherId |
    | `void` | `setTenantId​(Long tenantId)` | Atribui valor para tenantId |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### CardIndexVO

      ```
      public CardIndexVO()
      ```

  + ### Method Detail

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
    - #### getPublisherId

      ```
      public String getPublisherId()
      ```

      Recupera valor do publisherId

      Returns:
      :   the publisherId
    - #### setPublisherId

      ```
      public void setPublisherId​(String publisherId)
      ```

      Atribui valor para publisherId

      Parameters:
      :   `publisherId` - the publisherId to set
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
    - #### getCardDescription

      ```
      public String getCardDescription()
      ```

      Recupera valor do cardDescription

      Returns:
      :   the cardDescription
    - #### setCardDescription

      ```
      public void setCardDescription​(String cardDescription)
      ```

      Atribui valor para cardDescription

      Parameters:
      :   `cardDescription` - the cardDescription to set
    - #### getDatasetName

      ```
      public String getDatasetName()
      ```

      Recupera valor do datasetName

      Returns:
      :   the datasetName
    - #### setDatasetName

      ```
      public void setDatasetName​(String datasetName)
      ```

      Atribui valor para datasetName

      Parameters:
      :   `datasetName` - the datasetName to set
    - #### getPersistenceType

      ```
      public Integer getPersistenceType()
      ```

      Recupera valor do persistenceType

      Returns:
      :   the persistenceType
    - #### setPersistenceType

      ```
      public void setPersistenceType​(Integer persistenceType)
      ```

      Atribui valor para persistenceType

      Parameters:
      :   `persistenceType` - the persistenceType to set
    - #### getAttachments

      ```
      public List<CardIndexAttachmentVO> getAttachments()
      ```

      Recupera valor do attachments

      Returns:
      :   the attachments
    - #### setAttachments

      ```
      public void setAttachments​(List<CardIndexAttachmentVO> attachments)
      ```

      Atribui valor para attachments

      Parameters:
      :   `attachments` - the attachments to set
