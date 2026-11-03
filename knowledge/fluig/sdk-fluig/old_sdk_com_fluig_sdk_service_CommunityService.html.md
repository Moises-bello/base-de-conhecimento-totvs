---
content_hash: 62ea0624faa41a07454078ff153f3acbfc99bb77a4f4d2cb6180a63b1502112a
fetched_at: '2026-11-03T14:35:06.574401+00:00'
page_id: com/fluig/sdk/service/CommunityService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CommunityService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CommunityService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CommunityService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CommunityService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de manutenção de comunidades.

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
    | `void` | `addUser​(Long communityId, String alias)` | Adiciona um usuário em uma comunidade. |
    | `void` | `addUsers​(String communityAlias, List<String> users)` | Adiciona uma lista de usuários na comunidade |
    | `CommunityVO` | `create​(CommunityVO vo)` | Cria uma nova comunidade. |
    | `void` | `disablePostEditionAllCommunities()` | Desabilita a edição de post para todas as comunidades, incluindo no papel de usuario |
    | `CommunityVO` | `update​(CommunityVO vo)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CommunityService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CommunityService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### create

      ```
      CommunityVO create​(CommunityVO vo)
                  throws com.fluig.sdk.api.common.SDKException
      ```

      Cria uma nova comunidade.

      Parameters:
      :   `vo` - Dados da comunidade a ser criada.

      Returns:
      :   Comunidade criada.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possível criar a comunidade.
    - #### addUser

      ```
      void addUser​(Long communityId,
                   String alias)
            throws com.fluig.sdk.api.common.SDKException
      ```

      Adiciona um usuário em uma comunidade.

      Parameters:
      :   `communityId` - ID da comunidade.
      :   `alias` - Alias do usuário.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### addUsers

      ```
      void addUsers​(String communityAlias,
                    List<String> users)
             throws com.fluig.sdk.api.common.SDKException
      ```

      Adiciona uma lista de usuários na comunidade

      Parameters:
      :   `communityAlias` -
      :   `userList` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### update

      ```
      CommunityVO update​(CommunityVO vo)
                  throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### disablePostEditionAllCommunities

      ```
      void disablePostEditionAllCommunities()
                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Desabilita a edição de post para todas as comunidades, incluindo no papel de usuario

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
