---
content_hash: 2391b0a2d638d4b15cd7189fb1d99940652fab40acbbf36b6cf01a53d636edfe
fetched_at: '2026-11-03T14:35:06.550778+00:00'
page_id: com/fluig/sdk/service/CollaborationSDKService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CollaborationSDKService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CollaborationSDKService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CollaborationSDKService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CollaborationSDKService
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
    | `void` | `addGuests​(Long collaborationId, List<String> guests)` |  |
    | `String` | `checkConnect​(String appKey)` |  |
    | `CollaborationVO` | `findCollaborationById​(Long collaborationId)` |  |
    | `CollaborationAppVO` | `getApp​(String appKey)` |  |
    | `Map<String,​Serializable>` | `getCollaborationStatus​(Integer documentId, Integer documentVersion)` |  |
    | `List<CollaborationAppVO>` | `listApps()` |  |
    | `List<UserVO>` | `listCollaborators​(Long collaborationId, String pattern, int limit, int offset)` |  |
    | `String` | `startCollaboration​(String appKey, CollaborationVO collaborateVO)` |  |
    | `Map<String,​Serializable>` | `startEditingByGuest​(String appKey, String guestCode, CollaborationVO collaborateVO)` |  |
    | `String` | `startGuestCollaboration​(String appKey, CollaborationVO collaborateVO)` |  |
    | `CollaborationAppVO` | `updateApp​(CollaborationAppVO vo)` |  |
    | `Map<String,​Serializable>` | `uploadFlow​(String appKey, CollaborationVO collaborationVO)` |  |
    | `void` | `validateUserPermissionToEdit​(int documentId, int documentVersion, String userCode)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CollaborationSDKService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CollaborationSDKService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### listApps

      ```
      List<CollaborationAppVO> listApps()
      ```
    - #### getApp

      ```
      CollaborationAppVO getApp​(String appKey)
      ```
    - #### startCollaboration

      ```
      String startCollaboration​(String appKey,
                                CollaborationVO collaborateVO)
                         throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### uploadFlow

      ```
      Map<String,​Serializable> uploadFlow​(String appKey,
                                                CollaborationVO collaborationVO)
                                         throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### startGuestCollaboration

      ```
      String startGuestCollaboration​(String appKey,
                                     CollaborationVO collaborateVO)
                              throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### startEditingByGuest

      ```
      Map<String,​Serializable> startEditingByGuest​(String appKey,
                                                         String guestCode,
                                                         CollaborationVO collaborateVO)
                                                  throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### updateApp

      ```
      CollaborationAppVO updateApp​(CollaborationAppVO vo)
                            throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### addGuests

      ```
      void addGuests​(Long collaborationId,
                     List<String> guests)
              throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### getCollaborationStatus

      ```
      Map<String,​Serializable> getCollaborationStatus​(Integer documentId,
                                                            Integer documentVersion)
                                                     throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### checkConnect

      ```
      String checkConnect​(String appKey)
                   throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### listCollaborators

      ```
      List<UserVO> listCollaborators​(Long collaborationId,
                                     String pattern,
                                     int limit,
                                     int offset)
                              throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findCollaborationById

      ```
      CollaborationVO findCollaborationById​(Long collaborationId)
                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### validateUserPermissionToEdit

      ```
      void validateUserPermissionToEdit​(int documentId,
                                        int documentVersion,
                                        String userCode)
                                 throws Exception
      ```

      Throws:
      :   `Exception`
