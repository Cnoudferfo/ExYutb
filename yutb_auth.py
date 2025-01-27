# Step 1: OAuth Authentication with YouTube
# For OAuth authentication, we'll use the google-auth and google-api-python-client libraries. Ensure you have them installed:
# ```bash 
# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client


# Here's a basic example of how to authenticate and get a YouTube API client object:
import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    creds = None
    token_path = 'token.json'

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)

service = get_authenticated_service()

# Ensure you have your client_secret.json file from the Google Console and store it in your project directory.

# Step 2: Fetching a Specific Playlist
# Now, with the authenticated service, you can fetch a playlist:
def get_playlist_items(service, playlist_id):
    request = service.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50
    )
    response = request.execute()

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['snippet']['resourceId']['videoId']
        print(f'Title: {title}, Video ID: {video_id}')

playlist_id = 'YOUR_PLAYLIST_ID'
get_playlist_items(service, playlist_id)
