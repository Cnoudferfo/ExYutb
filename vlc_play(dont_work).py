# Step 3: Streaming URL and Playing with VLC
# To stream an audio URL and play it using VLC, you'll need the vlc package:
# Replace https://your-audio-stream-url.example.com with the URL of the audio stream you want to play.
# To install the vlc package, run the following command:
# pip install python-vlc
# Here's how to stream and play the audio using the VLC API:
import vlc
import time

def play_audio_stream(url):
    print('Playing audio stream:', url)
    instance = vlc.Instance()
    print(f'VLC Version: {vlc.libvlc_get_version()}')
    player = instance.media_player_new()
    print(f'VLC Player State: {player.get_state()}')
    media = instance.media_new(url)
    print(f'Media State: {media.get_state()}')
    player.set_media(media)
    player.play()

    while True:
        state = player.get_state()
        print(f'Player State: {state}')
        if state in [vlc.State.Ended, vlc.State.Error]:
            break
        time.sleep(1)

# audio_url = 'https://your-audio-stream-url.example.com'
# audio_url = 'https://music.youtube.com/watch?v=DD-5_lCEMHY&si=chmXkAQIE6QuK6ve'
audio_url = 'https://youtu.be/WSduFBiW2EM'
play_audio_stream(audio_url)
# This code will stream and play the audio from the specified URL using the VLC API.

