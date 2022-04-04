import json, re, requests

class AUTH():

  # def OAuthImplicitCodeFlow(self):
  #   return requests.request('GET','https://id.twitch.tv/oauth2/authorize')

  # def OAuthAuthorizationCodeFlow(self):
  #   return requests.request('GET','https://id.twitch.tv/oauth2/authorize')

  def OAuthClientCredentialsFlow(self, client_id, client_secret, scope=None): #AppToken
    return requests.request('POST','https://id.twitch.tv/oauth2/token',data={'client_id':client_id,'client_secret':client_secret,'grant_type':'client_credentials','scope':scope})

  # def OIDCImplicitCodeFlow(self):
  #   return requests.request('GET','https://id.twitch.tv/oauth2/authorize')

  # def OIDCAuthorizationCodeFlow(self):
  #   return requests.request('GET','https://id.twitch.tv/oauth2/authorize')

  def RefreshingAccessTokens(self, client_id, client_secret, refresh_token, scope=None):
    return requests.request('POST','https://id.twitch.tv/oauth2/token',data={'client_id':client_id,'client_secret':client_secret,'grant_type':'refresh_token','refresh_token':refresh_token,'scope':scope})

  def RevokingAccessTokens(self, client_id, token):
    return requests.request('POST','https://id.twitch.tv/oauth2/revoke',data={'client_id':client_id,'token':token})

  def ValidatingRequests(self, token):
    return requests.request('GET','https://id.twitch.tv/oauth2/validate',headers={'Authorization':'Bearer '+token})

  def UserInfo(self, token):
    return requests.request('GET','https://id.twitch.tv/oauth2/userinfo',headers={'Authorization':'Bearer '+token})

  def delete_token(self, token):
    req = requests.request('GET','https://id.twitch.tv/oauth2/validate', headers={'Authorization':'Bearer '+token})
    if req.status_code==200:
      return requests.request('POST','https://id.twitch.tv/oauth2/revoke',data={'client_id':req.json()['client_id'],'token':token})

