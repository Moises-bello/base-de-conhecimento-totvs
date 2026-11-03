---
content_hash: 834af6b6a91e1462b52d54120ca0f259b852bfb277e64c67f96f0dce91ea30c0
fetched_at: '2026-11-03T14:35:05.538770+00:00'
page_id: com/fluig/sdk/api/workflow/CardIndexCreateVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.CardIndexCreateVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/CardIndexCreateVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class CardIndexCreateVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.CardIndexCreateVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CardIndexCreateVO
  extends Object
  implements Serializable
  ```

  Value Object para Criação de Card Index

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.CardIndexCreateVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CardIndexCreateVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<CardIndexAttachmentCreateVO>` | `getAttachments()` | Recupera valor do attachments |
    | `String` | `getCardDescription()` | Recupera valor do cardDescription |
    | `String` | `getDatasetName()` | Recupera valor do datasetName |
    | `String` | `getDocumentDescription()` | Recupera valor do documentDescription |
    | `Integer` | `getParentDocumentId()` | Recupera valor do parentDocumentId |
    | `Integer` | `getPersistenceType()` | Recupera valor do persistenceType |
    | `String` | `getPublisherId()` | Recupera valor do publisherId |
    | `Long` | `getTenantId()` | Recupera valor do tenantId |
    | `void` | `setAttachments​(List<CardIndexAttachmentCreateVO> attachments)` | Atribui valor para attachments |
    | `void` | `setCardDescription​(String cardDescription)` | Atribui valor para cardDescription |
    | `void` | `setDatasetName​(String datasetName)` | Atribui valor para datasetName |
    | `void` | `setDocumentDescription​(String documentDescription)` | Atribui valor para documentDescription |
    | `void` | `setParentDocumentId​(Integer parentDocumentId)` | Atribui valor para parentDocumentId |
    | `void` | `setPersistenceType​(Integer persistenceType)` | Atribui valor para persistenceType |
    | `void` | `setPublisherId​(String publisherId)` | Atribui valor para publisherId |
    | `void` | `setTenantId​(Long tenantId)` | Atribui valor para tenantId |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### CardIndexCreateVO

      ```
      public CardIndexCreateVO()
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
      public List<CardIndexAttachmentCreateVO> getAttachments()
      ```

      Recupera valor do attachments

      Returns:
      :   the attachments
    - #### setAttachments

      ```
      public void setAttachments​(List<CardIndexAttachmentCreateVO> attachments)
      ```

      Atribui valor para attachments

      Parameters:
      :   `attachments` - the attachments to set
