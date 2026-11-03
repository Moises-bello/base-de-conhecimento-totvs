---
content_hash: c84831bad0fd591870bdb97437e1c24682bf1e83e2106bbb0a91d4953849021d
fetched_at: '2026-11-03T14:35:06.461411+00:00'
page_id: com/fluig/sdk/service/BaseAPIService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.BaseAPIService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface BaseAPIService

* All Known Subinterfaces:
  :   `AlertService`, `ApplicationUserDataService`, `ArticleService`, `AuthorizeClientSdkService`, `CardAPIService`, `CardIndexAPIService`, `CardIndexService`, `CardService`, `CollaborationSDKService`, `CommentService`, `CommunityService`, `ContentFilesService`, `CustomAppKeyService`, `DocumentationProxyServiceService`, `DocumentService`, `FavoritesService`, `FilterAPIService`, `FolderDocumentService`, `GlobalParameterService`, `GroupService`, `HolidayAPIService`, `I18NService`, `IdentityService`, `JobService`, `LocalAPIService`, `MentionService`, `OAuthUserService`, `PageService`, `PageWidgetService`, `PostService`, `SearchService`, `SecurityService`, `SocialBreadcrumbService`, `SocialSDKService`, `TagsCloudService`, `TasksService`, `TenantService`, `UserService`, `WidgetService`, `WorkflowAPIService`

  ---

  ```
  public interface BaseAPIService
  ```

  Interface base

  Version:
  :   1.00.000

  Author:
  :   vanei

* + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Default Methods](javascript:show(16);)

    | Modifier and Type | Method | Description |
    | `default boolean` | `expand​(String expand, String attributeName)` |  |
    | `default List<com.totvs.technology.foundation.sdk.service.vo.common.OrderParam>` | `generateOrderParam​(String order, List<String> orderAttributes)` |  |

* + ### Method Detail

    - #### generateOrderParam

      ```
      default List<com.totvs.technology.foundation.sdk.service.vo.common.OrderParam> generateOrderParam​(String order,
                                                                                                        List<String> orderAttributes)
      ```
    - #### expand

      ```
      default boolean expand​(String expand,
                             String attributeName)
      ```
