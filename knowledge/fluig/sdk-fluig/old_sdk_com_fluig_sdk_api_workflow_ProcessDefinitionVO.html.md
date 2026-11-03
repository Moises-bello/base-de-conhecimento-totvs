---
content_hash: 08ad3458e0168b387776b3bd12f4da348e043c3b33c5fc6233cc47107d057a5b
fetched_at: '2026-11-03T14:35:05.707067+00:00'
page_id: com/fluig/sdk/api/workflow/ProcessDefinitionVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ProcessDefinitionVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ProcessDefinitionVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ProcessDefinitionVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ProcessDefinitionVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ProcessDefinitionVO
  extends Object
  implements Serializable
  ```

  Value Object para ProcessDefinition

  Version:
  :   1.6

  Author:
  :   leandro.carlos

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ProcessDefinitionVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ProcessDefinitionVO()` | Construtor padrão do ProcessDefinitionVO |
    | `ProcessDefinitionVO​(String processId, String processDescription)` | Cria uma instância do ProcessDefinitionVO |
    | `ProcessDefinitionVO​(String processId, String processDescription, String icon)` | Cria uma instância do ProcessDefinitionVO com ícone |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getIcon()` | Recupera valor do icon |
    | `String` | `getProcessDescription()` | Recupera valor do processDescription |
    | `String` | `getProcessId()` | Recupera valor do processId |
    | `void` | `setIcon​(String icon)` | Atribui valor para icon |
    | `void` | `setProcessDescription​(String processDescription)` | Atribui valor para processDescription |
    | `void` | `setProcessId​(String processId)` | Atribui valor para processId |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ProcessDefinitionVO

      ```
      public ProcessDefinitionVO()
      ```

      Construtor padrão do ProcessDefinitionVO
    - #### ProcessDefinitionVO

      ```
      public ProcessDefinitionVO​(String processId,
                                 String processDescription)
      ```

      Cria uma instância do ProcessDefinitionVO

      Parameters:
      :   `processId` - the processId to set
      :   `processDescription` - the processDescription to set
    - #### ProcessDefinitionVO

      ```
      public ProcessDefinitionVO​(String processId,
                                 String processDescription,
                                 String icon)
      ```

      Cria uma instância do ProcessDefinitionVO com ícone

      Parameters:
      :   `processId` - the processId to set
      :   `processDescription` - the processDescription to set
      :   `icon` - the icon to set

  + ### Method Detail

    - #### getProcessId

      ```
      public String getProcessId()
      ```

      Recupera valor do processId

      Returns:
      :   the processId
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```

      Atribui valor para processId

      Parameters:
      :   `processId` - the processId to set
    - #### getProcessDescription

      ```
      public String getProcessDescription()
      ```

      Recupera valor do processDescription

      Returns:
      :   the processDescription
    - #### setProcessDescription

      ```
      public void setProcessDescription​(String processDescription)
      ```

      Atribui valor para processDescription

      Parameters:
      :   `processDescription` - the processDescription to set
    - #### getIcon

      ```
      public String getIcon()
      ```

      Recupera valor do icon

      Returns:
      :   the icon
    - #### setIcon

      ```
      public void setIcon​(String icon)
      ```

      Atribui valor para icon

      Parameters:
      :   `icon` - the icon to set
