<h2>※ <code>pip install TwitchDev</code></h2>
<code>pip install TwitchDev</code> 명령어를 이용하여 TwitchDev 를 설치할 수 있습니다.<br>
트위치 공식 API 와 그외 비공식 API 등 다양한 요청을 쉽게 보내기 위해 제작되었습니다.<br>
아직 초기 개발버전이라 앱토큰을 이용하는 API 까지만 구현했습니다.<br>
업데이트를 원한다면 <code>pip install TwitchDev --upgrade</code> 명령어를 입력해주세요.<br><br>

<h2>※ <code>TwitchAUTH = TwitchDev.AUTH()</code></h2>
트위치 인증과 관련된 클래스 입니다.<br>
트위치 콘솔 (https://dev.twitch.tv/console) 에서 클라이언트 아이디와 시크릿을 발급받을 수 있습니다.<br>

* <code>.OAuthClientCredentialsFlow(self, client_id, client_secret, scope=None)</code> : 앱토큰을 요청합니다.<br>
* <code>.RefreshingAccessTokens(self, client_id, client_secret, refresh_token, scope=None)</code> : 토큰을 리프레쉬 합니다.<br>
* <code>.RevokingAccessTokens(self, client_id, token)</code> : 토큰을 제거합니다.<br>
* <code>.ValidatingRequests(self, token)</code> : 토큰을 검증합니다.<br>
* <code>.UserInfo(self, token)</code> : 토큰의 유저 정보를 확인합니다.<br>
* <code>.delete_token(self, token)</code> : 토큰을 제거합니다. (토큰을 검증하여 얻은 클라이언트id로 토큰을 제거합니다.)<br>
* <code>.reset_token(self, client_id, client_secret)</code> : 토큰을 완전 초기화 합니다. (50개 생성 후 삭제)<br><br>


<h2>※ <code>TwitchAPI = TwitchDev.API(token='', client_id='',client_secret='')</code></h2>
트위치 API와 관련된 클래스 입니다.<br>
트위치API 레퍼런스 (https://dev.twitch.tv/docs/api/reference) 를 기반으로 만들어졌습니다.<br>
따라서 해당 사이트에서 세부사항 (인증, 파라미터, 응답 정보 등) 을 확인할 수 있습니다.<br>
(토큰) 또는 (클라이언트 아이디 + 클라이언트 시크릿) 조합 만으로도 사용할 수 있습니다.<br>
우선 클래스를 생성할때 토큰을 이용하여 헤더를 생성을 시도합니다.<br>
정상적인 토큰이 아니라면 클라이언트 아이디와 클라이언트 시크릿을 이용하여 헤더를 생성합니다.<br>
헤더를 생성하지 못했다면 오류를 반환합니다.<br>

* <code>.GetCheermotes(self, broadcaster_id)</code> : 비트 이모티콘을 조회합니다.<br>
* <code>.GetChannelInformation(self, broadcaster_id)</code> : 채널 정보를 조회합니다.<br>
* <code>.GetChannelEmotes(self, broadcaster_id)</code> : 채널 이모티콘을 조회합니다.<br>
* <code>.GetGlobalEmotes(self)</code> : 글로벌 이모티콘을 조회합니다.<br>
* <code>.GetEmoteSets(self, emote_set_id)</code> : 이모티콘 세트를 조회합니다.<br>
* <code>.GetChannelChatBadges(self, broadcaster_id)</code> : 채널 뱃지를 조회합니다.<br>
* <code>.GetGlobalChatBadges(self)</code> : 글로벌 뱃지를 조회합니다.<br>
* <code>.GetChatSettings(self, broadcaster_id, moderator_id=None)</code> : 채팅 설정을 조회합니다.<br>
* <code>.GetClips(self, broadcaster_id=None, game_id=None, id=None, started_at=None, ended_at=None, first=None, after=None, before=None)</code> : 클립을 조회합니다.<br>
* <code>.GetTopGames(self, first=None, after=None, before=None)</code> : 상위 카테고리를 조회합니다.<br>
* <code>.GetGames(self, id=None, name=None)</code> : 키테고리를 조회합니다.<br>
* <code>.GetChannelStreamSchedule(self, broadcaster_id)</code> : 채널 스케줄을 조회합니다.<br>
* <code>.GetChanneliCalendar(self, broadcaster_id)</code> : 채널 i캘린더를 조회합니다.<br>
* <code>.SearchCategories(self, query, first=None, after=None)</code> : 카테고리를 검색합니다.<br>
* <code>.SearchChannels(self, query, live_only=None, first=None, after=None)</code> : 채널을 검색합니다.<br>
* <code>.GetStreams(self, user_id=None, user_login=None, game_id=None, language=None, first=None, after=None, before=None)</code> : 스트림 정보를 가져옵니다.<br>
* <code>.GetUsers(self, id=None, login=None)</code> : 유저 정보를 가져옵니다.<br>
* <code>.GetUsersFollows(self, from_id=None, to_id=None, first=None, after=None)</code> : 유저 팔로우 팔로잉 정보를 조회합니다.<br>
* <code>.GetVideos(self, id=None, user_id=None, game_id=None, language=None, period=None, sort=None, type=None, first=None, after=None, before=None)</code> : 비디오 정보를 조회합니다.<br>
* <ode>.uid(self, *login)</code> : 유저 login 리스트를 유저 id 리스트로 변환해줍니다. (최대100개) 파라미터로 login이 아닌 id 를 사용하는 경우 유용합니다.<br><br>

<h2>※ <code>TwitchGQL = TwitchDev.GQL()</code></h2>
트위치 GQL API 와 관련된 클래스 입니다.<br>

* <code>.PlaybackAccessToken(self, login="", vodID="")</code> : PlaybackAccessToken 을 발급합니다.<br>
* <code>.StreamPlayback(self, login)</code> : PlaybackAccessToken 을 발급하여 생방송 m3u8을 가져옵니다. (->text)<br>
* <code>.VideoPlayback(self ,vodID)</code> : PlaybackAccessToken 을 발급하여 다시보기 m3u8을 가져옵니다. (->text)<br>
* <code>.HomeTrackQuery(self,login)</code> : HomeTrackQuery 정보를 가져옵니다. (GQL)<br>
* <code>.Comments(self, vodID, content_offset_seconds=None, cursor=None)</code> : 다시보기에서 채팅을 가져옵니다.<br>
* <code>.regex_m3u8(self, Playback)</code> : Playback 으로 m3u8 목록을 추출합니다.<br><br>

<h2>※ <code>TwitchTMI = TwitchDev.TMI()</code></h2>
트위치 TMI API 와 관련된 클래스 입니다.<br>

* <code>.User(self, channel)</code> : 채널에 참여하고있는 유저 목록을 가져옵니다.<br>
* <code>.Chatters(self, channel)</code> : 채널에 참여하고 있는 유저수를 가져옵니다.<br>
* <code>.Servers(self)</code> : 트위치 IRC 서버 목록을 가져옵니다.<br><br>

<h2>※ <code>TwitchIVR = TwitchDev.IVR()</code></h2>
트위치 IVR API 와 관련된 클래스 입니다.<br>

* <code>.BitEmoteLookup(self, channel)</code> : 비트 이모티콘을 가져옵니다.<br>
* <code>.ChatDelayCheck(self, username, raw=None)</code> : 채팅 딜레이를 확인합니다.<br>
* <code>.EmoteLookup(self, emote, id=None)</code> : 이모티콘을 조회합니다.<br>
* <code>.EmoteSetLookup(self, setid)</code> : 이모티콘 세트를 조회합니다.<br>
* <code>.BulkEmotesetLookup(self, set_id)</code> : 이모티콘 세트를 조회합니다.<br>
* <code>.LowLatencyCheck(self, username, raw=None)</code> : 낮은 딜레이 설정을 조회합니다.<br>
* <code>.ModVIPLookup(self, channel)</code> : 매니저와 VIP를 조회합니다.<br>
* <code>.GetUserData(self, username, id=None, skipCache=None)</code> : 유저 데이터를 조회합니다.<br>
* <code>.StreamScheduleLookup(self, channel)</code> : 스트림 스케줄을 조회합니다.<br>
* <code>.SubageLookup(self, username, channel)</code> : 구독 상태를 확인합니다.<br><br>

<h2>※ <code>TwitchETC = TwitchDev.ETC()</code></h2>
그외 트위치 관련된 클래스 입니다.<br>

* <code>.vod_544146_workers_dev(self, vodID)</code> : vod의 m3u8 목록을 가져옵니다. (->list) (https://vod.544146.workers.dev/{vodID})<br><br>

<h2>※ Version</h2>

* ver0.0.5 : AUTH.reset_token 추가<br>
