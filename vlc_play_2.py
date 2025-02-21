import ytplaylists
import vlc
from yt_dlp import YoutubeDL
import time

# The URLs of the videos to be played
the_urls = [
    'https://music.youtube.com/watch?v=HzdD8kbDzZA',
    'https://music.youtube.com/watch?v=_WhnBdO8wuc',
    'https://music.youtube.com/watch?v=VQJQ1bvW-ac',
    'https://music.youtube.com/watch?v=DD-5_lCEMHY',
    'https://music.youtube.com/watch?v=luOwnc5bqho'
]
the_urls2 = [
    'https://www.youtube.com/watch?v=Klqjebjw8n4',
    'https://www.youtube.com/watch?v=GWtoeYznx8E'
]
the_urls_3 = [
    'https://music.youtube.com/watch?v=Ly61QG9yWOc',
    'https://music.youtube.com/watch?v=rbu9_v-LFnY'
]


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

if __name__ == '__main__':
    the_yt_playlist = ytplaylists.YTPlayLists()
    the_chosen_playlist = the_yt_playlist.get_playlist_id('pl_for_api')[0]
    the_urls_4 = [f'https://music.youtube.com/watch?v={item["video_id"]}' for item in the_yt_playlist.get_playlist_items(the_chosen_playlist['id'])]
    for item in the_urls_4:
        print(f'item={item}')
    

    print(f'VLC Version: {vlc.libvlc_get_version()}')
    
    for the_url in the_urls_4:
        info_dict = get_raw_YT_url_info(the_url)
        if info_dict is None:
            print('Panic! No video info found')
            exit(0)
        print(f'Video Title: {info_dict.get("title", None)}')
        video_url = info_dict.get('url', None)

        player = vlc.MediaPlayer(video_url)
        player.play()
        print(f'VLC Player State: {player.get_state()}')

        # To set the volume to 50%
        player.audio_set_volume(70)
        print(f'Audio volume: {player.audio_get_volume()}')

        try:
            while True:
                state = player.get_state()
                # print(f'Player State: {state}')
                if state in [vlc.State.Ended, vlc.State.Error]:
                    break
                time.sleep(1)
        except KeyboardInterrupt:
            print('Ctrl+C detected!')
            player.stop()
            break