# A class to fetch YouTube playlists and playlist items using the YouTube API v3.
# Install the required libraries:
# > pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
#
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class YTPlayLists:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
        try:
            self.service = self.__authenticated_service__()
            self.__my_playlists__ = self.__my_playlists__()
        except Exception as e:
            print
            raise Exception(f'class YutbPlayLists: Error: {e}')

    # To authenticate with the YouTube API
    def __authenticated_service__(self):
        creds = None
        token_path = 'token.json'
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # Ensure you have your client_secret.json file from the Google Console and store it in your project directory.
                flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
        print('class YutbPlayLists: Authenticated successfully!')
        return build('youtube', 'v3', credentials=creds)

    # To return a list of all my playlists in dictionary format {'title': xxx, 'id': yyy}
    def __my_playlists__(self) -> list:
        request = self.service.playlists().list(part='snippet', mine=True, maxResults=50)
        response = request.execute()
        ret = []
        for item in response['items']:
            title = item['snippet']['title']
            playlist_id = item['id']
            ret.append({'title': title, 'id': playlist_id})
        return ret
    # To return a list of all my playlists
    def get_my_playlists(self) -> list:
        return self.__my_playlists__
    # To return a list of playlist IDs which title containing the search key
    def get_playlist_id(self, srch_key='') -> list:
        ret = []
        for item in self.__my_playlists__:
            title = item['title']
            playlist_id = item['id']
            if srch_key in title:
                ret.append({'title': title, 'id': playlist_id})
                break
        return ret
    # To return a list of all video ids in a playlist
    def get_playlist_items(self, playlist_id) -> list:
        request = self.service.playlistItems().list(part='snippet', playlistId=playlist_id, maxResults=500)
        response = request.execute()
        ret = []
        for item in response['items']:
            title = item['snippet']['title']
            video_id = item['snippet']['resourceId']['videoId']
            ret.append({'title': title, 'video_id': video_id})
        return ret

if __name__ == '__main__':
    ypl = YTPlayLists()
    my_playlists = ypl.get_my_playlists()
    for item in my_playlists:
        print(f'title={item["title"]}, Playlist ID: {item["id"]}')
    srch_rst = ypl.get_playlist_id('pl_for_api')
    for item in srch_rst:
        print(f'title={item["title"]}, Playlist ID: {item["id"]}')
    srch_rst = ypl.get_playlist_items(srch_rst[0]['id'])
    for item in srch_rst:
        print(f'title={item["title"]}, Video ID: {item["video_id"]}')
