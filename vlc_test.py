from yt_dlp import YoutubeDL
import vlc

the_url = "https://music.youtube.com/watch?v=_WhnBdO8wuc"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def get_raw_YT_url_info(the_url) -> dict:
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(the_url, download=False)
        return info_dict

info_dict = get_raw_YT_url_info(the_url)
video_url = info_dict.get("url", None)
vlc_instance = vlc.Instance("--no-video")
media = vlc_instance.media_new(video_url)
player = vlc_instance.media_player_new()
player.set_media(media)
player.play()
input("Press Enter to stop the music: ")
player.stop()

