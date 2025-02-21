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
    def search_playlist_by_title(self, srch_key='') -> list:
        ret = []
        for item in self.__my_playlists__:
            title = item['title']
            playlist_id = item['id']
            if srch_key in title:
                ret.append({'title': title, 'id': playlist_id})
                break
        return ret
    def get_playlist_by_number(self, number) -> dict:
        # To check if the number is valid
        if number < 0 or number >= len(self.__my_playlists__):
            return None
        return self.__my_playlists__[number]
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
    # To list all my playlists and let user to pick up one
    def list_my_playlists_and_pick_one(self):
        cnt = 0
        for item in self.__my_playlists__:
            print(f'cnt={cnt}, title={item["title"]}, Playlist ID: {item["id"]}')
            cnt += 1
        # To read a valid number from stdin
        while True:
            number = int(input('Enter a number: '))
            if number >= 0 and number < len(self.__my_playlists__):
                break
            print('Invalid number! Please try again.')
        return self.get_playlist_by_number(number)

if __name__ == '__main__':
    ypl = YTPlayLists()
    my_playlists = ypl.get_my_playlists()
    cnt = 0
    for item in my_playlists:
        print(f'cnt={cnt}, title={item["title"]}, Playlist ID: {item["id"]}')
        cnt += 1
    # To read a number from stdin
    number = int(input('Enter a number: '))
    srch_rst = ypl.get_playlist_by_number(number)
    # To chech if the srch_rst is None
    if srch_rst is None:
        print('Invalid number')
    else:
        print(f'No.{number} playlist is: title={srch_rst["title"]}, Playlist ID: {srch_rst["id"]}')

    # srch_rst = ypl.search_playlist_by_title('pl_for_api')
    # for item in srch_rst:
    #     print(f'title={item["title"]}, Playlist ID: {item["id"]}')
    
    print(f'To list the items in the playlist: {srch_rst["title"]}')
    srch_rst = ypl.get_playlist_items(srch_rst['id'])    
    for item in srch_rst:
        print(f'Song title={item["title"]}, Video ID: {item["video_id"]}')
