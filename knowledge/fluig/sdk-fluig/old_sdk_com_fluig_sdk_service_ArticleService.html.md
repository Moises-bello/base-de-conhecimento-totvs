---
content_hash: 68dddc0c6a1322a456445dd46a3dfa1484a233ce1bda20ba1fb8278faf948a20
fetched_at: '2026-11-03T14:35:06.441662+00:00'
page_id: com/fluig/sdk/service/ArticleService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.ArticleService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/ArticleService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface ArticleService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface ArticleService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de artigos.

  Since:
  :   1.5.4

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
    | `ArticleVO` | `changeCover​(ArticleVO sdkVO)` | Update the cover image of an existing article.   Return the article that was updated in a community. |
    | `ArticleVO` | `create​(ArticleVO vo)` | Create an article.   Return the article that was updated in a community. |
    | `ArticleVO` | `createDraft​(ArticleVO vo)` | Create an article in draft mode.   Return the article that was created in a draft mode. |
    | `void` | `delete​(long articleId)` | Remove an article by his id |
    | `void` | `deleteDraft​(String alias, Long articleId)` | Remove a version in draft of article   Remove a draft version of article by his id. |
    | `ArticleVO` | `get​(String alias, long articleId, boolean draft)` | Retrieve an article   Return an article published in a community. |
    | `ArticleVO` | `getNextOrPrev​(Long folderId, Long articleId, String order)` | Retrive the next or previous article of one specific article.   Return the article that is the next or previous of the article passed by parameter. |
    | `List<ArticleVO>` | `list​(String alias, Long categoryId, Integer limit, Integer offset, String filterBy, String orderBy, String searchBy)` | Retrieve a list of article   Return a list of article published in a community. |
    | `ArticleVO` | `removeCover​(ArticleVO sdkVO)` | Remove the cover image of an existing article.   Return the article that was updated in a community. |
    | `ArticleVO` | `update​(ArticleVO vo)` | Save and update an article.   Return the article that was updated in a community. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.ArticleService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.ArticleService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### delete

      ```
      void delete​(long articleId)
           throws com.fluig.sdk.api.common.SDKException
      ```

      Remove an article by his id

      Parameters:
      :   `articleId` - the Id of a article that will be removed

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### get

      ```
      ArticleVO get​(String alias,
                    long articleId,
                    boolean draft)
             throws com.fluig.sdk.api.common.SDKException
      ```

      Retrieve an article  
        
      Return an article published in a community.

      Parameters:
      :   `alias` - the community's alias where the article is published
      :   `articleId` - The article's id
      :   `draft` - `true` if retrieving a draft version of the article  
          `false` if retrieving a published version of the article

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### list

      ```
      List<ArticleVO> list​(String alias,
                           Long categoryId,
                           Integer limit,
                           Integer offset,
                           String filterBy,
                           String orderBy,
                           String searchBy)
                    throws com.fluig.sdk.api.common.SDKException
      ```

      Retrieve a list of article  
        
      Return a list of article published in a community.

      Parameters:
      :   `alias` - the community's alias where the article is published
      :   `categoryId` - The category's id
      :   `limit` - The results limit
      :   `offset` - The pagination offset
      :   `offset` - The pagination offset
      :   `filterBy` - filter result
          `ALL_ARTICLES` return all published articles
          `MY_ARTICLES` return my publications
      :   `orderBy` - ordering result
          `CREATION_DATE_ASC` order by creation date
          `CREATION_DATE_DESC` order by creation date inverse
          `DESCRIPTION_ASC` order by description
          `DESCRIPTION_DESC` order by description inverse
      :   `searchBy` - literal pattern into document title

      Returns:
      :   List<[`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social")> This method returns VO of article

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createDraft

      ```
      ArticleVO createDraft​(ArticleVO vo)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Create an article in draft mode.  
        
      Return the article that was created in a draft mode.

      Parameters:
      :   `vo` - A article VO with data used to create a article

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article created

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### update

      ```
      ArticleVO update​(ArticleVO vo)
                throws com.fluig.sdk.api.common.SDKException
      ```

      Save and update an article.  
        
      Return the article that was updated in a community.

      Parameters:
      :   `vo` - A article VO with data used to save the article

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article updated

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### create

      ```
      ArticleVO create​(ArticleVO vo)
                throws com.fluig.sdk.api.common.SDKException
      ```

      Create an article.  
        
      Return the article that was updated in a community.

      Parameters:
      :   `vo` - A article VO with data used to save the article

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article updated

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### changeCover

      ```
      ArticleVO changeCover​(ArticleVO sdkVO)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Update the cover image of an existing article.  
        
      Return the article that was updated in a community.

      Parameters:
      :   `sdkVO` - A article VO with data used to update the article

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article updated

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### removeCover

      ```
      ArticleVO removeCover​(ArticleVO sdkVO)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Remove the cover image of an existing article.  
        
      Return the article that was updated in a community.

      Parameters:
      :   `sdkVO` - A article VO with data used to update the article

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article updated

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getNextOrPrev

      ```
      ArticleVO getNextOrPrev​(Long folderId,
                              Long articleId,
                              String order)
                       throws Exception
      ```

      Retrive the next or previous article of one specific article.  
        
      Return the article that is the next or previous of the article passed by parameter.

      Parameters:
      :   `folderId` - The folder's id where the next or previous will be searched.
      :   `articleId` - The article's Id that will be retrieved the next or previous.
      :   `order` - The order to get next or previous article. Use the string 'next' retrieve the next article.

      Returns:
      :   [`ArticleVO`](https://api.fluig.com/old/sdk/com/fluig/sdk/api/social/ArticleVO.html "class in com.fluig.sdk.api.social") This method returns VO of article that is the next or previous of the article
          passed by parameter

      Throws:
      :   `Exception`
    - #### deleteDraft

      ```
      void deleteDraft​(String alias,
                       Long articleId)
                throws com.fluig.sdk.api.common.SDKException
      ```

      Remove a version in draft of article  
        
      Remove a draft version of article by his id. If the article isn't in draft,
      a Error message wil be returned

      Parameters:
      :   `alias` - the community's alias where the article is published
      :   `articleId` - the Id of a article that will remove the draft version of an article

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
