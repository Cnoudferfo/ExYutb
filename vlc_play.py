import vlc
import yt_dlp
import time

the_url = 'https://music.youtube.com/watch?v=HzdD8kbDzZA&si=qGMMyvJQc0widPh2&t=4'

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(the_url, download=False)
    video_url = info_dict.get('url', None)

    player = vlc.MediaPlayer(video_url)
    player.play()
    print('Playing audio stream:', video_url)
    print(f'VLC Version: {vlc.libvlc_get_version()}')
    print(f'VLC Player State: {player.get_state()}')

    while True:
        state = player.get_state()
        # print(f'Player State: {state}')
        if state in [vlc.State.Ended, vlc.State.Error]:
            break
        time.sleep(1)