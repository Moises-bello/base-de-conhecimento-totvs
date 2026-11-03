---
content_hash: 555fbd5028d086d0239113cc3a21e332898bf325265b9edeb6c9e5971da9b569
fetched_at: '2026-11-03T14:35:05.676438+00:00'
page_id: com/fluig/sdk/api/workflow/ManagerDefinitionVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.ManagerDefinitionVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/ManagerDefinitionVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class ManagerDefinitionVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.ManagerDefinitionVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ManagerDefinitionVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.ManagerDefinitionVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ManagerDefinitionVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<String>` | `getAllProcessesFromThisDefinition()` |  |
    | `List<String>` | `getProcessesUnderManagement()` |  |
    | `List<String>` | `getUnknownManagement()` |  |
    | `void` | `setProcessesUnderManagement​(List<String> processesUnderManagement)` |  |
    | `void` | `setUnknownManagement​(List<String> unknownManagement)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ManagerDefinitionVO

      ```
      public ManagerDefinitionVO()
      ```

  + ### Method Detail

    - #### setProcessesUnderManagement

      ```
      public void setProcessesUnderManagement​(List<String> processesUnderManagement)
      ```
    - #### getProcessesUnderManagement

      ```
      public List<String> getProcessesUnderManagement()
      ```
    - #### setUnknownManagement

      ```
      public void setUnknownManagement​(List<String> unknownManagement)
      ```
    - #### getUnknownManagement

      ```
      public List<String> getUnknownManagement()
      ```
    - #### getAllProcessesFromThisDefinition

      ```
      public List<String> getAllProcessesFromThisDefinition()
      ```
