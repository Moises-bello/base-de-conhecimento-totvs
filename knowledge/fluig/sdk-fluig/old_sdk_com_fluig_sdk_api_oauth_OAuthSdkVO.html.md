---
content_hash: 47d0d1cf65094693518fc5a354873edccc01c81a72012208b0c61c17bc76e0a6
fetched_at: '2026-11-03T14:35:04.589739+00:00'
page_id: com/fluig/sdk/api/oauth/OAuthSdkVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.oauth.OAuthSdkVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/oauth/OAuthSdkVO.html
version: 1
---

Package [com.fluig.sdk.api.oauth](https://api.fluig.com/old/sdk/com/fluig/sdk/api/oauth/package-summary.html)

## Class OAuthSdkVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.oauth.OAuthSdkVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class OAuthSdkVO
  extends Object
  implements Serializable
  ```

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.oauth.OAuthSdkVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `OAuthSdkVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAccessTokenURL()` |  |
    | `String` | `getAuthenticationType()` |  |
    | `String` | `getAuthorizationURL()` |  |
    | `String` | `getCallbackUrl()` |  |
    | `String` | `getClientData()` |  |
    | `String` | `getClientId()` |  |
    | `String` | `getClientSecret()` |  |
    | `String` | `getCode()` |  |
    | `String` | `getConsumerKey()` |  |
    | `String` | `getConsumerSecret()` |  |
    | `Date` | `getCreationDate()` |  |
    | `String` | `getDescription()` |  |
    | `String` | `getDomain()` |  |
    | `Date` | `getExpirationDate()` |  |
    | `String` | `getGrantType()` |  |
    | `Long` | `getId()` |  |
    | `String` | `getMethod()` |  |
    | `Map<String,​Object>` | `getParams()` |  |
    | `String` | `getPassword()` |  |
    | `String` | `getPasswordConfirmation()` |  |
    | `String` | `getProviderName()` |  |
    | `String` | `getRedirectUri()` |  |
    | `String` | `getRefreshToken()` |  |
    | `String` | `getRefreshTokenURL()` |  |
    | `String` | `getRequestMethod()` |  |
    | `String` | `getRequestTokenURL()` |  |
    | `String` | `getScope()` |  |
    | `String` | `getServiceTestUrl()` |  |
    | `String` | `getServiceUrl()` |  |
    | `String` | `getSignatureMethod()` |  |
    | `String` | `getStrParams()` |  |
    | `Long` | `getTenantId()` |  |
    | `String` | `getToken()` |  |
    | `String` | `getTokenAccess()` |  |
    | `String` | `getTokenSecret()` |  |
    | `String` | `getUserAuthorizationURL()` |  |
    | `String` | `getUsername()` |  |
    | `void` | `setAccessTokenURL​(String accessTokenURL)` |  |
    | `void` | `setAuthenticationType​(String authenticationType)` |  |
    | `void` | `setAuthorizationURL​(String authorizationURL)` |  |
    | `void` | `setCallbackUrl​(String callbackUrl)` |  |
    | `void` | `setClientData​(String clientData)` |  |
    | `void` | `setClientId​(String clientId)` |  |
    | `void` | `setClientSecret​(String clientSecret)` |  |
    | `void` | `setCode​(String code)` |  |
    | `void` | `setConsumerKey​(String consumerKey)` |  |
    | `void` | `setConsumerSecret​(String consumerSecret)` |  |
    | `void` | `setCreationDate​(Date creationDate)` |  |
    | `void` | `setDescription​(String description)` |  |
    | `void` | `setDomain​(String domain)` |  |
    | `void` | `setExpirationDate​(Date expirationDate)` |  |
    | `void` | `setGrantType​(String grantType)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setMethod​(String method)` |  |
    | `void` | `setParams​(Map<String,​Object> param)` |  |
    | `void` | `setPassword​(String password)` |  |
    | `void` | `setPasswordConfirmation​(String passwordConfirmation)` |  |
    | `void` | `setProviderName​(String providerName)` |  |
    | `void` | `setRedirectUri​(String redirectUri)` |  |
    | `void` | `setRefreshToken​(String refreshToken)` |  |
    | `void` | `setRefreshTokenURL​(String refreshTokenURL)` |  |
    | `void` | `setRequestMethod​(String requestMethod)` |  |
    | `void` | `setRequestTokenURL​(String requestTokenURL)` |  |
    | `void` | `setScope​(String scope)` |  |
    | `void` | `setServiceTestUrl​(String serviceTestUrl)` |  |
    | `void` | `setServiceUrl​(String serviceUrl)` |  |
    | `void` | `setSignatureMethod​(String signatureMethod)` |  |
    | `void` | `setStrParams​(String strParams)` |  |
    | `void` | `setTenantId​(Long tenantId)` |  |
    | `void` | `setToken​(String token)` |  |
    | `void` | `setTokenAccess​(String tokenAccess)` |  |
    | `void` | `setTokenSecret​(String tokenSecret)` |  |
    | `void` | `setUserAuthorizationURL​(String userAuthorizationURL)` |  |
    | `void` | `setUsername​(String username)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### OAuthSdkVO

      ```
      public OAuthSdkVO()
      ```

  + ### Method Detail

    - #### getAccessTokenURL

      ```
      public String getAccessTokenURL()
      ```
    - #### setAccessTokenURL

      ```
      public void setAccessTokenURL​(String accessTokenURL)
      ```
    - #### getCode

      ```
      public String getCode()
      ```
    - #### setCode

      ```
      public void setCode​(String code)
      ```
    - #### getDescription

      ```
      public String getDescription()
      ```
    - #### setDescription

      ```
      public void setDescription​(String description)
      ```
    - #### getRequestMethod

      ```
      public String getRequestMethod()
      ```
    - #### setRequestMethod

      ```
      public void setRequestMethod​(String requestMethod)
      ```
    - #### getSignatureMethod

      ```
      public String getSignatureMethod()
      ```
    - #### setSignatureMethod

      ```
      public void setSignatureMethod​(String signatureMethod)
      ```
    - #### getConsumerKey

      ```
      public String getConsumerKey()
      ```
    - #### setConsumerKey

      ```
      public void setConsumerKey​(String consumerKey)
      ```
    - #### getConsumerSecret

      ```
      public String getConsumerSecret()
      ```
    - #### setConsumerSecret

      ```
      public void setConsumerSecret​(String consumerSecret)
      ```
    - #### getId

      ```
      public Long getId()
      ```
    - #### setId

      ```
      public void setId​(Long id)
      ```
    - #### getRequestTokenURL

      ```
      public String getRequestTokenURL()
      ```
    - #### setRequestTokenURL

      ```
      public void setRequestTokenURL​(String requestTokenURL)
      ```
    - #### getUserAuthorizationURL

      ```
      public String getUserAuthorizationURL()
      ```
    - #### setUserAuthorizationURL

      ```
      public void setUserAuthorizationURL​(String userAuthorizationURL)
      ```
    - #### getToken

      ```
      public String getToken()
      ```
    - #### setToken

      ```
      public void setToken​(String token)
      ```
    - #### getTokenAccess

      ```
      public String getTokenAccess()
      ```
    - #### setTokenAccess

      ```
      public void setTokenAccess​(String tokenAccess)
      ```
    - #### getTokenSecret

      ```
      public String getTokenSecret()
      ```
    - #### setTokenSecret

      ```
      public void setTokenSecret​(String tokenSecret)
      ```
    - #### getTenantId

      ```
      public Long getTenantId()
      ```
    - #### setTenantId

      ```
      public void setTenantId​(Long tenantId)
      ```
    - #### getAuthorizationURL

      ```
      public String getAuthorizationURL()
      ```
    - #### setAuthorizationURL

      ```
      public void setAuthorizationURL​(String authorizationURL)
      ```
    - #### getCreationDate

      ```
      public Date getCreationDate()
      ```
    - #### setCreationDate

      ```
      public void setCreationDate​(Date creationDate)
      ```
    - #### getExpirationDate

      ```
      public Date getExpirationDate()
      ```
    - #### setExpirationDate

      ```
      public void setExpirationDate​(Date expirationDate)
      ```
    - #### getClientData

      ```
      public String getClientData()
      ```
    - #### setClientData

      ```
      public void setClientData​(String clientData)
      ```
    - #### getProviderName

      ```
      public String getProviderName()
      ```
    - #### setProviderName

      ```
      public void setProviderName​(String providerName)
      ```
    - #### getCallbackUrl

      ```
      public String getCallbackUrl()
      ```
    - #### setCallbackUrl

      ```
      public void setCallbackUrl​(String callbackUrl)
      ```
    - #### getGrantType

      ```
      public String getGrantType()
      ```
    - #### setGrantType

      ```
      public void setGrantType​(String grantType)
      ```
    - #### getClientId

      ```
      public String getClientId()
      ```
    - #### setClientId

      ```
      public void setClientId​(String clientId)
      ```
    - #### getRedirectUri

      ```
      public String getRedirectUri()
      ```
    - #### setRedirectUri

      ```
      public void setRedirectUri​(String redirectUri)
      ```
    - #### getUsername

      ```
      public String getUsername()
      ```
    - #### setUsername

      ```
      public void setUsername​(String username)
      ```
    - #### getPassword

      ```
      public String getPassword()
      ```
    - #### setPassword

      ```
      public void setPassword​(String password)
      ```
    - #### getAuthenticationType

      ```
      public String getAuthenticationType()
      ```
    - #### setAuthenticationType

      ```
      public void setAuthenticationType​(String authenticationType)
      ```
    - #### getServiceTestUrl

      ```
      public String getServiceTestUrl()
      ```
    - #### setServiceTestUrl

      ```
      public void setServiceTestUrl​(String serviceTestUrl)
      ```
    - #### getServiceUrl

      ```
      public String getServiceUrl()
      ```
    - #### setServiceUrl

      ```
      public void setServiceUrl​(String serviceUrl)
      ```
    - #### getDomain

      ```
      public String getDomain()
      ```
    - #### setDomain

      ```
      public void setDomain​(String domain)
      ```
    - #### getClientSecret

      ```
      public String getClientSecret()
      ```
    - #### setClientSecret

      ```
      public void setClientSecret​(String clientSecret)
      ```
    - #### getRefreshToken

      ```
      public String getRefreshToken()
      ```
    - #### setRefreshToken

      ```
      public void setRefreshToken​(String refreshToken)
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
      public void setParams​(Map<String,​Object> param)
      ```
    - #### getStrParams

      ```
      public String getStrParams()
      ```
    - #### setStrParams

      ```
      public void setStrParams​(String strParams)
      ```
    - #### getScope

      ```
      public String getScope()
      ```
    - #### setScope

      ```
      public void setScope​(String scope)
      ```
    - #### getPasswordConfirmation

      ```
      public String getPasswordConfirmation()
      ```
    - #### setPasswordConfirmation

      ```
      public void setPasswordConfirmation​(String passwordConfirmation)
      ```
    - #### getRefreshTokenURL

      ```
      public String getRefreshTokenURL()
      ```
    - #### setRefreshTokenURL

      ```
      public void setRefreshTokenURL​(String refreshTokenURL)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
