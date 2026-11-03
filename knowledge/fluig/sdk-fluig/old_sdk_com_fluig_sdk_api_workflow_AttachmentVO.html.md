---
content_hash: 14176e5eeb12aa43431b87ca6a216729f1fcc39f51c8591d93b726abef589e53
fetched_at: '2026-11-03T14:35:05.160321+00:00'
page_id: com/fluig/sdk/api/workflow/AttachmentVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.AttachmentVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/AttachmentVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class AttachmentVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.AttachmentVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AttachmentVO
  extends Object
  implements Serializable
  ```

  Value Object para Anexos

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.AttachmentVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AttachmentVO()` | Nova instância para AttachmentVO.java |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAbsoluteFileName()` | Recupera valor do absoluteFileName |
    | `Boolean` | `getAttach()` | Recupera valor do attach |
    | `String` | `getFileName()` | Recupera valor do fileName |
    | `Boolean` | `getPrincipal()` | Recupera valor do principal |
    | `void` | `setAbsoluteFileName​(String absoluteFileName)` | Atribui valor para absoluteFileName |
    | `void` | `setAttach​(Boolean attach)` | Atribui valor para attach |
    | `void` | `setFileName​(String fileName)` | Atribui valor para fileName |
    | `void` | `setPrincipal​(Boolean principal)` | Atribui valor para principal |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### AttachmentVO

      ```
      public AttachmentVO()
      ```

      Nova instância para AttachmentVO.java

  + ### Method Detail

    - #### getAbsoluteFileName

      ```
      public String getAbsoluteFileName()
      ```

      Recupera valor do absoluteFileName

      Returns:
      :   the absoluteFileName
    - #### setAbsoluteFileName

      ```
      public void setAbsoluteFileName​(String absoluteFileName)
      ```

      Atribui valor para absoluteFileName

      Parameters:
      :   `absoluteFileName` - the absoluteFileName to set
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
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