class API():

  def __init__(self, token=None, client_id=None, client_secret=None, scope=None):
    self.token, self.client_id, self.client_secret, self.scope = token, client_id, client_secret, scope
    req = requests.request('GET','https://id.twitch.tv/oauth2/validate', headers={'Authorization':'Bearer '+self.token})
    if req.status_code==200:
      self.client_id = req.json()['client_id']
    else:
      req = requests.post('https://id.twitch.tv/oauth2/token', data={'client_id':self.client_id,'client_secret':self.client_secret,'grant_type':'client_credentials','scope':self.scope})
      if req.status_code==200:
        self.token = req.json()['access_token']
      else:
        raise
    self.headers = {'Client-Id':self.client_id,'Authorization':'Bearer '+self.token}

  # def StartCommercial(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/channels/commercial',headers=self.headers)

  # def GetExtensionAnalytics(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/analytics/extensions',headers=self.headers)

  # def GetGameAnalytics(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/analytics/games',headers=self.headers)

  # def GetBitsLeaderboard(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/bits/leaderboard',headers=self.headers)

  def GetCheermotes(self, broadcaster_id):
    return requests.request('GET','https://api.twitch.tv/helix/bits/cheermotes',params={'broadcaster_id':broadcaster_id},headers=self.headers)

  # def GetExtensionTransactions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/extensions/transactions',headers=self.headers)

  def GetChannelInformation(self, broadcaster_id):
    return requests.request('GET','https://api.twitch.tv/helix/channels',{'broadcaster_id':broadcaster_id},headers=self.headers)

  # def ModifyChannelInformation(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/channels',headers=self.headers)

  # def GetChannelEditors(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/channels/editors',headers=self.headers)

  # def CreateCustomRewards(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/channel_points/custom_rewards',headers=self.headers)

  # def DeleteCustomReward(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/channel_points/custom_rewards',headers=self.headers)

  # def GetCustomReward(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/channel_points/custom_rewards',headers=self.headers)

  # def GetCustomRewardRedemption(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions',headers=self.headers)

  # def UpdateCustomReward(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/channel_points/custom_rewards',headers=self.headers)

  # def UpdateRedemptionStatus(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions',headers=self.headers)

  def GetChannelEmotes(self, broadcaster_id):
    return requests.request('GET','https://api.twitch.tv/helix/chat/emotes',params={'broadcaster_id':broadcaster_id},headers=self.headers)

  def GetGlobalEmotes(self):
    return requests.request('GET','https://api.twitch.tv/helix/chat/emotes/global',headers=self.headers)

  def GetEmoteSets(self, emote_set_id):
    return requests.request('GET','https://api.twitch.tv/helix/chat/emotes/set',params={'emote_set_id':emote_set_id},headers=self.headers)

  def GetChannelChatBadges(self, broadcaster_id):
    return requests.request('GET','https://api.twitch.tv/helix/chat/badges',params={'broadcaster_id':broadcaster_id},headers=self.headers)

  def GetGlobalChatBadges(self):
    return requests.request('GET','https://api.twitch.tv/helix/chat/badges/global',headers=self.headers)

  def GetChatSettings(self, broadcaster_id, moderator_id=None):
    return requests.request('GET','https://api.twitch.tv/helix/chat/settings',params={'broadcaster_id':broadcaster_id,'moderator_id':moderator_id},headers=self.headers)

  # def UpdateChatSettings(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/chat/settings',headers=self.headers)

  # def CreateClip(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/clips',headers=self.headers)

  def GetClips(self, broadcaster_id=None, game_id=None, id=None, started_at=None, ended_at=None, first=None, after=None, before=None):
    return requests.request('GET','https://api.twitch.tv/helix/clips',params={'broadcaster_id':broadcaster_id,'game_id':game_id,'id':id,'after':after,'before':before,'ended_at':ended_at,'first':first,'started_at':started_at},headers=self.headers)

  # def GetCodeStatus(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/entitlements/codes',headers=self.headers)

  # def GetDropsEntitlements(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/entitlements/drops',headers=self.headers)

  # def UpdateDropsEntitlements(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/entitlements/drops',headers=self.headers)

  # def RedeemCode(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/entitlements/codes',headers=self.headers)

  # def GetExtensionConfigurationSegment(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/extensions/configurations',headers=self.headers)

  # def SetExtensionConfigurationSegment(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/extensions/configurations',headers=self.headers)

  # def SetExtensionRequiredConfiguration(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/extensions/required_configuration',headers=self.headers)

  # def SendExtensionPubSubMessage(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/extensions/pubsub',headers=self.headers)

  # def GetExtensionLiveChannels(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/extensions/live',headers=self.headers)

  # def GetExtensionSecrets(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/extensions/jwt/secrets',headers=self.headers)

  # def CreateExtensionSecret(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/extensions/jwt/secrets',headers=self.headers)

  # def SendExtensionChatMessage(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/extensions/chat',headers=self.headers)

  # def GetExtensions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/extensions',headers=self.headers)

  # def GetReleasedExtensions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/extensions/released',headers=self.headers)

  # def GetExtensionBitsProducts(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/bits/extensions',headers=self.headers)

  # def UpdateExtensionBitsProduct(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/bits/extensions',headers=self.headers)

  # def CreateEventSubSubscription(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/eventsub/subscriptions',headers=self.headers)

  # def DeleteEventSubSubscription(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/eventsub/subscriptions',headers=self.headers)

  # def GetEventSubSubscriptions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/eventsub/subscriptions',headers=self.headers)

  def GetTopGames(self, first=None, after=None, before=None):
    return requests.request('GET','https://api.twitch.tv/helix/games/top',params={'after':after,'before':before,'first':first},headers=self.headers)

  def GetGames(self, id=None, name=None):
    return requests.request('GET','https://api.twitch.tv/helix/games',params={'id':id,'name':name},headers=self.headers)

  # def GetCreatorGoals(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/goals',headers=self.headers)

  # def GetHypeTrainEvents(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/hypetrain/events',headers=self.headers)

  # def CheckAutoModStatus(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/moderation/enforcements/status',headers=self.headers)

  # def ManageHeldAutoModMessages(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/moderation/automod/message',headers=self.headers)

  # def GetAutoModSettings(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/moderation/automod/settings',headers=self.headers)

  # def UpdateAutoModSettings(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/moderation/automod/settings',headers=self.headers)

  # def GetBannedUsers(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/moderation/banned',headers=self.headers)

  # def BanUser(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/moderation/bans',headers=self.headers)

  # def UnbanUser(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/moderation/bans',headers=self.headers)

  # def GetBlockedTerms(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/moderation/blocked_terms',headers=self.headers)

  # def AddBlockedTerm(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/moderation/blocked_terms',headers=self.headers)

  # def RemoveBlockedTerm(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/moderation/blocked_terms',headers=self.headers)

  # def GetModerators(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/moderation/moderators',headers=self.headers)

  # def GetPolls(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/polls',headers=self.headers)

  # def CreatePoll(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/polls',headers=self.headers)

  # def EndPoll(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/polls',headers=self.headers)

  # def GetPredictions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/predictions',headers=self.headers)

  # def CreatePrediction(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/predictions',headers=self.headers)

  # def EndPrediction(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/predictions',headers=self.headers)

  def GetChannelStreamSchedule(self, broadcaster_id):
    return requests.request('GET','https://api.twitch.tv/helix/schedule',params={'broadcaster_id':broadcaster_id},headers=self.headers)

  def GetChanneliCalendar(self, broadcaster_id):
    return requests.request('GET','https://api.twitch.tv/helix/schedule/icalendar',params={'broadcaster_id':broadcaster_id},headers=self.headers)

  # def UpdateChannelStreamSchedule(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/schedule/settings',headers=self.headers)

  # def CreateChannelStreamScheduleSegment(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/schedule/segment',headers=self.headers)

  # def UpdateChannelStreamScheduleSegment(self):
  #   return requests.request('PATCH','https://api.twitch.tv/helix/schedule/segment',headers=self.headers)

  # def DeleteChannelStreamScheduleSegment(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/schedule/segment',headers=self.headers)

  def SearchCategories(self, query, first=None, after=None):
    return requests.request('GET','https://api.twitch.tv/helix/search/categories',params={'query':query,'first':first,'after':after},headers=self.headers)

  def SearchChannels(self, query, live_only=None, first=None, after=None):
    return requests.request('GET','https://api.twitch.tv/helix/search/channels',params={'query':query,'first':first,'after':after,'live_only':live_only},headers=self.headers)

  # def GetSoundtrackCurrentTrack(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/soundtrack/current_track',headers=self.headers)

  # def GetSoundtrackPlaylist(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/soundtrack/playlist',headers=self.headers)

  # def GetSoundtrackPlaylists(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/soundtrack/playlists',headers=self.headers)

  # def GetStreamKey(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/streams/key',headers=self.headers)

  def GetStreams(self, user_id=None, user_login=None, game_id=None, language=None, first=None, after=None, before=None):
    return requests.request('GET','https://api.twitch.tv/helix/streams',params={'user_id':user_id,'user_login':user_login,'after':after,'before':before,'first':first,'game_id':game_id,'language':language},headers=self.headers)

  # def GetFollowedStreams(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/streams/followed',headers=self.headers)

  # def CreateStreamMarker(self):
  #   return requests.request('POST','https://api.twitch.tv/helix/streams/markers',headers=self.headers)

  # def GetStreamMarkers(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/streams/markers',headers=self.headers)

  # def GetBroadcasterSubscriptions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/subscriptions',headers=self.headers)

  # def CheckUserSubscription(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/subscriptions/user',headers=self.headers)

  # def GetAllStreamTags(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/tags/streams',headers=self.headers)

  # def GetStreamTags(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/streams/tags',headers=self.headers)

  # def ReplaceStreamTags(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/streams/tags',headers=self.headers)

  # def GetChannelTeams(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/teams/channel',headers=self.headers)

  # def GetTeams(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/teams',headers=self.headers)

  def GetUsers(self, id=None, login=None):
    return requests.request('GET','https://api.twitch.tv/helix/users',params={'id':id,'login':login},headers=self.headers)

  # def UpdateUser(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/users?description=<description>',headers=self.headers)

  def GetUsersFollows(self, from_id=None, to_id=None, first=None, after=None):
    return requests.request('GET','https://api.twitch.tv/helix/users/follows',params={'from_id':from_id,'to_id':to_id,'first':first,'after':after},headers=self.headers)

  # def GetUserBlockList(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/users/blocks',headers=self.headers)

  # def BlockUser(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/users/blocks',headers=self.headers)

  # def UnblockUser(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/users/blocks',headers=self.headers)

  # def GetUserExtensions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/users/extensions/list',headers=self.headers)

  # def GetUserActiveExtensions(self):
  #   return requests.request('GET','https://api.twitch.tv/helix/users/extensions',headers=self.headers)

  # def UpdateUserExtensions(self):
  #   return requests.request('PUT','https://api.twitch.tv/helix/users/extensions',headers=self.headers)

  def GetVideos(self, id=None, user_id=None, game_id=None, language=None, period=None, sort=None, type=None, first=None, after=None, before=None):
    return requests.request('GET','https://api.twitch.tv/helix/videos',params={'id':id,'user_id':user_id,'game_id':game_id,'first':first,'language':language,'period':period,'sort':sort,'type':type,'after':after,'before':before},headers=self.headers)

  # def DeleteVideos(self):
  #   return requests.request('DELETE','https://api.twitch.tv/helix/videos',headers=self.headers)

  def uid(self, *login):
    return list(map(lambda x : x['id'], self.GetUsers(login=list(login)).json()['data']))

