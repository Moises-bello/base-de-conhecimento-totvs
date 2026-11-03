---
content_hash: 5e00fa5a27c4daf8e24c13ac17eeea1ccf2761e5acba936c589dfc18c3b90ed1
fetched_at: '2026-11-03T14:34:36.024524+00:00'
page_id: index
product: fluig
source: rest-fluig
title: Fluig REST — índice de recursos (paths e métodos)
type: documentation
url: https://api.fluig.com/old/index.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

[JAVADOC Fluig API](https://api.fluig.com/old/sdk/index.html)

# 

Resources

The resources use a data model that is supported by a set of client-side libraries that are made available on the
[files and libraries](https://api.fluig.com/old/downloads.html) page.

There is a [WADL document](https://api.fluig.com/old/application.wadl) available that describes the resources API.

| name | path | methods | description |
| --- | --- | --- | --- |
| AdHocServiceRest | * `/bpm/adhoc/create` * `/bpm/adhoc/{process}/{sequence}` | * `POST` * `GET` | AdHoc Processes (Task List) |
| AlertRest | * `/2.0/notification/countUnreadAlerts` * `/2.0/notification/getTenantTotalOfNotification` * `/2.0/notification/listAlertsWithAction` * `/2.0/notification/listAlertsWithNote` * `/2.0/notification/listAllAlerts` * `/2.0/notification/listAllAlertsByModule` * `/2.0/notification/markAlertAsRead` * `/2.0/notification/markAllAlertsAsRead` * `/2.0/notification/removeAlerts` * `/2.0/notification/saveConfiguration` | * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` | Notification - V2 |
| AlertServiceRest | * `/alert/customEmailSender` * `/alert/action/execute` * `/alert/alerts/countUnread` * `/alert/appSender/findVoList` * `/alert/appSender/registerApp` * `/alert/appSender/registerApplication` * `/alert/application/actives` * `/alert/application/enable` * `/alert/event/changeStatus` * `/alert/event/createEvent` * `/alert/event/enable` * `/alert/event/eventsByModule` * `/alert/module/create` * `/alert/module/findVoList` * `/alert/service/countGroupedUnreadAlerts` * `/alert/service/countUnreadAlerts` * `/alert/service/findAll` * `/alert/service/markAllAsRead` * `/alert/service/markAsRead` * `/alert/service/removeAlert` * `/alert/service/removeAlerts` * `/alert/service/sendAlert` * `/alert/service/sendNotification` * `/alert/action/execute/v2` * `/alert/alerts/countUnread/v2` * `/alert/application/isActive/{appKey}` * `/alert/sender/findSenders/{alertId}` * `/alert/service/countGroupedUnreadAlerts/v2` * `/alert/service/findAll/v2` * `/alert/service/findById/{alertId}` * `/alert/service/markAllAsRead/v2` * `/alert/service/markAsRead/v2` * `/alert/service/removeAlerts/v2` | * `POST` * `POST` * `GET` * `GET` * `POST` * `POST` * `GET` * `POST` * `POST` * `POST` * `POST` * `GET` * `POST` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` | Notifications |
| ArticleRest | * `/2.0/communities/articles/changeCover` * `/2.0/communities/articles/create` * `/2.0/communities/articles/createDraft` * `/2.0/communities/articles/removeCover` * `/2.0/communities/articles/update` * `/2.0/communities/articles/delete/{articleId}` * `/2.0/communities/articles/deleteDraft/{alias}/{articleId}` * `/2.0/communities/articles/get/{alias}/{articleId}` * `/2.0/communities/articles/list/{alias}/{categoryId}` * `/2.0/communities/articles/getNextOrPrev/{folderId}/{articleId}/{order}` | * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` | Articles - V2 |
| ArticleServiceRest | * `/social/article/remove` * `/social/article/save` * `/social/article/category/create` * `/social/article/category/remove` * `/social/article/category/update` * `/social/article/order/{categoryId}` * `/social/article/{alias}/{categoryId}` * `/social/article/category/{alias}/{parentId}` * `/social/article/byid/{alias}/{categoryId}/{articleId}` * `/social/article/category/byid/{alias}/{id}` * `/social/article/categoryarticle/{alias}/{parentId}/{categoryId}` * `/social/article/editbyid/{alias}/{categoryId}/{articleId}` | * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Articles (in communities) |
| AuthorizeClientRest | * `/2.0/authorize/client/invoke` * `/2.0/authorize/client/test` | * `POST` * `GET` | Authorize |
| CardIndexRest | * `/2.0/cardindexes/create` * `/2.0/cardindexes/getDefaultFormFolderId` * `/2.0/cardindexes/delete/{documentId}` | * `POST` * `GET` * `POST` | Card Index |
| CardRest | * `/2.0/cards/create` | * `POST` | Cards |
| CategoryServiceRest | * `/social/category/create` * `/social/category/update` * `/social/category/remove/{id}` * `/social/category/list/{alias}/{parent}` * `/social/category/root/{alias}/{type}` * `/social/category/find/{alias}/{id}/{type}` * `/social/category/findparent/{alias}/{id}/{parent}` | * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` | Categories |
| CollaborationRest | * `/2.0/collaboration/getCollaborationStatus` * `/2.0/collaboration/listApps` * `/2.0/collaboration/updateApp` * `/2.0/collaboration/addGuests/{collaborationId}` * `/2.0/collaboration/checkConnect/{appKey}` * `/2.0/collaboration/get/{collaborationId}` * `/2.0/collaboration/getApp/{appKey}` * `/2.0/collaboration/listCollaborators/{collaborationId}` * `/2.0/collaboration/startCollaboration/{appKey}` * `/2.0/collaboration/startGuestCollaboration/{appKey}` * `/2.0/collaboration/uploadFlow/{appKey}` * `/2.0/collaboration/startEditingByGuest/{appKey}/{guestLogin}` * `/2.0/collaboration/validateUserPermissionToEdit/{documentId}/{documentVersion}/{userCode}` | * `GET` * `GET` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `GET` | Collaboration |
| CommunityDocumentServiceRest | * `/social/community/document` * `/social/community/folder` * `/social/community/document/remove` * `/social/community/document/update` * `/social/community/document/{documentId}` * `/social/community/folder/remove` * `/social/community/folder/update` * `/social/community/folder/{folderId}` | * `POST` * `POST` * `POST` * `POST` * `GET` * `POST` * `POST` * `GET` | Document features for communities |
| CommunityRest | * `/2.0/communities/addUsers` * `/2.0/communities/create` * `/2.0/communities/disablePostEditionAllCommunities` * `/2.0/communities/update` * `/2.0/communities/addUser/{communityId}` | * `POST` * `POST` * `POST` * `POST` * `POST` | Community |
| CommunityServiceRest | * `/social/community/addGroups` * `/social/community/addParticipants` * `/social/community/changeImage` * `/social/community/create` * `/social/community/listCommunities` * `/social/community/listCommunitiesWithRelevance` * `/social/community/listFavoriteCommunitiesWithRelevance` * `/social/community/listPagesWithComunities` * `/social/community/new` * `/social/community/notify` * `/social/community/removeGroups` * `/social/community/request` * `/social/community/stopNotify` * `/social/community/update` * `/social/community/{alias}` * `/social/community/changeStatus/{alias}` * `/social/community/communitiesOrderFavorites/{genericId}` * `/social/community/communityMember/{alias}` * `/social/community/enabled/{alias}` * `/social/community/image/{alias}` * `/social/community/listModeratorsWithRelevance/{alias}` * `/social/community/listMyCommunitiesWithRelevance/{genericId}` * `/social/community/listMyCommunitiesWithRelevanceByLogin/{login}` * `/social/community/listParticipantsWithRelevance/{alias}` * `/social/community/listPendingRequestsWithRelevance/{alias}` * `/social/community/moderators/{alias}` * `/social/community/notifyList/{alias}` * `/social/community/participants/{alias}` * `/social/community/relationStatus/{aliasCommunity}` * `/social/community/v2/{alias}` * `/social/community/{alias}/forceAllMembersWatch` * `/social/community/accept/{communityAlias}/{requesterGenericId}` * `/social/community/addModerator/{communityAlias}/{genericId}` * `/social/community/changeAdmin/{communityAlias}/{genericId}` * `/social/community/communitiesOrderFavorites/v2/{genericId}` * `/social/community/folder/{alias}/{feature}` * `/social/community/imageBySize/{alias}/{size}` * `/social/community/isCommunityAdmin/{aliasCommunity}/{genericId}` * `/social/community/isCommunityModerator/{aliasCommunity}/{genericId}` * `/social/community/participants/v2/{alias}` * `/social/community/reject/{communityAlias}/{requesterGenericId}` * `/social/community/removeModerator/{communityAlias}/{genericId}` * `/social/community/removeParticipant/{communityAlias}/{genericId}` * `/social/community/comunity/participant/{communityId}/{pattern}` | * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `GET` | Communities |
| ConfigurationServiceRest | * `/2.0/wcm/config/availableConfigurations` * `/2.0/wcm/config/downloadConfig` * `/2.0/wcm/config/updateConfigurations` * `/2.0/wcm/config/uploadCertificate` * `/2.0/wcm/config/uploadCertificateKey` * `/2.0/wcm/config/validateCertificate` * `/2.0/wcm/config/validateCertificatePassword` * `/2.0/wcm/config/getConfiguration/{property}` | * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` | System Configuration |
| ContentFilesRest | * `/2.0/contentfiles/upload` | * `POST` | ContentFiles |
| DatasetServiceRest | * `/ecm/dataset/availableDatasets` * `/ecm/dataset/cardDatasetValues` * `/ecm/dataset/datasetJournaling` * `/ecm/dataset/datasets` * `/ecm/dataset/editable` * `/ecm/dataset/previewJournaling` * `/ecm/dataset/search` * `/ecm/dataset/standardDatasetValues` * `/ecm/dataset/synchronizeDataset` * `/ecm/dataset/datasetStructure/{datasetId}` * `/ecm/dataset/{componentId}/update` * `/ecm/dataset/{datasetId}/synchronize` * `/ecm/dataset/{componentId}/check/dependency` | * `GET` * `GET, POST` * `GET` * `POST` * `GET` * `GET` * `GET, POST` * `GET, POST` * `POST` * `GET` * `POST` * `POST` * `GET` | Datasets |
| DocumentRest | * `/2.0/documents/createDocument` * `/2.0/documents/createPrivateDocument` * `/2.0/documents/setDocumentPermissions` * `/2.0/documents/updateFile` * `/2.0/documents/approveDocument/{documentId}` * `/2.0/documents/copyDocumentToUploadArea/{documentId}` * `/2.0/documents/deleteDocument/{documentId}` * `/2.0/documents/getActive/{documentId}` * `/2.0/documents/getCurrentUserPermission/{documentId}` * `/2.0/documents/getDocumentApprovalHistory/{documentId}` * `/2.0/documents/getDocumentApprovers/{documentId}` * `/2.0/documents/getDownloadURL/{documentId}` * `/2.0/documents/getUserPermissions/{documentId}` * `/2.0/documents/setDocumentApprovers/{documentId}` * `/2.0/documents/getAllocatedDocument/{documentId}/{version}` * `/2.0/documents/getDocumentPermissions/{documentId}/{version}` | * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `GET` * `GET` | Document |
| DocumentServiceRest | * `/ecm/document/checkin` * `/ecm/document/checkout` * `/ecm/document/chunkedUploadURL` * `/ecm/document/create` * `/ecm/document/createDocument` * `/ecm/document/createFolder` * `/ecm/document/loggedUser` * `/ecm/document/maxUploadSize` * `/ecm/document/notify` * `/ecm/document/permissions` * `/ecm/document/remove` * `/ecm/document/stopNotify` * `/ecm/document/undoCheckout` * `/ecm/document/updateDescription` * `/ecm/document/updateDocumentFolder` * `/ecm/document/updateFile` * `/ecm/document/uploadURL` * `/ecm/document/activeDocumentFile/{documentId}` * `/ecm/document/activedocument/{documentId}` * `/ecm/document/allDocumentHits/{documentId}` * `/ecm/document/cancelChunkedUpload/{uploadId}` * `/ecm/document/createDocument/{uploadId}` * `/ecm/document/downloadURL/{documentId}` * `/ecm/document/getDocumentByDatasetName/{datasetName}` * `/ecm/document/getLastVersionNonDraft/{documentId}` * `/ecm/document/lastDocument/{documentId}` * `/ecm/document/listDocument/{folderId}` * `/ecm/document/listDocumentWithChildren/{folderId}` * `/ecm/document/liveurl/{documentId}` * `/ecm/document/{documentId}/{versionId}` * `/ecm/document/documentFileWithoutZip/{documentId}/{versionId}` * `/ecm/document/documentHitsByVersion/{documentId}/{version}` * `/ecm/document/documentfile/{documentId}/{versionId}` * `/ecm/document/notifyList/{documentId}/{versionId}` * `/ecm/document/documentFileThumbnail/{documentId}/{versionId}/{thumbnail}` | * `POST` * `POST` * `GET` * `POST` * `POST` * `POST` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Documents |
| DocumentationProxyRest | * `/2.0/documentationproxy/search` | * `GET` | DocumentationProxyRest |
| DriveServiceRest | * `/ecm/connect/config` | * `GET` | Fluig Connect |
| FavoriteServiceRest | * `/social/favorite` * `/social/favorite/remove` * `/social/favorite/bytype/{type}` * `/social/favorite/flag/{genericId}` * `/social/favorite/bytype/v2/{type}` | * `GET, POST` * `POST` * `GET` * `GET` * `GET` | Favorites |
| FavoritesRest | * `/2.0/favorites/findFavoritesDocuments/{colleagueId}` * `/2.0/favorites/findFavoritesProcess/{colleagueId}` | * `GET` * `GET` | Favorites |
| FieldsService | * `/ecm/filters/{filterId}/fields` * `/ecm/filters/{filterId}/fields/{id}` | * `GET` * `GET` | Central Tasks FilterFields Services |
| FilterRest | * `/2.0/filter/create` * `/2.0/filter/listProcessFilters` * `/2.0/filter/removeFilters` * `/2.0/filter/saveFiltersGroup` * `/2.0/filter/update` * `/2.0/filter/getFiltersGroup/{filterId}` * `/2.0/filter/getProcessFilterById/{filterId}` * `/2.0/filter/{filterId}/name` * `/2.0/filter/{instanceId}/sequence` * `/2.0/filter/updatePublicProcessFilter/{filterId}/{isPublic}` | * `POST` * `GET` * `POST` * `POST` * `POST` * `GET` * `GET` * `PATCH` * `POST` * `POST` | Filters - V2 |
| FilterService | * `/ecm/filters` * `/ecm/filters/create` * `/ecm/filters/remove` * `/ecm/filters/update` * `/ecm/filters/{id}` | * `GET` * `POST` * `POST` * `POST` * `GET` | Central Tasks Filter Services |
| FolderDocumentRest | * `/2.0/folderdocuments/create` * `/2.0/folderdocuments/listDocumentByFolder` * `/2.0/folderdocuments/get/{folderId}` | * `POST` * `POST` * `GET` | Folder Document |
| GlobalParameterRest | * `/2.0/globalparameter/getMaxUploadSizeForConnect` * `/2.0/globalparameter/getViewJustProcessWithApproval` * `/2.0/globalparameter/setMaxUploadSizeForConnect` | * `GET` * `GET` * `POST` | Global parameter |
| GroupRest | * `/2.0/groups/create` * `/2.0/groups/addUsers/{groupCode}` * `/2.0/groups/findGroupsByUser/{genericId}` * `/2.0/groups/listUsersByGroup/{groupId}` * `/2.0/groups/containsUser/{groupCode}/{genericId}` | * `POST` * `POST` * `GET` * `GET` * `GET` | Group |
| GroupServiceRest | * `/wcm/group` * `/wcm/group/findUsingFilter` * `/wcm/group/byuser/{genericId}` | * `GET` * `GET` * `GET` | Groups |
| HolidayRest | * `/2.0/holidays` * `/2.0/holidays/{id}` | * `GET, POST` * `DELETE, GET, PATCH, PUT` |  |
| I18nServiceRest | * `/wcm/i18n/changeLocale` | * `POST` | I18nServiceRest |
| IdentityRest | * `/2.0/identity/createSession` * `/2.0/identity/updateSession` | * `GET` * `GET` | Session |
| InviteServiceRest | * `/social/invite` * `/social/invite/filter/{email}/{status}` | * `GET, POST` * `GET` | Invites |
| JobRest | * `/2.0/job/createDaily` * `/2.0/job/createMonthly` * `/2.0/job/createWeekly` * `/2.0/job/delete` * `/2.0/job/list` | * `POST` * `POST` * `POST` * `POST` * `GET` | Job Scheduler - V2 |
| LiteralServiceRest | * `/wcm/literal/mobileCustomLiteral` * `/wcm/literal/mobileLastUpdate` | * `GET` * `GET` |  |
| LocalRest | * `/2.0/locals` * `/2.0/locals/timezone` * `/2.0/locals/{id}` * `/2.0/locals/{id}/default` * `/2.0/locals/{id}/holidays` * `/2.0/locals/{id}/users` * `/2.0/locals/{id}/usersgroup` * `/2.0/locals/{id}/holidays/{holidayId}` * `/2.0/locals/{id}/users/unrelated` * `/2.0/locals/{id}/users/{userCode}` | * `GET, POST` * `GET` * `DELETE, GET, PATCH, PUT` * `PUT` * `GET` * `GET, POST` * `POST` * `DELETE` * `GET` * `DELETE` | REST for locals |
| MechanismServiceRest | * `/bpm/mechanism/create` * `/bpm/mechanism/remove` * `/bpm/mechanism/update` * `/bpm/mechanism/{id}/{process}` | * `POST` * `POST` * `POST` * `GET` | Mechanisms |
| MediaServiceRest | * `/social/community/gallery` * `/social/community/media` * `/social/community/gallery/new` * `/social/community/gallery/remove` * `/social/community/gallery/update` * `/social/community/media/new` * `/social/community/media/remove` * `/social/community/media/update` * `/social/community/media/{galleryId}/{communityAlias}/{type}` * `/social/community/gallery/byid/{galleryId}/{communityAlias}/{type}` * `/social/community/gallery/byname/{galleryName}/{communityAlias}/{type}` * `/social/community/media/{mediaId}/{galleryId}/{communityAlias}/{type}` | * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` | Media |
| MentionServiceRest | * `/mention/findMentions` | * `GET` | Mention |
| PageRest | * `/2.0/pages/createPageDraftFromVersion` * `/2.0/pages/findMenuFromPage` * `/2.0/pages/findPages` * `/2.0/pages/publishPageDraft` * `/2.0/pages/reloadPageLayout` * `/2.0/pages/disable/{pageCode}` * `/2.0/pages/enable/{pageCode}` * `/2.0/pages/getWidgetPreferences/{instanceId}` * `/2.0/pages/hide/{pageCode}` * `/2.0/pages/mobileMapping/{pageCode}` * `/2.0/pages/pageHistory/{pageCode}` * `/2.0/pages/show/{pageCode}` * `/2.0/pages/updateWidgetMobileStatus/{instanceId}` | * `POST` * `GET` * `GET` * `POST` * `POST` * `PUT` * `PUT` * `GET` * `PUT` * `GET` * `GET` * `PUT` * `POST` | Page |
| PermissionRest | * `/2.0/permission/listall/widgets` * `/2.0/permission/find/widget/{widgetCode}` * `/2.0/permission/grantdefault/widget/{widgetCode}` * `/2.0/permission/revoke/widget/{widgetCode}` | * `GET` * `GET` * `POST` * `POST` | Permission |
| PostRest | * `/2.0/posts/create` * `/2.0/posts/editComment` * `/2.0/posts/editPost` * `/2.0/posts/findComment/{commentId}` * `/2.0/posts/create/with/upload` | * `POST` * `POST` * `POST` * `GET` * `POST` | Post |
| PostServiceRest | * `/social/post/create` * `/social/post/notify` * `/social/post/publish` * `/social/post/remove` * `/social/post/stopNotify` * `/social/post/{genericId}` * `/social/post/list/{genericId}` * `/social/post/listSortedPost/{genericId}` * `/social/post/listSortedPostByLogin/{login}` * `/social/post/notifyList/{postId}` * `/social/post/read/{postId}` * `/social/post/create/with/upload` * `/social/post/read/post/{postId}` | * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `GET` | Timeline posts |
| ProfileServiceRest | * `/profile/change/picture` * `/profile/edit/profile` * `/profile/image/{genericId}/{type}` | * `POST` * `POST` * `GET` | Profile |
| PushAlertServiceRest | * `/push/changeLanguage` * `/push/changeStatus` * `/push/register` | * `POST` * `POST` * `POST` | Push |
| RelationServiceRest | * `/relation/canAccessByLogin` * `/relation/canAccessByLogins` * `/relation/canAccessBySocialId` * `/relation/recountRelations` * `/relation/followers/{genericId}` * `/relation/following/{genericId}` * `/relation/isFollowing/{genericId}` * `/relation/listFollowersWithRelevance/{genericId}` * `/relation/listFollowingWithRelevance/{genericId}` * `/relation/followers/v2/{genericId}` * `/relation/following/v2/{genericId}` | * `GET` * `POST` * `GET` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Relation |
| RoleServiceRest | * `/wcm/role/findUsingFilter` | * `GET` | Roles |
| SearchRest | * `/2.0/search` * `/2.0/search/findInfluencers` * `/2.0/search/groupedSearch` * `/2.0/search/groupedSearchByType` | * `POST` * `GET` * `POST` * `POST` | Search |
| SearchServiceRest | * `/search/advanced` | * `POST` | Searches |
| SecurityRest | * `/2.0/security/changeUserPassword` * `/2.0/security/getCurrentTenant` * `/2.0/security/createPermissions/{resourceCode}` * `/2.0/security/deletePermissions/{resourceCode}` * `/2.0/security/getPermissionsByResourceCode/{resourceCode}` * `/2.0/security/listResourcesByCategory/{category}` * `/2.0/security/hasPermission/{resource}/{permiss}` | * `POST` * `GET` * `POST` * `POST` * `GET` * `GET` * `GET` | Security |
| ShareServiceRest | * `/social/share/share` * `/social/share/shareContent` * `/social/share/list/socialstoshare` * `/social/share/list/{sociableId}` * `/social/share/validate/share/{contentId}/{sourceShareType}` * `/social/share/validate/social/{contentId}/{genericId}/{shareType}` | * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` | Share |
| SociableDocumentServiceRest | * `/ecm/sociabledocument/comment` * `/ecm/sociabledocument/denounce` * `/ecm/sociabledocument/follow` * `/ecm/sociabledocument/like` * `/ecm/sociabledocument/share` * `/ecm/sociabledocument/comment/denounce` * `/ecm/sociabledocument/comment/remove` * `/ecm/sociabledocument/comment/v2` * `/ecm/sociabledocument/like/v2` * `/ecm/sociabledocument/comment/{id}/{version}` * `/ecm/sociabledocument/counter/{id}/{version}` * `/ecm/sociabledocument/denouncement/{id}/{version}` * `/ecm/sociabledocument/follow/{id}/{version}` * `/ecm/sociabledocument/like/{id}/{version}` * `/ecm/sociabledocument/share/{id}/{version}` * `/ecm/sociabledocument/comment/v2/{id}/{version}` * `/ecm/sociabledocument/counter/v2/{id}/{version}` * `/ecm/sociabledocument/folder/{tenant}/{alias}/{feature}` * `/ecm/sociabledocument/like/v2/{id}/{version}` * `/ecm/sociabledocument/enabled/{tenant}/{userCode}/{alias}/{feature}` | * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Social features for documents |
| SociableServiceRest | * `/sociable/comment` * `/sociable/comment/post` * `/sociable/comments/{sociableId}` * `/sociable/deleteStreamedFile/{fileName}` * `/sociable/like/{sociableObjectId}` * `/sociable/likers/{sociableId}` * `/sociable/comment/remove/{commentId}` * `/sociable/comments/v2/{sociableId}` * `/sociable/likers/v2/{sociableId}` * `/sociable/upload/stream/form/{fileName}` * `/sociable/upload/stream/octet/{fileName}` | * `POST` * `POST` * `GET` * `POST` * `POST` * `GET` * `POST` * `GET` * `GET` * `POST` * `POST` | Social features |
| SocialBreadcrumbRest | * `/2.0/communities/breadcrumb/get/{alias}/{documentId}` | * `GET` | SocialBreadcrumb - v2 |
| SocialCloudServiceRest | * `/socialcloud/defaultgroup` * `/socialcloud/add/securitygroups` * `/socialcloud/cloud/create` * `/socialcloud/cloud/getDefault` * `/socialcloud/cloud/isEnabled` * `/socialcloud/cloud/remove` * `/socialcloud/cloud/update` * `/socialcloud/list/allgroups` * `/socialcloud/remove/securitygroups` * `/socialcloud/add/community/group` * `/socialcloud/add/user/group` * `/socialcloud/cloud/enable/{enabled}` * `/socialcloud/cloud/setDefault/{cloudCode}` * `/socialcloud/list/clouds/search` * `/socialcloud/list/communities/group` * `/socialcloud/list/findCloud/{code}` * `/socialcloud/list/users/group` * `/socialcloud/listCloud/in/{genericId}` * `/socialcloud/listCloud/out/{genericId}` * `/socialcloud/listSecurityGroup/in/{cloudCode}` * `/socialcloud/listSecurityGroup/out/{cloudCode}` * `/socialcloud/remove/communities/group` * `/socialcloud/remove/community/group` * `/socialcloud/remove/user/group` * `/socialcloud/remove/users/group` * `/socialcloud/list/allcommunities/notin/group` * `/socialcloud/list/clouds/community/{alias}` * `/socialcloud/list/clouds/user/{genericId}` * `/socialcloud/list/users/notin/group` * `/socialcloud/listSocial/in/{socialType}/{cloudCode}` * `/socialcloud/listSocial/out/{socialType}/{cloudCode}` * `/socialcloud/remove/groups/social/{socialType}` | * `GET` * `POST` * `POST` * `GET` * `GET` * `POST` * `POST` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` | Cloud |
| SubstituteUserServiceRest | * `/bpm/substituteUser/create` * `/bpm/substituteUser/remove` * `/bpm/substituteUser/update` * `/bpm/substituteUser/getSubstitutesOfUser/{companyId}/{userId}` * `/bpm/substituteUser/getValidSubstituteOfUser/{companyId}/{userId}` * `/bpm/substituteUser/getValidSubstitutedUsers/{companyId}/{substituteId}` * `/bpm/substituteUser/getAllSubstitute/{companyId}/{userId}/{substituteId}` * `/bpm/substituteUser/getAllValidSubstitute/{companyId}/{userId}/{substituteId}` * `/bpm/substituteUser/getSubstitute/{companyId}/{userId}/{substituteId}` * `/bpm/substituteUser/getValidSubstitute/{companyId}/{userId}/{substituteId}` | * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Substitute User |
| TagsCloudRest | * `/2.0/tags` | * `POST` | Tags |
| TasksRest | * `/2.0/tasks/transfer` * `/2.0/tasks/findApprovalDocumentsByUser/{colleagueId}` * `/2.0/tasks/findDocsInAgreement/{colleagueId}` * `/2.0/tasks/findDocsInCheckout/{colleagueId}` * `/2.0/tasks/findDocumentsToApprove/{colleagueId}` * `/2.0/tasks/findExpiredWorkflowTasks/{colleagueId}` * `/2.0/tasks/findMyDocuments/{colleagueId}` * `/2.0/tasks/findMyRequests/{colleagueId}` * `/2.0/tasks/findTasksInAgreement/{colleagueId}` * `/2.0/tasks/findWorkflowTasks/{colleagueId}` * `/2.0/tasks/getResumedTasks/{colleagueId}` | * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Tasks |
| TenantRest | * `/2.0/tenants/create` * `/2.0/tenants/getTenantData/{keys}` | * `POST` * `GET` | Tenants - V2 |
| UserRest | * `/2.0/users/changeUserPassword` * `/2.0/users/create` * `/2.0/users/getCurrent` * `/2.0/users/listAll` * `/2.0/users/updateUser` * `/2.0/users/updateUserData` * `/2.0/users/updateUserEvenDisabled` * `/2.0/users/activateByCode/{genericId}` * `/2.0/users/deactivateByLogin/{genericId}` * `/2.0/users/findById/{id}` * `/2.0/users/getUser/{genericId}` * `/2.0/users/list/{state}` * `/2.0/users/listData/{login}` * `/2.0/users/listGroups/{login}` * `/2.0/users/{userCode}/locals` | * `POST` * `POST` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | User - V2 |
| UserServiceRest | * `/social/listFavoriteUsersWithRelevance` * `/social/listUsersWithRelevance` * `/social/user` * `/social/change/image` * `/social/follow/accept` * `/social/follow/cleanAll` * `/social/follow/reject` * `/social/follow/remove` * `/social/follow/removeAll` * `/social/follow/request` * `/social/follower/{genericId}` * `/social/following/{genericId}` * `/social/image/{genericId}` * `/social/user/logged` * `/social/user/{genericId}` * `/social/change/image/v2` * `/social/imageBySize/{genericId}/{size}` * `/social/user/disable/{genericId}` * `/social/user/enable/{genericId}` * `/social/user/logged/v2` | * `GET` * `GET` * `GET` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `GET` * `POST` * `POST` * `GET` | Users |
| UserServiceRest | * `/wcm/user/create` * `/wcm/user/deleteByIdpId` * `/wcm/user/findActiveUsersUsingFilter` * `/wcm/user/findUsingFilter` | * `POST` * `POST` * `GET` * `GET` | User |
| WCMAdminTenantRest | * `/admin/tenant` * `/admin/tenant/analytics` * `/admin/tenant/disableFluigViewerCloud` * `/admin/tenant/emailConfig` * `/admin/tenant/enableFluigViewerCloud` * `/admin/tenant/fluigViewerCloudEnabled` * `/admin/tenant/getEmailConfig` * `/admin/tenant/identityConfig` * `/admin/tenant/updateMailConfig` * `/admin/tenant/disableFluigViewerCloud/{tenantId}` * `/admin/tenant/enableFluigViewerCloud/{tenantId}` * `/admin/tenant/fluigViewerCloudEnabled/{tenantId}` * `/admin/tenant/identityConfig/v2` | * `GET, POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET, POST` * `POST` * `POST` * `POST` * `GET` * `POST` | Tenants |
| WCMServiceRest | * `/wcm/assembleMenu` * `/wcm/configuration` * `/wcm/display` * `/wcm/findPages` * `/wcm/isHighAvailability` * `/wcm/logout` * `/wcm/theme` * `/wcm/version` * `/wcm/chronos/meanTimes` * `/wcm/oauth/generateKeys` * `/wcm/oauth/generateKeysToUser` * `/wcm/version/v2` * `/wcm/findPageFriendlyURL/{tenantId}/{pageCode}` | * `GET` * `GET` * `GET` * `GET` * `GET` * `POST` * `GET` * `GET` * `GET` * `POST` * `POST` * `GET` * `GET` | WCM core services |
| WorkflowRest | * `/2.0/workflows/assumeProcessTask` * `/2.0/workflows/assumeProcessTasks` * `/2.0/workflows/cancelInstance` * `/2.0/workflows/cancelInstances` * `/2.0/workflows/createProcessObservation` * `/2.0/workflows/listProcess` * `/2.0/workflows/findActiveTasks/{processInstanceId}` * `/2.0/workflows/getProcessVersion/{processId}` * `/2.0/workflows/requests/listSlaProcess` * `/2.0/workflows/requests/sla` * `/2.0/workflows/requests/tasks` * `/2.0/workflows/getAvailableProcess/{tenantId}/{userId}` * `/2.0/workflows/requests/sla/resume` * `/2.0/workflows/requests/tasks/resume` * `/2.0/workflows/requests/{processInstanceId}/sla` * `/2.0/workflows/findObservations/{processInstanceId}/{stateSequence}/{threadSequence}` * `/2.0/workflows/requests/sla/assignee/me` * `/2.0/workflows/requests/sla/manager/me` * `/2.0/workflows/requests/sla/requester/me` * `/2.0/workflows/requests/tasks/assignee/me` * `/2.0/workflows/requests/tasks/manager/me` * `/2.0/workflows/requests/tasks/requester/me` * `/2.0/workflows/requests/sla/resume/assignee/me` * `/2.0/workflows/requests/sla/resume/manager/me` * `/2.0/workflows/requests/sla/resume/requester/me` * `/2.0/workflows/requests/tasks/resume/assignee/me` * `/2.0/workflows/requests/tasks/resume/manager/me` * `/2.0/workflows/requests/tasks/resume/requester/me` | * `POST` * `POST` * `POST` * `POST` * `POST` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` * `GET` | Workflow |

# Data Types

### JSON

| type | description |
| --- | --- |
| APIException | Class to build error responses thrown by the API. |
| AbstractFormComponentVO |  |
| AbstractSearch |  |
| AccessType |  |
| AccusoftWorkFileSession |  |
| ActivateApplicationVO |  |
| ActivateEventVO |  |
| AdHocProcessVO |  |
| AdHocServiceRest | AdHoc Processes (Task List) |
| AddParticipantsVO |  |
| AddUserToCommunityVO |  |
| AdminUserVO |  |
| AdminUserVO |  |
| AlertActionVO |  |
| AlertActionVO |  |
| AlertAppSenderVO |  |
| AlertConfigVO |  |
| AlertEventVO |  |
| AlertEventVO |  |
| AlertModuleVO |  |
| AlertModuleVO |  |
| AlertObjectVO |  |
| AlertObjectVO |  |
| AlertRest | Notification - V2 |
| AlertSenderVO |  |
| AlertSenderVO |  |
| AlertServiceRest | Notifications |
| AlertUserVO |  |
| AlertUserVO |  |
| AlertVO |  |
| AlertVO |  |
| AllocatedDocumentVO |  |
| AnalyticsOrderVO |  |
| AnalyticsVO |  |
| Annotation |  |
| ApiPublicConfig |  |
| ApiPublicConstant |  |
| Application |  |
| ApplicationCategoryVO |  |
| ApplicationConfig |  |
| ApplicationDTO |  |
| ApplicationInstanceVO |  |
| ApplicationPublisherVO |  |
| ApplicationRenderResourceVO |  |
| ApplicationRenderVO |  |
| ApplicationVO |  |
| ApproveDocumentVO |  |
| ArticleCategoryVO |  |
| ArticleCoverVO |  |
| ArticleCoverVO |  |
| ArticleCoverVO |  |
| ArticleCreateVO |  |
| ArticleLiveURLVO |  |
| ArticleRest | Articles - V2 |
| ArticleServiceRest | Articles (in communities) |
| ArticleVO |  |
| ArticleVO |  |
| AssumeProcessTaskVO |  |
| AssumeProcessTasksVO |  |
| Attachment |  |
| AttachmentSource |  |
| AttachmentUserActivityVO |  |
| AttachmentVO |  |
| AttachmentVO |  |
| AttachmentVO |  |
| AttachmentVO |  |
| AttributionMechanismVO |  |
| AuthorizationVO |  |
| AuthorizeClientRest | Authorize |
| AuthorizeClientVO |  |
| Base64MediaVO |  |
| CacheMode |  |
| CancelInstanceParameterVO |  |
| CancelInstanceVO |  |
| CancelInstancesVO |  |
| CardCreateVO |  |
| CardFieldVO |  |
| CardIndexAttachmentCreateVO |  |
| CardIndexAttachmentCreateVO |  |
| CardIndexAttachmentVO |  |
| CardIndexCreateVO |  |
| CardIndexCreateVO |  |
| CardIndexRest | Card Index |
| CardIndexVO |  |
| CardItemVO |  |
| CardPermissionVO |  |
| CardPersistenceType |  |
| CardPublisherAttachmentVO |  |
| CardRest | Cards |
| CategoryServiceRest | Categories |
| CategoryVO | Categories |
| CentralTaskFilterFieldVO |  |
| CentralTaskFilterVO |  |
| Certificate |  |
| CheckboxComponentVO |  |
| ClassLoader |  |
| CloudVO |  |
| ColComponentVO |  |
| ColFluidComponentVO |  |
| CollaborationAppVO |  |
| CollaborationRest | Collaboration |
| CollaborationVO |  |
| ColleagueVO |  |
| ColleagueVO |  |
| ComboComponentVO |  |
| CommentVO |  |
| CommunityCreateVO |  |
| CommunityDocumentServiceRest | Document features for communities |
| CommunityFolderType |  |
| CommunityRest | Community |
| CommunitySearch |  |
| CommunityServiceRest | Communities |
| CommunityVO |  |
| CommunityVO |  |
| CompanyDTO |  |
| CompleteFilterVO |  |
| ConfigurationDataVO |  |
| ConfigurationServiceRest | System Configuration |
| ConfigurationVO |  |
| ConfigurationVO |  |
| ConstraintType |  |
| ContentFilesRest | ContentFiles |
| ContinueThroughIntermediateErrorVO |  |
| Cookie |  |
| CopyAttachmentsVO |  |
| CreateEventVO |  |
| CreateModuleVO |  |
| CropVO |  |
| CropVO |  |
| Dataset |  |
| DatasetInfoVO |  |
| DatasetOfflineMobileRestVO |  |
| DatasetPK |  |
| DatasetServiceRest | Datasets |
| DatasetVO |  |
| DatasetVO |  |
| DatatableVO |  |
| DateGap |  |
| DefaultExceptionMapper |  |
| DefaultSearchResponse |  |
| DenounceCommentVO |  |
| DenounceVO |  |
| DivComponentVO |  |
| Document |  |
| DocumentApproverVO |  |
| DocumentCreatePermissionVO |  |
| DocumentCreateVO | Value Object para Documento |
| DocumentLanguageVO |  |
| DocumentPK |  |
| DocumentPermissionVO |  |
| DocumentRest | Document |
| DocumentRestrictionVO |  |
| DocumentSearch |  |
| DocumentSecurityConfigVO |  |
| DocumentSecurityVO |  |
| DocumentServiceRest | Documents |
| DocumentTaskVO |  |
| DocumentType |  |
| DocumentType |  |
| DocumentVO |  |
| DocumentVO |  |
| DocumentWatchVO |  |
| DocumentationProxyRest | DocumentationProxyRest |
| DriveServiceRest | Fluig Connect |
| DriveTenantDataVO |  |
| DriveVO |  |
| ECMExceptionMapper |  |
| EMailConfigVO |  |
| EncodedMediaType |  |
| ~~EncodedMediaType~~ |  |
| EntityMode |  |
| EntityTag |  |
| EnumerationOfServlet |  |
| EnumerationOfString |  |
| ErrorCode |  |
| ~~ErrorHandler~~ |  |
| ErrorVO |  |
| Exception |  |
| ExecuteUpdateResultCheckStyle |  |
| ExtendedCommunityVO | Extended Visual Object for community. Contains social DOCUMENT, GALLERY\_PHOTO, GALLERY\_VIDEO, ARTICLE, FORM. |
| FDNAlertActionType |  |
| FDNAlertIntegrationType |  |
| FDNCategory |  |
| FDNCategoryResource |  |
| FDNException |  |
| FDNGroup |  |
| FDNGroupData |  |
| FDNGroupDataVO |  |
| FDNGroupUserRole |  |
| FDNGroupVO |  |
| FDNJaasUserGroup |  |
| FDNLocal |  |
| FDNMessage |  |
| FDNMessageType |  |
| FDNParamGeral |  |
| FDNPermission |  |
| FDNProduct |  |
| FDNResource |  |
| FDNResourceType |  |
| FDNResourceTypePermission |  |
| FDNRole |  |
| FDNRoleData |  |
| FDNSite |  |
| FDNTenant |  |
| FDNTenantData |  |
| FDNTenantProduct |  |
| FDNTokenResourceType |  |
| FDNTransferObjectVO |  |
| FDNUser |  |
| FDNUserData |  |
| FDNUserLogging |  |
| FDNUserMobileToken |  |
| FDNUserPicture |  |
| FDNUserPictureVO |  |
| FDNUserRole |  |
| FDNUserTenant |  |
| FDNUserToken |  |
| FDNUserTokenResource |  |
| FDNUserType |  |
| FDNVolume |  |
| FDNVolumeSite |  |
| Family |  |
| FavoriteServiceRest | Favorites |
| FavoriteVO |  |
| FavoritesRest | Favorites |
| FieldsService | Central Tasks FilterFields Services |
| FileUploadData |  |
| FileUploadVO |  |
| Filter |  |
| FilterFieldService |  |
| FilterFieldVO |  |
| FilterFieldVO |  |
| FilterGroupVO |  |
| FilterOrderVO |  |
| FilterOrderVO |  |
| FilterRest | Filters - V2 |
| FilterService |  |
| FilterService | Central Tasks Filter Services |
| FilterUpdateNameVO |  |
| FilterVO |  |
| FilterVO |  |
| FlashRenderProperties |  |
| FluigMessage |  |
| FluigMessageType |  |
| FluigRest |  |
| FluigRestResult |  |
| FluigViewerVO | Created by rodrigo on 19/10/16. |
| FlushMode |  |
| FolderCreateVO |  |
| FolderDocumentRest | Folder Document |
| FolderPublisherCheckboxDefaultPropertyVO |  |
| FolderVO |  |
| ForbiddenServlet | Servlet to return correct [http forbidden](https://api.fluig.com/old/http forbidden) status to unauthenticated users. |
| FormComponentVO |  |
| FormDataset |  |
| FormDatasetVO |  |
| FormSearch |  |
| GalleryVO |  |
| GenerationTiming |  |
| GenericAlertObject |  |
| ~~GenericBean~~ |  |
| GenericServlet |  |
| ~~GenericVO~~ | ~~Use a classe WCMRestResult~~ |
| GlobalParameterRest | Global parameter |
| GlobalSearch |  |
| GlobalSearchVO |  |
| GroupCreateVO |  |
| GroupRest | Group |
| GroupServiceRest | Groups |
| GroupVO |  |
| GroupedAlertVO |  |
| GroupsVO |  |
| Header |  |
| HitsDto |  |
| HolidayRest |  |
| HolidayVO |  |
| Html5RenderProperties |  |
| HttpServlet |  |
| I18nServiceRest | I18nServiceRest |
| IdentityApplicationConfigVO |  |
| IdentityApplicationVO |  |
| IdentityCompanyVO |  |
| IdentityContextVO |  |
| IdentityMenuVO |  |
| IdentityQuickViewDataVO |  |
| IdentityQuickViewModelVO |  |
| IdentityQuickViewVO |  |
| IdentityResponseVO |  |
| IdentityRest | Session |
| IdentityVO |  |
| ImageComponentVO |  |
| InfluencersSearch |  |
| InputComponentVO |  |
| IntervalType |  |
| InviteServiceRest | Invites |
| InviteVO |  |
| JaxbCfgCacheUsageEnum |  |
| JaxbCfgCollectionCacheType |  |
| JaxbCfgConfigPropertyType |  |
| JaxbCfgEntityCacheType |  |
| JaxbCfgEventListenerGroupType |  |
| JaxbCfgEventListenerType |  |
| JaxbCfgEventTypeEnum |  |
| JaxbCfgGrant |  |
| JaxbCfgHibernateConfiguration |  |
| JaxbCfgMappingReferenceType |  |
| JaxbCfgSecurity |  |
| JaxbCfgSessionFactory |  |
| JaxbHbmAnyAssociationType |  |
| JaxbHbmAnyValueMappingType |  |
| JaxbHbmArrayType |  |
| JaxbHbmAuxiliaryDatabaseObjectType |  |
| JaxbHbmBagCollectionType |  |
| JaxbHbmBaseVersionAttributeType |  |
| JaxbHbmBasicAttributeType |  |
| JaxbHbmBasicCollectionElementType |  |
| JaxbHbmCacheInclusionEnum |  |
| JaxbHbmCacheType |  |
| JaxbHbmClassRenameType |  |
| JaxbHbmCollectionIdType |  |
| JaxbHbmColumnType |  |
| JaxbHbmCompositeAttributeType |  |
| JaxbHbmCompositeCollectionElementType |  |
| JaxbHbmCompositeIdType |  |
| JaxbHbmCompositeIndexType |  |
| JaxbHbmCompositeKeyBasicAttributeType |  |
| JaxbHbmCompositeKeyManyToOneType |  |
| JaxbHbmConfigParameterContainer |  |
| JaxbHbmConfigParameterType |  |
| JaxbHbmCustomSqlDmlType |  |
| JaxbHbmDefinition |  |
| JaxbHbmDialectScopeType |  |
| JaxbHbmDiscriminatorSubclassEntityType |  |
| JaxbHbmDynamicComponentType |  |
| JaxbHbmEntityBaseDefinition |  |
| JaxbHbmEntityDiscriminatorType |  |
| JaxbHbmFetch |  |
| JaxbHbmFetchProfileType |  |
| JaxbHbmFetchStyleEnum |  |
| JaxbHbmFetchStyleWithSubselectEnum |  |
| JaxbHbmFilterAliasMappingType |  |
| JaxbHbmFilterDefinitionType |  |
| JaxbHbmFilterParameterType |  |
| JaxbHbmFilterType |  |
| JaxbHbmGeneratorSpecificationType |  |
| JaxbHbmHibernateMapping |  |
| JaxbHbmIdBagCollectionType |  |
| JaxbHbmIdentifierGeneratorDefinitionType |  |
| JaxbHbmIndexManyToAnyType |  |
| JaxbHbmIndexManyToManyType |  |
| JaxbHbmIndexType |  |
| JaxbHbmJoinedSubclassEntityType |  |
| JaxbHbmKeyType |  |
| JaxbHbmLazyEnum |  |
| JaxbHbmLazyWithExtraEnum |  |
| JaxbHbmLazyWithNoProxyEnum |  |
| JaxbHbmListIndexType |  |
| JaxbHbmListType |  |
| JaxbHbmLoaderType |  |
| JaxbHbmManyToAnyCollectionElementType |  |
| JaxbHbmManyToManyCollectionElementType |  |
| JaxbHbmManyToOneType |  |
| JaxbHbmMapKeyBasicType |  |
| JaxbHbmMapKeyCompositeType |  |
| JaxbHbmMapKeyManyToManyType |  |
| JaxbHbmMapType |  |
| JaxbHbmMultiTenancyType |  |
| JaxbHbmNamedNativeQueryType |  |
| JaxbHbmNamedQueryType |  |
| JaxbHbmNativeQueryCollectionLoadReturnType |  |
| JaxbHbmNativeQueryJoinReturnType |  |
| JaxbHbmNativeQueryPropertyReturnType |  |
| JaxbHbmNativeQueryReturnType |  |
| JaxbHbmNativeQueryScalarReturnType |  |
| JaxbHbmNaturalIdCacheType |  |
| JaxbHbmNaturalIdType |  |
| JaxbHbmNestedCompositeElementType |  |
| JaxbHbmNotFoundEnum |  |
| JaxbHbmOnDeleteEnum |  |
| JaxbHbmOneToManyCollectionElementType |  |
| JaxbHbmOneToOneType |  |
| JaxbHbmOuterJoinEnum |  |
| JaxbHbmParentType |  |
| JaxbHbmPolymorphismEnum |  |
| JaxbHbmPrimitiveArrayType |  |
| JaxbHbmPropertiesType |  |
| JaxbHbmQueryParamType |  |
| JaxbHbmResultSetMappingType |  |
| JaxbHbmReturnColumn |  |
| JaxbHbmReturnDiscriminator |  |
| JaxbHbmRootEntityType |  |
| JaxbHbmSecondaryTableType |  |
| JaxbHbmSetType |  |
| JaxbHbmSimpleIdType |  |
| JaxbHbmSubclassEntityBaseDefinition |  |
| JaxbHbmSynchronizeType |  |
| JaxbHbmTimestampAttributeType |  |
| JaxbHbmTimestampSourceEnum |  |
| JaxbHbmToolingHintContainer |  |
| JaxbHbmToolingHintType |  |
| JaxbHbmTuplizerType |  |
| JaxbHbmTypeDefinitionType |  |
| JaxbHbmTypeSpecificationType |  |
| JaxbHbmUnionSubclassEntityType |  |
| JaxbHbmUnsavedValueCompositeIdEnum |  |
| JaxbHbmUnsavedValueTimestampEnum |  |
| JaxbHbmUnsavedValueVersionEnum |  |
| JaxbHbmVersionAttributeType |  |
| JobRest | Job Scheduler - V2 |
| JobRestVO |  |
| JobVO |  |
| JspConfigDescriptor |  |
| JspPropertyGroupDescriptor |  |
| Knowledge |  |
| KnowledgePK |  |
| KnowledgeVO |  |
| LicenseDataVO |  |
| LikerVO |  |
| Link |  |
| LiteralLastUpdateVO |  |
| LiteralServiceRest |  |
| LocalRest | REST for locals |
| LocalUserVO |  |
| LocalVO |  |
| LocaleFilter | Filter to set request locale |
| LockMode |  |
| MailConfigurationVO |  |
| MarkAlertAsReadVO |  |
| MarkupProcessStateDTO |  |
| MasterListFilterVO |  |
| MasterListPrintFormat |  |
| MechanismServiceRest | Mechanisms |
| MediaServiceRest | Media |
| MediaType |  |
| MediaType |  |
| MediaVO |  |
| MediaVO |  |
| MentionServiceRest | Mention |
| MentionVO |  |
| MenuAuth |  |
| MobileAttachmentVO |  |
| MobileDocumentVO |  |
| Module |  |
| ModuleDescriptor |  |
| ModuleLayer |  |
| MostUsedWorkflowProcessByUserVO |  |
| NameValue |  |
| NamedPackage |  |
| NewCookie |  |
| NoCodeAccessTokenVO |  |
| NoCodeAuthorizationCodeVO |  |
| NoCodeCredentialsVO |  |
| OAuthAppKeyVO |  |
| OAuthApplicationDataVO |  |
| OAuthSdkVO |  |
| OAuthVO |  |
| OptimisticLockStyle |  |
| OptionValueVO |  |
| Ordering |  |
| OrganizationKeyVO |  |
| OrganizationVO |  |
| PATCH |  |
| Package |  |
| PageAuth |  |
| PageRest | Page |
| PageVO |  |
| PanelComponentVO |  |
| PermissionAssetVO |  |
| PermissionResourceVO |  |
| PermissionRest | Permission |
| PermissionVO |  |
| PermissionVO |  |
| PingServlet |  |
| PluralAttributeInfoIdBagAdapter |  |
| PluralAttributeInfoPrimitiveArrayAdapter |  |
| PostCreateVO |  |
| PostRest | Post |
| PostServiceRest | Timeline posts |
| PostVO |  |
| PrivateKey |  |
| ProcessAttachment |  |
| ProcessAttachmentPK |  |
| ProcessAttachmentSavedVO |  |
| ProcessAttachmentVO |  |
| ProcessAttachmentVO |  |
| ProcessDefinitionVO |  |
| ProcessDefinitionVersionAlertStatusVO |  |
| ProcessDefinitionVersionAlertVO |  |
| ProcessDefinitionVersionAlertVO |  |
| ProcessDefinitionVersionVO |  |
| ProcessHistoryTypeEnumeration |  |
| ProcessHistoryVO |  |
| ProcessInstanceInfoVO |  |
| ProcessLinkMessageVO |  |
| ProcessObservationVO |  |
| ProcessSearch |  |
| ProcessSearchProcessListResultVO |  |
| ProcessSearchProcessResultVO |  |
| ProcessSearchProcessVO |  |
| ProcessSearchVO |  |
| ProcessStateDto |  |
| ProcessStateVO |  |
| ProcessTaskInfoVO |  |
| ProcessTaskVO |  |
| ProcessTaskVO |  |
| ProcessVersionVO |  |
| ProfileServiceRest | Profile |
| PublicApiPageVO |  |
| PublicApiPostVO |  |
| PublicKey |  |
| PublisherAllocatedPKVO |  |
| PublisherFileVO |  |
| PublisherVO |  |
| PushAlertServiceRest | Push |
| PushAppEnum |  |
| PushConfigurationException |  |
| PushConfigurationVO |  |
| PushServiceEnum |  |
| RadioComponentVO |  |
| RatingComponentVO |  |
| ReasonVO |  |
| RegisterApplicationVO |  |
| RelatedAction |  |
| RelatedDocumentVO |  |
| RelationServiceRest | Relation |
| RelationVO | Created by diego.lopes on 27/08/2015. |
| RemoveAlertByObjectAndEventVO |  |
| RemoveAlertVO |  |
| RemoveAlertsVO |  |
| RenderProperties |  |
| RequestParticipationVO |  |
| RequestProcessTaskVO |  |
| RequestSLAVO |  |
| RequestTaskLocalVO |  |
| RequestTaskSLAVO |  |
| RequestTaskVO |  |
| ResourceVO |  |
| Response |  |
| RestorePermissionObjectVO |  |
| RestorePermissionsVO |  |
| ResumeTasksVO |  |
| ResumeVO |  |
| ResumedTasksVO |  |
| RoleServiceRest | Roles |
| RoleVO |  |
| RowComponentVO |  |
| RowFluidComponentVO |  |
| RuleCollectionVO |  |
| RulesComponentVO |  |
| RulesVO |  |
| RuntimeException |  |
| SECURITY\_LEVEL |  |
| SearchConstraintVO |  |
| SearchConstraintVO |  |
| SearchGroupResultVO |  |
| SearchLicenseResultVO |  |
| SearchProductParamVO |  |
| SearchRest | Search |
| SearchServiceRest | Searches |
| SearchTagsCloudVO |  |
| SearchUserParamVO |  |
| SearchVo |  |
| SecurityRest | Security |
| SendAlertVO |  |
| SensitiveDataVO |  |
| Serializable |  |
| ServerLogLineExpandVO |  |
| ServerLogLineVO |  |
| ServletConfig |  |
| ServletContext |  |
| SessionCookieConfig |  |
| SessionTrackingMode |  |
| ShareServiceRest | Share |
| ShareVO |  |
| ShareVO |  |
| Sociable |  |
| SociableCommentVO |  |
| SociableDenouncementType |  |
| SociableDocumentCommentVO |  |
| SociableDocumentDenouncementVO |  |
| SociableDocumentDto |  |
| SociableDocumentFollowVO |  |
| SociableDocumentLikeVO |  |
| SociableDocumentServiceRest | Social features for documents |
| SociableDocumentShareVO |  |
| SociableDocumentVO |  |
| SociableServiceRest | Social features |
| SociableShareType |  |
| SociableVO |  |
| SociableVO |  |
| Social |  |
| SocialBaseEntity |  |
| SocialBreadcrumbItemVO |  |
| SocialBreadcrumbItemVO |  |
| SocialBreadcrumbItemVO |  |
| SocialBreadcrumbRest | SocialBreadcrumb - v2 |
| SocialBreadcrumbVO |  |
| SocialBreadcrumbVO |  |
| SocialBreadcrumbVO |  |
| SocialCloudServiceRest | Cloud |
| SocialDocDto |  |
| SocialDocsDto |  |
| SocialDocsVO |  |
| SocialDocumentType |  |
| SocialDocumentVO |  |
| SocialEcmVO |  |
| SocialFavoriteVO |  |
| SocialFolderVO |  |
| SocialInviteStatus |  |
| SocialInviteVO |  |
| SocialMediaType |  |
| SocialPostType |  |
| SocialPostVisibility |  |
| SocialRelationStatus |  |
| SocialType |  |
| SocialUser |  |
| SocialVO |  |
| SocialVO |  |
| ~~SocialVisibility~~ |  |
| SolvedPermissionVO |  |
| SourceShareType |  |
| StackTraceElement |  |
| StatesVO |  |
| Status |  |
| StatusType |  |
| SubstituteUserProcessVO |  |
| SubstituteUserServiceRest | Substitute User |
| SubstituteUserVO |  |
| SuggestTagSearch |  |
| SuggestWordSearch |  |
| TabComponentVO |  |
| TableComponentVO |  |
| TabsComponentVO |  |
| TaglibDescriptor |  |
| TagsCloudRest | Tags |
| TakeTaskParameterVO |  |
| TaskTransferVO |  |
| TaskTypeVO |  |
| TasksRest | Tasks |
| TenantCreateVO |  |
| TenantRest | Tenants - V2 |
| TenantVO |  |
| TenantVO |  |
| TextAreaComponentVO |  |
| Throwable |  |
| TimelineSearch |  |
| TimelineVO |  |
| TotalKnowledgeVO |  |
| UpdateUserVo |  |
| UriBuilder |  |
| UserAuthTokenSessionVO |  |
| UserCreateVO |  |
| UserKeyVO |  |
| UserMetadataVO |  |
| UserPasswordVO |  |
| UserPasswordVO |  |
| UserRest | User - V2 |
| UserSearch |  |
| UserServiceRest | User |
| UserServiceRest | Users |
| UserState |  |
| UserTokenStatus |  |
| UserVO |  |
| UserVO |  |
| UserVO |  |
| UserVO |  |
| UserWorkflowProcessVO |  |
| VO |  |
| ViewingSession |  |
| ViewingSessionProperties |  |
| WCMAdminTenantRest | Tenants |
| WCMApplication |  |
| WCMApplicationAppDependency |  |
| WCMApplicationCategory |  |
| WCMApplicationData |  |
| WCMApplicationDependency |  |
| WCMApplicationLocale |  |
| WCMApplicationProduct |  |
| WCMApplicationResource |  |
| WCMApplicationService |  |
| WCMApplicationUserData |  |
| WCMCRUDVO |  |
| WCMComponent |  |
| WCMComponentPage |  |
| WCMConfiguration |  |
| WCMConfigurationVO |  |
| WCMCountCategoryVO |  |
| WCMLayout |  |
| WCMLayoutSlot |  |
| WCMMenuItem |  |
| WCMPage |  |
| WCMPageData |  |
| WCMPageKeyVO |  |
| WCMPageVO |  |
| WCMPageVersion |  |
| WCMPageWidget |  |
| WCMResourceComponent |  |
| WCMResourceComponentFile |  |
| WCMResourceKit |  |
| WCMResourceKitFile |  |
| WCMRest |  |
| WCMRestResult |  |
| WCMServiceRest | WCM core services |
| WCMStoreItemMetric |  |
| WCMTenantApplication |  |
| WCMTheme |  |
| WCMThemeHistory |  |
| WCMWidget |  |
| WatermarkProperties |  |
| WebApplicationException |  |
| WidgetPartApproverConfigVO |  |
| WidgetPartDefaultPropertyCustomFieldsVO |  |
| WidgetPartDefaultPropertyDocumentTypeVO |  |
| WidgetPartDefaultPropertyTopicVO |  |
| WidgetPartDefaultPropertyVO |  |
| WidgetPartGeneralInformationCustomFieldsVO |  |
| WidgetPartGeneralInformationDocumentTypeVO |  |
| WidgetPartGeneralInformationIconVO |  |
| WidgetPartGeneralInformationTopicVO |  |
| WidgetPartGeneralInformationVO |  |
| WidgetPartRelatedDocumentVO |  |
| WidgetPartSecurityConfigVO |  |
| WidgetVO |  |
| WorkflowAdHocProcessVO |  |
| WorkflowBatchInstanceVO |  |
| WorkflowCentralTasksVO |  |
| WorkflowConsensusDecisionVO |  |
| WorkflowConsensusVO |  |
| WorkflowProcessAvailableUsersVO |  |
| WorkflowProcessDto |  |
| WorkflowProcessErrorLogStatusVO |  |
| WorkflowProcessEventVO |  |
| WorkflowProcessEventVersionVO |  |
| WorkflowProcessToMobileDto |  |
| WorkflowProcessVO |  |
| WorkflowRest | Workflow |
| WorkflowTasksVO |  |
| WorkflowVO |  |
| WorkflowViewAppointmentVO |  |
| WorkflowViewAppointmentVO |  |
| WorkflowViewAttachmentAttachVO |  |
| WorkflowViewAttachmentVO |  |
| WorkflowViewObservationVO |  |
| WorkflowViewProcessHistorySearchVO |  |
| WorkflowViewProcessHistoryVO |  |
| WorkflowViewProcessStateVO |  |
| WorkflowViewProcessTaskCompleteDetailVO |  |
| WorkflowViewProcessTaskVO |  |
| WorkflowViewSendVO |  |
| WorkflowViewUpdateAttachmentVO |  |
| XMLComponent |  |
| XMLComponentDependency |  |
| XMLPage |  |
| XMLPageData |  |
| XMLPageSlot |  |
| XMLPages |  |
| XMLPermission |  |
| XMLPermissionMapping |  |
| XMLWidgetPreferences |  |
| ZoomComponentVO |  |

### XML

Default Namespace ([schema](https://api.fluig.com/old/ns0.xsd))

| type | description |
| --- | --- |
| alertConfigVO |  |
| documentApproverVO |  |
| documentPermissionVO |  |
| documentRestrictionVO |  |
| documentSecurityConfigVO |  |
| documentSecurityVO |  |
| folderVO |  |
| authorizeClientVO |  |
| approveDocumentVO |  |
| documentCreateVO | Value Object para Documento |
| searchTagsCloudVO |  |
| userPasswordVO |  |
