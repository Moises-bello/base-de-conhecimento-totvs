---
content_hash: 281b9848d9420507ab34dabe57dad3cd37377ffd6442bcffd3d67ccd6e1ee3d6
fetched_at: '2026-11-03T14:35:06.632415+00:00'
page_id: com/fluig/sdk/service/DocumentService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.DocumentService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/DocumentService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface DocumentService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface DocumentService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de documentos (GED).

  Since:
  :   1.5

  Author:
  :   vanei

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `void` | `approveDocument​(int documentId, int version, boolean approved, String observation)` | Aprova ou reprova um documento. |
    | `String[]` | `copyDocumentToUploadArea​(int documentId)` | Copia o documento que esta na área de uplaod |
    | `DocumentVO` | `createDocument​(DocumentVO documentVO)` | Cria o documento com permissões e aprovadors |
    | `DocumentVO` | `createPrivateDocument​(Long companyId, String userId, String fileName, com.fluig.foundation.volume.vo.FDNLocalFileVO file)` | Cria uma documento privado |
    | `DocumentVO` | `createPrivateDocument​(Long companyId, String userId, String fileName, String filePath)` | Cria uma documento privado |
    | `void` | `deleteDocument​(int documentId)` | Remove o documento |
    | `DocumentVO` | `getActive​(Integer documentId)` | Retorna o documento ativo passado o ID do mesmo. |
    | `AllocatedDocumentVO` | `getAllocatedDocument​(int documentId, int version)` | Retorna documento com as informações de checkout |
    | `SolvedPermissionVO` | `getCurrentUserPermission​(Integer documentId)` |  |
    | `List<DocumentApprovementHistoryVO>` | `getDocumentApprovalHistory​(int documentId)` | Return the approvements history of the document |
    | `List<DocumentApproverVO>` | `getDocumentApprovers​(int documentId)` | Retrieve all document approvers and yours status. |
    | `List<DocumentApproverVO>` | `getDocumentApprovers​(int documentId, boolean checkInheritance)` | Retrieve all document approvers and yours status. |
    | `byte[]` | `getDocumentContentAsBytes​(Integer documentId)` | Retorna os bytes do conteúdo do documento. |
    | `String` | `getDocumentContentAsString​(Integer documentId, String charsetName)` | Retorna o conteúdo do documento. |
    | `List<DocumentPermissionVO>` | `getDocumentPermissions​(int documentId, int version)` | Retorna as permissões do documento |
    | `String` | `getDownloadURL​(Integer documentId)` | Retorna a url do documento |
    | `Integer` | `getUserPermissions​(Integer documentId, Integer version, String user)` | Retorna a permissão do usuário em um documento. |
    | `boolean` | `isCanDownloadDocument​(Long tenantId, int documentId, int version, String userCode, boolean fluigViewer)` |  |
    | `boolean` | `isDocumentDeleted​(Long tenantId, int documentId, int version)` |  |
    | `void` | `setDocumentApprovers​(Long companyId, DocumentSecurityVO documentSecurityVO)` | Set Approvers for a specific document |
    | `void` | `setDocumentPermissions​(int documentId, List<DocumentPermissionVO> permissions)` | Determina as permissões do documento |
    | `DocumentVO` | `updateFile​(DocumentVO docVO)` | Update file |
    | `void` | `validateDocumentPublicUrlConfiguration​(Long tenantId, int documentId, int version)` | Valida configurações de documento |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.DocumentService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.DocumentService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### getActive

      ```
      DocumentVO getActive​(Integer documentId)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna o documento ativo passado o ID do mesmo.

      Parameters:
      :   `documentId` - ID do documento.

      Returns:
      :   Dados do documento encontrado.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getUserPermissions

      ```
      Integer getUserPermissions​(Integer documentId,
                                 Integer version,
                                 String user)
                          throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a permissão do usuário em um documento.

      Parameters:
      :   `documentId` - ID do documento.
      :   `version` - Versão do documento.
      :   `user` - Matrícula do usuário.

      Returns:
      :   Permissão do usuário. Os valores possíveis são: `-1` -
          Sem permissão, `0` - Leitura, `1` -
          Gravação, `2` - Modificação, `3` - Controle
          Total

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha buscando permissão.
    - #### getCurrentUserPermission

      ```
      SolvedPermissionVO getCurrentUserPermission​(Integer documentId)
                                           throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createPrivateDocument

      ```
      DocumentVO createPrivateDocument​(Long companyId,
                                       String userId,
                                       String fileName,
                                       String filePath)
                                throws com.fluig.sdk.api.common.SDKException
      ```

      Cria uma documento privado

      Parameters:
      :   `companyId` - ID da empresa
      :   `userId` - ID do usuário
      :   `fileName` - Nome do arquivo
      :   `filePath` - Caminho do arquivo

      Returns:
      :   DocumentVO

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createPrivateDocument

      ```
      DocumentVO createPrivateDocument​(Long companyId,
                                       String userId,
                                       String fileName,
                                       com.fluig.foundation.volume.vo.FDNLocalFileVO file)
                                throws com.fluig.sdk.api.common.SDKException
      ```

      Cria uma documento privado

      Parameters:
      :   `companyId` - ID da empresa
      :   `userId` - ID do usuário
      :   `fileName` - Nome do arquivo
      :   `file` - Arquivo file

      Returns:
      :   DocumentVO

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getAllocatedDocument

      ```
      AllocatedDocumentVO getAllocatedDocument​(int documentId,
                                               int version)
                                        throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna documento com as informações de checkout

      Parameters:
      :   `documentId` - Id do documento
      :   `version` - Versão do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### getDownloadURL

      ```
      String getDownloadURL​(Integer documentId)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a url do documento

      Parameters:
      :   `documentId` - ID do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### getDocumentContentAsString

      ```
      String getDocumentContentAsString​(Integer documentId,
                                        String charsetName)
                                 throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna o conteúdo do documento.

      Exemplo de uso:
      var string = fluigAPI.getDocumentService().getDocumentContentAsString(documentId, "UTF-8");

      Parameters:
      :   `documentId` - ID do documento
      :   `charsetName` - Charset específico do conteúdo

      Returns:
      :   byte[]
          Array de byte do conteúdo do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.8.0
    - #### getDocumentContentAsBytes

      ```
      byte[] getDocumentContentAsBytes​(Integer documentId)
                                throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna os bytes do conteúdo do documento.

      Para converter o byte[] para String usando os sdk do Fluig em java:
      var string = new String(FluigAPI.getDocumentService().getDocumentContentAsBytes(documentId), "UTF-8");

      Para converter o byte[] para String usando javascript (evento de processo | dataset avançado):
      var string = new java.lang.String(fluigAPI.getDocumentService().getDocumentContentAsBytes(documentId), "UTF-8");

      Parameters:
      :   `documentId` - ID do documento

      Returns:
      :   byte[]
          Array de byte do conteúdo do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.8.0
    - #### createDocument

      ```
      DocumentVO createDocument​(DocumentVO documentVO)
                         throws com.fluig.sdk.api.common.SDKException
      ```

      Cria o documento com permissões e aprovadors

      Parameters:
      :   `documentVO` - Objeto do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### deleteDocument

      ```
      void deleteDocument​(int documentId)
                   throws com.fluig.sdk.api.common.SDKException
      ```

      Remove o documento

      Parameters:
      :   `documentId` - ID do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### copyDocumentToUploadArea

      ```
      String[] copyDocumentToUploadArea​(int documentId)
                                 throws com.fluig.sdk.api.common.SDKException
      ```

      Copia o documento que esta na área de uplaod

      Parameters:
      :   `documentId` - ID do documento

      Returns:
      :   Array de bytes documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### setDocumentPermissions

      ```
      void setDocumentPermissions​(int documentId,
                                  List<DocumentPermissionVO> permissions)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Determina as permissões do documento

      Parameters:
      :   `documentId` - ID do documento
      :   `permissions` - Lista de permissões do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### getDocumentPermissions

      ```
      List<DocumentPermissionVO> getDocumentPermissions​(int documentId,
                                                        int version)
                                                 throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna as permissões do documento

      Parameters:
      :   `documentId` - ID do documento
      :   `version` - Versão do documento

      Returns:
      :   Listas de permissões do documento

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### approveDocument

      ```
      void approveDocument​(int documentId,
                           int version,
                           boolean approved,
                           String observation)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Aprova ou reprova um documento.

      Parameters:
      :   `companyId` - ID da empresa
      :   `documentId` - ID do documento.
      :   `version` - Versão do documento.
      :   `approved` - passar true para aprovador e false para reprovado.
      :   `observation` - Observação do document.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha na aprovação.

      Since:
      :   1.5.12
    - #### getDocumentApprovers

      ```
      List<DocumentApproverVO> getDocumentApprovers​(int documentId)
                                             throws com.fluig.sdk.api.common.SDKException
      ```

      Retrieve all document approvers and yours status.

      Parameters:
      :   `documentId` - ID do documento.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha na aprovação.

      Since:
      :   1.5.12
    - #### getDocumentApprovers

      ```
      List<DocumentApproverVO> getDocumentApprovers​(int documentId,
                                                    boolean checkInheritance)
                                             throws com.fluig.sdk.api.common.SDKException
      ```

      Retrieve all document approvers and yours status.

      Parameters:
      :   `documentId` - ID do documento.
      :   `checkInheritance` - Caso true, tenta buscar os aprovadores no pai

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha na aprovação.

      Since:
      :   1.7.0
    - #### updateFile

      ```
      DocumentVO updateFile​(DocumentVO docVO)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Update file

      Parameters:
      :   `docVO` - Documento objeto

      Returns:
      :   Documento Objeto

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - 1.5.12
    - #### setDocumentApprovers

      ```
      void setDocumentApprovers​(Long companyId,
                                DocumentSecurityVO documentSecurityVO)
                         throws com.fluig.sdk.api.common.SDKException
      ```

      Set Approvers for a specific document

      Parameters:
      :   `Long` - companyId
      :   `DocumentSecurityVO` - documentSecurityVO

      Throws:
      :   `Exception`
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.11
    - #### getDocumentApprovalHistory

      ```
      List<DocumentApprovementHistoryVO> getDocumentApprovalHistory​(int documentId)
                                                             throws com.fluig.sdk.api.common.SDKException
      ```

      Return the approvements history of the document

      Parameters:
      :   `int` - documentId

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.12
    - #### validateDocumentPublicUrlConfiguration

      ```
      void validateDocumentPublicUrlConfiguration​(Long tenantId,
                                                  int documentId,
                                                  int version)
                                           throws Exception
      ```

      Valida configurações de documento

      Parameters:
      :   `tenantId` -
      :   `documentId` -
      :   `version` -

      Throws:
      :   `Exception`
    - #### isCanDownloadDocument

      ```
      boolean isCanDownloadDocument​(Long tenantId,
                                    int documentId,
                                    int version,
                                    String userCode,
                                    boolean fluigViewer)
                             throws Exception
      ```

      Throws:
      :   `Exception`
    - #### isDocumentDeleted

      ```
      boolean isDocumentDeleted​(Long tenantId,
                                int documentId,
                                int version)
                         throws Exception
      ```

      Throws:
      :   `Exception`
