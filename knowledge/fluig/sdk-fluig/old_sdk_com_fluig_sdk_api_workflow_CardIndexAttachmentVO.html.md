---
content_hash: 42586dbd1d4a44d53a1bbe4a7b649bf3e8952e8f3ccd53ba1e6934f56c886be4
fetched_at: '2026-11-03T14:35:05.516383+00:00'
page_id: com/fluig/sdk/api/workflow/CardIndexAttachmentVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.CardIndexAttachmentVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/CardIndexAttachmentVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class CardIndexAttachmentVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.CardIndexAttachmentVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CardIndexAttachmentVO
  extends Object
  implements Serializable
  ```

  Value Object para anexos do card index

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.CardIndexAttachmentVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CardIndexAttachmentVO()` | Nova instância para CardIndexAttachmentVO.java |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Boolean` | `getAttach()` | Recupera valor do attach |
    | `String` | `getFileName()` | Recupera valor do fileName |
    | `Boolean` | `getPrincipal()` | Recupera valor do principal |
    | `void` | `setAttach​(Boolean attach)` | Atribui valor para attach |
    | `void` | `setFileName​(String fileName)` | Atribui valor para fileName |
    | `void` | `setPrincipal​(Boolean principal)` | Atribui valor para principal |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### CardIndexAttachmentVO

      ```
      public CardIndexAttachmentVO()
      ```

      Nova instância para CardIndexAttachmentVO.java

  + ### Method Detail

    - #### getFileName

      ```
      public String getFileName()
      ```

      Recupera valor do fileName

      Returns:
      :   the fileName
    - #### setFileName

      ```
      public void setFileName​(String fileName)
      ```

      Atribui valor para fileName

      Parameters:
      :   `fileName` - the fileName to set
    - #### getPrincipal

      ```
      public Boolean getPrincipal()
      ```

      Recupera valor do principal

      Returns:
      :   the principal
    - #### setPrincipal

      ```
      public void setPrincipal​(Boolean principal)
      ```

      Atribui valor para principal

      Parameters:
      :   `principal` - the principal to set
    - #### getAttach

      ```
      public Boolean getAttach()
      ```

      Recupera valor do attach

      Returns:
      :   the attach
    - #### setAttach

      ```
      public void setAttach​(Boolean attach)
      ```

      Atribui valor para attach

      Parameters:
      :   `attach` - the attach to set
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
