import vlc
import yt_dlp
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
    'https://www.youtube.com/watch?v=q-hn8WH_-3U',
    'https://www.youtube.com/watch?v=2WJhax7Jmxs'
]


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    
    for the_url in the_urls2:
        info_dict = ydl.extract_info(the_url, download=False)
        if info_dict is None:
            print('Panic! No video info found')
            exit(0)
        print(f'Video Title: {info_dict.get("title", None)}')
        video_url = info_dict.get('url', None)

        player = vlc.MediaPlayer(video_url)
        player.play()
        print('Playing audio stream:', video_url)
        print(f'VLC Version: {vlc.libvlc_get_version()}')
        print(f'VLC Player State: {player.get_state()}')

        # To set the volume to 50%
        player.audio_set_volume(50)
        print(f'Audio volume: {player.audio_get_volume()}')

        while True:
            state = player.get_state()
            # print(f'Player State: {state}')
            if state in [vlc.State.Ended, vlc.State.Error]:
                break
            time.sleep(1)