# Description: This file contains the YTURL class which is used to get the URL of the video to be played.
# Install the required library:
# > pip install yt-dlp
#
from yt_dlp import YoutubeDL
class YTItem:
    # To get the URL of the video to be played
    def __get_raw_YT_url__(self, the_url) -> dict:
        with YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(the_url, download=False)
            return info_dict
    def __init__(self, item_url):
        # Options for downloading the audio via yt_dlp
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.item = self.__get_raw_YT_url__(item_url)
    def get_url(self) -> str:
        return self.item.get('url', None)
    def get_title(self) -> str:
        return self.item.get('title', None)
    def get_thumbnail(self) -> str:
        return self.item.get('thumbnail', None)
    def get_description(self) -> str:
        return self.item.get('description', None)
    def get_duration(self) -> int:
        return self.item.get('duration', None)
    def get_view_count(self) -> int:
        return self.item.get('view_count', None)
    def get_like_count(self) -> int:
        return self.item.get('like_count', None)
    def get_dislike_count(self) -> int:
        return self.item.get('dislike_count', None)
