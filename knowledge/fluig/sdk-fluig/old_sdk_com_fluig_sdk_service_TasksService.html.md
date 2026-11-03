---
content_hash: 78ce6dfd122fcb4ed2d4d862377c0e7ae9f9256a7986ae4ee729eab9dbd6fb46
fetched_at: '2026-11-03T14:35:07.019686+00:00'
page_id: com/fluig/sdk/service/TasksService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.TasksService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/TasksService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface TasksService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface TasksService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de Tasks.

  Since:
  :   1.5.2

  Author:
  :   marcelo.pereira

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `List<DocumentVO>` | `findApprovalDocumentsByUser​(String colleagueId)` | Busca todos os Documentos em aprovação por usuário |
    | `List<DocumentTaskVO>` | `findDocsInAgreement​(String colleagueId)` | Procura por documentos em consenso |
    | `List<DocumentTaskVO>` | `findDocsInCheckout​(String colleagueId)` | Procura documentos em checkout |
    | `List<DocumentVO>` | `findDocumentsToApprove​(String colleagueId)` | Busca os documentos para aprovação |
    | `List<WorkflowVO>` | `findExpiredWorkflowTasks​(String colleagueId)` | Solicitações Atrasadas |
    | `List<DocumentVO>` | `findMyDocuments​(String colleagueId)` | Busca os Documentos em aprovação |
    | `List<WorkflowVO>` | `findMyRequests​(String colleagueId)` | Minhas solicitações abertas |
    | `List<WorkflowVO>` | `findTasksInAgreement​(String colleagueId)` | Tarefas em consenso |
    | `List<WorkflowVO>` | `findWorkflowTasks​(String colleagueId)` | Solicitações Pendentes |
    | `int` | `getCountMyActiveRequests​(String colleagueId, List<String> processes)` | Count all my requests for the specified user |
    | `int` | `getCountMyDocuments​(String colleagueId)` | Find and count all pending documents |
    | `int` | `getCountOpenTasksByKind​(String colleagueId, TaskKindEnum kind)` | Count all open tasks that matches with kind and status |
    | `int` | `getCountOpenTasksByKind​(String colleagueId, TaskKindEnum kind, TaskStatusEnum status, List<String> processes)` | Count all open tasks that matches with kind and status |
    | `Map<String,​Long>` | `getOpenWorkflowTasksInPool​(String colleagueId, List<String> processes)` | Gets all groups and roles which contains tasks in pool |
    | `List<DocumentApproverVO>` | `getPendentApprovals​(Integer documentId)` | Return users pendent to approve a document |
    | `List<ResumedTasksVO>` | `getResumedTasksForPool​(Map<String,​Long> openInPool)` | Gets and mount the entire VO with related groups or roles inside the object |
    | `String` | `transferTasks​(TaskTransferVO tasksTransfer)` | Transfer tasks from one user to another |
    | `String` | `transferTasks​(Map<String,​String> transferOptions)` | Transfer tasks from one user to another |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.TasksService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.TasksService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### findDocumentsToApprove

      ```
      List<DocumentVO> findDocumentsToApprove​(String colleagueId)
                                       throws com.fluig.sdk.api.common.SDKException
      ```

      Busca os documentos para aprovação

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Documentos para aprovação

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar os documentos para aprovação
    - #### findMyDocuments

      ```
      List<DocumentVO> findMyDocuments​(String colleagueId)
                                throws com.fluig.sdk.api.common.SDKException
      ```

      Busca os Documentos em aprovação

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Documentos em aprovação

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar os Documentos em aprovação
    - #### findApprovalDocumentsByUser

      ```
      List<DocumentVO> findApprovalDocumentsByUser​(String colleagueId)
                                            throws com.fluig.sdk.api.common.SDKException
      ```

      Busca todos os Documentos em aprovação por usuário

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Documentos em aprovação

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar os Documentos em aprovação
    - #### findWorkflowTasks

      ```
      List<WorkflowVO> findWorkflowTasks​(String colleagueId)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Solicitações Pendentes

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Solicitações Pendentes

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar as solicitações Pendentes
    - #### findExpiredWorkflowTasks

      ```
      List<WorkflowVO> findExpiredWorkflowTasks​(String colleagueId)
                                         throws com.fluig.sdk.api.common.SDKException
      ```

      Solicitações Atrasadas

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Solicitações Atrasadas

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar as solicitações atrasadas
    - #### findMyRequests

      ```
      List<WorkflowVO> findMyRequests​(String colleagueId)
                               throws com.fluig.sdk.api.common.SDKException
      ```

      Minhas solicitações abertas

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Minhas solicitações abertas

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar as Minhas solicitações abertas
    - #### findTasksInAgreement

      ```
      List<WorkflowVO> findTasksInAgreement​(String colleagueId)
                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Tarefas em consenso

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Tarefas em consenso

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findDocsInAgreement

      ```
      List<DocumentTaskVO> findDocsInAgreement​(String colleagueId)
                                        throws com.fluig.sdk.api.common.SDKException
      ```

      Procura por documentos em consenso

      Parameters:
      :   `colleagueId` -

      Returns:
      :   List

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findDocsInCheckout

      ```
      List<DocumentTaskVO> findDocsInCheckout​(String colleagueId)
                                       throws com.fluig.sdk.api.common.SDKException
      ```

      Procura documentos em checkout

      Parameters:
      :   `colleagueId` -

      Returns:
      :   List

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCountOpenTasksByKind

      ```
      int getCountOpenTasksByKind​(String colleagueId,
                                  TaskKindEnum kind)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Count all open tasks that matches with kind and status

      Parameters:
      :   `colleagueId` -
      :   `kind` -

      Returns:
      :   total of open tasks

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCountOpenTasksByKind

      ```
      int getCountOpenTasksByKind​(String colleagueId,
                                  TaskKindEnum kind,
                                  TaskStatusEnum status,
                                  List<String> processes)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Count all open tasks that matches with kind and status

      Parameters:
      :   `colleagueId` -
      :   `kind` -
      :   `status` -
      :   `processes` -

      Returns:
      :   total of open tasks

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCountMyActiveRequests

      ```
      int getCountMyActiveRequests​(String colleagueId,
                                   List<String> processes)
                            throws com.fluig.sdk.api.common.SDKException
      ```

      Count all my requests for the specified user

      Parameters:
      :   `colleagueId` -
      :   `processes` -

      Returns:
      :   total of tasks

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getOpenWorkflowTasksInPool

      ```
      Map<String,​Long> getOpenWorkflowTasksInPool​(String colleagueId,
                                                        List<String> processes)
                                                 throws com.fluig.sdk.api.common.SDKException
      ```

      Gets all groups and roles which contains tasks in pool

      Parameters:
      :   `colleagueId` -
      :   `processes` -

      Returns:
      :   Map

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCountMyDocuments

      ```
      int getCountMyDocuments​(String colleagueId)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Find and count all pending documents

      Parameters:
      :   `colleagueId` -

      Returns:
      :   total of documents

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getResumedTasksForPool

      ```
      List<ResumedTasksVO> getResumedTasksForPool​(Map<String,​Long> openInPool)
                                           throws com.fluig.sdk.api.common.SDKException
      ```

      Gets and mount the entire VO with related groups or roles inside the object

      Parameters:
      :   `openInPool` -

      Returns:
      :   List contains tasks resume for group and roles

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### transferTasks

      ```
      String transferTasks​(Map<String,​String> transferOptions)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Transfer tasks from one user to another

      Returns:
      :   transfer log

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### transferTasks

      ```
      String transferTasks​(TaskTransferVO tasksTransfer)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Transfer tasks from one user to another

      Returns:
      :   transfer log

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getPendentApprovals

      ```
      List<DocumentApproverVO> getPendentApprovals​(Integer documentId)
                                            throws com.fluig.sdk.api.common.SDKException
      ```

      Return users pendent to approve a document

      Parameters:
      :   `documentId` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
