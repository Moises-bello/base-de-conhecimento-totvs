---
content_hash: 5256f5770c8bf559c8f539f8290d7be2bde702398cbb59406aa968437a98692d
fetched_at: '2026-11-03T14:35:04.275003+00:00'
page_id: com/fluig/sdk/api/document/RelatedDocumentVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.document.RelatedDocumentVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/RelatedDocumentVO.html
version: 1
---

Package [com.fluig.sdk.api.document](https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/package-summary.html)

## Class RelatedDocumentVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.document.RelatedDocumentVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class RelatedDocumentVO
  extends Object
  implements Serializable
  ```

  Value Object para RelatedDocumento

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.document.RelatedDocumentVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `RelatedDocumentVO()` | Nova instância sem valores definidos |
    | `RelatedDocumentVO​(Long tenantId, Integer relatedDocumentId, Integer version, Integer documentId)` | Nova instância do RelatedDocumentVO informando tenantId, relatedDocumentId, version, documentId |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Integer` | `getDocumentId()` | Retorna documentId |
    | `Integer` | `getRelatedDocumentId()` | Retorna relatedDocumentId |
    | `Long` | `getTenantId()` | Retorna tenantId |
    | `Integer` | `getVersion()` | Retorna versão |
    | `void` | `setDocumentId​(Integer documentId)` | Atribui valor para documentoId |
    | `void` | `setRelatedDocumentId​(Integer relatedDocumentId)` | Atribui valor para relatedDocumentId |
    | `void` | `setTenantId​(Long tenantId)` | Atribui valor para tenantId |
    | `void` | `setVersion​(Integer version)` | Atribui valor para versão |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### RelatedDocumentVO

      ```
      public RelatedDocumentVO()
      ```

      Nova instância sem valores definidos
    - #### RelatedDocumentVO

      ```
      public RelatedDocumentVO​(Long tenantId,
                               Integer relatedDocumentId,
                               Integer version,
                               Integer documentId)
      ```

      Nova instância do RelatedDocumentVO informando
      tenantId, relatedDocumentId, version, documentId

      Parameters:
      :   `tenantId` -
      :   `relatedDocumentId` -
      :   `version` -
      :   `documentId` -

  + ### Method Detail

    - #### getTenantId

      ```
      public Long getTenantId()
      ```

      Retorna tenantId

      Returns:
      :   Long tenantId
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

      Retorna documentId

      Returns:
      :   Integer
    - #### setDocumentId

      ```
      public void setDocumentId​(Integer documentId)
      ```

      Atribui valor para documentoId

      Parameters:
      :   `documentId` -
    - #### getVersion

      ```
      public Integer getVersion()
      ```

      Retorna versão

      Returns:
      :   Integer
    - #### setVersion

      ```
      public void setVersion​(Integer version)
      ```

      Atribui valor para versão

      Parameters:
      :   `version` -
    - #### getRelatedDocumentId

      ```
      public Integer getRelatedDocumentId()
      ```

      Retorna relatedDocumentId

      Returns:
      :   Integer
    - #### setRelatedDocumentId

      ```
      public void setRelatedDocumentId​(Integer relatedDocumentId)
      ```

      Atribui valor para relatedDocumentId

      Parameters:
      :   `relatedDocumentId` -
