---
content_hash: ef3c106fad45322e82a8474deb2d8784c4a4a8e773b0c0f6c53307641dda6f9b
fetched_at: '2026-11-03T14:35:05.808770+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessStateVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessStateVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessStateVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessStateVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessStateVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessStateVO
  extends Object
  implements Serializable
  ```

  Value Object para ProcessState

  Version:
  :   1.5.3

  Author:
  :   marcelo.pereira

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessStateVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessStateVO()` | Cria uma instância do ProcessStateVO |
    | `ProcessStateVO​(long tenantId, int sequence, String stateName, String stateDescription)` | Cria uma instância do ProcessStateVO |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `int` | `getSequence()` | Recupera valor do sequence |
    | `String` | `getStateDescription()` | Recupera valor do stateDescription |
    | `String` | `getStateName()` | Recupera valor do stateName |
    | `long` | `getTenantId()` | Recupera valor do tenantId |
    | `void` | `setSequence​(int sequence)` | Atribui valor para sequence |
    | `void` | `setStateDescription​(String stateDescription)` | Atribui valor para stateDescription |
    | `void` | `setStateName​(String stateName)` | Atribui valor para stateName |
    | `void` | `setTenantId​(long tenantId)` | Atribui valor para tenantId |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessStateVO

      ```
      public ProcessStateVO()
      ```

      Cria uma instância do ProcessStateVO
    - #### ProcessStateVO

      ```
      public ProcessStateVO​(long tenantId,
                            int sequence,
                            String stateName,
                            String stateDescription)
      ```

      Cria uma instância do ProcessStateVO

      Parameters:
      :   `tenantId` - the tenantId to set
      :   `sequence` - the sequence to set
      :   `stateName` - the stateName to set
      :   `stateDescription` - the stateDescription to set

  + ### Method Detail

    - #### getTenantId

      ```
      public long getTenantId()
      ```

      Recupera valor do tenantId

      Returns:
      :   the tenantId
    - #### setTenantId

      ```
      public void setTenantId​(long tenantId)
      ```

      Atribui valor para tenantId

      Parameters:
      :   `tenantId` - the tenantId to set
    - #### getSequence

      ```
      public int getSequence()
      ```

      Recupera valor do sequence

      Returns:
      :   the sequence
    - #### setSequence

      ```
      public void setSequence​(int sequence)
      ```

      Atribui valor para sequence

      Parameters:
      :   `sequence` - the sequence to set
    - #### getStateName

      ```
      public String getStateName()
      ```

      Recupera valor do stateName

      Returns:
      :   the stateName
    - #### setStateName

      ```
      public void setStateName​(String stateName)
      ```

      Atribui valor para stateName

      Parameters:
      :   `stateName` - the stateName to set
    - #### getStateDescription

      ```
      public String getStateDescription()
      ```

      Recupera valor do stateDescription

      Returns:
      :   the stateDescription
    - #### setStateDescription

      ```
      public void setStateDescription​(String stateDescription)
      ```

      Atribui valor para stateDescription

      Parameters:
      :   `stateDescription` - the stateDescription to set
