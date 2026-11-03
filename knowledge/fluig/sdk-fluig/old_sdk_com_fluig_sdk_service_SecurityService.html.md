---
content_hash: d2b6d58c70ad784ff4df70946d4c8dd40f400cb5ae49b37010625a63642721cf
fetched_at: '2026-11-03T14:35:06.958936+00:00'
page_id: com/fluig/sdk/service/SecurityService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.SecurityService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/SecurityService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface SecurityService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface SecurityService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de segurança.

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
    | `void` | `changeUserPassword​(String login, String currentPassword, String newPassword, String confirmNewPassword)` | Change user password |
    | `Boolean` | `createOrUpdateTenantData​(String key, String value)` | Cria um bjeto chave/valor no tenantData |
    | `void` | `createPermissions​(String resourceCode, List<PermissionVO> permissions)` | Cria as permissões para um determinado recurso |
    | `void` | `deletePermissions​(String resourceCode, List<PermissionVO> permissions)` | Deleta as permissões para um determinado recurso |
    | `GroupVO` | `findGroupByTenantIdAndCode​(Long tenantId, String code)` | Retorna o grupo por code e tenant |
    | `List<TenantVO>` | `findTenants()` | Retorna a lista de tentants. |
    | `TenantVO` | `getCurrentTenant()` | Get the current tenant |
    | `TenantVO` | `getCurrentTenantById​(Long tenantId)` | Get the current tenant |
    | `Long` | `getCurrentTenantId()` | Retorna o tenantId logado |
    | `List<PermissionVO>` | `getPermissionsByResourceCode​(String resourceCode)` | Lista as permissões do recurso informado |
    | `String` | `getTimeZoneLocalUser​(long companyId, String userCode)` |  |
    | `Boolean` | `hasPermission​(String resource, String permiss)` | Verifica se o usuário logado possui certa permissão no recurso dado. |
    | `List<PermissionAssetVO>` | `listResourcesByCategory​(String category, String filter, int offset, int limit)` | Lista os recursos da categoria informada |
    | `List<AdminUserVO>` | `listTenantAdmins​(Long tenantId)` | Retorna os admins de um tenant |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SecurityService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SecurityService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### hasPermission

      ```
      Boolean hasPermission​(String resource,
                            String permiss)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Verifica se o usuário logado possui certa permissão no recurso dado.

      Parameters:
      :   `resource` - Código do recurso.
      :   `permiss` - Código da permissão.

      Returns:
      :   **true** se o usuário tiver persmissão, **false** caso
          contrário.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5
    - #### listResourcesByCategory

      ```
      List<PermissionAssetVO> listResourcesByCategory​(String category,
                                                      String filter,
                                                      int offset,
                                                      int limit)
                                               throws com.fluig.sdk.api.common.SDKException
      ```

      Lista os recursos da categoria informada

      Parameters:
      :   `category` - - Categoria do recurso
      :   `filter` - - filtro para pesquisa
      :   `offset` - - offset da pesquisa
      :   `limit` - - limite da pesquisa

      Returns:
      :   Lista com os recursos.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getPermissionsByResourceCode

      ```
      List<PermissionVO> getPermissionsByResourceCode​(String resourceCode)
                                               throws com.fluig.sdk.api.common.SDKException
      ```

      Lista as permissões do recurso informado

      Parameters:
      :   `resourceCode` - - Código do recurso

      Returns:
      :   Lista com as permissões

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createPermissions

      ```
      void createPermissions​(String resourceCode,
                             List<PermissionVO> permissions)
                      throws com.fluig.sdk.api.common.SDKException
      ```

      Cria as permissões para um determinado recurso

      Parameters:
      :   `resourceCode` - - Código do recurso
      :   `permissions` - - lista de permissões a serem criadas para o recurso

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### deletePermissions

      ```
      void deletePermissions​(String resourceCode,
                             List<PermissionVO> permissions)
                      throws com.fluig.sdk.api.common.SDKException
      ```

      Deleta as permissões para um determinado recurso

      Parameters:
      :   `resourceCode` - - Código do recurso
      :   `permissions` - - lista de permissões a serem criadas para o recurso

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findTenants

      ```
      List<TenantVO> findTenants()
                          throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a lista de tentants.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCurrentTenantId

      ```
      Long getCurrentTenantId()
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna o tenantId logado

      Returns:
      :   current tenantId

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findGroupByTenantIdAndCode

      ```
      GroupVO findGroupByTenantIdAndCode​(Long tenantId,
                                         String code)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna o grupo por code e tenant

      Parameters:
      :   `tenantId` -
      :   `code` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createOrUpdateTenantData

      ```
      Boolean createOrUpdateTenantData​(String key,
                                       String value)
                                throws com.fluig.sdk.api.common.SDKException
      ```

      Cria um bjeto chave/valor no tenantData

      Parameters:
      :   `key` -
      :   `value` -

      Returns:
      :   If tenant data was updated

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### listTenantAdmins

      ```
      List<AdminUserVO> listTenantAdmins​(Long tenantId)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna os admins de um tenant

      Parameters:
      :   `tenantId` -

      Returns:
      :   List of tenant admin

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### changeUserPassword

      ```
      void changeUserPassword​(String login,
                              String currentPassword,
                              String newPassword,
                              String confirmNewPassword)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Change user password

      Parameters:
      :   `login` -
      :   `currentPassword` -
      :   `newPassword` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCurrentTenant

      ```
      TenantVO getCurrentTenant()
                         throws com.fluig.sdk.api.common.SDKException
      ```

      Get the current tenant

      Returns:
      :   Tenant data

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getCurrentTenantById

      ```
      TenantVO getCurrentTenantById​(Long tenantId)
                             throws com.fluig.sdk.api.common.SDKException
      ```

      Get the current tenant

      Returns:
      :   Tenant data

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getTimeZoneLocalUser

      ```
      String getTimeZoneLocalUser​(long companyId,
                                  String userCode)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Parameters:
      :   `companyId` -
      :   `userCode` -

      Returns:
      :   time zone for user

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
