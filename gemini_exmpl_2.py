import os
import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    """Shows basic usage of the YouTube Data API.
    Prints information about the default channel.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('youtube', 'v3', credentials=creds)

def search_youtube(service, q):
    """
    Searches for a specified query on YouTube.

    Args:
        service: The authenticated YouTube Data API service.
        q: The query to search.
    """
    request = service.search().list(
        part="snippet",
        maxResults=50,
        q=q,
        order="relevance",
    )
    response = request.execute()

    # Print IDs for each result.
    for item in response['items']:
        print(f"Video ID: {item['id']['videoId']}")
        print(f"Title: {item['snippet']['title']}")
        print(f"Description: {item['snippet']['description']}")
        print("-" * 20)

if __name__ == "__main__":
    try:
        service = get_authenticated_service()
        search_youtube(service, "機器學習")
    except Exception as e:
        print(f"An error occurred: {e}")
