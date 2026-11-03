---
content_hash: d91fdbd4f86a2401d599f9a19e5d8e764212a12ca959ea09620d4093bf7bc5e9
fetched_at: '2026-11-03T14:34:38.716133+00:00'
page_id: json_TimelineVO
product: fluig
source: rest-fluig
title: Fluig REST — TimelineVO Data Type
type: documentation
url: https://api.fluig.com/old/json_TimelineVO.html
version: 1
---

# TimelineVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| formattedLink | string |  |  |
| user | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |  |
| numberDenouncements | number |  |  |
| comments | array of [SociableCommentVO](https://api.fluig.com/old/json_SociableCommentVO.html) |  |  |
| numberComments | number |  |  |
| youtubeVideoId | string |  |  |
| editionDate | number |  |  |
| formattedText | string |  |  |
| updateDate | number |  |  |
| removed | boolean |  |  |
| recommendationMetadata | map of string |  |  |
| customData | map of string |  |  |
| hasDocumentPermission | boolean |  |  |
| numberWatchers | number |  |  |
| urlOrigin | string |  |  |
| linkedObject | [Sociable](https://api.fluig.com/old/json_Sociable.html) |  |  |
| visibility | [SocialPostVisibility](https://api.fluig.com/old/json_SocialPostVisibility.html) |  |  |
| documentType | [DocumentType](https://api.fluig.com/old/json_DocumentType_vo.html) |  |  |
| link | string |  |  |
| permissionViewPostAdmUser | boolean | required |  |
| permissions | array of string |  |  |
| formattedWithoutMention | string |  |  |
| tags | string |  |  |
| supported | boolean | required |  |
| postId | number |  |  |
| creationDate | number |  |  |
| shareMentionVO | [MentionVO](https://api.fluig.com/old/json_MentionVO.html) |  |  |
| originShare | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |  |
| text | string |  |  |
| numberShares | number |  |  |
| mentions | map of string |  |  |
| url | string |  |  |
| hasMentions | boolean |  |  |
| approved | boolean |  |  |
| type | [SocialPostType](https://api.fluig.com/old/json_SocialPostType.html) |  |  |
| numberLikes | number |  |  |
| social | [SocialVO](https://api.fluig.com/old/json_SocialVO.html) |  |  |
| tenantId | number |  |  |
| attachments | array of [Sociable](https://api.fluig.com/old/json_Sociable.html) |  |  |
| youtubeLink | boolean | required |  |
| watching | boolean | required |  |

Example

```
{
  "formattedLink" : "...",
  "user" : {
    "numberFriends" : 12345,
    "approvalRequired" : true,
    "stateName" : "...",
    "forumId" : 12345,
    "ecmInfo" : {
      "property1" : { },
      "property2" : { }
    },
    "lastUpdate" : 12345,
    "isAdmin" : true,
    "idpId" : "...",
    "type" : "COMMUNITY",
    "numberFollowing" : 12345,
    "numberParticipations" : 12345,
    "numberFollowers" : 12345,
    "favorite" : true,
    "userData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "isCommunityAdmin" : true,
    "followerStatus" : "BLOCKED",
    "numberModerations" : 12345,
    "tenantId" : 12345,
    "isModerator" : true,
    "alias" : "...",
    "customPage" : true,
    "page" : "...",
    "foundationUserId" : 12345,
    "lastName" : "...",
    "createDate" : 12345,
    "id" : 12345,
    "uriCommunity" : "...",
    "permissions" : [ "...", "..." ],
    "name" : "...",
    "tenantAdmin" : true,
    "privateContent" : true,
    "state" : "REMOVED",
    "participantStatus" : "BLOCKED",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "NOT_RELATED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "numberDenouncements" : 12345,
  "comments" : [ {
    "sociableId" : 12345,
    "social" : {
      "numberFriends" : 12345,
      "approvalRequired" : true,
      "stateName" : "...",
      "forumId" : 12345,
      "ecmInfo" : {
        "property1" : { },
        "property2" : { }
      },
      "lastUpdate" : 12345,
      "isAdmin" : true,
      "idpId" : "...",
      "type" : "EVENT",
      "numberFollowing" : 12345,
      "numberParticipations" : 12345,
      "numberFollowers" : 12345,
      "favorite" : true,
      "userData" : {
        "property1" : "...",
        "property2" : "..."
      },
      "isCommunityAdmin" : true,
      "followerStatus" : "NOT_RELATED",
      "numberModerations" : 12345,
      "tenantId" : 12345,
      "isModerator" : true,
      "alias" : "...",
      "customPage" : true,
      "page" : "...",
      "foundationUserId" : 12345,
      "lastName" : "...",
      "createDate" : 12345,
      "id" : 12345,
      "uriCommunity" : "...",
      "permissions" : [ "...", "..." ],
      "name" : "...",
      "tenantAdmin" : true,
      "privateContent" : true,
      "state" : "REMOVED",
      "participantStatus" : "REJECTED",
      "admin" : { },
      "description" : "...",
      "followingStatus" : "NOT_RELATED",
      "email" : "...",
      "fullName" : "...",
      "userCode" : "...",
      "tenantUUID" : "...",
      "hasMobileWidget" : true,
      "hidden" : true
    },
    "formattedTextWithoutMention" : "...",
    "mentions" : {
      "property1" : "...",
      "property2" : "..."
    },
    "user" : {
      "numberFriends" : 12345,
      "approvalRequired" : true,
      "stateName" : "...",
      "forumId" : 12345,
      "ecmInfo" : {
        "property1" : { },
        "property2" : { }
      },
      "lastUpdate" : 12345,
      "isAdmin" : true,
      "idpId" : "...",
      "type" : "APPLICATION",
      "numberFollowing" : 12345,
      "numberParticipations" : 12345,
      "numberFollowers" : 12345,
      "favorite" : true,
      "userData" : {
        "property1" : "...",
        "property2" : "..."
      },
      "isCommunityAdmin" : true,
      "followerStatus" : "ACCEPTED",
      "numberModerations" : 12345,
      "tenantId" : 12345,
      "isModerator" : true,
      "alias" : "...",
      "customPage" : true,
      "page" : "...",
      "foundationUserId" : 12345,
      "lastName" : "...",
      "createDate" : 12345,
      "id" : 12345,
      "uriCommunity" : "...",
      "permissions" : [ "...", "..." ],
      "name" : "...",
      "tenantAdmin" : true,
      "privateContent" : true,
      "state" : "REMOVED",
      "participantStatus" : "NOT_RELATED",
      "admin" : { },
      "description" : "...",
      "followingStatus" : "ACCEPTED",
      "email" : "...",
      "fullName" : "...",
      "userCode" : "...",
      "tenantUUID" : "...",
      "hasMobileWidget" : true,
      "hidden" : true
    },
    "comment" : "...",
    "hasMentions" : true,
    "id" : 12345,
    "link" : "...",
    "creationDate" : 12345,
    "updateDate" : 12345,
    "editionDate" : 12345,
    "supported" : true,
    "customData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "numberDenouncements" : 12345,
    "numberLikes" : 12345,
    "numberShares" : 12345,
    "numberComments" : 12345,
    "url" : "...",
    "objectId" : "...",
    "name" : "...",
    "objectClass" : "...",
    "userId" : 12345,
    "tags" : "...",
    "alias" : "...",
    "thumbURL" : "...",
    "sociableType" : "..."
  }, {
    "sociableId" : 12345,
    "social" : {
      "numberFriends" : 12345,
      "approvalRequired" : true,
      "stateName" : "...",
      "forumId" : 12345,
      "ecmInfo" : {
        "property1" : { },
        "property2" : { }
      },
      "lastUpdate" : 12345,
      "isAdmin" : true,
      "idpId" : "...",
      "type" : "EVENT",
      "numberFollowing" : 12345,
      "numberParticipations" : 12345,
      "numberFollowers" : 12345,
      "favorite" : true,
      "userData" : {
        "property1" : "...",
        "property2" : "..."
      },
      "isCommunityAdmin" : true,
      "followerStatus" : "ITSELF",
      "numberModerations" : 12345,
      "tenantId" : 12345,
      "isModerator" : true,
      "alias" : "...",
      "customPage" : true,
      "page" : "...",
      "foundationUserId" : 12345,
      "lastName" : "...",
      "createDate" : 12345,
      "id" : 12345,
      "uriCommunity" : "...",
      "permissions" : [ "...", "..." ],
      "name" : "...",
      "tenantAdmin" : true,
      "privateContent" : true,
      "state" : "UNCONFIRMED",
      "participantStatus" : "NOT_RELATED",
      "admin" : { },
      "description" : "...",
      "followingStatus" : "NOT_RELATED",
      "email" : "...",
      "fullName" : "...",
      "userCode" : "...",
      "tenantUUID" : "...",
      "hasMobileWidget" : true,
      "hidden" : true
    },
    "formattedTextWithoutMention" : "...",
    "mentions" : {
      "property1" : "...",
      "property2" : "..."
    },
    "user" : {
      "numberFriends" : 12345,
      "approvalRequired" : true,
      "stateName" : "...",
      "forumId" : 12345,
      "ecmInfo" : {
        "property1" : { },
        "property2" : { }
      },
      "lastUpdate" : 12345,
      "isAdmin" : true,
      "idpId" : "...",
      "type" : "COMMUNITY",
      "numberFollowing" : 12345,
      "numberParticipations" : 12345,
      "numberFollowers" : 12345,
      "favorite" : true,
      "userData" : {
        "property1" : "...",
        "property2" : "..."
      },
      "isCommunityAdmin" : true,
      "followerStatus" : "NOT_RELATED",
      "numberModerations" : 12345,
      "tenantId" : 12345,
      "isModerator" : true,
      "alias" : "...",
      "customPage" : true,
      "page" : "...",
      "foundationUserId" : 12345,
      "lastName" : "...",
      "createDate" : 12345,
      "id" : 12345,
      "uriCommunity" : "...",
      "permissions" : [ "...", "..." ],
      "name" : "...",
      "tenantAdmin" : true,
      "privateContent" : true,
      "state" : "REMOVED",
      "participantStatus" : "NOT_RELATED",
      "admin" : { },
      "description" : "...",
      "followingStatus" : "REJECTED",
      "email" : "...",
      "fullName" : "...",
      "userCode" : "...",
      "tenantUUID" : "...",
      "hasMobileWidget" : true,
      "hidden" : true
    },
    "comment" : "...",
    "hasMentions" : true,
    "id" : 12345,
    "link" : "...",
    "creationDate" : 12345,
    "updateDate" : 12345,
    "editionDate" : 12345,
    "supported" : true,
    "customData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "numberDenouncements" : 12345,
    "numberLikes" : 12345,
    "numberShares" : 12345,
    "numberComments" : 12345,
    "url" : "...",
    "objectId" : "...",
    "name" : "...",
    "objectClass" : "...",
    "userId" : 12345,
    "tags" : "...",
    "alias" : "...",
    "thumbURL" : "...",
    "sociableType" : "..."
  } ],
  "numberComments" : 12345,
  "youtubeVideoId" : "...",
  "editionDate" : 12345,
  "formattedText" : "...",
  "updateDate" : 12345,
  "removed" : true,
  "recommendationMetadata" : {
    "property1" : "...",
    "property2" : "..."
  },
  "customData" : {
    "property1" : "...",
    "property2" : "..."
  },
  "hasDocumentPermission" : true,
  "numberWatchers" : 12345,
  "urlOrigin" : "...",
  "linkedObject" : {
    "editionDate" : 12345,
    "width" : 12345,
    "mimeType" : "...",
    "numberComments" : 12345,
    "numberDenouncements" : 12345,
    "sociableType" : "...",
    "numberWatchers" : 12345,
    "customData" : "...",
    "removed" : true,
    "tags" : "...",
    "numberShares" : 12345,
    "height" : 12345,
    "social" : {
      "customPage" : true,
      "forumId" : 12345,
      "resourceType" : "...",
      "hidden" : true,
      "approvalRequired" : true,
      "alias" : "...",
      "userAdmin" : { },
      "privateContent" : true,
      "page" : "...",
      "type" : "EVENT",
      "state" : "BLOCKED",
      "name" : "...",
      "securityCode" : "...",
      "resourceDescription" : "...",
      "description" : "...",
      "id" : 12345,
      "tenantId" : 12345,
      "creationDate" : 12345,
      "lastUpdateDate" : 12345
    },
    "user" : {
      "foundationUserId" : 12345,
      "customPage" : true,
      "forumId" : 12345,
      "resourceType" : "...",
      "hidden" : true,
      "approvalRequired" : true,
      "alias" : "...",
      "userAdmin" : { },
      "privateContent" : true,
      "page" : "...",
      "type" : "EVENT",
      "state" : "UNCONFIRMED",
      "name" : "...",
      "securityCode" : "...",
      "resourceDescription" : "...",
      "description" : "...",
      "id" : 12345,
      "tenantId" : 12345,
      "creationDate" : 12345,
      "lastUpdateDate" : 12345
    },
    "numberLikes" : 12345,
    "url" : "...",
    "id" : 12345,
    "tenantId" : 12345,
    "creationDate" : 12345,
    "lastUpdateDate" : 12345
  },
  "visibility" : "CUSTOM",
  "documentType" : "VIDEO",
  "link" : "...",
  "permissionViewPostAdmUser" : true,
  "permissions" : [ "...", "..." ],
  "formattedWithoutMention" : "...",
  "tags" : "...",
  "supported" : true,
  "postId" : 12345,
  "creationDate" : 12345,
  "shareMentionVO" : {
    "formattedWithoutMention" : "...",
    "mentions" : {
      "property1" : "...",
      "property2" : "..."
    }
  },
  "originShare" : {
    "numberFriends" : 12345,
    "approvalRequired" : true,
    "stateName" : "...",
    "forumId" : 12345,
    "ecmInfo" : {
      "property1" : { },
      "property2" : { }
    },
    "lastUpdate" : 12345,
    "isAdmin" : true,
    "idpId" : "...",
    "type" : "COMMUNITY",
    "numberFollowing" : 12345,
    "numberParticipations" : 12345,
    "numberFollowers" : 12345,
    "favorite" : true,
    "userData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "isCommunityAdmin" : true,
    "followerStatus" : "BLOCKED",
    "numberModerations" : 12345,
    "tenantId" : 12345,
    "isModerator" : true,
    "alias" : "...",
    "customPage" : true,
    "page" : "...",
    "foundationUserId" : 12345,
    "lastName" : "...",
    "createDate" : 12345,
    "id" : 12345,
    "uriCommunity" : "...",
    "permissions" : [ "...", "..." ],
    "name" : "...",
    "tenantAdmin" : true,
    "privateContent" : true,
    "state" : "REMOVED",
    "participantStatus" : "PENDING",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "NOT_RELATED",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "text" : "...",
  "numberShares" : 12345,
  "mentions" : {
    "property1" : "...",
    "property2" : "..."
  },
  "url" : "...",
  "hasMentions" : true,
  "approved" : true,
  "type" : "DEFAULT",
  "numberLikes" : 12345,
  "social" : {
    "numberFriends" : 12345,
    "approvalRequired" : true,
    "stateName" : "...",
    "forumId" : 12345,
    "ecmInfo" : {
      "property1" : { },
      "property2" : { }
    },
    "lastUpdate" : 12345,
    "isAdmin" : true,
    "idpId" : "...",
    "type" : "USER",
    "numberFollowing" : 12345,
    "numberParticipations" : 12345,
    "numberFollowers" : 12345,
    "favorite" : true,
    "userData" : {
      "property1" : "...",
      "property2" : "..."
    },
    "isCommunityAdmin" : true,
    "followerStatus" : "ACCEPTED",
    "numberModerations" : 12345,
    "tenantId" : 12345,
    "isModerator" : true,
    "alias" : "...",
    "customPage" : true,
    "page" : "...",
    "foundationUserId" : 12345,
    "lastName" : "...",
    "createDate" : 12345,
    "id" : 12345,
    "uriCommunity" : "...",
    "permissions" : [ "...", "..." ],
    "name" : "...",
    "tenantAdmin" : true,
    "privateContent" : true,
    "state" : "UNCONFIRMED",
    "participantStatus" : "PENDING",
    "admin" : { },
    "description" : "...",
    "followingStatus" : "ITSELF",
    "email" : "...",
    "fullName" : "...",
    "userCode" : "...",
    "tenantUUID" : "...",
    "hasMobileWidget" : true,
    "hidden" : true
  },
  "tenantId" : 12345,
  "attachments" : [ {
    "editionDate" : 12345,
    "width" : 12345,
    "mimeType" : "...",
    "numberComments" : 12345,
    "numberDenouncements" : 12345,
    "sociableType" : "...",
    "numberWatchers" : 12345,
    "customData" : "...",
    "removed" : true,
    "tags" : "...",
    "numberShares" : 12345,
    "height" : 12345,
    "social" : {
      "customPage" : true,
      "forumId" : 12345,
      "resourceType" : "...",
      "hidden" : true,
      "approvalRequired" : true,
      "alias" : "...",
      "userAdmin" : { },
      "privateContent" : true,
      "page" : "...",
      "type" : "USER",
      "state" : "REMOVED",
      "name" : "...",
      "securityCode" : "...",
      "resourceDescription" : "...",
      "description" : "...",
      "id" : 12345,
      "tenantId" : 12345,
      "creationDate" : 12345,
      "lastUpdateDate" : 12345
    },
    "user" : {
      "foundationUserId" : 12345,
      "customPage" : true,
      "forumId" : 12345,
      "resourceType" : "...",
      "hidden" : true,
      "approvalRequired" : true,
      "alias" : "...",
      "userAdmin" : { },
      "privateContent" : true,
      "page" : "...",
      "type" : "USER",
      "state" : "ACTIVE",
      "name" : "...",
      "securityCode" : "...",
      "resourceDescription" : "...",
      "description" : "...",
      "id" : 12345,
      "tenantId" : 12345,
      "creationDate" : 12345,
      "lastUpdateDate" : 12345
    },
    "numberLikes" : 12345,
    "url" : "...",
    "id" : 12345,
    "tenantId" : 12345,
    "creationDate" : 12345,
    "lastUpdateDate" : 12345
  }, {
    "editionDate" : 12345,
    "width" : 12345,
    "mimeType" : "...",
    "numberComments" : 12345,
    "numberDenouncements" : 12345,
    "sociableType" : "...",
    "numberWatchers" : 12345,
    "customData" : "...",
    "removed" : true,
    "tags" : "...",
    "numberShares" : 12345,
    "height" : 12345,
    "social" : {
      "customPage" : true,
      "forumId" : 12345,
      "resourceType" : "...",
      "hidden" : true,
      "approvalRequired" : true,
      "alias" : "...",
      "userAdmin" : { },
      "privateContent" : true,
      "page" : "...",
      "type" : "COMMUNITY",
      "state" : "BLOCKED",
      "name" : "...",
      "securityCode" : "...",
      "resourceDescription" : "...",
      "description" : "...",
      "id" : 12345,
      "tenantId" : 12345,
      "creationDate" : 12345,
      "lastUpdateDate" : 12345
    },
    "user" : {
      "foundationUserId" : 12345,
      "customPage" : true,
      "forumId" : 12345,
      "resourceType" : "...",
      "hidden" : true,
      "approvalRequired" : true,
      "alias" : "...",
      "userAdmin" : { },
      "privateContent" : true,
      "page" : "...",
      "type" : "USER",
      "state" : "BLOCKED",
      "name" : "...",
      "securityCode" : "...",
      "resourceDescription" : "...",
      "description" : "...",
      "id" : 12345,
      "tenantId" : 12345,
      "creationDate" : 12345,
      "lastUpdateDate" : 12345
    },
    "numberLikes" : 12345,
    "url" : "...",
    "id" : 12345,
    "tenantId" : 12345,
    "creationDate" : 12345,
    "lastUpdateDate" : 12345
  } ],
  "youtubeLink" : true,
  "watching" : true
}
```