class GQL():

  def PlaybackAccessToken(self, login="", vodID=""):
    return requests.request('POST','https://gql.twitch.tv/gql',data=json.dumps({"operationName": "PlaybackAccessToken","extensions": {"persistedQuery": {"version": 1,"sha256Hash": "0828119ded1c13477966434e15800ff57ddacf13ba1911c129dc2200705b0712"}},"variables": {"isLive": True if login else False, "login": str(login), "isVod": True if vodID else False, "vodID": str(vodID), "playerType": "embed"}}),headers={'Client-id': "kimne78kx3ncx6brgo4mv6wki5h1ko"})

  def StreamPlayback(self, login):
    accessToken = self.PlaybackAccessToken(login=login).json()['data']['streamPlaybackAccessToken']
    return requests.request('GET',f'https://usher.ttvnw.net/api/channel/hls/{login}.m3u8', params={'client_id':'kimne78kx3ncx6brgo4mv6wki5h1ko','token':accessToken['value'],'sig':accessToken['signature'],'allow_source':True,'allow_audio_only':True})

  def VideoPlayback(self ,vodID):
    accessToken = self.PlaybackAccessToken(vodID=vodID).json()['data']['videoPlaybackAccessToken']
    return requests.request('GET',f'https://usher.ttvnw.net/vod/{vodID}.m3u8', params={'client_id':'kimne78kx3ncx6brgo4mv6wki5h1ko','token':accessToken['value'],'sig':accessToken['signature'],'allow_source':True,'allow_audio_only':True})

  def HomeTrackQuery(self,login):
    return requests.request('POST','https://gql.twitch.tv/gql',data=json.dumps({"operationName": "HomeTrackQuery", "variables": {"channelLogin": login}, "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "ec3cf4f02623f049d9a6c0b02e8c419b55e77c36db785facfade3871d3a86dc0"}}}),headers={'Client-id': "kimne78kx3ncx6brgo4mv6wki5h1ko"})

  def Comments(self, vodID, content_offset_seconds=None, cursor=None):
    return requests.request('GET',f'https://api.twitch.tv/v5/videos/{vodID}/comments', params={'content_offset_seconds':content_offset_seconds,'cursor':cursor}, headers={'Client-id': "kimne78kx3ncx6brgo4mv6wki5h1ko"})

  def regex_m3u8(self, Playback):
    return re.findall('https:[\w\/\-\.]*.m3u8', Playback.text)

class TMI():

  def User(self, channel):
    return requests.request('GET',f'https://tmi.twitch.tv/group/user/{channel}')

  def Chatters(self, channel):
    return requests.request('GET',f'https://tmi.twitch.tv/group/user/{channel}/chatters')

  def Servers(self):
    return requests.request('GET',f'https://tmi.twitch.tv/servers')

class IVR():

  def BitEmoteLookup(self, channel):
    return requests.request('GET',f'https://api.ivr.fi/twitch/bitemotes/{channel}')

  def ChatDelayCheck(self, username, raw=None):
    return requests.request('GET',f'https://api.ivr.fi/twitch/chatdelay/{username}', params={'raw':raw})

  def EmoteLookup(self, emote, id=None):
    return requests.request('GET',f'https://api.ivr.fi/twitch/emotes/{emote}', params={'id':id})

  def EmoteSetLookup(self, setid):
    return requests.request('GET',f'https://api.ivr.fi/twitch/emoteset/{setid}')

  def BulkEmotesetLookup(self, set_id):
    return requests.request('GET',f'https://api.ivr.fi/twitch/emoteset', params={'set_id':set_id})

  def LowLatencyCheck(self, username, raw=None):
    return requests.request('GET',f'https://api.ivr.fi/twitch/latency/{username}', params={'raw':raw})

  def ModVIPLookup(self, channel):
    return requests.request('GET',f'https://api.ivr.fi/twitch/modsvips/{channel}')

  def GetUserData(self, username, id=None, skipCache=None):
    return requests.request('GET',f'https://api.ivr.fi/twitch/resolve/{username}', params={'id':id,'skipCache':skipCache})

  def StreamScheduleLookup(self, channel):
    return requests.request('GET',f'https://api.ivr.fi/twitch/streamschedule/{channel}')

  def SubageLookup(self, username, channel):
    return requests.request('GET',f'https://api.ivr.fi/twitch/subage/{username}/{channel}')

class ETC():
  
  def vod_544146_workers_dev(self, vodID):
    return re.findall('https:[\w\/\-\.]*.m3u8',requests.request('GET',f'https://vod.544146.workers.dev/{vodID}').text)
