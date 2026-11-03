---
content_hash: db8147f90f4f10669b86ddf77c1e46f383b721083ceface4427560f93e9b9a0c
fetched_at: '2026-11-03T14:35:06.723092+00:00'
page_id: com/fluig/sdk/service/GroupService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.GroupService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/GroupService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface GroupService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface GroupService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de grupos.

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
    | `void` | `addUsers​(Long tenantId, String groupCode, List<String> logins)` |  |
    | `List<String>` | `addUsers​(String groupCode, List<String> logins)` | Adiciona um usuário ao grupo. |
    | `Boolean` | `containsUser​(String groupCode, String genericId)` | Verifica se o usuário pertence ao grupo. |
    | `GroupVO` | `create​(GroupVO vo)` | Cria um novo grupo. |
    | `GroupVO` | `create​(GroupVO vo, Long tenantId)` | Create grupo |
    | `List<GroupVO>` | `findGroupsByUser​(String genericId, String pattern)` | Retorna grupo por usuário |
    | `List<ColleagueVO>` | `findUsersByGroup​(String groupId, String pattern, int limit, int offset, String order)` | Retorna usuários por grupo |
    | `void` | `removeUser​(Long tenantId, String groupCode, String alias)` | Remove um usuário do grupo. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.GroupService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.GroupService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### create

      ```
      GroupVO create​(GroupVO vo)
              throws com.fluig.sdk.api.common.SDKException
      ```

      Cria um novo grupo.

      Parameters:
      :   `vo` - Dados do grupo.

      Returns:
      :   Dados do grupo criado.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possível criar o grupo.
    - #### containsUser

      ```
      Boolean containsUser​(String groupCode,
                           String genericId)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Verifica se o usuário pertence ao grupo.

      Parameters:
      :   `groupCode` - Código do grupo.
      :   `genericId` - User's generic indentifier, can be (login, idpId or userCode).

      Returns:
      :   **true** se o usuário pertence ao grupo, **false** caso
          contrário.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha buscando informação.
    - #### addUsers

      ```
      List<String> addUsers​(String groupCode,
                            List<String> logins)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Adiciona um usuário ao grupo.

      Parameters:
      :   `groupCode` - Código do grupo.
      :   `logins` - Lista de login de usuários.

      Returns:
      :   List
          Lista de usuários que não foram adicionados ao grupo

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha adicionando usuário ao grupo.
    - #### addUsers

      ```
      void addUsers​(Long tenantId,
                    String groupCode,
                    List<String> logins)
             throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### removeUser

      ```
      void removeUser​(Long tenantId,
                      String groupCode,
                      String alias)
               throws com.fluig.sdk.api.common.SDKException
      ```

      Remove um usuário do grupo.

      Parameters:
      :   `groupCode` - Código do grupo.
      :   `logins` - Lista de login de usuários.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha adicionando usuário ao grupo.
    - #### findUsersByGroup

      ```
      List<ColleagueVO> findUsersByGroup​(String groupId,
                                         String pattern,
                                         int limit,
                                         int offset,
                                         String order)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna usuários por grupo

      Parameters:
      :   `groupId` -
      :   `pattern` -

      Returns:
      :   lista dos usuários do grupo.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha ao retornar os usuários do grupo
    - #### findGroupsByUser

      ```
      List<GroupVO> findGroupsByUser​(String genericId,
                                     String pattern)
                              throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna grupo por usuário

      Parameters:
      :   `genericId` -
      :   `pattern` -

      Returns:
      :   lista dos grupos de usuário.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Falha ao retornar os grupo de usuário
    - #### create

      ```
      GroupVO create​(GroupVO vo,
                     Long tenantId)
              throws com.fluig.sdk.api.common.SDKException
      ```

      Create grupo

      Parameters:
      :   `vo` -
      :   `tenantId` -

      Returns:
      :   Dados do grupo criado.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possível criar o grupo.
