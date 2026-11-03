---
content_hash: de59cb59b7b9c5e249751cec713202e43a18eef527296d344b0fef1f1b8eaee6
fetched_at: '2026-11-03T14:35:06.796128+00:00'
page_id: com/fluig/sdk/service/JobService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.JobService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/JobService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface JobService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface JobService
  extends BaseAPIService
  ```

  Fornece acesso a serviços de Job Scheduler.

  Since:
  :   1.5.8

  Author:
  :   marcus.carvalho

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `JobVO` | `createDaily​(JobVO vo)` |  |
    | `JobVO` | `createMonthly​(JobVO vo)` |  |
    | `JobVO` | `createWeekly​(JobVO vo)` |  |
    | `void` | `delete​(JobVO vo)` |  |
    | `List<JobVO>` | `list​(Integer limit, Integer offset, String filter)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.JobService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.JobService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### createDaily

      ```
      JobVO createDaily​(JobVO vo)
                 throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createWeekly

      ```
      JobVO createWeekly​(JobVO vo)
                  throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createMonthly

      ```
      JobVO createMonthly​(JobVO vo)
                   throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### delete

      ```
      void delete​(JobVO vo)
           throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### list

      ```
      List<JobVO> list​(Integer limit,
                       Integer offset,
                       String filter)
                throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
