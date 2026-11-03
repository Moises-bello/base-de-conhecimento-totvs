---
content_hash: 58d9ab3c4f6cc9c3c484015cd24b76f2665c973986c117f08b437d003f1d29b4
fetched_at: '2026-11-03T14:35:07.029626+00:00'
page_id: com/fluig/sdk/service/TenantService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.TenantService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/TenantService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface TenantService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface TenantService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de tenância.

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
    | `TenantVO` | `create​(TenantVO vo)` | Cria um novo tenante. |
    | `Map<String,​String>` | `getTenantData​(String[] keys)` | Retorna, caso houver, objeto chaves/valores do tenantData |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.TenantService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.TenantService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### create

      ```
      TenantVO create​(TenantVO vo)
               throws com.fluig.sdk.api.common.SDKException
      ```

      Cria um novo tenante.

      Parameters:
      :   `vo` - Dados do tenante.

      Returns:
      :   Dados do tenante criado.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possível criar o tenante.
    - #### getTenantData

      ```
      Map<String,​String> getTenantData​(String[] keys)
                                      throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna, caso houver, objeto chaves/valores do tenantData

      Parameters:
      :   `keys` -

      Returns:
      :   map key/value tenantData

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
