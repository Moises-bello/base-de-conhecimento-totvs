---
content_hash: d2af78213666cdf6763d8b02d13b926fdabf18dfd8a23dc0e1046664171141e7
fetched_at: '2026-11-03T14:35:03.730118+00:00'
page_id: com/fluig/sdk/api/authorizeclient/AuthorizeClientSdkServiceVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.authorizeclient.AuthorizeClientSdkServiceVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/authorizeclient/AuthorizeClientSdkServiceVO.html
version: 1
---

Package [com.fluig.sdk.api.authorizeclient](https://api.fluig.com/old/sdk/com/fluig/sdk/api/authorizeclient/package-summary.html)

## Class AuthorizeClientSdkServiceVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.authorizeclient.AuthorizeClientSdkServiceVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AuthorizeClientSdkServiceVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.authorizeclient.AuthorizeClientSdkServiceVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AuthorizeClientSdkServiceVO​(Long companyId, String serviceCode, String description, String method)` |  |
    | `AuthorizeClientSdkServiceVO​(Long companyId, String serviceCode, String endpoint, String method, String timeoutService, Map<String,​Object> params)` |  |
    | `AuthorizeClientSdkServiceVO​(String serviceCode, String endpoint, String method, Map<String,​Object> params, String result)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object obj)` |  |
    | `Long` | `getCompanyId()` |  |
    | `String` | `getDescription()` |  |
    | `String` | `getEndpoint()` |  |
    | `Map<String,​String>` | `getHeaders()` |  |
    | `int` | `getHttpStatusResult()` |  |
    | `String` | `getMethod()` |  |
    | `Map<String,​Object>` | `getOptions()` |  |
    | `Map<String,​Object>` | `getParams()` |  |
    | `String` | `getResult()` |  |
    | `String` | `getServiceCode()` |  |
    | `String` | `getStrParams()` |  |
    | `String` | `getTimeoutService()` |  |
    | `int` | `hashCode()` |  |
    | `void` | `setCompanyId​(Long companyId)` |  |
    | `void` | `setDescription​(String description)` |  |
    | `void` | `setEndpoint​(String endpoint)` |  |
    | `void` | `setHeaders​(Map<String,​String> headers)` |  |
    | `void` | `setHttpStatusResult​(int httpStatusResult)` |  |
    | `void` | `setMethod​(String method)` |  |
    | `void` | `setOptions​(Map<String,​Object> options)` |  |
    | `void` | `setParams​(Map<String,​Object> params)` |  |
    | `void` | `setResult​(String result)` |  |
    | `void` | `setServiceCode​(String serviceCode)` |  |
    | `void` | `setStrParams​(String strParams)` |  |
    | `void` | `setTimeoutService​(String timeoutService)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### AuthorizeClientSdkServiceVO

      ```
      public AuthorizeClientSdkServiceVO​(Long companyId,
                                         String serviceCode,
                                         String description,
                                         String method)
      ```
    - #### AuthorizeClientSdkServiceVO

      ```
      public AuthorizeClientSdkServiceVO​(Long companyId,
                                         String serviceCode,
                                         String endpoint,
                                         String method,
                                         String timeoutService,
                                         Map<String,​Object> params)
      ```
    - #### AuthorizeClientSdkServiceVO

      ```
      public AuthorizeClientSdkServiceVO​(String serviceCode,
                                         String endpoint,
                                         String method,
                                         Map<String,​Object> params,
                                         String result)
      ```

  + ### Method Detail

    - #### getDescription

      ```
      public String getDescription()
      ```
    - #### setDescription

      ```
      public void setDescription​(String description)
      ```
    - #### getHttpStatusResult

      ```
      public int getHttpStatusResult()
      ```
    - #### setHttpStatusResult

      ```
      public void setHttpStatusResult​(int httpStatusResult)
      ```
    - #### getResult

      ```
      public String getResult()
      ```
    - #### setResult

      ```
      public void setResult​(String result)
      ```
    - #### getServiceCode

      ```
      public String getServiceCode()
      ```
    - #### setServiceCode

      ```
      public void setServiceCode​(String serviceCode)
      ```
    - #### getMethod

      ```
      public String getMethod()
      ```
    - #### setMethod

      ```
      public void setMethod​(String method)
      ```
    - #### getParams

      ```
      public Map<String,​Object> getParams()
      ```
    - #### setParams

      ```
      public void setParams​(Map<String,​Object> params)
      ```
    - #### getStrParams

      ```
      public String getStrParams()
      ```
    - #### setStrParams

      ```
      public void setStrParams​(String strParams)
      ```
    - #### getEndpoint

      ```
      public String getEndpoint()
      ```
    - #### setEndpoint

      ```
      public void setEndpoint​(String endpoint)
      ```
    - #### getOptions

      ```
      public Map<String,​Object> getOptions()
      ```
    - #### setOptions

      ```
      public void setOptions​(Map<String,​Object> options)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `Object`
    - #### equals

      ```
      public boolean equals​(Object obj)
      ```

      Overrides:
      :   `equals` in class `Object`
    - #### getCompanyId

      ```
      public Long getCompanyId()
      ```
    - #### setCompanyId

      ```
      public void setCompanyId​(Long companyId)
      ```
    - #### getTimeoutService

      ```
      public String getTimeoutService()
      ```
    - #### setTimeoutService

      ```
      public void setTimeoutService​(String timeoutService)
      ```
    - #### getHeaders

      ```
      public Map<String,​String> getHeaders()
      ```
    - #### setHeaders

      ```
      public void setHeaders​(Map<String,​String> headers)
      ```
