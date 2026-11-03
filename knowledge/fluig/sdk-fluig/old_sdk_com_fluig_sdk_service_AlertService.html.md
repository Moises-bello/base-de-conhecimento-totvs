---
content_hash: 4d2b03703db6bc9d0e6d5528978e499e81e7f2b62263c8c630a54152c6d79de5
fetched_at: '2026-11-03T14:35:06.391845+00:00'
page_id: com/fluig/sdk/service/AlertService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.AlertService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/AlertService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface AlertService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface AlertService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de notificações.

  Since:
  :   1.5.8

  Author:
  :   luis.junior

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `Long` | `countUnreadAlerts​(Long receiverId)` | Método que conta os alertas não lidos de um usuário. |
    | `Long` | `countUnreadAlertsByModule​(String module, Long receiverId)` | Método que conta os alertas de um modulo não lidos de um usuário |
    | `Long` | `getTenantTotalOfNotification()` | Get the number of notification in the tenant |
    | `List<AlertVO>` | `listAlertsWithAction​(int limit, int offset)` | Busca os alertas com ação vinculada, do usuário logado ordenado pela data de criação. |
    | `List<AlertVO>` | `listAlertsWithNote​(int limit, int offset)` | Busca os alertas com nota, do usuário logado ordenado pela data de criação. |
    | `List<AlertVO>` | `listAllAlerts​(int limit, int offset)` | Retorna todas as notificações do usuário logado ordenadas pela data de criação. |
    | `List<AlertVO>` | `listAllAlertsByModule​(String module, int limit, int offset)` | Retorna todas as notificações de um usuário por um único módulo |
    | `void` | `markAlertAsRead​(String loginReceiver, List<Long> alertsId)` | Método marca os alertas informados de um usuario tambem dado como lidos |
    | `void` | `markAllAlertsAsRead​(String loginReceiver)` | Método marca todos os alertas de um usuario como lidos. |
    | `void` | `removeAlerts​(String loginSender, List<Long> alertsId)` | Método que remove os alertas informados de um usuario tambem dado, esse método também é responsável por remover os senders, places e objects relacionado aos alertas |
    | `void` | `saveConfiguration​(AlertConfigVO alertConfig)` | Salva a configuração de um usuário para receber ou não alertas de um dado evento através de um dado aplicativo. |
    | `void` | `sendNotification​(String eventKey, String loginSender, String loginReceiver, com.totvs.technology.foundation.alert.AlertObject object, com.totvs.technology.foundation.alert.AlertObject place, List<com.totvs.technology.foundation.alert.AlertAction> actions, Map<String,​String> metadata)` | Método que deve ser invocado por todos os módulos do sistema para enviar alertas. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.AlertService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.AlertService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### getTenantTotalOfNotification

      ```
      Long getTenantTotalOfNotification()
                                 throws com.fluig.sdk.api.common.SDKException
      ```

      Get the number of notification in the tenant

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### listAllAlerts

      ```
      List<AlertVO> listAllAlerts​(int limit,
                                  int offset)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna todas as notificações do usuário logado ordenadas pela data de criação.

      Parameters:
      :   `limit` -
      :   `offset` -

      Returns:
      :   lista de notificações.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### listAlertsWithNote

      ```
      List<AlertVO> listAlertsWithNote​(int limit,
                                       int offset)
                                throws com.fluig.sdk.api.common.SDKException
      ```

      Busca os alertas com nota, do usuário logado ordenado pela data de criação.

      Parameters:
      :   `limit` - - limit de resultados
      :   `offset` - - offset

      Returns:
      :   lista de alertas

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### listAlertsWithAction

      ```
      List<AlertVO> listAlertsWithAction​(int limit,
                                         int offset)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Busca os alertas com ação vinculada, do usuário logado ordenado pela data de criação.

      Parameters:
      :   `limit` - - limit de resultados
      :   `offset` - - offset

      Returns:
      :   lista de alertas

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### listAllAlertsByModule

      ```
      List<AlertVO> listAllAlertsByModule​(String module,
                                          int limit,
                                          int offset)
                                   throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna todas as notificações de um usuário por um único módulo

      Parameters:
      :   `module` -
      :   `limit` -
      :   `offset` -

      Returns:
      :   lista de notificações.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### sendNotification

      ```
      void sendNotification​(String eventKey,
                            String loginSender,
                            String loginReceiver,
                            com.totvs.technology.foundation.alert.AlertObject object,
                            com.totvs.technology.foundation.alert.AlertObject place,
                            List<com.totvs.technology.foundation.alert.AlertAction> actions,
                            Map<String,​String> metadata)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Método que deve ser invocado por todos os módulos do sistema para enviar alertas.

      Parameters:
      :   `eventKey` - - String única que representa o evento que gerou o alerta.
      :   `loginSender` - - Login(alias) do usuário que está enviando a notificação (tabela FDN\_USERTENANT) (opcional)
      :   `loginReceiver` - - Login(alias) do usuário que receberá a notificação (tabela FDN\_USERTENANT)
      :   `object` - - Objeto sobre o qual o evento foi gerado (opcional)
      :   `place` - - Lugar onde o evento foi gerado (opcional)
      :   `actions` - - Ações disponibilizadas pela notificação
      :   `metadata` - - Metadados para serem armazenados no alerta

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - - Indica falha no envio
    - #### removeAlerts

      ```
      void removeAlerts​(String loginSender,
                        List<Long> alertsId)
                 throws com.fluig.sdk.api.common.SDKException
      ```

      Método que remove os alertas informados de um usuario tambem dado,
      esse método também é responsável por remover os senders, places e objects
      relacionado aos alertas

      Parameters:
      :   `loginSender` - - Login(alias) do usuário que está enviando a notificação (tabela FDN\_USERTENANT)
      :   `alertsId` - - Lista de id dos alertas

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - - Indica falha na remoção
    - #### markAlertAsRead

      ```
      void markAlertAsRead​(String loginReceiver,
                           List<Long> alertsId)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Método marca os alertas informados de um usuario tambem dado como lidos

      Parameters:
      :   `loginReceiver` - - Login(alias) do usuário que recebeu as notificações (tabela FDN\_USERTENANT)
      :   `alertsId` - - Lista de id dos alertas

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - - Indica falha na atualização
      :   `com.fluig.sdk.api.common.SDKException`
    - #### markAllAlertsAsRead

      ```
      void markAllAlertsAsRead​(String loginReceiver)
                        throws com.fluig.sdk.api.common.SDKException
      ```

      Método marca todos os alertas de um usuario como lidos.

      Parameters:
      :   `loginReceiver` - - Login(alias) do usuário que recebeu a notificação (tabela FDN\_USERTENANT)

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - - Indica falha na atualização
      :   `com.fluig.sdk.api.common.SDKException`
    - #### countUnreadAlerts

      ```
      Long countUnreadAlerts​(Long receiverId)
                      throws com.fluig.sdk.api.common.SDKException
      ```

      Método que conta os alertas não lidos de um usuário.

      Parameters:
      :   `receiverId` - - id do usuário.

      Returns:
      :   número de alertas não lidos

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - - Caso ocorra um erro na busca
      :   `com.fluig.sdk.api.common.SDKException`
    - #### countUnreadAlertsByModule

      ```
      Long countUnreadAlertsByModule​(String module,
                                     Long receiverId)
                              throws com.fluig.sdk.api.common.SDKException
      ```

      Método que conta os alertas de um modulo não lidos de um usuário

      Parameters:
      :   `receiverId` - - id do usuário.

      Returns:
      :   número de alertas não lidos

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - - Caso ocorra um erro na busca
      :   `com.fluig.sdk.api.common.SDKException`
    - #### saveConfiguration

      ```
      void saveConfiguration​(AlertConfigVO alertConfig)
                      throws com.fluig.sdk.api.common.SDKException
      ```

      Salva a configuração de um usuário para receber ou não alertas de um dado evento
      através de um dado aplicativo.

      Parameters:
      :   `alertConfig` - - Configuração do alertas

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - - Indica falha ao salvar a configuração
      :   `com.fluig.sdk.api.common.SDKException`
