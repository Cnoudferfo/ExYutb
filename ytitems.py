# Description: To get the real URLs from raw URLs given by youtube api
# Install the required library:
# > pip install yt-dlp
#
from yt_dlp import YoutubeDL
class YTItems:
    # To get the URL of the video to be played
    def __get_raw_YT_url__(self, the_url) -> dict:
        with YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(the_url, download=False)
            return info_dict
    def __init__(self, raw_urls):
        # Options for downloading the audio via yt_dlp
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.items = []
        for raw_url in raw_urls:
            try:
                rst = self.__get_raw_YT_url__(raw_url)
                if rst :
                    self.items.append({
                        'title': rst.get('title', None),
                        'url': rst.get('url', None),
                        'thumbnail': rst.get('thumbnail', None),
                        'description': rst.get('description', None),
                        'duration': rst.get('duration', None),
                        'view_count': rst.get('view_count', None),
                        'like_count': rst.get('like_count', None),
                        'dislike_count': rst.get('dislike_count', None)
                    })
            except Exception as e:
                print(f'Error: {e}')
                pass
    # To return the YT information items
    def get_items(self) -> list:
        return self.items
                
    # def get_url(self) -> str:
    #     return self.items.get('url', None)
    # def get_title(self) -> str:
    #     return self.items.get('title', None)
    # def get_thumbnail(self) -> str:
    #     return self.items.get('thumbnail', None)
    # def get_description(self) -> str:
    #     return self.items.get('description', None)
    # def get_duration(self) -> int:
    #     return self.items.get('duration', None)
    # def get_view_count(self) -> int:
    #     return self.items.get('view_count', None)
    # def get_like_count(self) -> int:
    #     return self.items.get('like_count', None)
    # def get_dislike_count(self) -> int:
    #     return self.items.get('dislike_count', None)
