---
content_hash: 8e3814458650888b7585c26e3dbcf5285588e9f235c33ae171dcb030075185d2
fetched_at: '2026-11-03T14:35:05.075238+00:00'
page_id: com/fluig/sdk/api/task/TaskTransferVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.task.TaskTransferVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/TaskTransferVO.html
version: 1
---

Package [com.fluig.sdk.api.task](https://api.fluig.com/old/sdk/com/fluig/sdk/api/task/package-summary.html)

## Class TaskTransferVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.task.TaskTransferVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class TaskTransferVO
  extends Object
  implements Serializable
  ```

  Value Object para Transferência de Pendências

  Version:
  :   1.00.000

  Author:
  :   Deividi Silva

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.task.TaskTransferVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `TaskTransferVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Integer` | `getDocumentIdFinal()` | Recupera valor do documentIdFinal |
    | `Integer` | `getDocumentIdInitial()` | Recupera valor do documentIdInitial |
    | `Integer` | `getInstanceIdFinal()` | Recupera valor do instanceIdFinal |
    | `Integer` | `getInstanceIdInitial()` | Recupera valor do instanceIdInitial |
    | `Boolean` | `getTransferActiveDocuments()` | Recupera valor do transferActiveDocuments |
    | `Boolean` | `getTransferApprovals()` | Recupera valor do transferApprovals |
    | `Boolean` | `getTransferApprovers()` | Recupera valor do transferApprovers |
    | `Boolean` | `getTransferDocumentSecurity()` | Recupera valor do transferDocumentSecurity |
    | `Boolean` | `getTransferMyDocumentsInApproval()` | Recupera valor do transferMyDocumentsInApproval |
    | `Boolean` | `getTransferOpenWorkflow()` | Recupera valor do transferOpenWorkflow |
    | `Boolean` | `getTransferPendingWorkflow()` | Recupera valor do transferPendingWorkflow |
    | `String` | `getUserFrom()` | Recupera valor do userFrom |
    | `String` | `getUserTo()` | Recupera valor do userTo |
    | `void` | `setDocumentIdFinal​(Integer documentIdFinal)` | Atribui valor para documentIdFinal |
    | `void` | `setDocumentIdInitial​(Integer documentIdInitial)` | Atribui valor para documentIdInitial |
    | `void` | `setInstanceIdFinal​(Integer instanceIdFinal)` | Atribui valor para instanceIdFinal |
    | `void` | `setInstanceIdInitial​(Integer instanceIdInitial)` | Atribui valor para instanceIdInitial |
    | `void` | `setTransferActiveDocuments​(Boolean transferActiveDocuments)` | Atribui valor para transferActiveDocuments |
    | `void` | `setTransferApprovals​(Boolean transferApprovals)` | Atribui valor para transferApprovals |
    | `void` | `setTransferApprovers​(Boolean transferApprovers)` | Atribui valor para transferApprovers |
    | `void` | `setTransferDocumentSecurity​(Boolean transferDocumentSecurity)` | Atribui valor para transferDocumentSecurity |
    | `void` | `setTransferMyDocumentsInApproval​(Boolean transferMyDocumentsInApproval)` | Atribui valor para transferMyDocumentsInApproval |
    | `void` | `setTransferOpenWorkflow​(Boolean transferOpenWorkflow)` | Atribui valor para transferOpenWorkflow |
    | `void` | `setTransferPendingWorkflow​(Boolean transferPendingWorkflow)` | Atribui valor para transferPendingWorkflow |
    | `void` | `setUserFrom​(String userFrom)` | Atribui valor para userFrom |
    | `void` | `setUserTo​(String userTo)` | Atribui valor para userTo |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### TaskTransferVO

      ```
      public TaskTransferVO()
      ```

  + ### Method Detail

    - #### getUserTo

      ```
      public String getUserTo()
      ```

      Recupera valor do userTo

      Returns:
      :   the userTo
    - #### setUserTo

      ```
      public void setUserTo​(String userTo)
      ```

      Atribui valor para userTo

      Parameters:
      :   `userTo` - the userTo to set
    - #### getUserFrom

      ```
      public String getUserFrom()
      ```

      Recupera valor do userFrom

      Returns:
      :   the userFrom
    - #### setUserFrom

      ```
      public void setUserFrom​(String userFrom)
      ```

      Atribui valor para userFrom

      Parameters:
      :   `userFrom` - the userFrom to set
    - #### getTransferActiveDocuments

      ```
      public Boolean getTransferActiveDocuments()
      ```

      Recupera valor do transferActiveDocuments

      Returns:
      :   the transferActiveDocuments
    - #### setTransferActiveDocuments

      ```
      public void setTransferActiveDocuments​(Boolean transferActiveDocuments)
      ```

      Atribui valor para transferActiveDocuments

      Parameters:
      :   `transferActiveDocuments` - the transferActiveDocuments to set
    - #### getTransferMyDocumentsInApproval

      ```
      public Boolean getTransferMyDocumentsInApproval()
      ```

      Recupera valor do transferMyDocumentsInApproval

      Returns:
      :   the transferMyDocumentsInApproval
    - #### setTransferMyDocumentsInApproval

      ```
      public void setTransferMyDocumentsInApproval​(Boolean transferMyDocumentsInApproval)
      ```

      Atribui valor para transferMyDocumentsInApproval

      Parameters:
      :   `transferMyDocumentsInApproval` - the transferMyDocumentsInApproval to set
    - #### getTransferPendingWorkflow

      ```
      public Boolean getTransferPendingWorkflow()
      ```

      Recupera valor do transferPendingWorkflow

      Returns:
      :   the transferPendingWorkflow
    - #### setTransferPendingWorkflow

      ```
      public void setTransferPendingWorkflow​(Boolean transferPendingWorkflow)
      ```

      Atribui valor para transferPendingWorkflow

      Parameters:
      :   `transferPendingWorkflow` - the transferPendingWorkflow to set
    - #### getTransferOpenWorkflow

      ```
      public Boolean getTransferOpenWorkflow()
      ```

      Recupera valor do transferOpenWorkflow

      Returns:
      :   the transferOpenWorkflow
    - #### setTransferOpenWorkflow

      ```
      public void setTransferOpenWorkflow​(Boolean transferOpenWorkflow)
      ```

      Atribui valor para transferOpenWorkflow

      Parameters:
      :   `transferOpenWorkflow` - the transferOpenWorkflow to set
    - #### getTransferApprovers

      ```
      public Boolean getTransferApprovers()
      ```

      Recupera valor do transferApprovers

      Returns:
      :   the transferApprovers
    - #### setTransferApprovers

      ```
      public void setTransferApprovers​(Boolean transferApprovers)
      ```

      Atribui valor para transferApprovers

      Parameters:
      :   `transferApprovers` - the transferApprovers to set
    - #### getTransferApprovals

      ```
      public Boolean getTransferApprovals()
      ```

      Recupera valor do transferApprovals

      Returns:
      :   the transferApprovals
    - #### setTransferApprovals

      ```
      public void setTransferApprovals​(Boolean transferApprovals)
      ```

      Atribui valor para transferApprovals

      Parameters:
      :   `transferApprovals` - the transferApprovals to set
    - #### getTransferDocumentSecurity

      ```
      public Boolean getTransferDocumentSecurity()
      ```

      Recupera valor do transferDocumentSecurity

      Returns:
      :   the transferDocumentSecurity
    - #### setTransferDocumentSecurity

      ```
      public void setTransferDocumentSecurity​(Boolean transferDocumentSecurity)
      ```

      Atribui valor para transferDocumentSecurity

      Parameters:
      :   `transferDocumentSecurity` - the transferDocumentSecurity to set
    - #### getInstanceIdInitial

      ```
      public Integer getInstanceIdInitial()
      ```

      Recupera valor do instanceIdInitial

      Returns:
      :   the instanceIdInitial
    - #### setInstanceIdInitial

      ```
      public void setInstanceIdInitial​(Integer instanceIdInitial)
      ```

      Atribui valor para instanceIdInitial

      Parameters:
      :   `instanceIdInitial` - the instanceIdInitial to set
    - #### getInstanceIdFinal

      ```
      public Integer getInstanceIdFinal()
      ```

      Recupera valor do instanceIdFinal

      Returns:
      :   the instanceIdFinal
    - #### setInstanceIdFinal

      ```
      public void setInstanceIdFinal​(Integer instanceIdFinal)
      ```

      Atribui valor para instanceIdFinal

      Parameters:
      :   `instanceIdFinal` - the instanceIdFinal to set
    - #### getDocumentIdInitial

      ```
      public Integer getDocumentIdInitial()
      ```

      Recupera valor do documentIdInitial

      Returns:
      :   the documentIdInitial
    - #### setDocumentIdInitial

      ```
      public void setDocumentIdInitial​(Integer documentIdInitial)
      ```

      Atribui valor para documentIdInitial

      Parameters:
      :   `documentIdInitial` - the documentIdInitial to set
    - #### getDocumentIdFinal

      ```
      public Integer getDocumentIdFinal()
      ```

      Recupera valor do documentIdFinal

      Returns:
      :   the documentIdFinal
    - #### setDocumentIdFinal

      ```
      public void setDocumentIdFinal​(Integer documentIdFinal)
      ```

      Atribui valor para documentIdFinal

      Parameters:
      :   `documentIdFinal` - the documentIdFinal to set
