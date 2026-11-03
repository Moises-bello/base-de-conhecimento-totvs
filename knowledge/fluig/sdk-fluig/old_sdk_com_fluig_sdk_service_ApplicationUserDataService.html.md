---
content_hash: 06ef9c419c07a9200fae971842c754513cad88353f9ae0e1a556c00a565d0d66
fetched_at: '2026-11-03T14:35:06.404099+00:00'
page_id: com/fluig/sdk/service/ApplicationUserDataService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.ApplicationUserDataService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/ApplicationUserDataService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface ApplicationUserDataService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface ApplicationUserDataService
  extends BaseAPIService
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `Long` | `countKeyByUsers​(String key)` |  |
    | `Map<String,​String>` | `create​(Long instanceId, Map<String,​String> applicationUserData)` |  |
    | `Map<String,​String>` | `findByInstanceIdAndLogin​(Long instanceId, String login)` |  |
    | `void` | `remove​(Long instanceId, String key)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.ApplicationUserDataService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.ApplicationUserDataService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### findByInstanceIdAndLogin

      ```
      Map<String,​String> findByInstanceIdAndLogin​(Long instanceId,
                                                        String login)
                                                 throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### create

      ```
      Map<String,​String> create​(Long instanceId,
                                      Map<String,​String> applicationUserData)
                               throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### remove

      ```
      void remove​(Long instanceId,
                  String key)
           throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### countKeyByUsers

      ```
      Long countKeyByUsers​(String key)
                    throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
