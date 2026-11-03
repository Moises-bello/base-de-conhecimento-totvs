---
content_hash: 086326435f4ca6e1c0b47ac8bf58092c534df8fde1916bfc2f7a73b38055288d
fetched_at: '2026-11-03T14:35:05.654593+00:00'
page_id: com/fluig/sdk/api/workflow/DatasetOfflineMobileRestVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.workflow.DatasetOfflineMobileRestVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/DatasetOfflineMobileRestVO.html
version: 1
---

Package [com.fluig.sdk.api.workflow](https://api.fluig.com/old/sdk/com/fluig/sdk/api/workflow/package-summary.html)

## Class DatasetOfflineMobileRestVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.workflow.DatasetOfflineMobileRestVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class DatasetOfflineMobileRestVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.workflow.DatasetOfflineMobileRestVO)

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `DAYS` |  |
    | `static String` | `HOURS` |  |
    | `static String` | `WEEKS` |  |

  + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `DatasetOfflineMobileRestVO()` |  |
    | `DatasetOfflineMobileRestVO​(long companyId, Integer documentId, int version, String datasetId, long updateInterval)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `long` | `getCompanyId()` |  |
    | `String` | `getDatasetId()` |  |
    | `Integer` | `getDocumentId()` |  |
    | `Long` | `getId()` |  |
    | `String` | `getTimeUnit()` |  |
    | `long` | `getUpdateInterval()` |  |
    | `int` | `getVersion()` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setDatasetId​(String datasetId)` |  |
    | `void` | `setDocumentId​(Integer documentId)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setTimeUnit​(String timeUnit)` |  |
    | `void` | `setUpdateInterval​(long updateInterval)` |  |
    | `void` | `setVersion​(int version)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### HOURS

      ```
      public static final String HOURS
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.api.workflow.DatasetOfflineMobileRestVO.HOURS)
    - #### DAYS

      ```
      public static final String DAYS
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.api.workflow.DatasetOfflineMobileRestVO.DAYS)
    - #### WEEKS

      ```
      public static final String WEEKS
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.api.workflow.DatasetOfflineMobileRestVO.WEEKS)

  + ### Constructor Detail

    - #### DatasetOfflineMobileRestVO

      ```
      public DatasetOfflineMobileRestVO()
      ```
    - #### DatasetOfflineMobileRestVO

      ```
      public DatasetOfflineMobileRestVO​(long companyId,
                                        Integer documentId,
                                        int version,
                                        String datasetId,
                                        long updateInterval)
      ```

  + ### Method Detail

    - #### getCompanyId

      ```
      public long getCompanyId()
      ```
    - #### setCompanyId

      ```
      public void setCompanyId​(long companyId)
      ```
    - #### getDocumentId

      ```
      public Integer getDocumentId()
      ```
    - #### setDocumentId

      ```
      public void setDocumentId​(Integer documentId)
      ```
    - #### getVersion

      ```
      public int getVersion()
      ```
    - #### setVersion

      ```
      public void setVersion​(int version)
      ```
    - #### getDatasetId

      ```
      public String getDatasetId()
      ```
    - #### setDatasetId

      ```
      public void setDatasetId​(String datasetId)
      ```
    - #### getUpdateInterval

      ```
      public long getUpdateInterval()
      ```
    - #### setUpdateInterval

      ```
      public void setUpdateInterval​(long updateInterval)
      ```
    - #### getId

      ```
      public Long getId()
      ```
    - #### setId

      ```
      public void setId​(Long id)
      ```
    - #### getTimeUnit

      ```
      public String getTimeUnit()
      ```
    - #### setTimeUnit

      ```
      public void setTimeUnit​(String timeUnit)
      ```
