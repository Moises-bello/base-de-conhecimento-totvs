---
content_hash: 03b8e3eb2b2dee5a7dc80b5d4763b7d0fe9bb5d689e2369a38686f6ea4542c23
fetched_at: '2026-11-03T14:35:03.809013+00:00'
page_id: com/fluig/sdk/api/cardindex/CardFindFieldVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.cardindex.CardFindFieldVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/cardindex/CardFindFieldVO.html
version: 1
---

Package [com.fluig.sdk.api.cardindex](https://api.fluig.com/old/sdk/com/fluig/sdk/api/cardindex/package-summary.html)

## Class CardFindFieldVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.cardindex.CardFindFieldVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CardFindFieldVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.cardindex.CardFindFieldVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CardFindFieldVO()` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Integer` | `getCardId()` |  |
    | `List<CardChildrenVO>` | `getChildren()` |  |
    | `long` | `getCompanyId()` |  |
    | `Integer` | `getParentDocumentId()` |  |
    | `static long` | `getSerialVersionUID()` |  |
    | `List<CardFieldVO>` | `getValues()` |  |
    | `int` | `getVersion()` |  |
    | `boolean` | `isActiveVersion()` |  |
    | `void` | `setActiveVersion​(boolean activeVersion)` |  |
    | `void` | `setCardId​(Integer cardId)` |  |
    | `void` | `setChildren​(List<CardChildrenVO> children)` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setParentDocumentId​(Integer parentDocumentId)` |  |
    | `void` | `setValues​(List<CardFieldVO> values)` |  |
    | `void` | `setVersion​(int version)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### CardFindFieldVO

      ```
      public CardFindFieldVO()
      ```

  + ### Method Detail

    - #### getCardId

      ```
      public Integer getCardId()
      ```
    - #### setCardId

      ```
      public void setCardId​(Integer cardId)
      ```
    - #### getVersion

      ```
      public int getVersion()
      ```
    - #### setVersion

      ```
      public void setVersion​(int version)
      ```
    - #### getCompanyId

      ```
      public long getCompanyId()
      ```
    - #### setCompanyId

      ```
      public void setCompanyId​(long companyId)
      ```
    - #### getParentDocumentId

      ```
      public Integer getParentDocumentId()
      ```
    - #### setParentDocumentId

      ```
      public void setParentDocumentId​(Integer parentDocumentId)
      ```
    - #### isActiveVersion

      ```
      public boolean isActiveVersion()
      ```
    - #### setActiveVersion

      ```
      public void setActiveVersion​(boolean activeVersion)
      ```
    - #### getValues

      ```
      public List<CardFieldVO> getValues()
      ```
    - #### setValues

      ```
      public void setValues​(List<CardFieldVO> values)
      ```
    - #### getSerialVersionUID

      ```
      public static long getSerialVersionUID()
      ```
    - #### getChildren

      ```
      public List<CardChildrenVO> getChildren()
      ```
    - #### setChildren

      ```
      public void setChildren​(List<CardChildrenVO> children)
      ```
